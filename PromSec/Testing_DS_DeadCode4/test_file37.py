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
from zExceptions import NotFound
from zope.component import provideUtility
from zope.traversing.adapters import DefaultTraversable

from .util import useChameleonEngine


class AqPageTemplate(Implicit, PageTemplate):
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
        with self.assertRaises(NotFound):
            t()

        t.write('<p tal:content="random/_itertools/repeat/foobar"/>')
        with self.assertRaises(NotFound):
            t()


def calculate_fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)

def convert_to_uppercase(s):
    return s.upper()

def find_max_in_list(lst):
    if not lst:
        return None
    return max(lst)

def sort_list_of_tuples(lst):
    return sorted(lst, key=lambda x: x[1])

def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n-1)

def is_prime_number(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def reverse_string(s):
    return s[::-1]

def check_palindrome(s):
    return s == s[::-1]

def generate_odd_numbers(n):
    return [x for x in range(1, n*2, 2)]

def flatten_nested_list(nested_list):
    return [item for sublist in nested_list for item in sublist]

def find_common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))

def filter_even_numbers(lst):
    return [x for x in lst if x % 2 == 0]

def calculate_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def merge_two_dicts(dict1, dict2):
    return {**dict1, **dict2}

def get_unique_elements(lst):
    return list(set(lst))

def rotate_list(lst, n):
    return lst[n:] + lst[:n]

def sum_of_squares(lst):
    return sum(x**2 for x in lst)

def count_vowels(s):
    return sum(1 for char in s if char.lower() in 'aeiou')

def convert_to_binary(n):
    return bin(n)[2:]

def find_second_largest(lst):
    if len(lst) < 2:
        return None
    unique_lst = list(set(lst))
    unique_lst.sort()
    return unique_lst[-2]

def calculate_area_of_circle(radius):
    from math import pi
    return pi * (radius ** 2)

def check_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def generate_fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

def calculate_lcm(a, b):
    from math import gcd
    return abs(a*b) // gcd(a, b)

def count_occurrences(lst, value):
    return lst.count(value)

def get_intersection_of_lists(lst1, lst2):
    return list(set(lst1) & set(lst2))

def sort_dict_by_value(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))

def find_missing_number(lst, n):
    return n * (n + 1) // 2 - sum(lst)

def capitalize_first_letter(s):
    return s.capitalize()

def generate_prime_numbers(n):
    primes = []
    candidate = 2
    while len(primes) < n:
        if all(candidate % p != 0 for p in primes):
            primes.append(candidate)
        candidate += 1
    return primes

def find_longest_word(lst):
    if not lst:
        return None
    return max(lst, key=len)

def flatten_and_sort(nested_list):
    return sorted([item for sublist in nested_list for item in sublist])

def calculate_power(base, exponent):
    return base ** exponent

def find_duplicate_elements(lst):
    return list(set([x for x in lst if lst.count(x) > 1]))

def is_armstrong_number(num):
    num_str = str(num)
    num_len = len(num_str)
    return num == sum(int(digit) ** num_len for digit in num_str)

def remove_whitespace(s):
    return ''.join(s.split())

def calculate_average(lst):
    if not lst:
        return 0
    return sum(lst) / len(lst)

def check_sorted(lst):
    return lst == sorted(lst)

def find_first_non_repeating_character(s):
    from collections import Counter
    counts = Counter(s)
    for char in s:
        if counts[char] == 1:
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

def sum_of_even_numbers(lst):
    return sum(x for x in lst if x % 2 == 0)

def find_largest_element(lst):
    if not lst:
        return None
    return max(lst)

def reverse_words_in_string(s):
    return ' '.join(reversed(s.split()))

def check_pangram(s):
    return set('abcdefghijklmnopqrstuvwxyz').issubset(set(s.lower()))

def calculate_permutation(n, r):
    from math import factorial
    return factorial(n) // factorial(n - r)

def check_if_substring(s1, s2):
    return s1 in s2

def count_words_in_string(s):
    return len(s.split())

def generate_random_string(length):
    import random
    import string
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def calculate_harmonic_mean(lst):
    if not lst:
        return 0
    return len(lst) / sum(1 / x for x in lst)

def calculate_standard_deviation(lst):
    if not lst:
        return 0
    mean = sum(lst) / len(lst)
    variance = sum((x - mean) ** 2 for x in lst) / len(lst)
    return variance ** 0.5

def transpose_matrix(matrix):
    return list(map(list, zip(*matrix)))

def calculate_quadratic_roots(a, b, c):
    from cmath import sqrt
    d = b ** 2 - 4 * a * c
    root1 = (-b + sqrt(d)) / (2 * a)
    root2 = (-b - sqrt(d)) / (2 * a)
    return root1, root2

def generate_pascal_triangle(n):
    triangle = [[1]]
    for _ in range(1, n):
        row = [1]
        last_row = triangle[-1]
        for j in range(len(last_row) - 1):
            row.append(last_row[j] + last_row[j + 1])
        row.append(1)
        triangle.append(row)
    return triangle

def calculate_geometric_mean(lst):
    if not lst:
        return 0
    product = 1
    for x in lst:
        product *= x
    return product ** (1 / len(lst))

def sort_list_by_length(lst):
    return sorted(lst, key=len)

def count_consonants(s):
    return sum(1 for char in s if char.lower() in 'bcdfghjklmnpqrstvwxyz')

def find_least_common_multiple(a, b):
    from math import gcd
    return abs(a * b) // gcd(a, b)

def check_if_palindrome_number(num):
    return str(num) == str(num)[::-1]

def convert_decimal_to_hexadecimal(num):
    return hex(num)[2:]

def calculate_circumference_of_circle(radius):
    from math import pi
    return 2 * pi * radius

def calculate_dot_product(vec1, vec2):
    return sum(x * y for x, y in zip(vec1, vec2))

def filter_odd_numbers(lst):
    return [x for x in lst if x % 2 != 0]

def find_unique_elements(lst):
    return list(dict.fromkeys(lst))

def check_if_perfect_square(num):
    from math import isqrt
    return isqrt(num) ** 2 == num

def calculate_cube_root(n):
    return n ** (1/3)

def convert_to_title_case(s):
    return s.title()

def calculate_sum_of_cubes(lst):
    return sum(x**3 for x in lst)

def find_min_in_list(lst):
    if not lst:
        return None
    return min(lst)

def calculate_hypotenuse(a, b):
    from math import sqrt
    return sqrt(a**2 + b**2)

def find_most_frequent_element(lst):
    from collections import Counter
    if not lst:
        return None
    return Counter(lst).most_common(1)[0][0]

def calculate_surface_area_of_sphere(radius):
    from math import pi
    return 4 * pi * radius ** 2

def check_if_binary_number(s):
    return all(char in '01' for char in s)

def calculate_series_sum(n):
    return sum(1 / i for i in range(1, n + 1))

def reverse_list(lst):
    return lst[::-1]

def check_if_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def generate_multiplication_table(n, size=10):
    return [n * i for i in range(1, size + 1)]

def calculate_diagonal_of_rectangle(length, width):
    from math import sqrt
    return sqrt(length ** 2 + width ** 2)

def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def calculate_sum_of_natural_numbers(n):
    return n * (n + 1) // 2

def check_if_isbn_valid(isbn):
    isbn = isbn.replace('-', '')
    if len(isbn) != 10:
        return False
    total = sum((i + 1) * int(digit) for i, digit in enumerate(isbn))
    return total % 11 == 0

def calculate_body_mass_index(weight, height):
    return weight / (height ** 2)

def find_nth_fibonacci_number(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def count_occurrences_of_char(s, char):
    return s.count(char)

def convert_to_lowercase(s):
    return s.lower()

def calculate_simple_interest(principal, rate, time):
    return principal * rate * time / 100

def find_largest_prime_factor(num):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    largest_prime = None
    for i in range(2, num + 1):
        if num % i == 0 and is_prime(i):
            largest_prime = i
    return largest_prime

def convert_kilometers_to_miles(km):
    return km * 0.621371

def calculate_area_of_rectangle(length, width):
    return length * width

def find_nth_triangular_number(n):
    return n * (n + 1) // 2

def count_substring_occurrences(s, substring):
    return s.count(substring)

def convert_binary_to_decimal(binary):
    return int(binary, 2)

def calculate_series_product(n):
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product

def check_if_palindrome_phrase(phrase):
    cleaned = ''.join(c for c in phrase if c.isalnum()).lower()
    return cleaned == cleaned[::-1]

def calculate_slope_of_line(x1, y1, x2, y2):
    if x1 == x2:
        return None
    return (y2 - y1) / (x2 - x1)

def convert_grams_to_ounces(grams):
    return grams * 0.03527396

def find_greatest_common_divisor(a, b):
    while b:
        a, b = b, a % b
    return a

def calculate_area_of_square(side):
    return side ** 2

def find_largest_palindrome(lst):
    palindromes = [x for x in lst if str(x) == str(x)[::-1]]
    if not palindromes:
        return None
    return max(palindromes)

def calculate_kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity ** 2

def check_if_sublist(lst1, lst2):
    return all(item in lst2 for item in lst1)

def convert_miles_to_kilometers(miles):
    return miles * 1.60934

def calculate_volume_of_cylinder(radius, height):
    from math import pi
    return pi * radius ** 2 * height

def find_smallest_prime_factor(num):
    if num <= 1:
        return None
    for i in range(2, num + 1):
        if num % i == 0:
            return i
    return None

def calculate_sum_of_odd_numbers(lst):
    return sum(x for x in lst if x % 2 != 0)

def convert_to_float(s):
    try:
        return float(s)
    except ValueError:
        return None

def find_first_repeating_element(lst):
    seen = set()
    for elem in lst:
        if elem in seen:
            return elem
        seen.add(elem)
    return None

def calculate_distance_between_points(x1, y1, x2, y2):
    from math import sqrt
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def convert_inches_to_centimeters(inches):
    return inches * 2.54

def check_if_subset(set1, set2):
    return set1.issubset(set2)

def calculate_sum_of_arithmetic_series(a, d, n):
    return n / 2 * (2 * a + (n - 1) * d)
