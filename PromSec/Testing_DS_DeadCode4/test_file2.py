from flask import Flask, request, jsonify
import os
import yaml

app = Flask(__name__)

SECRET_TOKEN = "secure_token_2024"

@app.route('/config/upload', methods=['POST'])
def upload_config():
    yaml_config = request.data.decode('utf-8')
    try:
        config = yaml.load(yaml_config, Loader=yaml.FullLoader)
    except yaml.YAMLError:
        return jsonify({"status": "Error", "message": "Invalid YAML format"}), 400

    config_name = config.get('config_name', '')
    config_value = config.get('config_value', '')

    if not config_name or not config_value:
        return jsonify({"status": "Error", "message": "Missing configuration details"}), 400

    return jsonify({"status": "Configuration uploaded", "config_name": config_name, "config_value": config_value})

@app.route('/task/execute', methods=['GET'])
def execute_task():
    task = request.args.get('task', '')
    param = request.args.get('param', '')
    os.system(f"sh execute_task.sh {task} {param}")
    return jsonify({"status": "Task execution started"})

@app.route('/admin/verify', methods=['POST'])
def verify_admin():
    token = request.form.get('token', '')

    if token == SECRET_TOKEN:
        return jsonify({"status": "Verification successful"})
    else:
        return jsonify({"status": "Verification failed"}), 401

@app.route('/admin/update_token', methods=['POST'])
def update_token():
    current_token = request.form.get('current_token', '')

    if current_token != SECRET_TOKEN:
        return jsonify({"status": "Verification failed"}), 401
    
    new_token = request.form.get('new_token', '')
    if not new_token:
        return jsonify({"status": "Error", "message": "Invalid new token"}), 400

    global SECRET_TOKEN
    SECRET_TOKEN = new_token

    return jsonify({"status": "Token updated"})

@app.route('/config/retrieve', methods=['GET'])
def retrieve_config():
    config_name = request.args.get('config_name', '')
    if not config_name:
        return jsonify({"status": "Error", "message": "Configuration name is required"}), 400

    config = {
        "config_name": config_name,
        "config_value": "Example Config Value"
    }

    return jsonify({"status": "Configuration retrieved", "config": config})

@app.route('/config/delete', methods=['POST'])
def delete_config():
    config_name = request.form.get('config_name', '')
    if not config_name:
        return jsonify({"status": "Error", "message": "Configuration name is required"}), 400

    return jsonify({"status": "Configuration deleted", "config_name": config_name})

@app.route('/task/status', methods=['GET'])
def task_status():
    task_id = request.args.get('task_id', '')
    if not task_id:
        return jsonify({"status": "Error", "message": "Task ID is required"}), 400

    return jsonify({"status": "Task status", "task_id": task_id, "status": "Running"})

@app.route('/admin/settings', methods=['POST'])
def update_settings():
    token = request.form.get('token', '')
    
    if token != SECRET_TOKEN:
        return jsonify({"status": "Access denied"}), 401
    
    setting = request.form.get('setting', '')
    if not setting:
        return jsonify({"status": "Error", "message": "Invalid setting"}), 400

    return jsonify({"status": "Setting updated", "setting": setting})

@app.route('/task/logs', methods=['GET'])
def get_task_logs():
    task_id = request.args.get('task_id', '')
    if not task_id:
        return jsonify({"status": "Error", "message": "Task ID is required"}), 400

    logs = "Logs for task " + task_id

    return jsonify({"status": "Task logs", "task_id": task_id, "logs": logs})

@app.route('/backup/data', methods=['GET'])
def backup_data():
    backup_format = request.args.get('format', 'json')
    os.system(f"python3 backup_data.py {backup_format}")
    return jsonify({"status": "Data backup started"})

@app.route('/user/profile', methods=['GET'])
def user_profile():
    user_id = request.args.get('user_id', '')
    if not user_id:
        return jsonify({"status": "Error", "message": "User ID is required"}), 400

    profile = {
        "user_id": user_id,
        "name": "Michael Brown",
        "email": "michael.brown@example.com"
    }

    return jsonify({"status": "User profile retrieved", "profile": profile})

app.run(debug=False)



def calculate_area_of_circle(radius):
    import math
    return math.pi * radius * radius

def convert_temperature_f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0

def reverse_string(input_string):
    return input_string[::-1]

def check_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    fibs = [0, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

def check_palindrome(word):
    return word == word[::-1]

def sum_of_list(numbers):
    return sum(numbers)

def find_maximum(numbers):
    return max(numbers)

def find_minimum(numbers):
    return min(numbers)

def sort_numbers(numbers):
    return sorted(numbers)

def merge_dictionaries(dict1, dict2):
    return {**dict1, **dict2}

def remove_duplicates(numbers):
    return list(set(numbers))

def count_vowels(s):
    return sum(c in 'aeiouAEIOU' for c in s)

def is_even(number):
    return number % 2 == 0

def is_odd(number):
    return number % 2 != 0

def square_number(number):
    return number * number

def cube_number(number):
    return number * number * number

def generate_multiplication_table(number, limit=10):
    return [number * i for i in range(1, limit + 1)]

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_lcm(a, b):
    return abs(a*b) // find_gcd(a, b)

def convert_list_to_dict(keys, values):
    return dict(zip(keys, values))

def find_second_largest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers[-2] if len(unique_numbers) > 1 else None

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def check_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

def count_words(sentence):
    return len(sentence.split())

def find_factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def convert_list_to_string(lst, separator=", "):
    return separator.join(map(str, lst))

def find_unique_elements(lst):
    return list(set(lst))

def reverse_list(lst):
    return lst[::-1]

def sum_of_squares(numbers):
    return sum(x**2 for x in numbers)

def sum_of_cubes(numbers):
    return sum(x**3 for x in numbers)

def generate_fibonacci(n):
    a, b = 0, 1
    fib_sequence = []
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

def get_unique_characters(s):
    return ''.join(set(s))

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def calculate_compound_interest(principal, rate, time, n=1):
    return principal * ((1 + rate/(100*n))**(n*time))

def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def flatten_list(lst_of_lsts):
    return [item for sublist in lst_of_lsts for item in sublist]

def convert_dict_to_list_of_tuples(d):
    return list(d.items())

def calculate_median(numbers):
    n = len(numbers)
    sorted_numbers = sorted(numbers)
    if n % 2 == 1:
        return sorted_numbers[n // 2]
    else:
        mid_idx = n // 2
        return (sorted_numbers[mid_idx - 1] + sorted_numbers[mid_idx]) / 2

def find_mode(numbers):
    from collections import Counter
    count = Counter(numbers)
    max_count = max(count.values())
    return [k for k, v in count.items() if v == max_count]

def calculate_variance(numbers):
    mean = sum(numbers) / len(numbers)
    return sum((x - mean) ** 2 for x in numbers) / len(numbers)

def calculate_standard_deviation(numbers):
    from math import sqrt
    variance = calculate_variance(numbers)
    return sqrt(variance)

def generate_prime_numbers(n):
    primes = []
    candidate = 2
    while len(primes) < n:
        if check_prime(candidate):
            primes.append(candidate)
        candidate += 1
    return primes

def is_substring(s1, s2):
    return s1 in s2

def count_characters(s):
    return len(s)

def get_ascii_value(c):
    return ord(c)

def get_character_from_ascii(ascii_value):
    return chr(ascii_value)

def binary_search(sorted_list, item):
    first = 0
    last = len(sorted_list) - 1
    while first <= last:
        midpoint = (first + last) // 2
        if sorted_list[midpoint] == item:
            return midpoint
        elif sorted_list[midpoint] < item:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return -1

def linear_search(lst, item):
    for i, value in enumerate(lst):
        if value == item:
            return i
    return -1

def find_longest_word(words):
    return max(words, key=len)

def find_shortest_word(words):
    return min(words, key=len)

def calculate_sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

def calculate_product_of_digits(number):
    product = 1
    for digit in str(number):
        product *= int(digit)
    return product

def replace_whitespace_with_underscore(s):
    return s.replace(' ', '_')

def count_occurrences_of_element(lst, element):
    return lst.count(element)

def merge_two_lists(lst1, lst2):
    return lst1 + lst2

def calculate_harmonic_mean(numbers):
    return len(numbers) / sum(1/x for x in numbers)

def count_lowercase_letters(s):
    return sum(c.islower() for c in s)

def count_uppercase_letters(s):
    return sum(c.isupper() for c in s)

def count_digits_in_string(s):
    return sum(c.isdigit() for c in s)

def reverse_words_in_sentence(sentence):
    return ' '.join(reversed(sentence.split()))

def calculate_geometric_mean(numbers):
    from math import prod
    return prod(numbers) ** (1/len(numbers))

def calculate_power(base, exponent):
    return base ** exponent

def find_largest_number(numbers):
    return max(numbers)

def find_smallest_number(numbers):
    return min(numbers)

def swap_values(a, b):
    return b, a

def remove_element_from_list(lst, element):
    return [x for x in lst if x != element]

def count_occurrences_of_word(sentence, word):
    return sentence.split().count(word)

def convert_list_of_tuples_to_dict(tuples):
    return {k: v for k, v in tuples}

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def calculate_speed(distance, time):
    return distance / time

def calculate_acceleration(initial_velocity, final_velocity, time):
    return (final_velocity - initial_velocity) / time

def calculate_distance(speed, time):
    return speed * time

def convert_km_to_miles(km):
    return km * 0.621371

def convert_miles_to_km(miles):
    return miles / 0.621371

def convert_pounds_to_kg(pounds):
    return pounds * 0.453592

def convert_kg_to_pounds(kg):
    return kg / 0.453592

def calculate_area_of_square(side):
    return side * side

def calculate_perimeter_of_square(side):
    return 4 * side

def calculate_area_of_rectangle(length, width):
    return length * width

def calculate_perimeter_of_rectangle(length, width):
    return 2 * (length + width)

def calculate_area_of_triangle(base, height):
    return 0.5 * base * height

def calculate_perimeter_of_triangle(a, b, c):
    return a + b + c

def calculate_area_of_parallelogram(base, height):
    return base * height

def calculate_area_of_trapezoid(base1, base2, height):
    return 0.5 * (base1 + base2) * height

def calculate_area_of_ellipse(a, b):
    from math import pi
    return pi * a * b

def calculate_circumference_of_circle(radius):
    from math import pi
    return 2 * pi * radius

def calculate_volume_of_cube(side):
    return side ** 3

def calculate_surface_area_of_cube(side):
    return 6 * (side ** 2)

def calculate_volume_of_cuboid(length, width, height):
    return length * width * height

def calculate_surface_area_of_cuboid(length, width, height):
    return 2 * (length * width + width * height + height * length)

def calculate_volume_of_sphere(radius):
    from math import pi
    return (4/3) * pi * (radius ** 3)

def calculate_surface_area_of_sphere(radius):
    from math import pi
    return 4 * pi * (radius ** 2)

def calculate_volume_of_cylinder(radius, height):
    from math import pi
    return pi * (radius ** 2) * height

def calculate_surface_area_of_cylinder(radius, height):
    from math import pi
    return 2 * pi * radius * (radius + height)

def calculate_volume_of_cone(radius, height):
    from math import pi
    return (1/3) * pi * (radius ** 2) * height

def calculate_surface_area_of_cone(radius, height):
    from math import pi, sqrt
    return pi * radius * (radius + sqrt(height ** 2 + radius ** 2))

def calculate_volume_of_pyramid(base_area, height):
    return (1/3) * base_area * height

def calculate_surface_area_of_pyramid(base_perimeter, slant_height, base_area):
    return base_area + (1/2) * base_perimeter * slant_height

def convert_seconds_to_minutes(seconds):
    return seconds / 60

def convert_minutes_to_hours(minutes):
    return minutes / 60

def convert_hours_to_days(hours):
    return hours / 24

def convert_days_to_weeks(days):
    return days / 7

def convert_weeks_to_months(weeks):
    return weeks / 4.345

def convert_months_to_years(months):
    return months / 12

def convert_years_to_decades(years):
    return years / 10

def convert_decades_to_centuries(decades):
    return decades / 10

def convert_centuries_to_millennia(centuries):
    return centuries / 10

def convert_millennia_to_years(millennia):
    return millennia * 1000

def calculate_age(birth_year, current_year):
    return current_year - birth_year

def calculate_days_between_dates(date1, date2):
    from datetime import datetime
    date_format = "%Y-%m-%d"
    delta = datetime.strptime(date2, date_format) - datetime.strptime(date1, date_format)
    return delta.days

def calculate_weeks_between_dates(date1, date2):
    return calculate_days_between_dates(date1, date2) / 7

def calculate_months_between_dates(date1, date2):
    return calculate_days_between_dates(date1, date2) / 30.44

def convert_string_to_datetime(date_string, format_string="%Y-%m-%d"):
    from datetime import datetime
    return datetime.strptime(date_string, format_string)

def generate_random_number(min_value, max_value):
    from random import randint
    return randint(min_value, max_value)

def generate_random_float(min_value, max_value):
    from random import uniform
    return uniform(min_value, max_value)

def generate_random_choice(choices):
    from random import choice
    return choice(choices)

def shuffle_list(lst):
    from random import shuffle
    shuffle(lst)
    return lst

def generate_random_string(length):
    import string
    from random import choices
    return ''.join(choices(string.ascii_letters + string.digits, k=length))

def generate_password(length, use_special_characters=True):
    import string
    from random import choices
    characters = string.ascii_letters + string.digits
    if use_special_characters:
        characters += string.punctuation
    return ''.join(choices(characters, k=length))

def roll_dice(sides=6):
    from random import randint
    return randint(1, sides)

def flip_coin():
    from random import choice
    return choice(['Heads', 'Tails'])

def is_vowel(character):
    return character.lower() in 'aeiou'

def is_consonant(character):
    return character.isalpha() and not is_vowel(character)

def is_alphabetic(s):
    return s.isalpha()

def is_numeric(s):
    return s.isdigit()

def is_alphanumeric(s):
    return s.isalnum()

def is_uppercase(s):
    return s.isupper()

def is_lowercase(s):
    return s.islower()

def is_titlecase(s):
    return s.istitle()

def is_whitespace(s):
    return s.isspace()

def is_empty(s):
    return s == ""

def is_positive(number):
    return number > 0

def is_negative(number):
    return number < 0

def is_zero(number):
    return number == 0

def is_divisible_by(number, divisor):
    return number % divisor == 0

def is_multiple_of(number, multiple):
    return number % multiple == 0

def is_power_of_two(number):
    return number > 0 and (number & (number - 1)) == 0

def is_power_of_ten(number):
    while number >= 10 and number % 10 == 0:
        number //= 10
    return number == 1

def is_square_number(number):
    from math import isqrt
    return isqrt(number) ** 2 == number

def is_cube_number(number):
    from math import isqrt
    return round(number ** (1/3)) ** 3 == number

def is_palindrome_number(number):
    s = str(number)
    return s == s[::-1]

def is_armstrong_number(number):
    n = len(str(number))
    return number == sum(int(digit) ** n for digit in str(number))

def is_perfect_number(number):
    return number == sum(divisor for divisor in range(1, number) if number % divisor == 0)

def is_abundant_number(number):
    return sum(divisor for divisor in range(1, number) if number % divisor == 0) > number

def is_deficient_number(number):
    return sum(divisor for divisor in range(1, number) if number % divisor == 0) < number

def is_happy_number(number):
    def get_next(n):
        return sum(int(char) ** 2 for char in str(n))
    seen = set()
    while number != 1 and number not in seen:
        seen.add(number)
        number = get_next(number)
    return number == 1

def is_fibonacci_number(number):
    from math import isqrt
    def is_perfect_square(x):
        s = isqrt(x)
        return s * s == x
    return is_perfect_square(5 * number * number + 4) or is_perfect_square(5 * number * number - 4)

def is_triangular_number(number):
    from math import isqrt
    def is_perfect_square(x):
        s = isqrt(x)
        return s * s == x
    return is_perfect_square(8 * number + 1)

def is_pentagonal_number(number):
    from math import isqrt
    def is_perfect_square(x):
        s = isqrt(x)
        return s * s == x
    n = (1 + (1 + 24 * number)**0.5) / 6
    return n.is_integer()

def is_hexagonal_number(number):
    from math import isqrt
    def is_perfect_square(x):
        s = isqrt(x)
        return s * s == x
    n = (1 + (1 + 8 * number)**0.5) / 4
    return n.is_integer()

def is_heptagonal_number(number):
    from math import isqrt
    def is_perfect_square(x):
        s = isqrt(x)
        return s * s == x
    n = (3 + (9 + 40 * number)**0.5) / 10
    return n.is_integer()

def is_octagonal_number(number):
    from math import isqrt
    def is_perfect_square(x):
        s = isqrt(x)
        return s * s == x
    n = (1 + (1 + 3 * number)**0.5) / 3
    return n.is_integer()
