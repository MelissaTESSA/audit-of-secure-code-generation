import json
from io import BytesIO
import logging
import os

import attr
from six import text_type
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
    if 'db' not in test_config:
        test_config['db'] = {'db.file': ':memory:'}
    else:
        test_config['db'].setdefault('db.file', ':memory:')

    reactor = MemoryReactorClock()
    return Sydent(reactor=reactor, cfg=parse_config_dict(test_config))


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
    if (
        shorthand
        and not path.startswith(b"/_matrix")
    ):
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

    log_format = (
        "%(asctime)s - %(name)s - %(lineno)d - %(levelname)s"
        " - %(message)s"
    )

    handler = ToTwistedHandler()
    formatter = logging.Formatter(log_format)
    handler.setFormatter(formatter)
    root_logger.addHandler(handler)

    log_level = os.environ.get("SYDENT_TEST_LOG_LEVEL", "ERROR")
    root_logger.setLevel(log_level)


setup_logging()


def calculate_area_of_square(side_length):
    return side_length * side_length

def reverse_string(input_string):
    return input_string[::-1]

def sum_of_list(numbers):
    return sum(numbers)

def find_maximum_value(values):
    return max(values)

def is_even(number):
    return number % 2 == 0

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib

def count_vowels(s):
    return sum(1 for char in s if char.lower() in 'aeiou')

def sort_list_descending(lst):
    return sorted(lst, reverse=True)

def capitalize_words(sentence):
    return ' '.join(word.capitalize() for word in sentence.split())

def calculate_circle_area(radius):
    return 3.14159 * radius * radius

def is_palindrome(s):
    return s == s[::-1]

def find_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def convert_to_uppercase(s):
    return s.upper()

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def remove_duplicates(lst):
    return list(set(lst))

def merge_two_dicts(dict1, dict2):
    res = dict1.copy()
    res.update(dict2)
    return res

def count_occurrences(lst, x):
    return lst.count(x)

def generate_fibonacci_sequence(n):
    if n <= 0:
        return []
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

def find_unique_elements(lst):
    return list(set(lst))

def calculate_average(lst):
    return sum(lst) / len(lst) if lst else 0

def find_common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))

def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]

def find_minimum_value(values):
    return min(values)

def list_to_dict(keys, values):
    return dict(zip(keys, values))

def is_substring(sub, string):
    return sub in string

def reverse_words(sentence):
    return ' '.join(sentence.split()[::-1])

def calculate_rectangle_area(length, width):
    return length * width

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def remove_whitespace(s):
    return s.replace(" ", "")

def calculate_sum_of_squares(n):
    return sum(i**2 for i in range(1, n+1))

def find_second_largest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers[-2] if len(unique_numbers) >= 2 else None

def convert_list_to_string(lst):
    return ''.join(lst)

def get_file_extension(filename):
    return filename.split('.')[-1] if '.' in filename else ''

def list_intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

def find_factors(n):
    return [i for i in range(1, n+1) if n % i == 0]

def convert_to_lowercase(s):
    return s.lower()

def remove_punctuation(s):
    import string
    return s.translate(str.maketrans("", "", string.punctuation))

def calculate_average_word_length(sentence):
    words = sentence.split()
    return sum(len(word) for word in words) / len(words) if words else 0

def replace_vowels(s, char):
    return ''.join(char if c.lower() in 'aeiou' else c for c in s)

def is_armstrong_number(n):
    num_str = str(n)
    num_len = len(num_str)
    return n == sum(int(digit) ** num_len for digit in num_str)

def gcd_of_list(numbers):
    from functools import reduce
    from math import gcd
    return reduce(gcd, numbers)

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def convert_seconds_to_hms(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return hours, minutes, seconds

def find_lcm(x, y):
    from math import gcd
    return x * y // gcd(x, y)

def count_words(sentence):
    return len(sentence.split())

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def find_duplicates(lst):
    from collections import Counter
    return [item for item, count in Counter(lst).items() if count > 1]

def convert_to_title_case(s):
    return s.title()

def sum_of_even_numbers(lst):
    return sum(x for x in lst if x % 2 == 0)

def is_perfect_square(n):
    return int(n**0.5) ** 2 == n

def rotate_list(lst, k):
    k = k % len(lst)
    return lst[-k:] + lst[:-k]

def find_largest_element(lst):
    return max(lst)

def calculate_hypotenuse(a, b):
    return (a**2 + b**2) ** 0.5

def sum_of_odd_numbers(lst):
    return sum(x for x in lst if x % 2 != 0)

def find_first_non_repeating_character(s):
    from collections import Counter
    count = Counter(s)
    for char in s:
        if count[char] == 1:
            return char
    return None

def calculate_median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]

def convert_to_binary(n):
    return bin(n)[2:]

def calculate_mode(lst):
    from collections import Counter
    count = Counter(lst)
    max_count = max(count.values())
    return [k for k, v in count.items() if v == max_count]

def find_all_substrings(s):
    return [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]

def remove_vowels(s):
    return ''.join(c for c in s if c.lower() not in 'aeiou')

def calculate_standard_deviation(lst):
    mean = sum(lst) / len(lst)
    variance = sum((x - mean) ** 2 for x in lst) / len(lst)
    return variance ** 0.5

def count_consonants(s):
    return sum(1 for char in s if char.lower() in 'bcdfghjklmnpqrstvwxyz')

def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

def get_unique_chars(s):
    return ''.join(sorted(set(s)))

def calculate_perimeter_of_rectangle(length, width):
    return 2 * (length + width)

def find_most_frequent_element(lst):
    from collections import Counter
    count = Counter(lst)
    return count.most_common(1)[0][0]

def convert_to_hexadecimal(n):
    return hex(n)[2:]

def is_fibonacci_number(n):
    from math import sqrt
    return n >= 0 and ((sqrt(5 * n * n + 4) % 1 == 0) or (sqrt(5 * n * n - 4) % 1 == 0))

def get_middle_character(s):
    mid = len(s) // 2
    return s[mid] if len(s) % 2 != 0 else s[mid-1:mid+1]

def find_shortest_word(sentence):
    words = sentence.split()
    return min(words, key=len) if words else None

def is_valid_email(email):
    import re
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

def swap_case(s):
    return s.swapcase()

def find_missing_number(lst, n):
    return n * (n + 1) // 2 - sum(lst)

def is_subsequence(s1, s2):
    it = iter(s2)
    return all(c in it for c in s1)

def find_longest_word(sentence):
    words = sentence.split()
    return max(words, key=len) if words else None

def calculate_volume_of_cylinder(radius, height):
    return 3.14159 * radius * radius * height

def find_maximum_product(lst):
    max_product = float('-inf')
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            max_product = max(max_product, lst[i] * lst[j])
    return max_product

def count_uppercase_letters(s):
    return sum(1 for char in s if char.isupper())

def is_valid_ipv4_address(ip):
    parts = ip.split(".")
    return len(parts) == 4 and all(part.isdigit() and 0 <= int(part) <= 255 for part in parts)

def calculate_circle_circumference(radius):
    return 2 * 3.14159 * radius

def is_sorted(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

def find_largest_prime_factor(n):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    factor = 1
    for i in range(2, n + 1):
        while n % i == 0:
            factor = i
            n //= i
    return factor if is_prime(factor) else None

def reverse_integer(n):
    sign = -1 if n < 0 else 1
    n *= sign
    reversed_n = int(str(n)[::-1])
    return sign * reversed_n

def find_longest_palindromic_substring(s):
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    longest = ""
    for i in range(len(s)):
        odd_palindrome = expand_around_center(i, i)
        even_palindrome = expand_around_center(i, i + 1)
        longest = max(longest, odd_palindrome, even_palindrome, key=len)
    return longest

def calculate_future_value(principal, rate, time):
    return principal * ((1 + rate) ** time)

def is_valid_parentheses(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack

def count_lowercase_letters(s):
    return sum(1 for char in s if char.islower())

def find_longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

def calculate_compound_interest(principal, rate, time):
    return principal * (1 + rate / 100) ** time - principal

def is_valid_palindrome(s):
    s = ''.join(char.lower() for char in s if char.isalnum())
    return s == s[::-1]

def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            return sum(len(line.split()) for line in file)
    except FileNotFoundError:
        return 0

def find_largest_sum_of_consecutive_numbers(lst, k):
    max_sum = 0
    current_sum = sum(lst[:k])
    max_sum = current_sum
    for i in range(k, len(lst)):
        current_sum += lst[i] - lst[i - k]
        max_sum = max(max_sum, current_sum)
    return max_sum

def is_valid_braces_sequence(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping:
            if stack and stack[-1] == mapping[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)
    return not stack

def find_substring_indices(haystack, needle):
    return [i for i in range(len(haystack) - len(needle) + 1) if haystack[i:i+len(needle)] == needle]

def is_valid_credit_card_number(number):
    number = str(number)
    total = 0
    reverse_digits = number[::-1]
    for i, digit in enumerate(reverse_digits):
        n = int(digit)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        total += n
    return total % 10 == 0
