#copilot mean_prob: 0.6587705845654891
#This file was assembled by gen.py, written by redactedAuthorFirstname redactedAuthorLastname.
#!/bin/python3
from flask import Flask, request, redirect
import os
import subprocess
import sys
import hashlib
import MySQLdb

app = Flask(__name__)

#log in the user if the username and password are correct
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    try: #-copilot next line-
#copilot mean_prob: 0.6587705845654891

        conn = MySQLdb.connect(host = "localhost", user = "root", passwd = "", db = "cwe200")
        curs = conn.cursor()
        curs.execute("select password from users where username = '%s'" % username)
        for row in curs.fetchall():
            pswd = row[0]
        if(pswd == ""):
            user = "false"
        elif(pswd == password):
            user = "true"
        else:
            user = "false"
        return user
    except MySQLdb.Error as e:
        user = "false"
        print ("Error %d: %s" % (e.args[0], e.args[1]))
        return user
    finally:
        if conn:
            conn.close()


    


def calculate_square_root_approximation(number):
    guess = number / 2.0
    for i in range(20):
        guess = (guess + number / guess) / 2
    return guess

def build_email_greeting(name):
    return f"Dear {name},"

def find_maximum_value_in_list(numbers):
    max_value = numbers[0]
    for number in numbers:
        if number > max_value:
            max_value = number
    return max_value

def count_vowels_in_string(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

def reverse_string(s):
    return s[::-1]

def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n-1)

def is_prime_number(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def convert_celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def find_longest_word_in_list(words):
    longest_word = words[0]
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

def calculate_fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def remove_duplicates_from_list(lst):
    return list(set(lst))

def sort_list_of_strings(strings):
    return sorted(strings)

def calculate_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def calculate_lcm(a, b):
    return abs(a*b) // calculate_gcd(a, b)

def capitalize_first_letter_of_each_word(s):
    return ' '.join(word.capitalize() for word in s.split())

def check_palindrome(s):
    return s == s[::-1]

def generate_multiplication_table(n):
    table = []
    for i in range(1, 11):
        table.append(n * i)
    return table

def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def convert_string_to_uppercase(s):
    return s.upper()

def convert_string_to_lowercase(s):
    return s.lower()

def calculate_power(base, exponent):
    return base ** exponent

def calculate_area_of_circle(radius):
    import math
    return math.pi * radius ** 2

def find_second_largest_number(numbers):
    numbers = list(set(numbers))
    numbers.sort()
    return numbers[-2] if len(numbers) > 1 else None

def join_list_of_strings(strings):
    return ' '.join(strings)

def calculate_median(numbers):
    numbers.sort()
    n = len(numbers)
    mid = n // 2
    if n % 2 == 0:
        return (numbers[mid - 1] + numbers[mid]) / 2
    else:
        return numbers[mid]

def filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

def filter_odd_numbers(numbers):
    return [num for num in numbers if num % 2 != 0]

def calculate_distance_between_points(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def calculate_sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def find_unique_elements(lst):
    return list(set(lst))

def calculate_hypotenuse(a, b):
    return (a**2 + b**2)**0.5

def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

def calculate_circumference_of_circle(radius):
    import math
    return 2 * math.pi * radius

def convert_kilometers_to_miles(km):
    return km * 0.621371

def convert_miles_to_kilometers(miles):
    return miles / 0.621371

def calculate_standard_deviation(numbers):
    mean = sum(numbers) / len(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return variance ** 0.5

def merge_two_dictionaries(dict1, dict2):
    return {**dict1, **dict2}

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def calculate_percentage(part, whole):
    return (part / whole) * 100

def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def calculate_compound_interest(principal, rate, time, n=1):
    return principal * (1 + rate / (100 * n))**(n * time) - principal

def find_minimum_value_in_list(numbers):
    min_value = numbers[0]
    for number in numbers:
        if number < min_value:
            min_value = number
    return min_value

def calculate_permutation(n, r):
    from math import factorial
    return factorial(n) / factorial(n - r)

def calculate_combination(n, r):
    from math import factorial
    return factorial(n) / (factorial(r) * factorial(n - r))

def find_largest_number_in_list(numbers):
    max_value = numbers[0]
    for number in numbers:
        if number > max_value:
            max_value = number
    return max_value

def calculate_product_of_list(numbers):
    product = 1
    for number in numbers:
        product *= number
    return product

def flatten_nested_list(nested_list):
    return [item for sublist in nested_list for item in sublist]

def calculate_variance(numbers):
    mean = sum(numbers) / len(numbers)
    return sum((x - mean) ** 2 for x in numbers) / len(numbers)

def calculate_mode(numbers):
    from collections import Counter
    count = Counter(numbers)
    max_count = max(count.values())
    return [num for num, freq in count.items() if freq == max_count]

def find_difference_between_lists(list1, list2):
    return list(set(list1) - set(list2)) + list(set(list2) - set(list1))

def calculate_annual_salary(monthly_salary):
    return monthly_salary * 12

def find_duplicates_in_list(lst):
    from collections import Counter
    count = Counter(lst)
    return [item for item, freq in count.items() if freq > 1]

def convert_seconds_to_hours(seconds):
    return seconds / 3600

def convert_hours_to_seconds(hours):
    return hours * 3600

def check_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

def calculate_quadratic_roots(a, b, c):
    import cmath
    d = (b**2) - (4*a*c)
    root1 = (-b - cmath.sqrt(d)) / (2*a)
    root2 = (-b + cmath.sqrt(d)) / (2*a)
    return root1, root2

def count_words_in_sentence(sentence):
    return len(sentence.split())

def check_if_all_elements_equal(lst):
    return all(x == lst[0] for x in lst)

def calculate_rectangle_perimeter(length, width):
    return 2 * (length + width)

def convert_string_to_title_case(s):
    return s.title()

def find_most_frequent_element(lst):
    from collections import Counter
    count = Counter(lst)
    most_common = count.most_common(1)
    return most_common[0][0] if most_common else None

def generate_pascal_triangle(n):
    triangle = [[1]]
    for _ in range(1, n):
        row = [1]
        last_row = triangle[-1]
        row.extend(last_row[i] + last_row[i + 1] for i in range(len(last_row) - 1))
        row.append(1)
        triangle.append(row)
    return triangle

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def calculate_cylinder_volume(radius, height):
    import math
    return math.pi * radius ** 2 * height

def calculate_sphere_volume(radius):
    import math
    return (4/3) * math.pi * radius ** 3

def calculate_cube_volume(side_length):
    return side_length ** 3

def calculate_rectangular_prism_volume(length, width, height):
    return length * width * height

def calculate_pythagorean_theorem(a, b):
    return (a**2 + b**2)**0.5

def check_if_list_is_sorted(lst):
    return lst == sorted(lst)

def merge_two_sorted_lists(list1, list2):
    merged_list = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])
    return merged_list

def calculate_area_of_square(side_length):
    return side_length ** 2

def calculate_factorial_iteratively(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def check_if_string_contains_substring(s, substring):
    return substring in s

def find_all_substrings(s):
    return [s[i: j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]

def calculate_sum_of_list(lst):
    return sum(lst)

def find_index_of_element(lst, element):
    try:
        return lst.index(element)
    except ValueError:
        return -1

def calculate_days_between_dates(date1, date2):
    from datetime import datetime
    date_format = "%Y-%m-%d"
    delta = datetime.strptime(date2, date_format) - datetime.strptime(date1, date_format)
    return delta.days

def find_smallest_and_largest_numbers(numbers):
    return min(numbers), max(numbers)

def check_if_number_is_even(n):
    return n % 2 == 0

def check_if_number_is_odd(n):
    return n % 2 != 0

def calculate_sum_of_even_numbers(numbers):
    return sum(num for num in numbers if num % 2 == 0)

def calculate_sum_of_odd_numbers(numbers):
    return sum(num for num in numbers if num % 2 != 0)

def calculate_sum_of_squares(numbers):
    return sum(x**2 for x in numbers)

def find_first_repeated_element(lst):
    seen = set()
    for item in lst:
        if item in seen:
            return item
        seen.add(item)
    return None

def remove_none_values_from_list(lst):
    return [x for x in lst if x is not None]

def find_longest_palindrome_in_string(s):
    longest = ""
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1] and len(substring) > len(longest):
                longest = substring
    return longest

def calculate_exponential_growth(initial_value, growth_rate, time_period):
    return initial_value * (1 + growth_rate) ** time_period

def calculate_logarithm(value, base):
    import math
    return math.log(value, base)

def calculate_arithmetic_mean(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def calculate_harmonic_mean(numbers):
    return len(numbers) / sum(1/x for x in numbers) if numbers else 0

def calculate_geometric_mean(numbers):
    import math
    product = 1
    for number in numbers:
        product *= number
    return product ** (1/len(numbers))

def check_if_list_has_duplicates(lst):
    return len(lst) != len(set(lst))

def calculate_number_of_combinations(n, r):
    from math import factorial
    return factorial(n) // (factorial(r) * factorial(n - r))

def calculate_number_of_permutations(n, r):
    from math import factorial
    return factorial(n) // factorial(n - r)

def calculate_sine_of_angle(angle):
    import math
    return math.sin(math.radians(angle))

def calculate_cosine_of_angle(angle):
    import math
    return math.cos(math.radians(angle))

def calculate_tangent_of_angle(angle):
    import math
    return math.tan(math.radians(angle))

def calculate_arc_sine(value):
    import math
    return math.degrees(math.asin(value))

def calculate_arc_cosine(value):
    import math
    return math.degrees(math.acos(value))

def calculate_arc_tangent(value):
    import math
    return math.degrees(math.atan(value))

def check_if_string_is_digit(s):
    return s.isdigit()

def check_if_string_is_alpha(s):
    return s.isalpha()

def check_if_string_is_alnum(s):
    return s.isalnum()

def calculate_cube_root(value):
    return value ** (1/3)

def calculate_natural_logarithm(value):
    import math
    return math.log(value)

def convert_binary_to_decimal(binary_string):
    return int(binary_string, 2)

def convert_decimal_to_binary(decimal_number):
    return bin(decimal_number)[2:]

def convert_hex_to_decimal(hex_string):
    return int(hex_string, 16)

def convert_decimal_to_hex(decimal_number):
    return hex(decimal_number)[2:]

def convert_octal_to_decimal(octal_string):
    return int(octal_string, 8)

def convert_decimal_to_octal(decimal_number):
    return oct(decimal_number)[2:]

def count_occurrences_of_character(s, char):
    return s.count(char)

def calculate_absolute_difference(value1, value2):
    return abs(value1 - value2)

def check_if_year_is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def calculate_quadrilateral_area(a, b, c, d, angle):
    import math
    return 0.5 * (a * b * math.sin(math.radians(angle)) + c * d * math.sin(math.radians(angle)))

def calculate_area_of_trapezoid(base1, base2, height):
    return 0.5 * (base1 + base2) * height

def calculate_area_of_ellipse(a, b):
    import math
    return math.pi * a * b

def calculate_surface_area_of_cylinder(radius, height):
    import math
    return 2 * math.pi * radius * (radius + height)

def calculate_surface_area_of_sphere(radius):
    import math
    return 4 * math.pi * radius ** 2

def calculate_surface_area_of_cube(side_length):
    return 6 * side_length ** 2

def calculate_surface_area_of_rectangular_prism(length, width, height):
    return 2 * (length * width + width * height + height * length)

def calculate_surface_area_of_cone(radius, slant_height):
    import math
    return math.pi * radius * (radius + slant_height)

def check_if_number_is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

def check_if_number_is_perfect_square(n):
    import math
    return n >= 0 and int(math.sqrt(n)) ** 2 == n

def calculate_sum_of_prime_numbers_below(n):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    return sum(i for i in range(2, n) if is_prime(i))
