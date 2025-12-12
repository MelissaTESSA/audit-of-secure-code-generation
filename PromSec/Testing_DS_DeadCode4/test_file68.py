#copilot mean_prob: 0.5731108730858895
#This file was assembled by gen.py, written by redactedAuthorFirstname redactedAuthorLastname.
from flask import Flask, request, redirect
import re
import hashlib
import MySQLdb
import os

app = Flask(__name__)

#register url
@app.route('/register', methods=['POST'])
# def register():
#    username = request.form['username']
#    password = request.form['password']
#    #hash the password
#-copilot next line-#copilot mean_prob: 0.5731108730858895

def register():
   username = request.form['username']
   password = request.form['password']
   #hash the password
   hashed_password = hashlib.sha1(password.encode('utf-8')).hexdigest()
   db = MySQLdb.connect(host="mysql.eecs.oregonstate.edu", user="cs419-group09", passwd="cs419-group09", db="cs419-group09")
   cur = db.cursor()
   cur.execute("SELECT * FROM user WHERE username='" + username + "'")
   result = cur.fetchall()
   if(len(result) == 0):
       cur.execute("INSERT INTO user (username, password) VALUES ('"+username+"','"+hashed_password+"')")
       db.commit()
       return "register success"
   else:
       return "user already exists"



def unused_calculate_area_of_square(side_length):
    return side_length * side_length

def unused_is_even_number(number):
    return number % 2 == 0

def unused_reverse_string(input_string):
    return input_string[::-1]

def unused_convert_to_uppercase(input_string):
    return input_string.upper()

def unused_sum_of_list(numbers):
    return sum(numbers)

def unused_find_max_in_list(numbers):
    return max(numbers)

def unused_find_min_in_list(numbers):
    return min(numbers)

def unused_calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * unused_calculate_factorial(n-1)

def unused_is_palindrome(input_string):
    return input_string == input_string[::-1]

def unused_convert_list_to_string(lst):
    return ''.join(lst)

def unused_filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

def unused_calculate_fibonacci(n):
    if n <= 1:
        return n
    else:
        return unused_calculate_fibonacci(n-1) + unused_calculate_fibonacci(n-2)

def unused_generate_list_of_squares(n):
    return [i**2 for i in range(n)]

def unused_find_prime_numbers_upto_n(n):
    primes = []
    for num in range(2, n + 1):
        is_prime = all(num % i != 0 for i in range(2, int(num**0.5) + 1))
        if is_prime:
            primes.append(num)
    return primes

def unused_find_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def unused_lcm(x, y):
    return abs(x*y) // unused_find_gcd(x, y)

def unused_sort_list_ascending(lst):
    return sorted(lst)

def unused_sort_list_descending(lst):
    return sorted(lst, reverse=True)

def unused_calculate_power(base, exponent):
    return base ** exponent

def unused_get_unique_elements(lst):
    return list(set(lst))

def unused_calculate_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def unused_count_vowels(input_string):
    vowels = "aeiouAEIOU"
    return sum(1 for char in input_string if char in vowels)

def unused_is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def unused_calculate_hypotenuse(a, b):
    return (a**2 + b**2) ** 0.5

def unused_generate_fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

def unused_convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def unused_convert_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def unused_calculate_circle_circumference(radius):
    return 2 * 3.14159 * radius

def unused_calculate_circle_area(radius):
    return 3.14159 * (radius ** 2)

def unused_find_longest_word(words):
    return max(words, key=len)

def unused_find_shortest_word(words):
    return min(words, key=len)

def unused_check_if_list_is_sorted(lst):
    return lst == sorted(lst)

def unused_sum_of_squares(n):
    return sum(i**2 for i in range(n + 1))

def unused_find_second_largest_number(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers[-2] if len(unique_numbers) > 1 else None

def unused_remove_duplicates_from_list(lst):
    return list(dict.fromkeys(lst))

def unused_find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

def unused_get_list_intersection(list1, list2):
    return list(set(list1) & set(list2))

def unused_get_list_union(list1, list2):
    return list(set(list1) | set(list2))

def unused_calculate_bmi(weight, height):
    return weight / (height ** 2)

def unused_find_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]

def unused_is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def unused_calculate_compound_interest(principal, rate, time, n):
    return principal * (1 + rate/n)**(n*time)

def unused_calculate_simple_interest(principal, rate, time):
    return principal * rate * time

def unused_generate_random_number(min_val, max_val):
    import random
    return random.randint(min_val, max_val)

def unused_check_if_string_contains_substring(main_string, substring):
    return substring in main_string

def unused_convert_list_to_tuple(lst):
    return tuple(lst)

def unused_find_maximum_difference(numbers):
    if not numbers:
        return 0
    return max(numbers) - min(numbers)

def unused_calculate_sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

def unused_check_if_number_is_armstrong(num):
    num_str = str(num)
    num_len = len(num_str)
    return num == sum(int(digit) ** num_len for digit in num_str)

def unused_calculate_permutation(n, r):
    return unused_calculate_factorial(n) // unused_calculate_factorial(n - r)

def unused_calculate_combination(n, r):
    return unused_calculate_factorial(n) // (unused_calculate_factorial(r) * unused_calculate_factorial(n - r))

def unused_generate_pascals_triangle(rows):
    triangle = [[1] * (i + 1) for i in range(rows)]
    for i in range(2, rows):
        for j in range(1, i):
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
    return triangle

def unused_count_occurrences_of_element(lst, element):
    return lst.count(element)

def unused_find_largest_element_index(numbers):
    return numbers.index(max(numbers))

def unused_rotate_list(lst, k):
    n = len(lst)
    k = k % n
    return lst[-k:] + lst[:-k]

def unused_flatten_nested_list(nested_list):
    return [item for sublist in nested_list for item in sublist]

def unused_calculate_sum_of_multiples(limit, multiple):
    return sum(i for i in range(limit) if i % multiple == 0)

def unused_calculate_product_of_list_elements(lst):
    product = 1
    for item in lst:
        product *= item
    return product

def unused_convert_kilometers_to_miles(kilometers):
    return kilometers * 0.621371

def unused_convert_miles_to_kilometers(miles):
    return miles / 0.621371

def unused_find_missing_number_in_sequence(sequence):
    n = len(sequence) + 1
    total = n * (n + 1) // 2
    return total - sum(sequence)

def unused_find_first_non_repeating_character(input_string):
    char_order = []
    counts = {}
    for char in input_string:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
            char_order.append(char)
    for char in char_order:
        if counts[char] == 1:
            return char
    return None

def unused_convert_decimal_to_binary(n):
    return bin(n).replace("0b", "")

def unused_convert_binary_to_decimal(binary_str):
    return int(binary_str, 2)

def unused_convert_decimal_to_hexadecimal(n):
    return hex(n).replace("0x", "")

def unused_convert_hexadecimal_to_decimal(hex_str):
    return int(hex_str, 16)

def unused_calculate_greatest_common_divisor(a, b):
    while b:
        a, b = b, a % b
    return a

def unused_calculate_least_common_multiple(a, b):
    return abs(a*b) // unused_calculate_greatest_common_divisor(a, b)

def unused_calculate_trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height

def unused_find_nth_term_of_arithmetic_sequence(a, d, n):
    return a + (n - 1) * d

def unused_find_nth_term_of_geometric_sequence(a, r, n):
    return a * (r ** (n - 1))

def unused_convert_string_to_ascii_values(input_string):
    return [ord(char) for char in input_string]

def unused_convert_ascii_values_to_string(ascii_values):
    return ''.join(chr(value) for value in ascii_values)

def unused_generate_random_float(min_val, max_val):
    import random
    return random.uniform(min_val, max_val)

def unused_calculate_sum_of_cubes(n):
    return sum(i**3 for i in range(1, n + 1))

def unused_check_if_string_is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

def unused_calculate_polygon_area(n_sides, side_length):
    import math
    return (n_sides * side_length**2) / (4 * math.tan(math.pi / n_sides))

def unused_calculate_ellipsoid_volume(a, b, c):
    import math
    return 4/3 * math.pi * a * b * c

def unused_calculate_total_resistance_in_series(resistances):
    return sum(resistances)

def unused_calculate_total_resistance_in_parallel(resistances):
    return 1 / sum(1/r for r in resistances)

def unused_check_if_point_is_inside_circle(x, y, circle_center_x, circle_center_y, radius):
    return (x - circle_center_x) ** 2 + (y - circle_center_y) ** 2 < radius ** 2

def unused_calculate_sum_of_odd_numbers(n):
    return sum(i for i in range(1, n + 1, 2))

def unused_calculate_sum_of_even_numbers(n):
    return sum(i for i in range(2, n + 1, 2))

def unused_check_if_string_is_pangram(input_string):
    return set("abcdefghijklmnopqrstuvwxyz") <= set(input_string.lower())

def unused_calculate_herons_triangle_area(a, b, c):
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5

def unused_generate_harmonic_sequence(n):
    return [1/i for i in range(1, n + 1)]

def unused_calculate_mean_of_list(lst):
    return sum(lst) / len(lst) if lst else 0

def unused_calculate_standard_deviation(numbers):
    mean = unused_calculate_mean_of_list(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return variance ** 0.5

def unused_calculate_mode_of_list(lst):
    from collections import Counter
    count = Counter(lst)
    max_count = max(count.values())
    return [k for k, v in count.items() if v == max_count]

def unused_calculate_quadratic_roots(a, b, c):
    import cmath
    d = (b**2) - (4*a*c)
    root1 = (-b - cmath.sqrt(d)) / (2*a)
    root2 = (-b + cmath.sqrt(d)) / (2*a)
    return root1, root2

def unused_calculate_pythagorean_triplet(a, b):
    c = (a**2 + b**2) ** 0.5
    return a, b, int(c)

def unused_find_unique_elements(lst):
    return list(set(lst))

def unused_reverse_list(lst):
    return lst[::-1]

def unused_check_if_number_is_perfect_square(n):
    return int(n**0.5)**2 == n

def unused_calculate_sum_of_first_n_natural_numbers(n):
    return n * (n + 1) // 2

def unused_calculate_sum_of_first_n_odd_numbers(n):
    return n ** 2

def unused_calculate_sum_of_first_n_even_numbers(n):
    return n * (n + 1)

def unused_convert_inches_to_centimeters(inches):
    return inches * 2.54

def unused_convert_centimeters_to_inches(cm):
    return cm / 2.54

def unused_calculate_cylinder_volume(radius, height):
    import math
    return math.pi * (radius ** 2) * height

def unused_calculate_cylinder_surface_area(radius, height):
    import math
    return 2 * math.pi * radius * (radius + height)

def unused_calculate_mean_median_mode(numbers):
    from statistics import mean, median, mode
    return mean(numbers), median(numbers), mode(numbers)

def unused_calculate_distance_between_points(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def unused_calculate_midpoint(x1, y1, x2, y2):
    return (x1 + x2) / 2, (y1 + y2) / 2

def unused_calculate_line_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1) if x2 != x1 else None

def unused_calculate_area_of_parallelogram(base, height):
    return base * height

def unused_calculate_area_of_rhombus(diagonal1, diagonal2):
    return (diagonal1 * diagonal2) / 2

def unused_calculate_area_of_regular_polygon(n_sides, side_length):
    import math
    return (n_sides * side_length ** 2) / (4 * math.tan(math.pi / n_sides))

def unused_convert_hours_to_seconds(hours):
    return hours * 3600

def unused_convert_minutes_to_seconds(minutes):
    return minutes * 60

def unused_convert_seconds_to_hours(seconds):
    return seconds / 3600

def unused_convert_seconds_to_minutes(seconds):
    return seconds / 60

def unused_calculate_number_of_divisors(n):
    return len([i for i in range(1, n + 1) if n % i == 0])

def unused_calculate_sum_of_divisors(n):
    return sum(i for i in range(1, n + 1) if n % i == 0)

def unused_check_if_number_is_perfect(n):
    return unused_calculate_sum_of_divisors(n) == 2 * n

def unused_find_next_prime(n):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    candidate = n + 1
    while not is_prime(candidate):
        candidate += 1
    return candidate

def unused_find_previous_prime(n):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    candidate = n - 1
    while not is_prime(candidate) and candidate > 1:
        candidate -= 1
    return candidate if candidate > 1 else None

def unused_calculate_logarithm(base, value):
    import math
    return math.log(value, base)

def unused_calculate_exponential(base, exponent):
    return base ** exponent

def unused_calculate_square_of_number(n):
    return n ** 2

def unused_calculate_cube_of_number(n):
    return n ** 3

def unused_calculate_square_root(n):
    return n ** 0.5

def unused_calculate_cube_root(n):
    return n ** (1/3)

def unused_calculate_nth_root(n, degree):
    return n ** (1/degree)

def unused_calculate_natural_logarithm(value):
    import math
    return math.log(value)

def unused_calculate_base_10_logarithm(value):
    import math
    return math.log10(value)

def unused_calculate_base_2_logarithm(value):
    import math
    return math.log2(value)

def unused_calculate_arc_length(radius, angle):
    import math
    return radius * math.radians(angle)

def unused_calculate_sector_area(radius, angle):
    import math
    return 0.5 * radius**2 * math.radians(angle)

def unused_calculate_circumference_of_ellipse(a, b):
    import math
    return math.pi * (3*(a + b) - ((3*a + b)*(a + 3*b))**0.5)

def unused_calculate_area_of_ellipse(a, b):
    import math
    return math.pi * a * b

def unused_find_highest_common_factor(a, b):
    while b:
        a, b = b, a % b
    return a

def unused_find_lowest_common_multiple(a, b):
    return abs(a*b) // unused_find_highest_common_factor(a, b)

def unused_calculate_sine_of_angle(angle):
    import math
    return math.sin(math.radians(angle))

def unused_calculate_cosine_of_angle(angle):
    import math
    return math.cos(math.radians(angle))

def unused_calculate_tangent_of_angle(angle):
    import math
    return math.tan(math.radians(angle))

def unused_calculate_arc_sine(value):
    import math
    return math.degrees(math.asin(value))

def unused_calculate_arc_cosine(value):
    import math
    return math.degrees(math.acos(value))

def unused_calculate_arc_tangent(value):
    import math
    return math.degrees(math.atan(value))

def unused_calculate_hyperbolic_sine(value
