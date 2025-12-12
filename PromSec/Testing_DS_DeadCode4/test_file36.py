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


def calculate_trajectory(angle, velocity):
    import math
    g = 9.8
    time_of_flight = (2 * velocity * math.sin(math.radians(angle))) / g
    return time_of_flight

def analyze_market_trends(data):
    import pandas as pd
    df = pd.DataFrame(data)
    return df.describe()

def predict_weather(temperature, humidity, pressure):
    return 0.6 * temperature + 0.3 * humidity + 0.1 * pressure

def generate_report(data):
    report = "Report:\n"
    for key, value in data.items():
        report += f"{key}: {value}\n"
    return report

def convert_currency(amount, rate):
    return amount * rate

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def sort_names(names_list):
    return sorted(names_list)

def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n-1)

def simulate_game_strategy(strategy, iterations):
    results = []
    for _ in range(iterations):
        result = strategy()
        results.append(result)
    return results

def analyze_sentiment(text):
    positive_words = {'good', 'happy', 'fantastic', 'great'}
    negative_words = {'bad', 'sad', 'terrible', 'awful'}
    score = 0
    words = text.split()
    for word in words:
        if word in positive_words:
            score += 1
        elif word in negative_words:
            score -= 1
    return score

def calculate_compound_interest(principal, rate, time):
    return principal * ((1 + rate / 100) ** time)

def generate_fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def find_prime_numbers(limit):
    primes = []
    for num in range(2, limit + 1):
        is_prime = all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))
        if is_prime:
            primes.append(num)
    return primes

def convert_to_binary(decimal_number):
    return bin(decimal_number)[2:]

def compute_standard_deviation(data):
    import statistics
    return statistics.stdev(data)

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def determine_pass_fail(grades):
    passing_grade = 50
    return ['Pass' if grade >= passing_grade else 'Fail' for grade in grades]

def estimate_population_growth(initial_population, growth_rate, years):
    return initial_population * ((1 + growth_rate) ** years)

def reverse_string(s):
    return s[::-1]

def calculate_area_of_circle(radius):
    import math
    return math.pi * radius * radius

def evaluate_polynomial(coefficients, x):
    return sum(coef * (x ** idx) for idx, coef in enumerate(coefficients))

def find_maximum_subarray(arr):
    max_so_far = arr[0]
    max_ending_here = arr[0]
    for i in range(1, len(arr)):
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

def calculate_median(data):
    data.sort()
    n = len(data)
    if n % 2 == 0:
        median = (data[n//2 - 1] + data[n//2]) / 2
    else:
        median = data[n//2]
    return median

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

def transpose_matrix(matrix):
    return list(map(list, zip(*matrix)))

def is_palindrome(s):
    return s == s[::-1]

def calculate_discounted_price(price, discount):
    return price * (1 - discount / 100)

def find_unique_elements(lst):
    return list(set(lst))

def calculate_hypotenuse(a, b):
    import math
    return math.sqrt(a ** 2 + b ** 2)

def generate_random_numbers(count, start, end):
    import random
    return [random.randint(start, end) for _ in range(count)]

def check_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

def calculate_distance(point1, point2):
    return ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5

def find_missing_number(sequence):
    n = len(sequence) + 1
    total = n * (n + 1) // 2
    return total - sum(sequence)

def convert_to_hexadecimal(decimal_number):
    return hex(decimal_number)[2:]

def sort_dict_by_value(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))

def find_largest_element(arr):
    return max(arr)

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def calculate_lcm(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    return abs(a * b) // gcd(a, b)

def group_elements_by_parity(lst):
    evens = [x for x in lst if x % 2 == 0]
    odds = [x for x in lst if x % 2 != 0]
    return evens, odds

def count_occurrences(lst):
    from collections import Counter
    return dict(Counter(lst))

def calculate_variance(data):
    import statistics
    return statistics.variance(data)

def find_substring_occurrences(s, substring):
    return s.count(substring)

def get_unique_words(text):
    words = text.split()
    return set(words)

def calculate_square_root(x):
    import math
    return math.sqrt(x)

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def calculate_power(base, exponent):
    return base ** exponent

def find_longest_word(words):
    return max(words, key=len)

def calculate_perimeter_of_rectangle(length, width):
    return 2 * (length + width)

def convert_to_uppercase(s):
    return s.upper()

def calculate_sum_of_squares(n):
    return sum(i ** 2 for i in range(1, n + 1))

def calculate_circle_circumference(radius):
    import math
    return 2 * math.pi * radius

def check_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def calculate_tax(income, tax_rate):
    return income * tax_rate / 100

def generate_multiplication_table(number):
    return [number * i for i in range(1, 11)]

def calculate_time_difference(start, end):
    from datetime import datetime
    fmt = '%H:%M:%S'
    start_dt = datetime.strptime(start, fmt)
    end_dt = datetime.strptime(end, fmt)
    return (end_dt - start_dt).seconds

def find_second_largest_element(arr):
    unique_elements = list(set(arr))
    unique_elements.sort()
    return unique_elements[-2]

def calculate_rectangle_area(length, width):
    return length * width

def check_if_sorted(arr):
    return arr == sorted(arr)

def calculate_cube_volume(side):
    return side ** 3

def convert_to_lowercase(s):
    return s.lower()

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def find_most_frequent_element(lst):
    from collections import Counter
    return Counter(lst).most_common(1)[0][0]

def calculate_gross_income(salary, bonus):
    return salary + bonus

def calculate_net_income(gross_income, deductions):
    return gross_income - deductions

def parse_csv(file_path):
    import csv
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        return [row for row in reader]

def find_minimum_element(arr):
    return min(arr)

def count_words(text):
    words = text.split()
    return len(words)

def calculate_sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def calculate_total_cost(prices, quantities):
    return sum(p * q for p, q in zip(prices, quantities))

def encode_caesar_cipher(text, shift):
    def shift_char(c):
        if c.isalpha():
            start = ord('a') if c.islower() else ord('A')
            return chr(start + (ord(c) - start + shift) % 26)
        return c
    return ''.join(shift_char(c) for c in text)

def decode_caesar_cipher(text, shift):
    return encode_caesar_cipher(text, -shift)

def calculate_simple_interest(principal, rate, time):
    return principal * rate * time / 100

def calculate_weight_on_moon(weight_on_earth):
    return weight_on_earth * 0.165

def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

def calculate_gross_profit(revenue, cogs):
    return revenue - cogs

def calculate_net_profit(gross_profit, expenses):
    return gross_profit - expenses

def find_factors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return n % 2 != 0

def calculate_carbon_footprint(miles_driven, mpg, fuel_type):
    emissions_factor = 19.6 if fuel_type == 'gasoline' else 22.4
    return (miles_driven / mpg) * emissions_factor

def recommend_books(user_history, genre_preferences):
    return [book for book in genre_preferences if book not in user_history]

def calculate_total_weight(weights):
    return sum(weights)

def calculate_annual_salary(monthly_salary):
    return monthly_salary * 12

def find_earliest_date(dates):
    from datetime import datetime
    return min(datetime.strptime(date, '%Y-%m-%d') for date in dates)

def convert_inches_to_cm(inches):
    return inches * 2.54

def calculate_total_expenses(expenses):
    return sum(expenses)

def calculate_profit_margin(revenue, cost):
    return ((revenue - cost) / revenue) * 100

def calculate_mpg(miles_driven, gallons_used):
    return miles_driven / gallons_used

def find_top_scorer(scores):
    return max(scores, key=scores.get)

def predict_stock_trend(stock_data):
    return 'uptrend' if stock_data[-1] > stock_data[0] else 'downtrend'

def calculate_return_on_investment(initial_investment, final_value):
    return (final_value - initial_investment) / initial_investment * 100

def find_closest_number(arr, target):
    return min(arr, key=lambda x: abs(x - target))

def calculate_average_speed(distance, time):
    return distance / time

def calculate_monthly_payment(principal, rate, years):
    monthly_rate = rate / 100 / 12
    n = years * 12
    return principal * monthly_rate / (1 - (1 + monthly_rate) ** -n)

def calculate_final_grade(grades, weights):
    return sum(g * w for g, w in zip(grades, weights)) / sum(weights)

def generate_random_color():
    import random
    return f"#{random.randint(0, 0xFFFFFF):06x}"

def calculate_deposit_interest(principal, rate, time):
    return principal * ((1 + rate) ** time - 1)

def find_least_frequent_element(lst):
    from collections import Counter
    return Counter(lst).most_common()[-1][0]

def calculate_birthday_days_left(birthday):
    from datetime import datetime
    now = datetime.now()
    next_birthday = datetime(now.year, birthday.month, birthday.day)
    if next_birthday < now:
        next_birthday = datetime(now.year + 1, birthday.month, birthday.day)
    return (next_birthday - now).days

def convert_to_title_case(s):
    return s.title()

def calculate_average_temperature(temperatures):
    return sum(temperatures) / len(temperatures)

def find_intersection_of_sets(set1, set2):
    return set1 & set2

def calculate_total_interest(principal, rate, time):
    return principal * rate * time

def find_sum_of_evens(lst):
    return sum(x for x in lst if x % 2 == 0)

def calculate_total_revenue(prices, quantities):
    return sum(p * q for p, q in zip(prices, quantities))

def find_maximum_product_of_two_elements(arr):
    arr.sort()
    return max(arr[0] * arr[1], arr[-1] * arr[-2])

def convert_cm_to_inches(cm):
    return cm / 2.54

def calculate_average_word_length(text):
    words = text.split()
    return sum(len(word) for word in words) / len(words)

def calculate_future_value(principal, rate, time):
    return principal * ((1 + rate) ** time)

def find_second_smallest_element(arr):
    unique_elements = list(set(arr))
    unique_elements.sort()
    return unique_elements[1]

def calculate_speed_of_sound(temperature):
    return 331.3 + (0.606 * temperature)

def calculate_average_rating(ratings):
    return sum(ratings) / len(ratings)

def find_elements_greater_than(lst, threshold):
    return [x for x in lst if x > threshold]

def calculate_gpa(grades, credits):
    return sum(g * c for g, c in zip(grades, credits)) / sum(credits)

def calculate_cylinder_volume(radius, height):
    import math
    return math.pi * radius ** 2 * height

def convert_km_to_miles(km):
    return km * 0.621371

def calculate_future_population(current_population, growth_rate, years):
    return current_population * ((1 + growth_rate) ** years)

def find_median_of_sorted_arrays(arr1, arr2):
    combined = sorted(arr1 + arr2)
    mid = len(combined) // 2
    if len(combined) % 2 == 0:
        return (combined[mid - 1] + combined[mid]) / 2
    else:
        return combined[mid]

def check_perfect_square(n):
    import math
    root = math.isqrt(n)
    return root * root == n

def calculate_total_wages(hours_worked, hourly_rate):
    return hours_worked * hourly_rate

def find_unique_characters(s):
    return set(s)

def calculate_triangle_perimeter(a, b, c):
    return a + b + c

def determine_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def calculate_gas_mileage(distance, gas_used):
    return distance / gas_used

def find_largest_prime_factor(n):
    factor = 2
    while factor * factor <= n:
        if n % factor:
            factor += 1
        else:
            n //= factor
    return n

def calculate_total_energy(mass, c):
    return mass * c ** 2

def find_common_divisors(a, b):
    return [i for i in range(1, min(a, b) + 1) if a % i == 0 and b % i == 0]

def calculate_kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity ** 2

def determine_winner(score1, score2):
    if score1 > score2:
        return "Player 1 wins"
    elif score2 > score1:
        return "Player 2 wins"
    else:
        return "Draw"
