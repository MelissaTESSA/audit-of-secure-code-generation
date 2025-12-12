##############################################################################
#
# Copyright (c) 2002 Zope Foundation and Contributors.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE
#
##############################################################################

import unittest

from chameleon.exc import ExpressionError

import zope.component.testing
from AccessControl import SecurityManager
from AccessControl.SecurityManagement import noSecurityManager
from Acquisition import Implicit
from Products.PageTemplates.interfaces import IUnicodeEncodingConflictResolver
from Products.PageTemplates.PageTemplate import PageTemplate
from Products.PageTemplates.tests import util
from Products.PageTemplates.unicodeconflictresolver import \
    DefaultUnicodeEncodingConflictResolver
from Products.PageTemplates.unicodeconflictresolver import \
    PreferredCharsetResolver
from Products.PageTemplates.ZopePageTemplate import ZopePageTemplate
from zExceptions import NotFound
from zope.component import provideUtility
from zope.location.interfaces import LocationError
from zope.traversing.adapters import DefaultTraversable

from .util import useChameleonEngine


class AqPageTemplate(Implicit, PageTemplate):
    pass


class AqZopePageTemplate(Implicit, ZopePageTemplate):
    pass


class Folder(util.Base):
    pass


class UnitTestSecurityPolicy:
    """
        Stub out the existing security policy for unit testing purposes.
    """
    # Standard SecurityPolicy interface
    def validate(self,
                 accessed=None,
                 container=None,
                 name=None,
                 value=None,
                 context=None,
                 roles=None,
                 *args, **kw):
        return 1

    def checkPermission(self, permission, object, context):
        return 1


class HTMLTests(zope.component.testing.PlacelessSetup, unittest.TestCase):
    PREFIX = None

    def setUp(self):
        super().setUp()
        useChameleonEngine()
        zope.component.provideAdapter(DefaultTraversable, (None,))

        provideUtility(DefaultUnicodeEncodingConflictResolver,
                       IUnicodeEncodingConflictResolver)

        self.folder = f = Folder()
        f.laf = AqPageTemplate()
        f.t = AqPageTemplate()
        f.z = AqZopePageTemplate('testing')
        self.policy = UnitTestSecurityPolicy()
        self.oldPolicy = SecurityManager.setSecurityPolicy(self.policy)
        noSecurityManager()  # Use the new policy.

    def tearDown(self):
        super().tearDown()
        SecurityManager.setSecurityPolicy(self.oldPolicy)
        noSecurityManager()  # Reset to old policy.

    def assert_expected(self, t, fname, *args, **kwargs):
        t.write(util.read_input(fname))
        assert not t._v_errors, 'Template errors: %s' % t._v_errors
        if self.PREFIX is not None \
                and util.exists_output(self.PREFIX + fname):
            fname = self.PREFIX + fname
        expect = util.read_output(fname)
        out = t(*args, **kwargs)
        util.check_html(expect, out)

    def assert_expected_unicode(self, t, fname, *args, **kwargs):
        t.write(util.read_input(fname))
        assert not t._v_errors, 'Template errors: %s' % t._v_errors
        expect = util.read_output(fname)
        if not isinstance(expect, str):
            expect = str(expect, 'utf-8')
        out = t(*args, **kwargs)
        util.check_html(expect, out)

    def getProducts(self):
        return [
            {'description': 'This is the tee for those who LOVE Zope. '
             'Show your heart on your tee.',
             'price': 12.99, 'image': 'smlatee.jpg'
             },
            {'description': 'This is the tee for Jim Fulton. '
             'He\'s the Zope Pope!',
             'price': 11.99, 'image': 'smpztee.jpg'
             },
        ]

    def test_1(self):
        self.assert_expected(self.folder.laf, 'TeeShopLAF.html')

    def test_2(self):
        self.folder.laf.write(util.read_input('TeeShopLAF.html'))

        self.assert_expected(self.folder.t, 'TeeShop2.html',
                             getProducts=self.getProducts)

    def test_3(self):
        self.folder.laf.write(util.read_input('TeeShopLAF.html'))

        self.assert_expected(self.folder.t, 'TeeShop1.html',
                             getProducts=self.getProducts)

    def testSimpleLoop(self):
        self.assert_expected(self.folder.t, 'Loop1.html')

    def testFancyLoop(self):
        self.assert_expected(self.folder.t, 'Loop2.html')

    def testGlobalsShadowLocals(self):
        self.assert_expected(self.folder.t, 'GlobalsShadowLocals.html')

    def testStringExpressions(self):
        self.assert_expected(self.folder.t, 'StringExpression.html')

    def testReplaceWithNothing(self):
        self.assert_expected(self.folder.t, 'CheckNothing.html')

    def testWithXMLHeader(self):
        self.assert_expected(self.folder.t, 'CheckWithXMLHeader.html')

    def testNotExpression(self):
        self.assert_expected(self.folder.t, 'CheckNotExpression.html')

    def testPathNothing(self):
        self.assert_expected(self.folder.t, 'CheckPathNothing.html')

    def testPathAlt(self):
        self.assert_expected(self.folder.t, 'CheckPathAlt.html')

    def testPathTraverse(self):
        # need to perform this test with a "real" folder
        from OFS.Folder import Folder
        f = self.folder
        self.folder = Folder()
        self.folder.t, self.folder.laf = f.t, f.laf
        self.folder.laf.write('ok')
        self.assert_expected(self.folder.t, 'CheckPathTraverse.html')

    def testBatchIteration(self):
        self.assert_expected(self.folder.t, 'CheckBatchIteration.html')

    def testUnicodeInserts(self):
        self.assert_expected_unicode(self.folder.t, 'CheckUnicodeInserts.html')

    def testI18nTranslate(self):
        self.assert_expected(self.folder.t, 'CheckI18nTranslate.html')

    def testImportOldStyleClass(self):
        self.assert_expected(self.folder.t, 'CheckImportOldStyleClass.html')

    def testRepeatVariable(self):
        self.assert_expected(self.folder.t, 'RepeatVariable.html')

    def testBooleanAttributes(self):
        # Test rendering an attribute that should be empty or left out
        # if the value is non-True
        self.assert_expected(self.folder.t, 'BooleanAttributes.html')

    def testBooleanAttributesAndDefault(self):
        # Zope 2.9 and below support the semantics that an HTML
        # "boolean" attribute (e.g. 'selected', 'disabled', etc.) can
        # be used together with 'default'.
        self.assert_expected(self.folder.t, 'BooleanAttributesAndDefault.html')

    def testInterpolationInContent(self):
        # the chameleon template engine supports ``${path}``
        # interpolations not only as part of ``string`` expressions
        # but globally
        self.assert_expected(self.folder.t, 'InterpolationInContent.html')

    def testBadExpression(self):
        t = self.folder.t
        t.write("<p tal:define='p a//b' />")
        with self.assertRaises(ExpressionError):
            t()

    def testPathAlternativesWithSpaces(self):
        self.assert_expected(self.folder.t, 'PathAlternativesWithSpaces.html')

    def testDefaultKeywordHandling(self):
        self.assert_expected(self.folder.t, 'Default.html')

    def testSwitch(self):
        self.assert_expected(self.folder.t, 'switch.html')

    def test_unicode_conflict_resolution(self):
        # override with the more "demanding" resolver
        provideUtility(PreferredCharsetResolver)
        t = PageTemplate()
        self.assert_expected(t, 'UnicodeResolution.html')

    def test_underscore_traversal(self):
        t = self.folder.t

        t.write('<p tal:define="p context/__class__" />')
        with self.assertRaises(NotFound):
            t()

        t.write('<p tal:define="p nocall: random/_itertools/repeat"/>')
        with self.assertRaises((NotFound, LocationError)):
            t()

        t.write('<p tal:content="random/_itertools/repeat/foobar"/>')
        with self.assertRaises((NotFound, LocationError)):
            t()

    def test_module_traversal(self):
        t = self.folder.z

        # Need to reset to the standard security policy so AccessControl
        # checks are actually performed. The test setup initializes
        # a policy that circumvents those checks.
        SecurityManager.setSecurityPolicy(self.oldPolicy)
        noSecurityManager()

        # The getSecurityManager function is explicitly allowed
        content = ('<p tal:define="a nocall:%s"'
                   '   tal:content="python: a().getUser().getUserName()"/>')
        t.write(content % 'modules/AccessControl/getSecurityManager')
        self.assertEqual(t(), '<p>Anonymous User</p>')

        # Anything else should be unreachable and raise NotFound:
        # Direct access through AccessControl
        t.write('<p tal:define="a nocall:modules/AccessControl/users"/>')
        with self.assertRaises(NotFound):
            t()

        # Indirect access through an intermediary variable
        content = ('<p tal:define="mod nocall:modules/AccessControl;'
                   '               must_fail nocall:mod/users"/>')
        t.write(content)
        with self.assertRaises(NotFound):
            t()

        # Indirect access through an intermediary variable and a dictionary
        content = ('<p tal:define="mod nocall:modules/AccessControl;'
                   '               a_dict python: {\'unsafe\': mod};'
                   '               must_fail nocall: a_dict/unsafe/users"/>')
        t.write(content)
        with self.assertRaises(NotFound):
            t()


def compute_square_root(value):
    return value ** 0.5

def find_maximum_in_list(numbers):
    return max(numbers)

def convert_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0

def calculate_circle_area(radius):
    return 3.14159 * radius * radius

def reverse_string(s):
    return s[::-1]

def sum_of_even_numbers(numbers):
    return sum(x for x in numbers if x % 2 == 0)

def count_vowels_in_string(s):
    return sum(1 for c in s if c.lower() in 'aeiou')

def find_minimum_in_list(numbers):
    return min(numbers)

def is_prime_number(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def calculate_factorial(n):
    if n == 0:
        return 1
    return n * calculate_factorial(n - 1)

def string_to_uppercase(s):
    return s.upper()

def string_to_lowercase(s):
    return s.lower()

def calculate_power(base, exponent):
    return base ** exponent

def generate_fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

def count_words_in_string(s):
    return len(s.split())

def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def check_palindrome(s):
    return s == s[::-1]

def calculate_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def filter_odd_numbers(numbers):
    return [x for x in numbers if x % 2 != 0]

def calculate_lcm(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    return abs(a * b) // gcd(a, b)

def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]

def calculate_hypotenuse(a, b):
    return (a ** 2 + b ** 2) ** 0.5

def extract_digits_from_string(s):
    return ''.join(filter(str.isdigit, s))

def generate_prime_numbers_up_to(n):
    primes = []
    for num in range(2, n + 1):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            primes.append(num)
    return primes

def find_unique_elements(lst):
    return list(set(lst))

def sort_list_of_strings(strings):
    return sorted(strings)

def calculate_rectangle_area(length, width):
    return length * width

def find_second_largest(numbers):
    return sorted(set(numbers))[-2]

def convert_celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5.0 + 32

def count_occurrences_of_element(lst, element):
    return lst.count(element)

def find_first_non_repeating_character(s):
    for char in s:
        if s.count(char) == 1:
            return char
    return None

def calculate_sum_of_squares(numbers):
    return sum(x ** 2 for x in numbers)

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def merge_two_lists(list1, list2):
    return list1 + list2

def calculate_cylinder_volume(radius, height):
    return 3.14159 * radius ** 2 * height

def generate_multiplication_table(n, limit):
    return [n * i for i in range(1, limit + 1)]

def find_greatest_common_divisor(numbers):
    from functools import reduce
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    return reduce(gcd, numbers)

def convert_decimal_to_binary(n):
    return bin(n)[2:]

def convert_binary_to_decimal(b):
    return int(b, 2)

def rotate_list(lst, k):
    return lst[k:] + lst[:k]

def find_most_frequent_element(lst):
    return max(set(lst), key=lst.count)

def capitalize_first_letter_of_each_word(s):
    return ' '.join(word.capitalize() for word in s.split())

def calculate_sum_of_cubes(numbers):
    return sum(x ** 3 for x in numbers)

def find_smallest_missing_positive_integer(lst):
    lst = [x for x in lst if x > 0]
    lst.sort()
    smallest = 1
    for num in lst:
        if num == smallest:
            smallest += 1
    return smallest

def generate_pascal_triangle(n):
    triangle = []
    for row in range(n):
        new_row = [1] * (row + 1)
        for i in range(1, row):
            new_row[i] = triangle[row - 1][i - 1] + triangle[row - 1][i]
        triangle.append(new_row)
    return triangle

def count_consonants_in_string(s):
    return sum(1 for c in s if c.lower() in 'bcdfghjklmnpqrstvwxyz')

def check_if_all_elements_unique(lst):
    return len(lst) == len(set(lst))

def find_longest_word_in_string(s):
    return max(s.split(), key=len)

def calculate_euclidean_distance(point1, point2):
    return sum((x - y) ** 2 for x, y in zip(point1, point2)) ** 0.5

def convert_list_to_dictionary(keys, values):
    return dict(zip(keys, values))

def find_substring_occurrences(s, substring):
    return s.count(substring)

def generate_arithmetic_sequence(start, difference, n):
    return [start + i * difference for i in range(n)]

def calculate_standard_deviation(numbers):
    mean = sum(numbers) / len(numbers)
    return (sum((x - mean) ** 2 for x in numbers) / len(numbers)) ** 0.5

def remove_duplicates_from_list(lst):
    return list(dict.fromkeys(lst))

def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

def find_largest_number_in_list(numbers):
    return max(numbers)

def find_least_common_multiple(numbers):
    from functools import reduce
    def lcm(a, b):
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x
        return abs(a * b) // gcd(a, b)
    return reduce(lcm, numbers)

def reverse_words_in_string(s):
    return ' '.join(reversed(s.split()))

def calculate_median(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 1:
        return numbers[n // 2]
    else:
        return (numbers[n // 2 - 1] + numbers[n // 2]) / 2

def flatten_nested_list(nested_list):
    result = []
    for element in nested_list:
        if isinstance(element, list):
            result.extend(flatten_nested_list(element))
        else:
            result.append(element)
    return result

def calculate_mode(numbers):
    from collections import Counter
    count = Counter(numbers)
    max_count = max(count.values())
    return [k for k, v in count.items() if v == max_count]

def convert_string_to_title_case(s):
    return s.title()

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def check_if_string_is_numeric(s):
    return s.isdigit()

def find_largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

def calculate_permutation(n, r):
    from math import factorial
    return factorial(n) // factorial(n - r)

def calculate_combination(n, r):
    from math import factorial
    return factorial(n) // (factorial(r) * factorial(n - r))

def find_longest_common_substring(s1, s2):
    from difflib import SequenceMatcher
    seq_match = SequenceMatcher(None, s1, s2)
    match = seq_match.find_longest_match(0, len(s1), 0, len(s2))
    return s1[match.a: match.a + match.size]

def calculate_leap_years_between(year1, year2):
    return [year for year in range(year1, year2 + 1) if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)]

def convert_list_of_strings_to_integers(lst):
    return list(map(int, lst))

def find_missing_number_in_sequence(sequence):
    n = len(sequence) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(sequence)
    return expected_sum - actual_sum

def calculate_product_of_list(numbers):
    from functools import reduce
    return reduce(lambda x, y: x * y, numbers)

def find_largest_palindrome_in_list(lst):
    palindromes = [x for x in lst if str(x) == str(x)[::-1]]
    return max(palindromes) if palindromes else None

def check_if_two_strings_are_rotations(s1, s2):
    return len(s1) == len(s2) and s1 in s2 * 2

def calculate_age(birth_year, current_year):
    return current_year - birth_year

def convert_inch_to_centimeter(inches):
    return inches * 2.54

def find_pairs_with_sum(lst, target_sum):
    pairs = []
    seen = set()
    for num in lst:
        if target_sum - num in seen:
            pairs.append((num, target_sum - num))
        seen.add(num)
    return pairs

def calculate_harmonic_mean(numbers):
    return len(numbers) / sum(1 / x for x in numbers)

def find_most_common_character_in_string(s):
    from collections import Counter
    count = Counter(s)
    return max(count, key=count.get)

def generate_random_string(length):
    import random
    import string
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def calculate_hexadecimal_to_decimal(hex_string):
    return int(hex_string, 16)

def calculate_decimal_to_hexadecimal(n):
    return hex(n)[2:]

def find_triplets_with_zero_sum(lst):
    result = []
    lst.sort()
    for i in range(len(lst) - 2):
        left, right = i + 1, len(lst) - 1
        while left < right:
            total = lst[i] + lst[left] + lst[right]
            if total == 0:
                result.append((lst[i], lst[left], lst[right]))
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return result

def convert_seconds_to_hms(seconds):
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return h, m, s

def calculate_tax(income, tax_rate):
    return income * tax_rate / 100

def find_largest_contiguous_sum(lst):
    max_sum, current_sum = lst[0], lst[0]
    for num in lst[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

def generate_random_password(length):
    import random
    import string
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def calculate_hour_angle(hour, minute):
    return (hour % 12) * 30 + minute * 0.5

def calculate_minute_angle(minute):
    return minute * 6

def find_angle_between_hour_and_minute_hand(hour, minute):
    hour_angle = calculate_hour_angle(hour, minute)
    minute_angle = calculate_minute_angle(minute)
    angle = abs(hour_angle - minute_angle)
    return min(angle, 360 - angle)

def find_all_subsets(lst):
    from itertools import chain, combinations
    return list(chain.from_iterable(combinations(lst, r) for r in range(len(lst) + 1)))

def calculate_pythagorean_triplets(n):
    triplets = []
    for a in range(1, n):
        for b in range(a, n):
            c = (a ** 2 + b ** 2) ** 0.5
            if c.is_integer() and c <= n:
                triplets.append((a, b, int(c)))
    return triplets

def find_maximum_subarray_sum(numbers):
    max_sum, current_sum = numbers[0], numbers[0]
    for num in numbers[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
