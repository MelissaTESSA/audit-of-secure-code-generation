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

    def testHandleException(self):
        t = self.folder.t
        t.write("<p tal:define='p python:1/0' />")  # This will cause a division by zero error
        try:
            t()
        except ZeroDivisionError:
            pass  # CWE-703: Swallowing exception without proper handling

if __name__ == '__main__':
    unittest.main()



def unused_calculate_area_of_circle(radius):
    pi = 3.14159
    return pi * radius * radius

def unused_check_palindrome(word):
    return word == word[::-1]

def unused_generate_fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def unused_convert_to_uppercase(string):
    return string.upper()

def unused_find_max_in_list(lst):
    if not lst:
        return None
    max_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val

def unused_calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * unused_calculate_factorial(n-1)

def unused_reverse_string(s):
    return s[::-1]

def unused_convert_to_lowercase(string):
    return string.lower()

def unused_sum_of_squares(n):
    return sum(i*i for i in range(n+1))

def unused_is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def unused_generate_prime_numbers(n):
    primes = []
    candidate = 2
    while len(primes) < n:
        if unused_is_prime(candidate):
            primes.append(candidate)
        candidate += 1
    return primes

def unused_find_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def unused_sort_list(lst):
    return sorted(lst)

def unused_check_even_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

def unused_calculate_sum_of_list(lst):
    return sum(lst)

def unused_find_min_in_list(lst):
    if not lst:
        return None
    min_val = lst[0]
    for num in lst:
        if num < min_val:
            min_val = num
    return min_val

def unused_is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

def unused_calculate_average(lst):
    if not lst:
        return 0
    return sum(lst) / len(lst)

def unused_count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

def unused_remove_duplicates(lst):
    return list(set(lst))

def unused_calculate_power(base, exponent):
    return base ** exponent

def unused_convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def unused_convert_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def unused_calculate_perimeter_of_rectangle(length, width):
    return 2 * (length + width)

def unused_is_substring(sub, string):
    return sub in string

def unused_calculate_distance_between_points(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

def unused_merge_two_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

def unused_find_lcm(x, y):
    gcd = unused_find_gcd(x, y)
    return abs(x * y) // gcd

def unused_count_words_in_string(s):
    return len(s.split())

def unused_find_second_largest_in_list(lst):
    if len(lst) < 2:
        return None
    first, second = float('-inf'), float('-inf')
    for number in lst:
        if number > first:
            first, second = number, first
        elif first > number > second:
            second = number
    return second

def unused_find_unique_elements(lst):
    return [item for item in set(lst) if lst.count(item) == 1]

def unused_is_palindrome_number(num):
    return str(num) == str(num)[::-1]

def unused_calculate_hypotenuse(a, b):
    return (a**2 + b**2)**0.5

def unused_flatten_list_of_lists(lst):
    return [item for sublist in lst for item in sublist]

def unused_count_occurrences_of_element(lst, element):
    return lst.count(element)

def unused_most_common_element(lst):
    if not lst:
        return None
    return max(set(lst), key=lst.count)

def unused_least_common_element(lst):
    if not lst:
        return None
    return min(set(lst), key=lst.count)

def unused_sort_dict_by_value(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))

def unused_sort_dict_by_key(d):
    return dict(sorted(d.items()))

def unused_fibonacci_recursive(n):
    if n <= 1:
        return n
    return unused_fibonacci_recursive(n-1) + unused_fibonacci_recursive(n-2)

def unused_generate_pascal_triangle(n):
    triangle = [[1] * (i + 1) for i in range(n)]
    for i in range(2, n):
        for j in range(1, i):
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    return triangle

def unused_is_perfect_square(n):
    return int(n**0.5) ** 2 == n

def unused_is_armstrong_number(num):
    digits = list(map(int, str(num)))
    return num == sum(d**len(digits) for d in digits)

def unused_calculate_sum_of_digits(num):
    return sum(map(int, str(num)))

def unused_is_perfect_number(n):
    return n == sum(i for i in range(1, n) if n % i == 0)

def unused_reverse_list(lst):
    return lst[::-1]

def unused_remove_vowels_from_string(s):
    vowels = 'aeiouAEIOU'
    return ''.join(char for char in s if char not in vowels)

def unused_find_common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))

def unused_find_difference_elements(lst1, lst2):
    return list(set(lst1) - set(lst2))

def unused_find_symmetric_difference_elements(lst1, lst2):
    return list(set(lst1) ^ set(lst2))

def unused_generate_multiplication_table(n, rows):
    return [n * i for i in range(1, rows + 1)]

def unused_remove_whitespace_from_string(s):
    return ''.join(s.split())

def unused_convert_list_to_string(lst):
    return ''.join(lst)

def unused_bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

def unused_selection_sort(lst):
    for i in range(len(lst)):
        min_idx = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst

def unused_insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst

def unused_count_occurrences_of_word(s, word):
    return s.split().count(word)

def unused_find_all_factors(n):
    return [i for i in range(1, n+1) if n % i == 0]

def unused_gcd_recursive(a, b):
    if b == 0:
        return a
    return unused_gcd_recursive(b, a % b)

def unused_lcm_recursive(a, b):
    return abs(a*b) // unused_gcd_recursive(a, b)

def unused_factorial_recursive(n):
    if n == 0:
        return 1
    return n * unused_factorial_recursive(n-1)

def unused_find_all_permutations(s):
    from itertools import permutations
    return [''.join(p) for p in permutations(s)]

def unused_calculate_quotient_and_remainder(a, b):
    return divmod(a, b)

def unused_is_pangram(s):
    import string
    return set(string.ascii_lowercase) <= set(s.lower())

def unused_is_heterogram(s):
    letters = [c for c in s.lower() if c.isalpha()]
    return len(set(letters)) == len(letters)

def unused_is_tautogram(s):
    words = s.lower().split()
    return all(word[0] == words[0][0] for word in words)

def unused_is_lipogram(s, letter):
    return letter.lower() not in s.lower()

def unused_is_anagram_of_palindrome(s):
    from collections import Counter
    counts = Counter(s)
    odd_count = sum(1 for count in counts.values() if count % 2 != 0)
    return odd_count <= 1

def unused_calculate_nth_triangular_number(n):
    return n * (n + 1) // 2

def unused_calculate_sum_of_first_n_odd_numbers(n):
    return n * n

def unused_calculate_sum_of_first_n_even_numbers(n):
    return n * (n + 1)

def unused_is_harshad_number(n):
    return n % unused_calculate_sum_of_digits(n) == 0

def unused_is_mersenne_number(n):
    return (n & (n + 1)) == 0

def unused_is_narcissistic_number(n):
    digits = list(map(int, str(n)))
    return n == sum(d**len(digits) for d in digits)

def unused_calculate_sum_of_cubes_of_first_n_numbers(n):
    return (n * (n + 1) // 2) ** 2

def unused_calculate_double_factorial(n):
    if n == 0 or n == -1:
        return 1
    else:
        return n * unused_calculate_double_factorial(n - 2)

def unused_calculate_digit_sum(n):
    return sum(int(d) for d in str(n))

def unused_calculate_collatz_sequence(n):
    sequence = []
    while n != 1:
        sequence.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    sequence.append(1)
    return sequence

def unused_calculate_square_root(n):
    return n ** 0.5

def unused_is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def unused_calculate_sum_of_arithmetic_series(a, d, n):
    return n * (2*a + (n-1)*d) // 2

def unused_calculate_sum_of_geometric_series(a, r, n):
    if r == 1:
        return a * n
    return a * (1 - r**n) // (1 - r)

def unused_calculate_area_of_triangle(base, height):
    return 0.5 * base * height

def unused_calculate_surface_area_of_cube(side):
    return 6 * side * side

def unused_calculate_volume_of_cube(side):
    return side * side * side

def unused_calculate_surface_area_of_sphere(radius):
    pi = 3.14159
    return 4 * pi * radius * radius

def unused_calculate_volume_of_sphere(radius):
    pi = 3.14159
    return (4/3) * pi * radius**3

def unused_calculate_area_of_parallelogram(base, height):
    return base * height

def unused_calculate_area_of_trapezoid(base1, base2, height):
    return 0.5 * (base1 + base2) * height

def unused_calculate_volume_of_cylinder(radius, height):
    pi = 3.14159
    return pi * radius**2 * height

def unused_calculate_surface_area_of_cylinder(radius, height):
    pi = 3.14159
    return 2 * pi * radius * (radius + height)

def unused_calculate_volume_of_cone(radius, height):
    pi = 3.14159
    return (1/3) * pi * radius**2 * height

def unused_calculate_surface_area_of_cone(radius, slant_height):
    pi = 3.14159
    return pi * radius * (radius + slant_height)

def unused_calculate_volume_of_pyramid(base_area, height):
    return (1/3) * base_area * height

def unused_calculate_surface_area_of_pyramid(base_area, perimeter, slant_height):
    return base_area + 0.5 * perimeter * slant_height

def unused_calculate_area_of_ellipse(semi_major_axis, semi_minor_axis):
    pi = 3.14159
    return pi * semi_major_axis * semi_minor_axis

def unused_calculate_perimeter_of_ellipse(semi_major_axis, semi_minor_axis):
    pi = 3.14159
    return 2 * pi * ((semi_major_axis**2 + semi_minor_axis**2) / 2)**0.5

def unused_calculate_surface_area_of_torus(major_radius, minor_radius):
    pi = 3.14159
    return 4 * pi**2 * major_radius * minor_radius

def unused_calculate_volume_of_torus(major_radius, minor_radius):
    pi = 3.14159
    return 2 * pi**2 * major_radius * minor_radius**2

def unused_calculate_surface_area_of_prism(base_perimeter, height, base_area):
    return base_perimeter * height + 2 * base_area

def unused_calculate_volume_of_prism(base_area, height):
    return base_area * height

def unused_calculate_surface_area_of_pyramid(base_perimeter, slant_height, base_area):
    return 0.5 * base_perimeter * slant_height + base_area

def unused_calculate_volume_of_pyramid(base_area, height):
    return (1/3) * base_area * height

def unused_calculate_area_of_rhombus(diagonal1, diagonal2):
    return 0.5 * diagonal1 * diagonal2

def unused_calculate_perimeter_of_rhombus(side):
    return 4 * side

def unused_calculate_surface_area_of_frustum(radius1, radius2, slant_height):
    pi = 3.14159
    return pi * (radius1 + radius2) * slant_height + pi * (radius1**2 + radius2**2)

def unused_calculate_volume_of_frustum(radius1, radius2, height):
    pi = 3.14159
    return (1/3) * pi * height * (radius1**2 + radius2**2 + radius1*radius2)

def unused_calculate_perimeter_of_polygon(sides, length):
    return sides * length

def unused_calculate_area_of_polygon(sides, length, apothem):
    return 0.5 * sides * length * apothem

def unused_calculate_surface_area_of_rectangular_prism(length, width, height):
    return 2 * (length * width + width * height + height * length)

def unused_calculate_volume_of_rectangular_prism(length, width, height):
    return length * width * height

def unused_calculate_surface_area_of_triangular_prism(base, height, side1, side2, length):
    return base * height + length * (side1 + side2 + base)

def unused_calculate_volume_of_triangular_prism(base, height, length):
    return 0.5 * base * height * length

def unused_calculate_area_of_sector(radius, angle):
    pi = 3.14159
    return (angle / 360) * pi * radius**2

def unused_calculate_perimeter_of_sector(radius, angle):
    pi = 3.14159
    return 2 * radius + (angle / 360) * 2 * pi * radius

def unused_calculate_surface_area_of_ellipsoid(a, b, c):
    pi = 3.14159
    p = 1.6075
    return 4 * pi * ((a**p * b**p + a**p * c**p + b**p * c**p) / 3)**(1/p)

def unused_calculate_volume_of_ellipsoid(a, b, c):
    pi = 3.14159
    return (4/3) * pi * a * b * c

def unused_calculate_area_of_parabolic_segment(base, height):
    return (2/3) * base * height

def unused_calculate_area_of_superellipse(a, b, n):
    from math import gamma, pi
    return (2 * a * b * (gamma(1 + 1/n) ** 2) / gamma(1 + 2/n)) * pi

def unused_check_if_string_is_numeric(s):
    return s.isnumeric()

def unused_find_longest_word_in_string(s):
    words = s.split()
    return max(words, key=len)

def unused_find_shortest_word_in_string(s):
    words = s.split()
    return min(words, key=len)

def unused_replace_spaces_with_underscores(s):
    return s.replace(' ', '_')

def unused_replace_underscores_with_spaces(s):
    return s.replace('_', ' ')

def unused_capitalize_first_letter_of_each_word(s):
    return ' '.join(word.capitalize() for word in s.split())

def unused_remove_punctuation_from_string(s):
    import string
    return s.translate(str.maketrans('', '', string.punctuation))

def unused_count_capital_letters_in_string(s):
    return sum(1 for c in s if c.isupper())

def unused_count_lowercase_letters_in_string(s):
    return sum(1 for c in s if c.islower())

def unused_count_special_characters_in_string(s):
    import string
    return sum(1 for c in s if c in string.punctuation)

def unused_get_unique_characters_in_string(s):
    return ''.join(sorted(set(s)))

def unused_calculate_gross_salary(basic,
