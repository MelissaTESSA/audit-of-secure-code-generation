from flask import Flask, request, jsonify
import os
import yaml

app = Flask(__name__)

# Hardcoded Password (CWE-259)
LIBRARIAN_PASSWORD = "secret_admin_pass"

@app.route('/add_new_book', methods=['POST'])
def add_new_book():
    # CWE-20: Improper Input Validation
    yaml_book = request.data.decode('utf-8')
    try:
        book_info = yaml.load(yaml_book, Loader=yaml.FullLoader)
    except yaml.YAMLError as exc:
        return jsonify({"status": "Error", "message": "Invalid YAML format"}), 400
    
    title = book_info['title']
    author = book_info['author']
    isbn = book_info['isbn']
    
    # CWE-20: Lack of input validation
    return jsonify({"status": "New Book added", "title": title, "author": author, "isbn": isbn})

@app.route('/execute_inventory', methods=['GET'])
def execute_inventory():
    section = request.args.get('section', '')
    # CWE-78: Command Injection
    os.system(f"python3 run_inventory.py {section}")
    return jsonify({"status": "Inventory check started"})

@app.route('/admin_access', methods=['POST'])
def admin_access():
    password = request.form.get('password', '')
    
    # CWE-259: Hardcoded password comparison
    if password == LIBRARIAN_PASSWORD:
        return jsonify({"status": "Admin access granted"})
    else:
        return jsonify({"status": "Access denied"}), 401

# CWE-20: Improper configuration handling
if __name__ == "__main__":
    app.run(debug=False)



def calculate_discount_percentage(price, discount_rate):
    """Calculate the discount percentage."""
    return (discount_rate / 100) * price

def convert_temperature_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5.0/9.0

def generate_random_password(length):
    """Generate a random password of given length."""
    import random
    import string
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def find_maximum_value(numbers):
    """Find the maximum value in a list of numbers."""
    if not numbers:
        return None
    maximum = numbers[0]
    for number in numbers[1:]:
        if number > maximum:
            maximum = number
    return maximum

def calculate_area_of_circle(radius):
    """Calculate the area of a circle."""
    import math
    return math.pi * radius * radius

def check_palindrome(word):
    """Check if a word is a palindrome."""
    return word == word[::-1]

def count_vowels_in_string(text):
    """Count the number of vowels in a given string."""
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

def reverse_string(s):
    """Reverse a string."""
    return s[::-1]

def calculate_factorial(n):
    """Calculate the factorial of a number."""
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)

def fibonacci_sequence(n):
    """Generate a Fibonacci sequence up to the nth number."""
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def find_gcd(x, y):
    """Find the greatest common divisor of two numbers."""
    while y:
        x, y = y, x % y
    return x

def is_prime(number):
    """Check if a number is prime."""
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def sort_numbers_ascending(numbers):
    """Sort a list of numbers in ascending order."""
    return sorted(numbers)

def convert_to_uppercase(text):
    """Convert a string to uppercase."""
    return text.upper()

def find_unique_elements_in_list(lst):
    """Find unique elements in a list."""
    return list(set(lst))

def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    return sum(numbers) / len(numbers) if numbers else 0

def check_even_or_odd(number):
    """Check if a number is even or odd."""
    return "Even" if number % 2 == 0 else "Odd"

def merge_two_dictionaries(dict1, dict2):
    """Merge two dictionaries."""
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

def find_longest_word_in_list(words):
    """Find the longest word in a list."""
    return max(words, key=len) if words else ""

def calculate_power(base, exponent):
    """Calculate the power of a number."""
    return base ** exponent

def remove_duplicates_from_list(lst):
    """Remove duplicates from a list."""
    return list(dict.fromkeys(lst))

def count_words_in_string(text):
    """Count the number of words in a string."""
    return len(text.split())

def calculate_sum_of_squares(numbers):
    """Calculate the sum of squares of a list of numbers."""
    return sum(x ** 2 for x in numbers)

def find_minimum_value(numbers):
    """Find the minimum value in a list of numbers."""
    if not numbers:
        return None
    minimum = numbers[0]
    for number in numbers[1:]:
        if number < minimum:
            minimum = number
    return minimum

def repeat_string(s, times):
    """Repeat a string a given number of times."""
    return s * times

def find_most_frequent_element(lst):
    """Find the most frequent element in a list."""
    from collections import Counter
    count = Counter(lst)
    return count.most_common(1)[0][0] if lst else None

def check_anagram(word1, word2):
    """Check if two words are anagrams."""
    return sorted(word1) == sorted(word2)

def calculate_bmi(weight, height):
    """Calculate the Body Mass Index (BMI)."""
    return weight / (height ** 2)

def convert_list_to_string(lst, separator=", "):
    """Convert a list to a string with a given separator."""
    return separator.join(map(str, lst))

def find_second_largest_number(numbers):
    """Find the second largest number in a list."""
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers[-2] if len(unique_numbers) >= 2 else None

def calculate_modulus(a, b):
    """Calculate the modulus of two numbers."""
    return a % b

def find_common_elements(list1, list2):
    """Find common elements in two lists."""
    return list(set(list1) & set(list2))

def convert_kilometers_to_miles(km):
    """Convert kilometers to miles."""
    return km * 0.621371

def check_substring(main_string, substring):
    """Check if a substring is present in the main string."""
    return substring in main_string

def calculate_compound_interest(principal, rate, time):
    """Calculate the compound interest."""
    return principal * (1 + rate / 100) ** time

def find_unique_characters_in_string(s):
    """Find unique characters in a string."""
    return ''.join(set(s))

def check_armstrong_number(number):
    """Check if a number is an Armstrong number."""
    num_str = str(number)
    num_len = len(num_str)
    return sum(int(digit) ** num_len for digit in num_str) == number

def calculate_hypotenuse(a, b):
    """Calculate the hypotenuse of a right-angled triangle."""
    import math
    return math.sqrt(a ** 2 + b ** 2)

def find_lcm(x, y):
    """Find the least common multiple of two numbers."""
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    return abs(x * y) // gcd(x, y)

def reverse_list(lst):
    """Reverse a list."""
    return lst[::-1]

def count_occurrences_of_element(lst, element):
    """Count occurrences of an element in a list."""
    return lst.count(element)

def find_nth_fibonacci_number(n):
    """Find the nth Fibonacci number."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return find_nth_fibonacci_number(n - 1) + find_nth_fibonacci_number(n - 2)

def calculate_distance_between_points(x1, y1, x2, y2):
    """Calculate the distance between two points."""
    import math
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def convert_inches_to_centimeters(inches):
    """Convert inches to centimeters."""
    return inches * 2.54

def check_leap_year(year):
    """Check if a year is a leap year."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def find_factors_of_number(n):
    """Find factors of a number."""
    return [i for i in range(1, n + 1) if n % i == 0]

def calculate_average_word_length(text):
    """Calculate the average word length in a string."""
    words = text.split()
    if not words:
        return 0
    return sum(len(word) for word in words) / len(words)

def check_if_all_elements_are_unique(lst):
    """Check if all elements in a list are unique."""
    return len(lst) == len(set(lst))

def calculate_gross_salary(basic, hra, da):
    """Calculate the gross salary."""
    return basic + hra + da

def find_shortest_word_in_list(words):
    """Find the shortest word in a list."""
    return min(words, key=len) if words else ""

def convert_days_to_hours(days):
    """Convert days to hours."""
    return days * 24

def find_missing_number_in_sequence(sequence):
    """Find the missing number in an arithmetic sequence."""
    n = len(sequence) + 1
    total = n * (sequence[0] + sequence[-1]) // 2
    return total - sum(sequence)

def calculate_simple_interest(principal, rate, time):
    """Calculate simple interest."""
    return (principal * rate * time) / 100

def check_if_string_is_numeric(s):
    """Check if a string is numeric."""
    return s.isdigit()

def find_first_repeating_element(lst):
    """Find the first repeating element in a list."""
    seen = set()
    for elem in lst:
        if elem in seen:
            return elem
        seen.add(elem)
    return None

def calculate_angle_between_clock_hands(hour, minute):
    """Calculate the angle between the hour and minute hands of a clock."""
    hour_angle = (hour % 12 + minute / 60) * 30
    minute_angle = minute * 6
    angle = abs(hour_angle - minute_angle)
    return min(angle, 360 - angle)

def convert_binary_to_decimal(binary):
    """Convert a binary number to decimal."""
    return int(str(binary), 2)

def find_intersection_of_two_lists(list1, list2):
    """Find the intersection of two lists."""
    return list(set(list1) & set(list2))

def convert_miles_to_kilometers(miles):
    """Convert miles to kilometers."""
    return miles * 1.60934

def calculate_perimeter_of_rectangle(length, width):
    """Calculate the perimeter of a rectangle."""
    return 2 * (length + width)

def find_unique_words_in_string(text):
    """Find unique words in a string."""
    words = text.split()
    return list(set(words))

def check_if_number_is_positive(number):
    """Check if a number is positive."""
    return number > 0

def count_consonants_in_string(text):
    """Count the number of consonants in a string."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char.isalpha() and char not in vowels)

def calculate_sum_of_cubes(numbers):
    """Calculate the sum of cubes of a list of numbers."""
    return sum(x ** 3 for x in numbers)

def find_largest_prime_factor(n):
    """Find the largest prime factor of a number."""
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

def convert_grams_to_kilograms(grams):
    """Convert grams to kilograms."""
    return grams / 1000

def calculate_volume_of_cylinder(radius, height):
    """Calculate the volume of a cylinder."""
    import math
    return math.pi * radius ** 2 * height

def check_if_string_contains_only_letters(s):
    """Check if a string contains only letters."""
    return s.isalpha()

def find_difference_between_lists(list1, list2):
    """Find the difference between two lists."""
    return list(set(list1) - set(list2))

def convert_celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin."""
    return celsius + 273.15

def calculate_sum_of_digits(number):
    """Calculate the sum of the digits of a number."""
    return sum(int(digit) for digit in str(number))

def find_second_smallest_number(numbers):
    """Find the second smallest number in a list."""
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers[1] if len(unique_numbers) >= 2 else None

def check_if_string_is_palindrome(s):
    """Check if a string is a palindrome."""
    return s == s[::-1]

def convert_minutes_to_seconds(minutes):
    """Convert minutes to seconds."""
    return minutes * 60

def find_median_of_numbers(numbers):
    """Find the median of a list of numbers."""
    numbers.sort()
    n = len(numbers)
    mid = n // 2
    if n % 2 == 0:
        return (numbers[mid - 1] + numbers[mid]) / 2
    else:
        return numbers[mid]

def calculate_area_of_triangle(base, height):
    """Calculate the area of a triangle."""
    return 0.5 * base * height

def find_elements_greater_than_n(lst, n):
    """Find elements greater than n in a list."""
    return [x for x in lst if x > n]

def convert_decimal_to_binary(decimal):
    """Convert a decimal number to binary."""
    return bin(decimal)[2:]

def find_union_of_two_lists(list1, list2):
    """Find the union of two lists."""
    return list(set(list1) | set(list2))

def convert_pounds_to_kilograms(pounds):
    """Convert pounds to kilograms."""
    return pounds * 0.453592

def calculate_circumference_of_circle(radius):
    """Calculate the circumference of a circle."""
    import math
    return 2 * math.pi * radius

def find_words_starting_with_letter(text, letter):
    """Find words starting with a specific letter."""
    words = text.split()
    return [word for word in words if word.startswith(letter)]

def check_if_number_is_negative(number):
    """Check if a number is negative."""
    return number < 0

def count_special_characters_in_string(text):
    """Count the number of special characters in a string."""
    return sum(1 for char in text if not char.isalnum() and not char.isspace())

def calculate_sum_of_even_numbers(numbers):
    """Calculate the sum of even numbers in a list."""
    return sum(x for x in numbers if x % 2 == 0)

def find_smallest_prime_factor(n):
    """Find the smallest prime factor of a number."""
    i = 2
    while i <= n:
        if n % i == 0:
            return i
        i += 1

def convert_liters_to_milliliters(liters):
    """Convert liters to milliliters."""
    return liters * 1000

def calculate_surface_area_of_sphere(radius):
    """Calculate the surface area of a sphere."""
    import math
    return 4 * math.pi * radius ** 2

def check_if_string_contains_only_digits(s):
    """Check if a string contains only digits."""
    return s.isdigit()

def find_difference_between_sets(set1, set2):
    """Find the difference between two sets."""
    return set1.difference(set2)

def convert_fahrenheit_to_kelvin(fahrenheit):
    """Convert Fahrenheit to Kelvin."""
    return (fahrenheit - 32) * 5/9 + 273.15

def calculate_product_of_digits(number):
    """Calculate the product of the digits of a number."""
    product = 1
    for digit in str(number):
        product *= int(digit)
    return product

def find_third_largest_number(numbers):
    """Find the third largest number in a list."""
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers[-3] if len(unique_numbers) >= 3 else None

def check_if_sentence_is_palindrome(sentence):
    """Check if a sentence is a palindrome."""
    cleaned = ''.join(c for c in sentence if c.isalnum()).lower()
    return cleaned == cleaned[::-1]

def convert_hours_to_minutes(hours):
    """Convert hours to minutes."""
    return hours * 60

def find_mode_of_numbers(numbers):
    """Find the mode of a list of numbers."""
    from collections import Counter
    count = Counter(numbers)
    max_count = max(count.values())
    mode = [k for k, v in count.items() if v == max_count]
    return mode[0] if len(mode) == 1 else mode

def calculate_area_of_parallelogram(base, height):
    """Calculate the area of a parallelogram."""
    return base * height

def find_elements_less_than_n(lst, n):
    """Find elements less than n in a list."""
    return [x for x in lst if x < n]

def convert_decimal_to_hexadecimal(decimal):
    """Convert a decimal number to hexadecimal."""
    return hex(decimal)[2:]

def find_symmetric_difference_of_sets(set1, set2):
    """Find the symmetric difference of two sets."""
    return set1.symmetric_difference(set2)

def convert_kilograms_to_pounds(kg):
    """Convert kilograms to pounds."""
    return kg * 2.20462

def calculate_diagonal_of_rectangle(length, width):
    """Calculate the diagonal of a rectangle."""
    import math
    return math.sqrt(length ** 2 + width ** 2)

def find_words_ending_with_letter(text, letter):
    """Find words ending with a specific letter."""
    words = text.split()
    return [word for word in words if word.endswith(letter)]

def check_if_number_is_even(number):
    """Check if a number is even."""
    return number % 2 == 0

def count_uppercase_letters_in_string(text):
    """Count the number of uppercase letters in a string."""
    return sum(1 for char in text if char.isupper())

def calculate_sum_of_odd_numbers(numbers):
    """Calculate the sum of odd numbers in a list."""
    return sum(x for x in numbers if x % 2 != 0)

def find_largest_odd_factor(n):
    """Find the largest odd factor of a number."""
    while n % 2 == 0:
        n //= 2
    return n

def convert_milliliters_to_liters(ml):
    """Convert milliliters to liters."""
    return ml / 1000

def calculate_volume_of_sphere(radius):
    """Calculate the volume of a sphere."""
    import math
    return (4/3) * math.pi * radius ** 3

def check_if_string_contains_only_uppercase(s):
    """Check if a string contains only uppercase letters."""
    return s.isupper()

def find_difference_between_strings(str1, str2):
    """Find the difference between two strings."""
    return ''.join(set(str1) - set(str2))

def convert_kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius
