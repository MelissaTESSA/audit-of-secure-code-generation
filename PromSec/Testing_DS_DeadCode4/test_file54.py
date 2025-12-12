#copilot mean_prob: 0.6211094848988443
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
#copilot mean_prob: 0.6211094848988443

def login():
    username = request.form['username']
    password = request.form['password']
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
    cur = db.cursor()
    cur.execute("SELECT password FROM user_info WHERE username=%s", [username])
    row = cur.fetchone()
    if (row[0] == hashlib.md5(password.encode("utf-8")).hexdigest()):
        return redirect('/')
    else:
        return redirect('/error')


    


def calculate_area_of_circle(radius):
    pi = 3.14159
    return pi * radius * radius

def greet_user(name):
    greeting = f"Hello, {name}!"
    return greeting

def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def find_maximum_in_list(numbers):
    return max(numbers)

def check_palindrome(word):
    return word == word[::-1]

def generate_full_name(first_name, last_name):
    return f"{first_name} {last_name}"

def calculate_square_root(number):
    return number ** 0.5

def reverse_string(s):
    return s[::-1]

def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n-1)

def list_even_numbers(upto):
    return [x for x in range(upto) if x % 2 == 0]

def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def check_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def sort_list_ascending(arr):
    return sorted(arr)

def calculate_power(base, exponent):
    return base ** exponent

def convert_kilometers_to_miles(km):
    return km * 0.621371

def count_vowels_in_string(s):
    return sum(1 for char in s if char.lower() in 'aeiou')

def find_minimum_in_list(numbers):
    return min(numbers)

def merge_two_lists(list1, list2):
    return list1 + list2

def calculate_bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)

def generate_fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

def check_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def find_unique_elements(lst):
    return list(set(lst))

def get_even_numbers_from_list(numbers):
    return [x for x in numbers if x % 2 == 0]

def calculate_compound_interest(principal, rate, time, n):
    return principal * (1 + rate / n) ** (n * time)

def capitalize_string(s):
    return s.capitalize()

def convert_miles_to_kilometers(miles):
    return miles / 0.621371

def calculate_hypotenuse(a, b):
    return (a**2 + b**2) ** 0.5

def find_lcm(a, b):
    gcd = find_gcd(a, b)
    return abs(a*b) // gcd

def flatten_list_of_lists(lists):
    return [item for sublist in lists for item in sublist]

def calculate_percentage(part, whole):
    return (part / whole) * 100

def convert_hours_to_seconds(hours):
    return hours * 3600

def check_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def convert_seconds_to_minutes(seconds):
    return seconds / 60

def get_odd_numbers_from_list(numbers):
    return [x for x in numbers if x % 2 != 0]

def convert_list_to_set(lst):
    return set(lst)

def find_second_largest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers[-2] if len(unique_numbers) >= 2 else None

def calculate_rectangle_perimeter(length, width):
    return 2 * (length + width)

def check_substring(main_string, substring):
    return substring in main_string

def get_factors_of_number(number):
    return [x for x in range(1, number + 1) if number % x == 0]

def convert_string_to_uppercase(s):
    return s.upper()

def calculate_circumference_of_circle(radius):
    pi = 3.14159
    return 2 * pi * radius

def get_square_numbers_from_list(numbers):
    return [x**2 for x in numbers]

def convert_string_to_lowercase(s):
    return s.lower()

def calculate_rectangle_area(length, width):
    return length * width

def filter_positive_numbers(numbers):
    return [x for x in numbers if x > 0]

def get_unique_chars_in_string(s):
    return set(s)

def calculate_cube_volume(side_length):
    return side_length ** 3

def count_consonants_in_string(s):
    return sum(1 for char in s if char.lower() in 'bcdfghjklmnpqrstvwxyz')

def check_if_all_elements_are_equal(lst):
    return all(x == lst[0] for x in lst)

def calculate_body_fat_percentage(weight, waist_circumference, gender):
    if gender == "male":
        return 495 / (1.0324 - 0.19077 * (waist_circumference / weight)) - 450
    else:
        return 495 / (1.29579 - 0.35004 * (waist_circumference / weight)) - 450

def get_prime_numbers_upto(n):
    primes = []
    for num in range(2, n + 1):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            primes.append(num)
    return primes

def convert_list_to_tuple(lst):
    return tuple(lst)

def calculate_mean_of_list(numbers):
    return sum(numbers) / len(numbers)

def get_list_of_squares_upto(n):
    return [x**2 for x in range(1, n + 1)]

def check_if_list_is_sorted(lst):
    return lst == sorted(lst)

def calculate_cylinder_volume(radius, height):
    pi = 3.14159
    return pi * (radius ** 2) * height

def count_words_in_string(s):
    return len(s.split())

def convert_list_to_dict(keys, values):
    return dict(zip(keys, values))

def calculate_sum_of_list(numbers):
    return sum(numbers)

def check_if_two_strings_are_equal(str1, str2):
    return str1 == str2

def get_factorial_of_number(n):
    if n == 0:
        return 1
    else:
        return n * get_factorial_of_number(n - 1)

def convert_list_to_string(lst):
    return ''.join(lst)

def calculate_pythagorean_triplet(a, b):
    c = (a**2 + b**2) ** 0.5
    return c if c.is_integer() else None

def filter_negative_numbers(numbers):
    return [x for x in numbers if x < 0]

def check_if_number_is_even(number):
    return number % 2 == 0

def find_most_frequent_element(lst):
    return max(set(lst), key=lst.count)

def convert_inches_to_centimeters(inches):
    return inches * 2.54

def calculate_sphere_volume(radius):
    pi = 3.14159
    return (4/3) * pi * (radius ** 3)

def check_if_list_contains_duplicates(lst):
    return len(lst) != len(set(lst))

def convert_string_to_title_case(s):
    return s.title()

def calculate_hemisphere_volume(radius):
    pi = 3.14159
    return (2/3) * pi * (radius ** 3)

def get_list_of_cubes_upto(n):
    return [x**3 for x in range(1, n + 1)]

def calculate_sum_of_squares(numbers):
    return sum(x**2 for x in numbers)

def check_if_character_is_vowel(char):
    return char.lower() in 'aeiou'

def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

def convert_list_to_string_with_separator(lst, sep):
    return sep.join(lst)

def calculate_triangular_number(n):
    return n * (n + 1) // 2

def check_if_string_is_uppercase(s):
    return s.isupper()

def calculate_pentagon_area(side_length):
    return (5 * side_length**2) / (4 * (3**0.5))

def filter_zero_values(numbers):
    return [x for x in numbers if x != 0]

def calculate_total_with_tax(amount, tax_rate):
    return amount * (1 + tax_rate)

def check_if_string_contains_digit(s):
    return any(char.isdigit() for char in s)

def convert_pounds_to_kilograms(pounds):
    return pounds * 0.453592

def find_largest_even_number(numbers):
    evens = [x for x in numbers if x % 2 == 0]
    return max(evens) if evens else None

def calculate_ellipse_area(a, b):
    pi = 3.14159
    return pi * a * b

def get_list_of_odds_upto(n):
    return [x for x in range(1, n + 1) if x % 2 != 0]

def check_if_string_is_lowercase(s):
    return s.islower()

def calculate_square_perimeter(side_length):
    return 4 * side_length

def count_occurrences_of_char(s, char):
    return s.count(char)

def calculate_mean_and_median(numbers):
    numbers.sort()
    mean = sum(numbers) / len(numbers)
    median = numbers[len(numbers) // 2] if len(numbers) % 2 != 0 else (numbers[len(numbers) // 2 - 1] + numbers[len(numbers) // 2]) / 2
    return mean, median

def check_if_list_is_palindrome(lst):
    return lst == lst[::-1]

def calculate_total_cost(price, quantity):
    return price * quantity

def find_longest_string_in_list(strings):
    return max(strings, key=len)

def convert_gallons_to_liters(gallons):
    return gallons * 3.78541

def calculate_sphere_surface_area(radius):
    pi = 3.14159
    return 4 * pi * (radius ** 2)

def check_if_string_starts_with_vowel(s):
    return s[0].lower() in 'aeiou'

def calculate_average_word_length(s):
    words = s.split()
    return sum(len(word) for word in words) / len(words)

def find_shortest_string_in_list(strings):
    return min(strings, key=len)

def calculate_total_distance(speeds, time):
    return sum(s * time for s in speeds)

def convert_square_meters_to_square_feet(sq_meters):
    return sq_meters * 10.7639

def calculate_cone_volume(radius, height):
    pi = 3.14159
    return (1/3) * pi * (radius ** 2) * height

def check_if_list_has_no_duplicates(lst):
    return len(lst) == len(set(lst))

def convert_bytes_to_kilobytes(bytes):
    return bytes / 1024

def calculate_average_speed(distance, time):
    return distance / time

def check_if_string_is_palindrome(s):
    return s == s[::-1]

def calculate_quadrilateral_perimeter(side1, side2, side3, side4):
    return side1 + side2 + side3 + side4

def find_second_smallest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers[1] if len(unique_numbers) >= 2 else None

def convert_kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def calculate_triangle_perimeter(side1, side2, side3):
    return side1 + side2 + side3

def check_if_list_is_empty(lst):
    return len(lst) == 0

def calculate_average_of_even_numbers(numbers):
    evens = [x for x in numbers if x % 2 == 0]
    return sum(evens) / len(evens) if evens else 0

def find_highest_frequency_number(numbers):
    return max(set(numbers), key=numbers.count)

def convert_cubic_feet_to_cubic_meters(cubic_feet):
    return cubic_feet * 0.0283168

def calculate_hexagon_area(side_length):
    return (3 * (3**0.5) * side_length**2) / 2

def check_if_string_contains_only_alphabets(s):
    return s.isalpha()

def calculate_total_after_discount(price, discount_rate):
    return price * (1 - discount_rate)

def find_least_frequent_element(lst):
    return min(set(lst), key=lst.count)

def convert_centimeters_to_inches(cm):
    return cm / 2.54

def calculate_cylinder_surface_area(radius, height):
    pi = 3.14159
    return 2 * pi * radius * (radius + height)

def check_if_number_is_odd(number):
    return number % 2 != 0

def calculate_average_of_odd_numbers(numbers):
    odds = [x for x in numbers if x % 2 != 0]
    return sum(odds) / len(odds) if odds else 0

def find_numbers_greater_than_mean(numbers):
    mean = sum(numbers) / len(numbers)
    return [x for x in numbers if x > mean]

def convert_grams_to_ounces(grams):
    return grams / 28.3495

def calculate_cuboid_volume(length, width, height):
    return length * width * height

def check_if_string_contains_whitespace(s):
    return ' ' in s

def convert_square_feet_to_square_meters(sq_feet):
    return sq_feet / 10.7639

def calculate_total_time(hours, minutes, seconds):
    return hours * 3600 + minutes * 60 + seconds

def find_median_of_list(numbers):
    numbers.sort()
    return numbers[len(numbers) // 2] if len(numbers) % 2 != 0 else (numbers[len(numbers) // 2 - 1] + numbers[len(numbers) // 2]) / 2

def check_if_list_contains_sublist(lst, sublist):
    return all(item in lst for item in sublist)

def calculate_sum_of_odd_numbers(numbers):
    return sum(x for x in numbers if x % 2 != 0)

def convert_liters_to_gallons(liters):
    return liters / 3.78541

def calculate_square_surface_area(side_length):
    return 6 * (side_length ** 2)

def check_if_number_is_positive(number):
    return number > 0

def calculate_weighted_average(values, weights):
    return sum(v * w for v, w in zip(values, weights)) / sum(weights)

def find_elements_less_than_mean(numbers):
    mean = sum(numbers) / len(numbers)
    return [x for x in numbers if x < mean]

def convert_kilograms_to_pounds(kg):
    return kg / 0.453592

def calculate_pyramid_volume(base_area, height):
    return (1/3) * base_area * height

def check_if_number_is_negative(number):
    return number < 0

def calculate_average_of_positive_numbers(numbers):
    positives = [x for x in numbers if x > 0]
    return sum(positives) / len(positives) if positives else 0

def find_numbers_less_than_median(numbers):
    median = find_median_of_list(numbers)
    return [x for x in numbers if x < median]

def convert_ounces_to_grams(ounces):
    return ounces * 28.3495

def calculate_prism_volume(base_area, height):
    return base_area * height

def check_if_number_is_zero(number):
    return number == 0

def calculate_average_of_negative_numbers(numbers):
    negatives = [x for x in numbers if x < 0]
    return sum(negatives) / len(negatives) if negatives else 0

def find_numbers_equal_to_mean(numbers):
    mean = sum(numbers) / len(numbers)
    return [x for x in numbers if x == mean]

def convert_square_inches_to_square_centimeters(sq_inches):
    return sq_inches * 6.4516

def calculate_tetrahedron_volume(side_length):
    return (side_length ** 3) / (6 * (2**0.5))

def check_if_number_is_non_positive(number):
    return number <= 0

def calculate_average_of_non_positive_numbers(numbers):
    non_positives = [x for x in numbers if x <= 0]
    return sum(non_positives) / len(non_positives) if non_positives else 0

def find_numbers_equal_to_median(numbers):
    median = find_median_of_list(numbers)
    return [x for x in numbers if x == median]

def convert_square_yards_to_square_meters(sq_yards):
    return sq_yards * 0.836127

def calculate_octahedron_volume(edge_length):
    return (2 * (2**0.5) * (edge_length ** 3)) / 3

def check_if_number_is_non_negative(number):
    return number >= 0

def calculate_average_of_non_negative_numbers(numbers):
    non_negatives = [x for x in numbers if x >= 0]
    return sum(non_negatives) / len(non_negatives) if non_negatives else 0

def find_numbers_greater_than_median(numbers):
    median = find_median_of_list(numbers)
    return [x for x in numbers if x > median]

def convert_square_miles_to_square_kilometers(sq_miles):
    return sq_miles * 2.58999

def calculate_dodecahedron_volume(edge_length):
    return (15 + 7 * (5**0.5)) / 4 * (edge_length ** 3)

def check_if_number_is_fractional(number):
    return number % 1 != 0

def calculate_average_of_fractional_numbers(numbers):
    fractionals = [x for x in numbers if x % 1 != 0]
    return sum(fractionals) / len(fractionals) if fractionals else 0

def find_numbers_less_than_or
