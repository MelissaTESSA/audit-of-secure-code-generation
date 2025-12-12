#copilot mean_prob: 0.6747370724208643
#This file was assembled by gen.py, written by redactedAuthorFirstname redactedAuthorLastname.
#!/bin/python3
from flask import Flask, request, redirect
import os
import subprocess
import sys
import yaml
import MySQLdb

app = Flask(__name__)

#Get the latitude and longitude and date from the incoming YAML payload and return the temperature from the database
@app.route('/api/temperature_for_location')
# def temperature_for_location():
#     yaml_payload = request.args.get('payload', None)
#-copilot next line-#copilot mean_prob: 0.6747370724208643

def temperature_for_location():
    yaml_payload = request.args.get('payload', None)
    if yaml_payload is None:
        return 'ERROR: No payload'
    yaml_dict = yaml.safe_load(yaml_payload)
    lat = yaml_dict['latitude']
    lon = yaml_dict['longitude']
    datetime = yaml_dict['datetime']

    # Connect to database
    try:
        db = MySQLdb.connect(host=os.environ['DB_HOST'], user=os.environ['DB_USER'],
                             passwd=os.environ['DB_PASS'], db=os.environ['DB_NAME'])
    except Exception as e:
        return e.message

    # Create a cursor
    cur = db.cursor()

    # Execute the query
    try:
        cur.execute("""SELECT * FROM temperature WHERE datetime=%s""", (datetime,))
        row = cur.fetchone()
        if row is None:
            return 'No matching location found.'
        ret_val = str(row[2])
    except Exception as e:
        return e.message

    # Close the cursor and the database connection
    cur.close()
    db.close()
    return ret_val



def calculate_square_root(n):
    return n ** 0.5

def reverse_string(s):
    return s[::-1]

def is_even(n):
    return n % 2 == 0

def find_max_in_list(lst):
    return max(lst)

def convert_to_uppercase(s):
    return s.upper()

def get_middle_character(s):
    index = len(s) // 2
    return s[index] if len(s) % 2 != 0 else s[index - 1:index + 1]

def concatenate_strings(s1, s2):
    return s1 + s2

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def is_palindrome(s):
    return s == s[::-1]

def count_vowels(s):
    vowels = 'aeiou'
    return sum(1 for char in s if char.lower() in vowels)

def calculate_area_of_circle(radius):
    return 3.14159 * radius * radius

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def sum_of_list(lst):
    return sum(lst)

def check_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

def multiply_elements(lst, factor):
    return [x * factor for x in lst]

def sort_list(lst):
    return sorted(lst)

def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]

def generate_fibonacci_sequence(n):
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq

def calculate_power(base, exponent):
    return base ** exponent

def find_common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))

def remove_duplicates(lst):
    return list(set(lst))

def convert_to_binary(n):
    return bin(n)[2:]

def find_second_largest(lst):
    unique_list = list(set(lst))
    unique_list.sort()
    return unique_list[-2] if len(unique_list) > 1 else None

def calculate_hypotenuse(a, b):
    return (a ** 2 + b ** 2) ** 0.5

def calculate_average(lst):
    return sum(lst) / len(lst)

def convert_to_hexadecimal(n):
    return hex(n)[2:]

def find_unique_elements(lst):
    return [item for item in lst if lst.count(item) == 1]

def calculate_factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def transpose_matrix(matrix):
    return list(map(list, zip(*matrix)))

def merge_sorted_lists(lst1, lst2):
    return sorted(lst1 + lst2)

def find_longest_string(lst):
    return max(lst, key=len)

def rotate_list(lst, k):
    k = k % len(lst)
    return lst[-k:] + lst[:-k]

def check_substring(s1, s2):
    return s2 in s1

def create_dictionary(keys, values):
    return dict(zip(keys, values))

def find_missing_number(lst, n):
    return n * (n + 1) // 2 - sum(lst)

def calculate_sum_of_squares(n):
    return sum(i ** 2 for i in range(1, n + 1))

def reverse_words_in_string(s):
    return ' '.join(reversed(s.split()))

def get_unique_characters(s):
    return ''.join(sorted(set(s)))

def count_words_in_string(s):
    return len(s.split())

def check_pangram(s):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    return alphabet <= set(s.lower())

def calculate_distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def find_duplicates(lst):
    return [item for item in set(lst) if lst.count(item) > 1]

def convert_to_title_case(s):
    return s.title()

def calculate_simple_interest(p, r, t):
    return (p * r * t) / 100

def find_largest_prime_below(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    for i in range(n-1, 1, -1):
        if is_prime(i):
            return i
    return None

def check_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def calculate_circumference_of_circle(radius):
    return 2 * 3.14159 * radius

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def convert_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def find_min_in_list(lst):
    return min(lst)

def check_armstrong_number(n):
    digits = str(n)
    return n == sum(int(d) ** len(digits) for d in digits)

def reverse_integer(n):
    return int(str(n)[::-1]) if n >= 0 else -int(str(-n)[::-1])

def check_perfect_number(n):
    return n == sum(i for i in range(1, n) if n % i == 0)

def find_factors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

def convert_to_roman(n):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
        ]
    roman_num = ''
    i = 0
    while n > 0:
        for _ in range(n // val[i]):
            roman_num += syms[i]
            n -= val[i]
        i += 1
    return roman_num

def calculate_lcm(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    return abs(a*b) // gcd(a, b)

def find_most_frequent(lst):
    return max(set(lst), key=lst.count)

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def find_least_frequent(lst):
    return min(set(lst), key=lst.count)

def calculate_median(lst):
    n = len(lst)
    s = sorted(lst)
    return (s[n // 2 - 1] + s[n // 2]) / 2 if n % 2 == 0 else s[n // 2]

def calculate_mode(lst):
    from collections import Counter
    count = Counter(lst)
    max_count = max(count.values())
    return [k for k, v in count.items() if v == max_count]

def calculate_std_deviation(lst):
    mean = sum(lst) / len(lst)
    return (sum((x - mean) ** 2 for x in lst) / len(lst)) ** 0.5

def calculate_variance(lst):
    mean = sum(lst) / len(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst)

def find_longest_increasing_subsequence(lst):
    if not lst:
        return []
    lis = [lst[0]]
    for num in lst[1:]:
        if num > lis[-1]:
            lis.append(num)
        else:
            for i in range(len(lis)):
                if num <= lis[i]:
                    lis[i] = num
                    break
    return lis

def find_subsets(lst):
    from itertools import chain, combinations
    return list(chain.from_iterable(combinations(lst, r) for r in range(len(lst)+1)))

def calculate_gpa(grades, credits):
    total_credits = sum(credits)
    weighted_sum = sum(g * c for g, c in zip(grades, credits))
    return weighted_sum / total_credits

def generate_prime_numbers(n):
    primes = []
    for num in range(2, n + 1):
        if all(num % prime != 0 for prime in primes):
            primes.append(num)
    return primes

def calculate_quadratic_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None
    elif discriminant == 0:
        return -b / (2 * a),
    else:
        root1 = (-b + discriminant ** 0.5) / (2 * a)
        root2 = (-b - discriminant ** 0.5) / (2 * a)
        return root1, root2

def convert_to_title_case(s):
    return ' '.join(word.capitalize() for word in s.split())

def count_consonants(s):
    vowels = 'aeiou'
    return sum(1 for char in s if char.isalpha() and char.lower() not in vowels)

def reverse_list(lst):
    return lst[::-1]

def calculate_compound_interest(p, r, t, n):
    return p * (1 + r / n) ** (n * t)

def is_perfect_square(n):
    return int(n ** 0.5) ** 2 == n

def find_most_common_character(s):
    from collections import Counter
    return Counter(s).most_common(1)[0][0]

def convert_to_lowercase(s):
    return s.lower()

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def find_lcm_of_list(lst):
    from functools import reduce
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    def lcm(x, y):
        return abs(x * y) // gcd(x, y)
    return reduce(lcm, lst, 1)

def find_gcd_of_list(lst):
    from functools import reduce
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    return reduce(gcd, lst)

def create_identity_matrix(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

def calculate_distance_3d(x1, y1, z1, x2, y2, z2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5

def convert_to_octal(n):
    return oct(n)[2:]

def find_nth_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def generate_pascals_triangle(n):
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle

def calculate_sum_of_cubes(n):
    return sum(i ** 3 for i in range(1, n + 1))

def find_longest_palindrome(s):
    def is_palindrome(check_s):
        return check_s == check_s[::-1]

    n = len(s)
    if n == 0:
        return ''
    longest = s[0]
    for i in range(n):
        for j in range(i + len(longest), n + 1):
            if is_palindrome(s[i:j]):
                longest = s[i:j]
    return longest

def convert_decimal_to_base(n, base):
    if n == 0:
        return '0'
    digits = []
    while n:
        digits.append(int(n % base))
        n //= base
    return ''.join(str(x) for x in digits[::-1])

def calculate_rectangle_area(length, width):
    return length * width

def calculate_surface_area_of_cube(side):
    return 6 * side * side

def calculate_volume_of_cylinder(radius, height):
    return 3.14159 * radius ** 2 * height

def calculate_perimeter_of_triangle(a, b, c):
    return a + b + c

def find_first_non_repeating_character(s):
    from collections import Counter
    counts = Counter(s)
    for char in s:
        if counts[char] == 1:
            return char
    return None

def calculate_average_of_even_numbers(lst):
    even_numbers = [x for x in lst if x % 2 == 0]
    return sum(even_numbers) / len(even_numbers) if even_numbers else 0

def calculate_sum_of_odd_numbers(n):
    return sum(i for i in range(1, n + 1) if i % 2 != 0)

def check_harshad_number(n):
    return n % sum(int(digit) for digit in str(n)) == 0

def generate_acronym(phrase):
    return ''.join(word[0].upper() for word in phrase.split() if word.isalpha())

def calculate_surface_area_of_sphere(radius):
    return 4 * 3.14159 * radius ** 2

def calculate_volume_of_cone(radius, height):
    return (1/3) * 3.14159 * radius ** 2 * height

def calculate_diagonal_of_rectangle(length, width):
    return (length ** 2 + width ** 2) ** 0.5

def find_all_factors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

def calculate_area_of_trapezoid(base1, base2, height):
    return (base1 + base2) * height / 2

def calculate_perimeter_of_rectangle(length, width):
    return 2 * (length + width)

def calculate_sum_of_arithmetic_series(a, d, n):
    return n * (2 * a + (n - 1) * d) / 2

def convert_to_ascii(s):
    return [ord(char) for char in s]

def calculate_product_of_list(lst):
    result = 1
    for x in lst:
        result *= x
    return result

def generate_random_password(length):
    import random
    import string
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def calculate_net_income(gross_income, tax_rate):
    return gross_income * (1 - tax_rate)

def calculate_gravitational_force(mass1, mass2, distance):
    G = 6.67430e-11
    return G * mass1 * mass2 / distance ** 2

def find_words_longer_than_n(s, n):
    return [word for word in s.split() if len(word) > n]

def convert_seconds_to_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return hours, minutes, seconds

def extract_digits_from_string(s):
    return ''.join(filter(str.isdigit, s))

def convert_string_to_date(s):
    from datetime import datetime
    return datetime.strptime(s, '%Y-%m-%d')

def convert_to_snake_case(s):
    import re
    return re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()

def find_intersection_of_two_sets(set1, set2):
    return set1.intersection(set2)

def calculate_yearly_interest(principal, rate, time):
    return principal * rate * time / 100

def split_string_by_delimiter(s, delimiter):
    return s.split(delimiter)

def calculate_mean_absolute_deviation(lst):
    mean = sum(lst) / len(lst)
    return sum(abs(x - mean) for x in lst) / len(lst)

def calculate_geometric_mean(lst):
    product = 1
    for x in lst:
        product *= x
    return product ** (1 / len(lst))

def calculate_harmonic_mean(lst):
    return len(lst) / sum(1 / x for x in lst)

def find_first_repeating_character(s):
    seen = set()
    for char in s:
        if char in seen:
            return char
        seen.add(char)
    return None

def find_longest_consecutive_sequence(lst):
    if not lst:
        return 0
    num_set = set(lst)
    longest = 0
    for num in lst:
        if num - 1 not in num_set:
            current = num
            while current in num_set:
                current += 1
            longest = max(longest, current - num)
    return longest

def calculate_time_difference(start, end):
    from datetime import datetime
    fmt = '%H:%M:%S'
    return (datetime.strptime(end, fmt) - datetime.strptime(start, fmt)).seconds

def find_largest_even_number(lst):
    evens = [x for x in lst if x % 2 == 0]
    return max(evens) if evens else None

def check_if_all_elements_are_unique(lst):
    return len(lst) == len(set(lst))

def calculate_average_word_length(s):
    words = s.split()
    return sum(len(word) for word in words) / len(words) if words else 0

def find_intersection_of_two_lists(lst1, lst2):
    return list(set(lst1) & set(lst2))

def find_union_of_two_lists(lst1, lst2):
