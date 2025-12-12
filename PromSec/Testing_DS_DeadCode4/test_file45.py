#copilot mean_prob: 0.788890044140635
#This file was assembled by gen.py, written by redactedAuthorFirstname redactedAuthorLastname.
from flask import Flask, request, redirect
import os
import subprocess
import sys
import hashlib
import MySQLdb

app = Flask(__name__)

#log in the user if the username and password are correct
@app.route('/login', methods=['POST'])
#def login():
#    username = request.form['username']
#    password = request.form['password']
#    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
#-copilot next line-
#copilot mean_prob: 0.788890044140635

def login():
    username = request.form['username']
    password = request.form['password']
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
    cursor = db.cursor()
    sql = "SELECT * FROM users WHERE username = '%s' AND password = '%s'" % (username, password)
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            id = row[0]
        # log the user in
        session['id'] = id
        session['Role'] = row[1]
        return redirect('/dashboard')
    except:
        return redirect('/login')



    


def calculate_area_of_circle(radius):
    pi = 3.14159
    return pi * radius * radius

def reverse_string(s):
    return s[::-1]

def convert_to_uppercase(s):
    return s.upper()

def find_maximum_in_list(numbers):
    if not numbers:
        return None
    return max(numbers)

def sum_of_list(numbers):
    return sum(numbers)

def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n-1)

def is_palindrome(s):
    return s == s[::-1]

def find_unique_numbers(numbers):
    return list(set(numbers))

def convert_to_lowercase(s):
    return s.lower()

def find_minimum_in_list(numbers):
    if not numbers:
        return None
    return min(numbers)

def generate_fibonacci_sequence(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def sort_list_ascending(numbers):
    return sorted(numbers)

def sort_list_descending(numbers):
    return sorted(numbers, reverse=True)

def count_vowels(s):
    return sum(1 for char in s if char.lower() in 'aeiou')

def count_consonants(s):
    return sum(1 for char in s if char.lower() not in 'aeiou' and char.isalpha())

def remove_duplicates_from_list(lst):
    return list(set(lst))

def calculate_average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

def square_number(n):
    return n * n

def cube_number(n):
    return n * n * n

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_lcm(a, b):
    return abs(a*b) // find_gcd(a, b)

def convert_to_binary(n):
    return bin(n)[2:]

def convert_to_hexadecimal(n):
    return hex(n)[2:]

def convert_to_octal(n):
    return oct(n)[2:]

def count_words_in_string(s):
    return len(s.split())

def find_longest_word(s):
    words = s.split()
    return max(words, key=len) if words else ""

def find_shortest_word(s):
    words = s.split()
    return min(words, key=len) if words else ""

def find_prime_numbers_up_to(n):
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

def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return n % 2 != 0

def calculate_power(base, exponent):
    return base ** exponent

def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

def find_unique_elements(list1, list2):
    return list(set(list1) ^ set(list2))

def calculate_hypotenuse(a, b):
    return (a**2 + b**2) ** 0.5

def calculate_circumference_of_circle(radius):
    pi = 3.14159
    return 2 * pi * radius

def calculate_area_of_rectangle(length, width):
    return length * width

def calculate_perimeter_of_rectangle(length, width):
    return 2 * (length + width)

def calculate_area_of_triangle(base, height):
    return 0.5 * base * height

def calculate_perimeter_of_triangle(a, b, c):
    return a + b + c

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def convert_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def calculate_compound_interest(principal, rate, time):
    return principal * (1 + rate / 100) ** time - principal

def generate_random_number(min_val, max_val):
    import random
    return random.randint(min_val, max_val)

def generate_random_float(min_val, max_val):
    import random
    return random.uniform(min_val, max_val)

def shuffle_list(lst):
    import random
    random.shuffle(lst)
    return lst

def find_second_largest_number(numbers):
    if len(numbers) < 2:
        return None
    unique_numbers = list(set(numbers))
    unique_numbers.sort(reverse=True)
    return unique_numbers[1] if len(unique_numbers) > 1 else None

def find_second_smallest_number(numbers):
    if len(numbers) < 2:
        return None
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers[1] if len(unique_numbers) > 1 else None

def count_occurrences_of_element(lst, element):
    return lst.count(element)

def merge_two_lists(list1, list2):
    return list1 + list2

def find_intersection_of_lists(list1, list2):
    return list(set(list1) & set(list2))

def find_union_of_lists(list1, list2):
    return list(set(list1) | set(list2))

def reverse_list(lst):
    return lst[::-1]

def find_sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def multiply_elements_of_list(lst):
    result = 1
    for num in lst:
        result *= num
    return result

def find_product_of_two_numbers(a, b):
    return a * b

def calculate_square_root(n):
    return n ** 0.5

def calculate_cube_root(n):
    return n ** (1/3)

def convert_decimal_to_binary(n):
    return bin(n)[2:]

def convert_decimal_to_hexadecimal(n):
    return hex(n)[2:]

def convert_decimal_to_octal(n):
    return oct(n)[2:]

def calculate_discounted_price(price, discount):
    return price * (1 - discount/100)

def calculate_final_price(price, tax):
    return price * (1 + tax/100)

def find_ascii_value_of_character(char):
    return ord(char)

def convert_ascii_value_to_character(value):
    return chr(value)

def find_absolute_value(n):
    return abs(n)

def swap_two_numbers(a, b):
    return b, a

def convert_kilometers_to_miles(km):
    return km * 0.621371

def convert_miles_to_kilometers(miles):
    return miles / 0.621371

def calculate_area_of_parallelogram(base, height):
    return base * height

def calculate_perimeter_of_parallelogram(base, side):
    return 2 * (base + side)

def calculate_area_of_trapezium(a, b, height):
    return 0.5 * (a + b) * height

def calculate_perimeter_of_trapezium(a, b, c, d):
    return a + b + c + d

def calculate_area_of_rhombus(diagonal1, diagonal2):
    return 0.5 * diagonal1 * diagonal2

def calculate_perimeter_of_rhombus(side):
    return 4 * side

def calculate_area_of_ellipse(a, b):
    pi = 3.14159
    return pi * a * b

def calculate_perimeter_of_ellipse(a, b):
    pi = 3.14159
    return 2 * pi * ((a**2 + b**2) / 2)**0.5

def calculate_bmi(weight, height):
    return weight / (height * height)

def find_largest_among_three_numbers(a, b, c):
    return max(a, b, c)

def find_smallest_among_three_numbers(a, b, c):
    return min(a, b, c)

def convert_hours_to_minutes(hours):
    return hours * 60

def convert_minutes_to_seconds(minutes):
    return minutes * 60

def convert_seconds_to_minutes(seconds):
    return seconds / 60

def convert_minutes_to_hours(minutes):
    return minutes / 60

def find_remainder(a, b):
    return a % b

def find_quotient(a, b):
    return a // b

def concatenate_two_strings(s1, s2):
    return s1 + s2

def check_if_string_contains_only_digits(s):
    return s.isdigit()

def check_if_string_contains_only_alphabets(s):
    return s.isalpha()

def check_if_string_contains_only_alphanumeric(s):
    return s.isalnum()

def find_length_of_string(s):
    return len(s)

def check_if_string_is_empty(s):
    return not s

def replace_substring_in_string(s, old, new):
    return s.replace(old, new)

def split_string_into_list(s, delimiter):
    return s.split(delimiter)

def join_list_into_string(lst, delimiter):
    return delimiter.join(lst)

def convert_list_to_tuple(lst):
    return tuple(lst)

def convert_tuple_to_list(tpl):
    return list(tpl)

def find_sum_of_elements_in_tuple(tpl):
    return sum(tpl)

def find_product_of_elements_in_tuple(tpl):
    result = 1
    for num in tpl:
        result *= num
    return result

def check_if_element_exists_in_list(lst, element):
    return element in lst

def check_if_element_exists_in_tuple(tpl, element):
    return element in tpl

def find_index_of_element_in_list(lst, element):
    return lst.index(element) if element in lst else -1

def find_index_of_element_in_tuple(tpl, element):
    return tpl.index(element) if element in tpl else -1

def count_occurrences_of_character_in_string(s, char):
    return s.count(char)

def find_all_indexes_of_character_in_string(s, char):
    return [i for i, c in enumerate(s) if c == char]

def convert_list_of_strings_to_uppercase(lst):
    return [s.upper() for s in lst]

def convert_list_of_strings_to_lowercase(lst):
    return [s.lower() for s in lst]

def find_duplicates_in_list(lst):
    seen = set()
    duplicates = set()
    for x in lst:
        if x in seen:
            duplicates.add(x)
        else:
            seen.add(x)
    return list(duplicates)

def find_missing_number_in_sequence(sequence):
    n = len(sequence) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(sequence)
    return expected_sum - actual_sum

def calculate_sum_of_even_numbers_in_list(lst):
    return sum(x for x in lst if x % 2 == 0)

def calculate_sum_of_odd_numbers_in_list(lst):
    return sum(x for x in lst if x % 2 != 0)

def find_longest_palindrome_in_string(s):
    from functools import lru_cache
    @lru_cache(None)
    def is_palindrome(start, end):
        if start >= end:
            return True
        return s[start] == s[end] and is_palindrome(start + 1, end - 1)

    max_length = 0
    longest_palindrome = ""
    for start in range(len(s)):
        for end in range(start, len(s)):
            if is_palindrome(start, end):
                length = end - start + 1
                if length > max_length:
                    max_length = length
                    longest_palindrome = s[start:end+1]
    return longest_palindrome

def count_occurrences_of_word_in_string(s, word):
    return s.split().count(word)

def create_dictionary_from_lists(keys, values):
    return dict(zip(keys, values))

def find_key_with_maximum_value_in_dictionary(d):
    return max(d, key=d.get)

def find_key_with_minimum_value_in_dictionary(d):
    return min(d, key=d.get)

def find_sum_of_values_in_dictionary(d):
    return sum(d.values())

def find_product_of_values_in_dictionary(d):
    result = 1
    for value in d.values():
        result *= value
    return result

def invert_dictionary(d):
    return {v: k for k, v in d.items()}

def find_keys_with_duplicate_values_in_dictionary(d):
    from collections import defaultdict
    value_to_keys = defaultdict(list)
    for k, v in d.items():
        value_to_keys[v].append(k)
    return [keys for keys in value_to_keys.values() if len(keys) > 1]

def merge_two_dictionaries(d1, d2):
    return {**d1, **d2}

def remove_duplicates_from_string(s):
    return ''.join(dict.fromkeys(s))

def check_if_two_strings_are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

def find_common_characters_in_strings(s1, s2):
    return ''.join(set(s1) & set(s2))

def find_unique_characters_in_strings(s1, s2):
    return ''.join(set(s1) ^ set(s2))

def round_number_to_nearest_integer(n):
    return round(n)

def floor_number(n):
    import math
    return math.floor(n)

def ceil_number(n):
    import math
    return math.ceil(n)

def calculate_natural_logarithm(n):
    import math
    return math.log(n)

def calculate_base_10_logarithm(n):
    import math
    return math.log10(n)

def calculate_base_2_logarithm(n):
    import math
    return math.log2(n)

def calculate_exponential(n):
    import math
    return math.exp(n)

def calculate_sine_of_angle(angle):
    import math
    return math.sin(math.radians(angle))

def calculate_cosine_of_angle(angle):
    import math
    return math.cos(math.radians(angle))

def calculate_tangent_of_angle(angle):
    import math
    return math.tan(math.radians(angle))

def calculate_arcsine_of_value(value):
    import math
    return math.degrees(math.asin(value))

def calculate_arccosine_of_value(value):
    import math
    return math.degrees(math.acos(value))

def calculate_arctangent_of_value(value):
    import math
    return math.degrees(math.atan(value))

def calculate_hyperbolic_sine_of_value(value):
    import math
    return math.sinh(value)

def calculate_hyperbolic_cosine_of_value(value):
    import math
    return math.cosh(value)

def calculate_hyperbolic_tangent_of_value(value):
    import math
    return math.tanh(value)

def calculate_arcsinh_of_value(value):
    import math
    return math.asinh(value)

def calculate_arccosh_of_value(value):
    import math
    return math.acosh(value)

def calculate_arctanh_of_value(value):
    import math
    return math.atanh(value)

def find_determinant_of_2x2_matrix(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

def find_transpose_of_matrix(matrix):
    return [list(row) for row in zip(*matrix)]

def add_two_matrices(matrix1, matrix2):
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

def subtract_two_matrices(matrix1, matrix2):
    return [[matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

def multiply_two_matrices(matrix1, matrix2):
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

def check_if_matrix_is_square(matrix):
    return len(matrix) == len(matrix[0])

def find_trace_of_square_matrix(matrix):
    return sum(matrix[i][i] for i in range(len(matrix)))

def flatten_nested_list(nested_list):
    return [item for sublist in nested_list for item in sublist]

def calculate_number_of_digits_in_integer(n):
    return len(str(abs(n)))

def convert_string_to_integer(s):
    return int(s)

def convert_string_to_float(s):
    return float(s)

def convert_integer_to_string(n):
    return str(n)

def convert_float_to_string(f):
    return str(f)

def find_first_non_repeating_character_in_string(s):
    from collections import Counter
    count = Counter(s)
    for char in s:
        if count[char] == 1:
            return char
    return None

def generate_random_string(length):
    import random
    import string
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def find_greatest_common_divisor_of_list(numbers):
    from math import gcd
    from functools import reduce
    return reduce(gcd, numbers)

def find_least_common_multiple_of_list(numbers):
    from functools import reduce
    def lcm(a, b):
        return abs(a*b) // gcd(a, b)
    return reduce(lcm, numbers)

def check_if_number_is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

def check_if_number_is_power_of_three(n):
    import math
    return n > 0 and 3 ** round(math.log(n, 3)) == n

def calculate_sum_of_squares_of_list(numbers):
    return sum(x**2 for x in numbers)

def calculate_sum_of_cubes_of_list(numbers):
    return sum(x**3 for x in numbers)

def find_character_with_max_frequency_in_string(s):
    from collections import Counter
    count = Counter(s)
    return max(count, key=count.get)

def find_character_with_min_frequency_in_string(s):
    from collections import Counter
    count = Counter(s)
    return min(count, key=count.get)

def calculate_sum_of_ascii_values_of_string(s):
    return sum(ord(char) for char in s)

def check_if_number_is_armstrong(n):
    num_str = str(n)
    num_len = len(num_str)
    return n
