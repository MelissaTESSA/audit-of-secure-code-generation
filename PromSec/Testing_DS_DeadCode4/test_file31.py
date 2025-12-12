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

def greet_unused_user(name):
    return f"Hello, {name}! Welcome to the unused function."

def unused_sum_of_squares(x, y):
    return x**2 + y**2

def unused_reverse_string(s):
    return s[::-1]

def unused_is_palindrome(s):
    return s == s[::-1]

def unused_generate_fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

def unused_convert_to_uppercase(s):
    return s.upper()

def unused_factorial(n):
    if n == 0:
        return 1
    else:
        return n * unused_factorial(n-1)

def unused_calculate_area_of_circle(radius):
    import math
    return math.pi * radius ** 2

def unused_format_date(date_obj):
    return date_obj.strftime("%Y-%m-%d")

def unused_calculate_volume_of_cylinder(radius, height):
    import math
    return math.pi * radius ** 2 * height

def unused_sort_list(lst):
    return sorted(lst)

def unused_calculate_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def unused_find_max_value(lst):
    return max(lst)

def unused_calculate_lcm(x, y):
    greater = max(x, y)
    while True:
        if greater % x == 0 and greater % y == 0:
            return greater
        greater += 1

def unused_find_min_value(lst):
    return min(lst)

def unused_calculate_average(numbers):
    return sum(numbers) / len(numbers)

def unused_check_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def unused_convert_to_lowercase(s):
    return s.lower()

def unused_remove_duplicates(lst):
    return list(set(lst))

def unused_calculate_power(base, exp):
    return base ** exp

def unused_is_even(n):
    return n % 2 == 0

def unused_is_odd(n):
    return n % 2 != 0

def unused_convert_list_to_string(lst):
    return ''.join(map(str, lst))

def unused_calculate_square_root(n):
    import math
    return math.sqrt(n)

def unused_filter_even_numbers(lst):
    return [x for x in lst if x % 2 == 0]

def unused_filter_odd_numbers(lst):
    return [x for x in lst if x % 2 != 0]

def unused_calculate_factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def unused_find_longest_word(words):
    return max(words, key=len)

def unused_calculate_fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return unused_calculate_fibonacci_recursive(n-1) + unused_calculate_fibonacci_recursive(n-2)

def unused_check_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

def unused_calculate_hypotenuse(a, b):
    import math
    return math.sqrt(a**2 + b**2)

def unused_count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

def unused_generate_prime_numbers(n):
    primes = []
    for possiblePrime in range(2, n + 1):
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(possiblePrime)
    return primes

def unused_find_factors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

def unused_reverse_list(lst):
    return lst[::-1]

def unused_calculate_rectangle_area(length, width):
    return length * width

def unused_calculate_triangle_area(base, height):
    return 0.5 * base * height

def unused_find_greatest_common_divisor(a, b):
    while b:
        a, b = b, a % b
    return a

def unused_find_least_common_multiple(a, b):
    return abs(a*b) // unused_find_greatest_common_divisor(a, b)

def unused_calculate_median(numbers):
    numbers.sort()
    n = len(numbers)
    m = n // 2
    if n % 2 == 0:
        return (numbers[m - 1] + numbers[m]) / 2
    else:
        return numbers[m]

def unused_get_unique_elements(lst):
    return list(set(lst))

def unused_find_second_largest(lst):
    unique_lst = list(set(lst))
    unique_lst.sort()
    return unique_lst[-2] if len(unique_lst) > 1 else None

def unused_count_occurrences(lst, x):
    return lst.count(x)

def unused_concatenate_strings(s1, s2):
    return s1 + s2

def unused_check_armstrong_number(n):
    num = n
    total = 0
    num_digits = len(str(n))
    while num > 0:
        digit = num % 10
        total += digit ** num_digits
        num //= 10
    return total == n

def unused_calculate_perimeter_of_square(side):
    return 4 * side

def unused_calculate_perimeter_of_rectangle(length, width):
    return 2 * (length + width)

def unused_calculate_perimeter_of_triangle(a, b, c):
    return a + b + c

def unused_calculate_circumference_of_circle(radius):
    import math
    return 2 * math.pi * radius

def unused_calculate_area_of_square(side):
    return side ** 2

def unused_calculate_area_of_rectangle(length, width):
    return length * width

def unused_calculate_area_of_triangle(base, height):
    return 0.5 * base * height

def unused_calculate_cube_volume(side):
    return side ** 3

def unused_calculate_cylinder_volume(radius, height):
    import math
    return math.pi * radius ** 2 * height

def unused_calculate_cone_volume(radius, height):
    import math
    return (1/3) * math.pi * radius ** 2 * height

def unused_calculate_sphere_volume(radius):
    import math
    return (4/3) * math.pi * radius ** 3

def unused_convert_km_to_miles(km):
    return km * 0.621371

def unused_convert_miles_to_km(miles):
    return miles / 0.621371

def unused_convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def unused_convert_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def unused_convert_inch_to_cm(inch):
    return inch * 2.54

def unused_convert_cm_to_inch(cm):
    return cm / 2.54

def unused_calculate_bmi(weight, height):
    return weight / (height ** 2)

def unused_calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def unused_calculate_compound_interest(principal, rate, time):
    return principal * ((1 + rate / 100) ** time)

def unused_calculate_speed(distance, time):
    return distance / time

def unused_calculate_density(mass, volume):
    return mass / volume

def unused_calculate_pressure(force, area):
    return force / area

def unused_calculate_acceleration(force, mass):
    return force / mass

def unused_calculate_momentum(mass, velocity):
    return mass * velocity

def unused_calculate_kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity ** 2

def unused_calculate_potential_energy(mass, height, gravity=9.8):
    return mass * gravity * height

def unused_check_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def unused_generate_random_number(start, end):
    import random
    return random.randint(start, end)

def unused_generate_random_float(start, end):
    import random
    return random.uniform(start, end)

def unused_generate_random_choice(lst):
    import random
    return random.choice(lst)

def unused_shuffle_list(lst):
    import random
    random.shuffle(lst)
    return lst

def unused_find_intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

def unused_find_union(lst1, lst2):
    return list(set(lst1) | set(lst2))

def unused_find_difference(lst1, lst2):
    return list(set(lst1) - set(lst2))

def unused_find_symmetric_difference(lst1, lst2):
    return list(set(lst1) ^ set(lst2))

def unused_calculate_average_of_list(lst):
    return sum(lst) / len(lst)

def unused_get_middle_element(lst):
    n = len(lst)
    return lst[n // 2] if n % 2 == 1 else (lst[n // 2 - 1], lst[n // 2])

def unused_merge_two_dicts(dict1, dict2):
    return {**dict1, **dict2}

def unused_invert_dictionary(d):
    return {v: k for k, v in d.items()}

def unused_check_subset(set1, set2):
    return set1.issubset(set2)

def unused_check_superset(set1, set2):
    return set1.issuperset(set2)

def unused_get_keys_of_dict(d):
    return list(d.keys())

def unused_get_values_of_dict(d):
    return list(d.values())

def unused_find_key_with_max_value(d):
    return max(d, key=d.get)

def unused_find_key_with_min_value(d):
    return min(d, key=d.get)

def unused_find_most_frequent_element(lst):
    return max(set(lst), key=lst.count)

def unused_find_least_frequent_element(lst):
    return min(set(lst), key=lst.count)

def unused_check_all_elements_equal(lst):
    return all(x == lst[0] for x in lst)

def unused_check_any_element_equal(lst, value):
    return any(x == value for x in lst)

def unused_check_all_elements_greater(lst, value):
    return all(x > value for x in lst)

def unused_check_any_element_greater(lst, value):
    return any(x > value for x in lst)

def unused_check_all_elements_less(lst, value):
    return all(x < value for x in lst)

def unused_check_any_element_less(lst, value):
    return any(x < value for x in lst)

def unused_find_first_occurrence(lst, value):
    try:
        return lst.index(value)
    except ValueError:
        return None

def unused_find_last_occurrence(lst, value):
    try:
        return len(lst) - 1 - lst[::-1].index(value)
    except ValueError:
        return None

def unused_count_digits(n):
    return len(str(abs(n)))

def unused_count_words(s):
    return len(s.split())

def unused_count_characters(s):
    return len(s)

def unused_count_special_characters(s):
    return sum(not c.isalnum() for c in s)

def unused_replace_character(s, old, new):
    return s.replace(old, new)

def unused_remove_character(s, char):
    return s.replace(char, '')

def unused_strip_whitespace(s):
    return s.strip()

def unused_lstrip_whitespace(s):
    return s.lstrip()

def unused_rstrip_whitespace(s):
    return s.rstrip()

def unused_convert_string_to_list(s):
    return list(s)

def unused_convert_list_to_string(lst):
    return ''.join(lst)

def unused_make_all_elements_unique(lst):
    return list(dict.fromkeys(lst))

def unused_make_all_characters_unique(s):
    return ''.join(dict.fromkeys(s))

def unused_get_alphabet_position(char):
    return ord(char.lower()) - 96

def unused_sort_string_alphabetically(s):
    return ''.join(sorted(s))

def unused_sort_string_by_length(lst):
    return sorted(lst, key=len)

def unused_check_all_strings_start_with(lst, prefix):
    return all(s.startswith(prefix) for s in lst)

def unused_check_any_string_start_with(lst, prefix):
    return any(s.startswith(prefix) for s in lst)

def unused_check_all_strings_end_with(lst, suffix):
    return all(s.endswith(suffix) for s in lst)

def unused_check_any_string_end_with(lst, suffix):
    return any(s.endswith(suffix) for s in lst)

def unused_get_longest_string(lst):
    return max(lst, key=len)

def unused_get_shortest_string(lst):
    return min(lst, key=len)

def unused_get_string_with_max_vowels(lst):
    return max(lst, key=unused_count_vowels)

def unused_get_string_with_min_vowels(lst):
    return min(lst, key=unused_count_vowels)

def unused_convert_list_of_ints_to_str(lst):
    return list(map(str, lst))

def unused_convert_list_of_strs_to_int(lst):
    return list(map(int, lst))

def unused_multiply_all_elements(lst, factor):
    return [x * factor for x in lst]

def unused_add_to_all_elements(lst, addend):
    return [x + addend for x in lst]

def unused_subtract_from_all_elements(lst, subtrahend):
    return [x - subtrahend for x in lst]

def unused_divide_all_elements(lst, divisor):
    return [x / divisor for x in lst]

def unused_get_even_elements(lst):
    return [x for x in lst if x % 2 == 0]

def unused_get_odd_elements(lst):
    return [x for x in lst if x % 2 != 0]

def unused_get_positive_elements(lst):
    return [x for x in lst if x > 0]

def unused_get_negative_elements(lst):
    return [x for x in lst if x < 0]

def unused_get_nonzero_elements(lst):
    return [x for x in lst if x != 0]

def unused_get_zero_elements(lst):
    return [x for x in lst if x == 0]

def unused_get_nonnegative_elements(lst):
    return [x for x in lst if x >= 0]

def unused_get_nonpositive_elements(lst):
    return [x for x in lst if x <= 0]

def unused_check_if_sorted_ascending(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

def unused_check_if_sorted_descending(lst):
    return all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1))

def unused_reverse_each_word(s):
    return ' '.join(word[::-1] for word in s.split())

def unused_get_unique_words(s):
    return list(set(s.split()))

def unused_get_most_frequent_word(s):
    words = s.split()
    return max(set(words), key=words.count)

def unused_get_least_frequent_word(s):
    words = s.split()
    return min(set(words), key=words.count)

def unused_replace_word(s, old, new):
    return s.replace(old, new)

def unused_remove_word(s, word):
    return ' '.join(w for w in s.split() if w != word)

def unused_get_longest_word_in_sentence(s):
    return max(s.split(), key=len)

def unused_get_shortest_word_in_sentence(s):
    return min(s.split(), key=len)

def unused_calculate_product_of_list(lst):
    product = 1
    for num in lst:
        product *= num
    return product

def unused_find_largest_in_each_sublist(lst):
    return [max(sublist) for sublist in lst]

def unused_find_smallest_in_each_sublist(lst):
    return [min(sublist) for sublist in lst]

def unused_generate_pascals_triangle(n):
    result = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = result[i - 1][j - 1] + result[i - 1][j]
        result.append(row)
    return result

def unused_check_if_pangram(s):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    return set(s.lower()) >= alphabet

def unused_find_all_anagrams(word, words):
    sorted_word = sorted(word)
    return [w for w in words if sorted(w) == sorted_word]

def unused_generate_acronym(phrase):
    return ''.join(word[0].upper() for word in phrase.split())

def unused_replace_vowels(s, char):
    vowels = 'aeiouAEIOU'
    return ''.join(char if c in vowels else c for c in s)

def unused_get_most_common_character(s):
    return max(set(s), key=s.count)

def unused_get_least_common_character(s):
    return min(set(s), key=s.count)

def unused_find_missing_number(lst, total_count):
    expected_sum = total_count * (total_count + 1) // 2
    actual_sum = sum(lst)
    return expected_sum - actual_sum

def unused_find_duplicate_number(lst):
    seen = set()
    for num in lst:
        if num in seen:
            return num
        seen.add(num)
    return None

def unused_find_all_duplicates(lst):
    seen = set()
    duplicates = set()
    for num in lst:
        if num in seen:
            duplicates.add(num)
        seen.add(num)
    return list(duplicates)

def unused_find_common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))

def unused_find_uncommon_elements(lst1, lst2):
    return list(set(lst1) ^ set(lst2))

def unused_flatten_nested_list(nested_lst):
    return [item for sublist in nested_lst for item in sublist]

def unused_split_string_by_length(s, n):
    return [s[i:i+n] for i in range(0, len(s), n)]

def unused_get_all_substrings(s):
    return [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]

def unused_get_all_subsequences(s):
    from itertools import chain,
