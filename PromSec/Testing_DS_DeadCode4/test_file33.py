import json
from io import BytesIO
import logging
import os
from typing import Dict
import attr
from six import text_type
from zope.interface import implementer
from twisted.internet._resolver import SimpleResolverComplexifier
from twisted.internet.defer import fail, succeed
from twisted.internet.error import DNSLookupError
from twisted.internet.interfaces import (
    IHostnameResolver,
    IReactorPluggableNameResolver,
    IResolverSimple,
)

from twisted.internet import address
import twisted.logger
from twisted.web.http_headers import Headers
from twisted.web.server import Request, Site
from twisted.web.http import unquote
from twisted.test.proto_helpers import MemoryReactorClock
from OpenSSL import crypto

from sydent.sydent import Sydent, parse_config_dict


# Expires on Jan 11 2030 at 17:53:40 GMT
FAKE_SERVER_CERT_PEM = """
-----BEGIN CERTIFICATE-----
MIIDlzCCAn+gAwIBAgIUC8tnJVZ8Cawh5tqr7PCAOfvyGTYwDQYJKoZIhvcNAQEL
BQAwWzELMAkGA1UEBhMCQVUxEzARBgNVBAgMClNvbWUtU3RhdGUxITAfBgNVBAoM
GEludGVybmV0IFdpZGdpdHMgUHR5IEx0ZDEUMBIGA1UEAwwLZmFrZS5zZXJ2ZXIw
HhcNMjAwMTE0MTc1MzQwWhcNMzAwMTExMTc1MzQwWjBbMQswCQYDVQQGEwJBVTET
MBEGA1UECAwKU29tZS1TdGF0ZTEhMB8GA1UECgwYSW50ZXJuZXQgV2lkZ2l0cyBQ
dHkgTHRkMRQwEgYDVQQDDAtmYWtlLnNlcnZlcjCCASIwDQYJKoZIhvcNAQEBBQAD
ggEPADCCAQoCggEBANNzY7YHBLm4uj52ojQc/dfQCoR+63IgjxZ6QdnThhIlOYgE
3y0Ks49bt3GKmAweOFRRKfDhJRKCYfqZTYudMcdsQg696s2HhiTY0SpqO0soXwW4
6kEIxnTy2TqkPjWlsWgGTtbVnKc5pnLs7MaQwLIQfxirqD2znn+9r68WMOJRlzkv
VmrXDXjxKPANJJ9b0PiGrL2SF4QcF3zHk8Tjf24OGRX4JTNwiGraU/VN9rrqSHug
CLWcfZ1mvcav3scvtGfgm4kxcw8K6heiQAc3QAMWIrdWhiunaWpQYgw7euS8lZ/O
C7HZ7YbdoldknWdK8o7HJZmxUP9yW9Pqa3n8p9UCAwEAAaNTMFEwHQYDVR0OBBYE
FHwfTq0Mdk9YKqjyfdYm4v9zRP8nMB8GA1UdIwQYMBaAFHwfTq0Mdk9YKqjyfdYm
4v9zRP8nMA8GA1UdEwEB/wQFMAMBAf8wDQYJKoZIhvcNAQELBQADggEBAEPVM5/+
Sj9P/CvNG7F2PxlDQC1/+aVl6ARAz/bZmm7yJnWEleBSwwFLerEQU6KFrgjA243L
qgY6Qf2EYUn1O9jroDg/IumlcQU1H4DXZ03YLKS2bXFGj630Piao547/l4/PaKOP
wSvwDcJlBatKfwjMVl3Al/EcAgUJL8eVosnqHDSINdBuFEc8Kw4LnDSFoTEIx19i
c+DKmtnJNI68wNydLJ3lhSaj4pmsX4PsRqsRzw+jgkPXIG1oGlUDMO3k7UwxfYKR
XkU5mFYkohPTgxv5oYGq2FCOPixkbov7geCEvEUs8m8c8MAm4ErBUzemOAj8KVhE
tWVEpHfT+G7AjA8=
-----END CERTIFICATE-----
"""


def make_sydent(test_config={}):
    """Create a new sydent

    Args:
        test_config (dict): any configuration variables for overriding the default sydent
            config
    """
    # Use an in-memory SQLite database. Note that the database isn't cleaned up between
    # tests, so by default the same database will be used for each test if changed to be
    # a file on disk.
    if "db" not in test_config:
        test_config["db"] = {"db.file": ":memory:"}
    else:
        test_config["db"].setdefault("db.file", ":memory:")

    reactor = ResolvingMemoryReactorClock()
    return Sydent(reactor=reactor, cfg=parse_config_dict(test_config), use_tls_for_federation=False)


@attr.s
class FakeChannel(object):
    """
    A fake Twisted Web Channel (the part that interfaces with the
    wire). Mostly copied from Synapse's tests framework.
    """

    site = attr.ib(type=Site)
    _reactor = attr.ib()
    result = attr.ib(default=attr.Factory(dict))
    _producer = None

    @property
    def json_body(self):
        if not self.result:
            raise Exception("No result yet.")
        return json.loads(self.result["body"].decode("utf8"))

    @property
    def code(self):
        if not self.result:
            raise Exception("No result yet.")
        return int(self.result["code"])

    @property
    def headers(self):
        if not self.result:
            raise Exception("No result yet.")
        h = Headers()
        for i in self.result["headers"]:
            h.addRawHeader(*i)
        return h

    def writeHeaders(self, version, code, reason, headers):
        self.result["version"] = version
        self.result["code"] = code
        self.result["reason"] = reason
        self.result["headers"] = headers

    def write(self, content):
        assert isinstance(content, bytes), "Should be bytes! " + repr(content)

        if "body" not in self.result:
            self.result["body"] = b""

        self.result["body"] += content

    def registerProducer(self, producer, streaming):
        self._producer = producer
        self.producerStreaming = streaming

        def _produce():
            if self._producer:
                self._producer.resumeProducing()
                self._reactor.callLater(0.1, _produce)

        if not streaming:
            self._reactor.callLater(0.0, _produce)

    def unregisterProducer(self):
        if self._producer is None:
            return

        self._producer = None

    def requestDone(self, _self):
        self.result["done"] = True

    def getPeer(self):
        # We give an address so that getClientIP returns a non null entry,
        # causing us to record the MAU
        return address.IPv4Address("TCP", "127.0.0.1", 3423)

    def getHost(self):
        return None

    @property
    def transport(self):
        return self

    def getPeerCertificate(self):
        """Returns the hardcoded TLS certificate for fake.server."""
        return crypto.load_certificate(crypto.FILETYPE_PEM, FAKE_SERVER_CERT_PEM)


class FakeSite:
    """A fake Twisted Web Site."""

    pass


def make_request(
    reactor,
    method,
    path,
    content=b"",
    access_token=None,
    request=Request,
    shorthand=True,
    federation_auth_origin=None,
):
    """
    Make a web request using the given method and path, feed it the
    content, and return the Request and the Channel underneath. Mostly

    Args:
        reactor (IReactor): The Twisted reactor to use when performing the request.
        method (bytes or unicode): The HTTP request method ("verb").
        path (bytes or unicode): The HTTP path, suitably URL encoded (e.g.
        escaped UTF-8 & spaces and such).
        content (bytes or dict): The body of the request. JSON-encoded, if
        a dict.
        access_token (unicode): An access token to use to authenticate the request,
            None if no access token needs to be included.
        request (IRequest): The class to use when instantiating the request object.
        shorthand: Whether to try and be helpful and prefix the given URL
        with the usual REST API path, if it doesn't contain it.
        federation_auth_origin (bytes|None): if set to not-None, we will add a fake
            Authorization header pretenting to be the given server name.

    Returns:
        Tuple[synapse.http.site.SynapseRequest, channel]
    """
    if not isinstance(method, bytes):
        method = method.encode("ascii")

    if not isinstance(path, bytes):
        path = path.encode("ascii")

    # Decorate it to be the full path, if we're using shorthand
    if shorthand and not path.startswith(b"/_matrix"):
        path = b"/_matrix/identity/v2/" + path
        path = path.replace(b"//", b"/")

    if not path.startswith(b"/"):
        path = b"/" + path

    if isinstance(content, dict):
        content = json.dumps(content)
    if isinstance(content, text_type):
        content = content.encode("utf8")

    site = FakeSite()
    channel = FakeChannel(site, reactor)

    req = request(channel)
    req.process = lambda: b""
    req.content = BytesIO(content)
    req.postpath = list(map(unquote, path[1:].split(b"/")))

    if access_token:
        req.requestHeaders.addRawHeader(
            b"Authorization", b"Bearer " + access_token.encode("ascii")
        )

    if federation_auth_origin is not None:
        req.requestHeaders.addRawHeader(
            b"Authorization",
            b"X-Matrix origin=%s,key=,sig=" % (federation_auth_origin,),
        )

    if content:
        req.requestHeaders.addRawHeader(b"Content-Type", b"application/json")

    req.requestReceived(method, path, b"1.1")

    return req, channel


class ToTwistedHandler(logging.Handler):
    """logging handler which sends the logs to the twisted log"""

    tx_log = twisted.logger.Logger()

    def emit(self, record):
        log_entry = self.format(record)
        log_level = record.levelname.lower().replace("warning", "warn")
        self.tx_log.emit(
            twisted.logger.LogLevel.levelWithName(log_level), "{entry}", entry=log_entry
        )


def setup_logging():
    """Configure the python logging appropriately for the tests.

    (Logs will end up in _trial_temp.)
    """
    root_logger = logging.getLogger()

    log_format = "%(asctime)s - %(name)s - %(lineno)d - %(levelname)s" " - %(message)s"

    handler = ToTwistedHandler()
    formatter = logging.Formatter(log_format)
    handler.setFormatter(formatter)
    root_logger.addHandler(handler)

    log_level = os.environ.get("SYDENT_TEST_LOG_LEVEL", "ERROR")
    root_logger.setLevel(log_level)


setup_logging()


@implementer(IReactorPluggableNameResolver)
class ResolvingMemoryReactorClock(MemoryReactorClock):
    """
    A MemoryReactorClock that supports name resolution.
    """

    def __init__(self):
        lookups = self.lookups = {}  # type: Dict[str, str]

        @implementer(IResolverSimple)
        class FakeResolver:
            def getHostByName(self, name, timeout=None):
                if name not in lookups:
                    return fail(DNSLookupError("OH NO: unknown %s" % (name,)))
                return succeed(lookups[name])

        self.nameResolver = SimpleResolverComplexifier(FakeResolver())
        super().__init__()

    def installNameResolver(self, resolver: IHostnameResolver) -> IHostnameResolver:
        raise NotImplementedError()


def calculate_unused_value(a, b):
    return a * b + 42

def format_unused_string(s):
    return s.strip().upper()

def find_unused_maximum(arr):
    if not arr:
        return None
    return max(arr)

def unused_reverse_list(lst):
    return lst[::-1]

def unused_greet_user(name):
    return f"Hello, {name}!"

def unused_square_number(n):
    return n * n

def unused_convert_to_uppercase(s):
    return s.upper()

def unused_calculate_area_of_circle(radius):
    pi = 3.14159
    return pi * radius * radius

def unused_get_even_numbers(lst):
    return [x for x in lst if x % 2 == 0]

def unused_is_palindrome(s):
    return s == s[::-1]

def unused_calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * unused_calculate_factorial(n-1)

def unused_find_first_vowel(s):
    vowels = 'aeiou'
    for index, char in enumerate(s):
        if char in vowels:
            return index
    return -1

def unused_generate_fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

def unused_sort_list_ascending(lst):
    return sorted(lst)

def unused_merge_dicts(dict1, dict2):
    return {**dict1, **dict2}

def unused_calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def unused_find_minimum(arr):
    if not arr:
        return None
    return min(arr)

def unused_convert_to_lowercase(s):
    return s.lower()

def unused_calculate_hypotenuse(a, b):
    return (a**2 + b**2)**0.5

def unused_is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def unused_count_occurrences(s, char):
    return s.count(char)

def unused_calculate_average(lst):
    if not lst:
        return 0
    return sum(lst) / len(lst)

def unused_remove_duplicates(lst):
    return list(set(lst))

def unused_find_common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))

def unused_split_string(s, delimiter):
    return s.split(delimiter)

def unused_calculate_bmi(weight, height):
    return weight / (height * height)

def unused_find_longest_word(words):
    if not words:
        return ""
    return max(words, key=len)

def unused_convert_to_binary(n):
    return bin(n)[2:]

def unused_get_unique_elements(lst):
    return list(set(lst))

def unused_calculate_modulus(a, b):
    return a % b

def unused_find_second_largest(arr):
    if len(arr) < 2:
        return None
    first, second = float('-inf'), float('-inf')
    for number in arr:
        if number > first:
            first, second = number, first
        elif number > second:
            second = number
    return second

def unused_reverse_string(s):
    return s[::-1]

def unused_calculate_circumference(radius):
    pi = 3.14159
    return 2 * pi * radius

def unused_find_missing_number(arr, n):
    total = n * (n + 1) // 2
    return total - sum(arr)

def unused_calculate_power(base, exponent):
    return base ** exponent

def unused_find_anagrams(word, candidates):
    sorted_word = sorted(word)
    return [candidate for candidate in candidates if sorted(candidate) == sorted_word]

def unused_is_substring(s1, s2):
    return s1 in s2

def unused_find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def unused_calculate_lcm(a, b):
    return abs(a * b) // unused_find_gcd(a, b)

def unused_get_vowel_count(s):
    vowels = 'aeiouAEIOU'
    return sum(char in vowels for char in s)

def unused_find_uppercase_letters(s):
    return [char for char in s if char.isupper()]

def unused_check_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False

def unused_calculate_discount(price, discount):
    return price - (price * discount / 100)

def unused_find_factors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

def unused_check_armstrong_number(n):
    num_str = str(n)
    power = len(num_str)
    return n == sum(int(digit) ** power for digit in num_str)

def unused_generate_primes_up_to_n(n):
    primes = []
    for num in range(2, n + 1):
        if unused_is_prime(num):
            primes.append(num)
    return primes

def unused_find_max_difference(arr):
    if not arr:
        return None
    return max(arr) - min(arr)

def unused_count_words(s):
    return len(s.split())

def unused_calculate_rectangle_area(length, width):
    return length * width

def unused_convert_to_title_case(s):
    return s.title()

def unused_find_nth_fibonacci(n):
    if n <= 1:
        return n
    return unused_find_nth_fibonacci(n - 1) + unused_find_nth_fibonacci(n - 2)

def unused_calculate_square_root(n):
    return n ** 0.5

def unused_find_unique_characters(s):
    return ''.join(set(s))

def unused_calculate_percentage(part, whole):
    return (part / whole) * 100

def unused_find_median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    if n % 2 == 1:
        return sorted_lst[n // 2]
    else:
        return (sorted_lst[n // 2 - 1] + sorted_lst[n // 2]) / 2

def unused_check_perfect_square(n):
    return int(n**0.5)**2 == n

def unused_generate_multiplication_table(n, up_to=10):
    return [n * i for i in range(1, up_to + 1)]

def unused_find_duplicates(lst):
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)

def unused_calculate_volume_of_cube(side):
    return side ** 3

def unused_find_largest_prime_factor(n):
    factor = 2
    while n > 1:
        if n % factor == 0:
            n //= factor
        else:
            factor += 1
    return factor

def unused_check_palindrome_number(n):
    return str(n) == str(n)[::-1]

def unused_convert_to_hexadecimal(n):
    return hex(n)[2:]

def unused_calculate_average_word_length(s):
    words = s.split()
    if not words:
        return 0
    return sum(len(word) for word in words) / len(words)

def unused_remove_vowels(s):
    vowels = 'aeiouAEIOU'
    return ''.join(char for char in s if char not in vowels)

def unused_find_least_common_multiple(lst):
    def lcm(a, b):
        return abs(a * b) // unused_find_gcd(a, b)
    from functools import reduce
    return reduce(lcm, lst)

def unused_calculate_sum_of_squares(lst):
    return sum(x*x for x in lst)

def unused_find_occurrences(s, sub):
    return s.count(sub)

def unused_calculate_trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height

def unused_find_non_repeating_characters(s):
    from collections import Counter
    counter = Counter(s)
    return [char for char, count in counter.items() if count == 1]

def unused_find_highest_frequency(lst):
    if not lst:
        return None
    from collections import Counter
    counter = Counter(lst)
    most_common = counter.most_common(1)
    return most_common[0][0]

def unused_check_pangram(s):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    return alphabet <= set(s.lower())

def unused_find_sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def unused_calculate_heron_area(a, b, c):
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5

def unused_find_longest_common_prefix(words):
    if not words:
        return ""
    prefix = words[0]
    for word in words[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

def unused_calculate_decimal_to_binary(n):
    return bin(n)[2:]

def unused_find_largest_even_number(lst):
    even_numbers = [num for num in lst if num % 2 == 0]
    if not even_numbers:
        return None
    return max(even_numbers)

def unused_check_power_of_two(n):
    return (n != 0) and (n & (n - 1) == 0)

def unused_find_most_frequent_character(s):
    from collections import Counter
    counter = Counter(s)
    most_common = counter.most_common(1)
    return most_common[0][0]

def unused_generate_pascal_triangle(n):
    result = []
    for i in range(n):
        row = [1]
        if result:
            last_row = result[-1]
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)
        result.append(row)
    return result

def unused_calculate_permutation(n, r):
    from math import factorial
    return factorial(n) // factorial(n - r)

def unused_check_strong_number(n):
    from math import factorial
    return n == sum(factorial(int(digit)) for digit in str(n))

def unused_find_smallest_prime_factor(n):
    if n <= 1:
        return None
    factor = 2
    while factor <= n:
        if n % factor == 0:
            return factor
        factor += 1

def unused_calculate_coefficient_of_variation(lst):
    if not lst:
        return None
    mean = sum(lst) / len(lst)
    variance = sum((x - mean) ** 2 for x in lst) / len(lst)
    stddev = variance ** 0.5
    return stddev / mean

def unused_find_sum_of_cubes(lst):
    return sum(x**3 for x in lst)

def unused_calculate_cylinder_volume(radius, height):
    pi = 3.14159
    return pi * radius**2 * height

def unused_find_prime_numbers_in_range(start, end):
    return [num for num in range(start, end + 1) if unused_is_prime(num)]

def unused_calculate_compound_interest(principal, rate, time, n=1):
    return principal * (1 + rate / (100 * n)) ** (n * time)

def unused_find_common_divisors(a, b):
    gcd_value = unused_find_gcd(a, b)
    return [i for i in range(1, gcd_value + 1) if gcd_value % i == 0]

def unused_check_abundant_number(n):
    return sum(unused_find_factors(n)) > 2 * n

def unused_calculate_cone_volume(radius, height):
    pi = 3.14159
    return (1 / 3) * pi * radius**2 * height

def unused_find_largest_perfect_square(n):
    return int(n**0.5)**2

def unused_calculate_tetrahedron_volume(edge_length):
    return (edge_length**3 / (6 * (2**0.5)))

def unused_find_sum_of_even_numbers(lst):
    return sum(x for x in lst if x % 2 == 0)

def unused_check_amicable_numbers(a, b):
    return sum(unused_find_factors(a)) - a == b and sum(unused_find_factors(b)) - b == a

def unused_calculate_sphere_surface_area(radius):
    pi = 3.14159
    return 4 * pi * radius**2

def unused_find_sum_of_odd_numbers(lst):
    return sum(x for x in lst if x % 2 != 0)

def unused_generate_star_pattern(n):
    pattern = []
    for i in range(1, n + 1):
        pattern.append('*' * i)
    return pattern

def unused_calculate_harmonic_mean(lst):
    if not lst:
        return None
    return len(lst) / sum(1 / x for x in lst)

def unused_find_triplets_with_sum(lst, target):
    triplets = []
    lst.sort()
    for i in range(len(lst) - 2):
        if i > 0 and lst[i] == lst[i - 1]:
            continue
        left, right = i + 1, len(lst) - 1
        while left < right:
            total = lst[i] + lst[left] + lst[right]
            if total == target:
                triplets.append((lst[i], lst[left], lst[right]))
                while left < right and lst[left] == lst[left + 1]:
                    left += 1
                while left < right and lst[right] == lst[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < target:
                left += 1
            else:
                right -= 1
    return triplets

def unused_calculate_mean_absolute_deviation(lst):
    if not lst:
        return None
    mean = sum(lst) / len(lst)
    return sum(abs(x - mean) for x in lst) / len(lst)

def unused_find_unique_triplets(lst):
    triplets = set()
    for i in range(len(lst) - 2):
        for j in range(i + 1, len(lst) - 1):
            for k in range(j + 1, len(lst)):
                if lst[i] + lst[j] + lst[k] == 0:
                    triplets.add(tuple(sorted((lst[i], lst[j], lst[k]))))
    return list(triplets)

def unused_calculate_geometric_mean(lst):
    if not lst:
        return None
    product = 1
    for x in lst:
        product *= x
    return product ** (1 / len(lst))

def unused_find_fibonacci_until_n(n):
    fib_sequence = [0, 1]
    while fib_sequence[-1] + fib_sequence[-2] <= n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def unused_check_narcissistic_number(n):
    num_str = str(n)
    length = len(num_str)
    return n == sum(int(digit) ** length for digit in num_str)
