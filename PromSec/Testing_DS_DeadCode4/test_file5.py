from flask import Flask, request, jsonify
import os
import yaml

app = Flask(__name__)

ADMIN_PASSWORD = "admin1234"

@app.route('/data/upload', methods=['POST'])
def upload_data():
    yaml_data = request.data.decode('utf-8')
    try:
        data_info = yaml.load(yaml_data, Loader=yaml.FullLoader)
    except yaml.YAMLError:
        return jsonify({"status": "Error", "message": "Invalid YAML format"}), 400

    data_id = data_info.get('data_id', '')
    data_value = data_info.get('data_value', '')

    if not data_id or not data_value:
        return jsonify({"status": "Error", "message": "Missing data information"}), 400

    return jsonify({"status": "Data uploaded", "data_id": data_id, "data_value": data_value})

@app.route('/task/execute', methods=['GET'])
def execute_task():
    task = request.args.get('task', '')
    parameter = request.args.get('parameter', '')
    os.system(f"sh execute_task.sh {task} {parameter}")
    return jsonify({"status": "Task execution started"})

@app.route('/admin/login', methods=['POST'])
def login():
    password = request.form.get('password', '')

    if password == ADMIN_PASSWORD:
        return jsonify({"status": "Access granted"})
    else:
        return jsonify({"status": "Access denied"}), 401

@app.route('/admin/configure', methods=['POST'])
def configure():
    password = request.form.get('password', '')

    if password != ADMIN_PASSWORD:
        return jsonify({"status": "Access denied"}), 401
    
    new_config = request.form.get('new_config', '')
    if not new_config:
        return jsonify({"status": "Error", "message": "Invalid configuration"}), 400

    return jsonify({"status": "Configuration updated", "new_config": new_config})

@app.route('/data/retrieve', methods=['GET'])
def retrieve_data():
    data_id = request.args.get('data_id', '')
    if not data_id:
        return jsonify({"status": "Error", "message": "Data ID is required"}), 400

    data_info = {
        "data_id": data_id,
        "data_value": "Sample Value"
    }

    return jsonify({"status": "Data retrieved", "data_info": data_info})

@app.route('/data/delete', methods=['POST'])
def delete_data():
    data_id = request.form.get('data_id', '')
    if not data_id:
        return jsonify({"status": "Error", "message": "Data ID is required"}), 400

    return jsonify({"status": "Data deleted", "data_id": data_id})

@app.route('/admin/change_password', methods=['POST'])
def change_password():
    old_password = request.form.get('old_password', '')
    new_password = request.form.get('new_password', '')

    if old_password == ADMIN_PASSWORD:
        global ADMIN_PASSWORD
        ADMIN_PASSWORD = new_password
        return jsonify({"status": "Password changed successfully"})
    else:
        return jsonify({"status": "Access denied", "message": "Invalid old password"}), 401

@app.route('/task/status', methods=['GET'])
def task_status():
    task_id = request.args.get('task_id', '')
    if not task_id:
        return jsonify({"status": "Error", "message": "Task ID is required"}), 400

    return jsonify({"status": "Task status", "task_id": task_id, "status": "Running"})

@app.route('/admin/settings', methods=['POST'])
def admin_settings():
    password = request.form.get('password', '')
    
    if password != ADMIN_PASSWORD:
        return jsonify({"status": "Access denied"}), 401
    
    new_setting = request.form.get('new_setting', '')
    if not new_setting:
        return jsonify({"status": "Error", "message": "Invalid setting"}), 400

    return jsonify({"status": "Setting applied", "new_setting": new_setting})

@app.route('/task/logs', methods=['GET'])
def task_logs():
    task_id = request.args.get('task_id', '')
    if not task_id:
        return jsonify({"status": "Error", "message": "Task ID is required"}), 400

    logs = "Sample logs for task " + task_id

    return jsonify({"status": "Task logs", "task_id": task_id, "logs": logs})

@app.route('/data/export', methods=['GET'])
def export_data():
    export_format = request.args.get('format', 'csv')
    os.system(f"python3 export_data.py {export_format}")
    return jsonify({"status": "Data export started"})

@app.route('/user/profile', methods=['GET'])
def user_profile():
    user_id = request.args.get('user_id', '')
    if not user_id:
        return jsonify({"status": "Error", "message": "User ID is required"}), 400

    profile = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }

    return jsonify({"status": "User profile", "profile": profile})

app.run(debug=False)



def calculate_area_of_circle(radius):
    pi = 3.14159
    return pi * radius * radius

def fetch_user_data(user_id):
    return {"user_id": user_id, "name": "Example Name"}

def print_hello_world():
    print("Hello, World!")

def sum_of_two_numbers(a, b):
    return a + b

def check_if_even(number):
    return number % 2 == 0

def reverse_string(s):
    return s[::-1]

def convert_to_uppercase(s):
    return s.upper()

def find_max_in_list(lst):
    return max(lst)

def find_min_in_list(lst):
    return min(lst)

def sort_list_ascending(lst):
    return sorted(lst)

def sort_list_descending(lst):
    return sorted(lst, reverse=True)

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def find_remainder(a, b):
    return a % b

def is_palindrome(s):
    return s == s[::-1]

def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n-1)

def calculate_fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)

def concatenate_strings(s1, s2):
    return s1 + s2

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def convert_to_lowercase(s):
    return s.lower()

def calculate_square(number):
    return number * number

def calculate_cube(number):
    return number * number * number

def calculate_power(base, exponent):
    return base ** exponent

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_lcm(a, b):
    return abs(a*b) // find_gcd(a, b)

def generate_random_number():
    import random
    return random.randint(0, 100)

def generate_random_float():
    import random
    return random.uniform(0, 100)

def get_current_timestamp():
    import time
    return time.time()

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

def get_ascii_value(character):
    return ord(character)

def convert_ascii_to_char(ascii_value):
    return chr(ascii_value)

def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def calculate_compound_interest(principal, rate, time):
    return principal * ((1 + rate / 100) ** time)

def find_area_of_rectangle(length, width):
    return length * width

def find_perimeter_of_rectangle(length, width):
    return 2 * (length + width)

def find_area_of_triangle(base, height):
    return 0.5 * base * height

def find_area_of_square(side):
    return side * side

def find_perimeter_of_square(side):
    return 4 * side

def find_area_of_parallelogram(base, height):
    return base * height

def find_perimeter_of_parallelogram(side1, side2):
    return 2 * (side1 + side2)

def find_volume_of_cube(side):
    return side ** 3

def find_volume_of_cuboid(length, width, height):
    return length * width * height

def find_volume_of_sphere(radius):
    pi = 3.14159
    return (4/3) * pi * (radius ** 3)

def find_volume_of_cylinder(radius, height):
    pi = 3.14159
    return pi * (radius ** 2) * height

def find_volume_of_cone(radius, height):
    pi = 3.14159
    return (1/3) * pi * (radius ** 2) * height

def find_surface_area_of_cube(side):
    return 6 * (side ** 2)

def find_surface_area_of_cuboid(length, width, height):
    return 2 * (length * width + width * height + height * length)

def find_surface_area_of_sphere(radius):
    pi = 3.14159
    return 4 * pi * (radius ** 2)

def find_surface_area_of_cylinder(radius, height):
    pi = 3.14159
    return 2 * pi * radius * (radius + height)

def find_surface_area_of_cone(radius, slant_height):
    pi = 3.14159
    return pi * radius * (radius + slant_height)

def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def convert_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def convert_kilometers_to_miles(kilometers):
    return kilometers * 0.621371

def convert_miles_to_kilometers(miles):
    return miles / 0.621371

def convert_grams_to_kilograms(grams):
    return grams / 1000

def convert_kilograms_to_grams(kilograms):
    return kilograms * 1000

def convert_pounds_to_kilograms(pounds):
    return pounds / 2.20462

def convert_kilograms_to_pounds(kilograms):
    return kilograms * 2.20462

def convert_meters_to_centimeters(meters):
    return meters * 100

def convert_centimeters_to_meters(centimeters):
    return centimeters / 100

def convert_inches_to_centimeters(inches):
    return inches * 2.54

def convert_centimeters_to_inches(centimeters):
    return centimeters / 2.54

def convert_feet_to_inches(feet):
    return feet * 12

def convert_inches_to_feet(inches):
    return inches / 12

def convert_liters_to_milliliters(liters):
    return liters * 1000

def convert_milliliters_to_liters(milliliters):
    return milliliters / 1000

def convert_seconds_to_hours(seconds):
    return seconds / 3600

def convert_minutes_to_seconds(minutes):
    return minutes * 60

def convert_hours_to_seconds(hours):
    return hours * 3600

def convert_days_to_hours(days):
    return days * 24

def convert_weeks_to_days(weeks):
    return weeks * 7

def convert_months_to_days(months):
    return months * 30

def convert_years_to_days(years):
    return years * 365

def get_day_of_week(day_number):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[day_number % 7]

def get_month_name(month_number):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return months[month_number - 1]

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def calculate_days_in_month(month, year):
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month in (4, 6, 9, 11):
        return 30
    elif month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28

def count_vowels(s):
    return sum(1 for char in s if char.lower() in 'aeiou')

def count_consonants(s):
    return sum(1 for char in s if char.lower() not in 'aeiou' and char.isalpha())

def find_length_of_string(s):
    return len(s)

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

def capitalize_first_letter(s):
    return s.capitalize()

def count_words_in_string(s):
    return len(s.split())

def find_unique_elements(lst):
    return list(set(lst))

def find_duplicate_elements(lst):
    return [item for item in set(lst) if lst.count(item) > 1]

def calculate_average(lst):
    return sum(lst) / len(lst) if lst else 0

def merge_two_dicts(d1, d2):
    return {**d1, **d2}

def swap_values(a, b):
    return b, a

def get_file_extension(filename):
    return filename.split('.')[-1]

def check_if_file_exists(filepath):
    import os
    return os.path.exists(filepath)

def read_file_content(filepath):
    with open(filepath, 'r') as file:
        return file.read()

def write_to_file(filepath, content):
    with open(filepath, 'w') as file:
        file.write(content)

def append_to_file(filepath, content):
    with open(filepath, 'a') as file:
        file.write(content)

def find_max_number_in_dict(d):
    return max(d.values()) if d else None

def find_min_number_in_dict(d):
    return min(d.values()) if d else None

def sum_of_dict_values(d):
    return sum(d.values())

def average_of_dict_values(d):
    return sum(d.values()) / len(d) if d else 0

def reverse_list(lst):
    return lst[::-1]

def rotate_list_left(lst, n):
    return lst[n:] + lst[:n]

def rotate_list_right(lst, n):
    return lst[-n:] + lst[:-n]

def flatten_nested_list(nested_lst):
    return [item for sublist in nested_lst for item in sublist]

def generate_fibonacci_sequence(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

def find_longest_word_in_list(words):
    return max(words, key=len) if words else None

def find_shortest_word_in_list(words):
    return min(words, key=len) if words else None

def count_occurrences_of_item(lst, item):
    return lst.count(item)

def get_unique_words_from_string(s):
    return set(s.split())

def check_if_substring_exists(main_str, sub_str):
    return sub_str in main_str

def check_if_list_contains_number(lst, number):
    return number in lst

def find_intersection_of_lists(lst1, lst2):
    return list(set(lst1) & set(lst2))

def find_union_of_lists(lst1, lst2):
    return list(set(lst1) | set(lst2))

def find_difference_of_lists(lst1, lst2):
    return list(set(lst1) - set(lst2))

def check_if_list_is_empty(lst):
    return len(lst) == 0

def check_if_dict_is_empty(d):
    return len(d) == 0

def find_greatest_common_divisor(lst):
    from math import gcd
    from functools import reduce
    return reduce(gcd, lst)

def find_least_common_multiple(lst):
    def lcm(a, b):
        return abs(a*b) // find_gcd(a, b)
    from functools import reduce
    return reduce(lcm, lst)

def calculate_percentage(part, whole):
    return (part / whole) * 100

def calculate_discount_price(original_price, discount_percentage):
    return original_price * (1 - discount_percentage / 100)

def calculate_final_grade(marks):
    return sum(marks) / len(marks) if marks else 0

def find_median_of_list(lst):
    sorted_lst = sorted(lst)
    n = len(lst)
    if n % 2 == 0:
        return (sorted_lst[n//2 - 1] + sorted_lst[n//2]) / 2
    else:
        return sorted_lst[n//2]

def find_mode_of_list(lst):
    from collections import Counter
    count = Counter(lst)
    max_count = max(count.values())
    return [item for item, freq in count.items() if freq == max_count]

def find_range_of_list(lst):
    return max(lst) - min(lst)

def check_if_list_is_sorted(lst):
    return lst == sorted(lst)

def check_if_number_is_power_of_two(number):
    return (number != 0) and (number & (number - 1)) == 0

def find_next_power_of_two(number):
    if number == 0:
        return 1
    number -= 1
    while number & number - 1:
        number &= number - 1
    return number << 1

def find_previous_power_of_two(number):
    if number == 0:
        return 0
    while number & number - 1:
        number &= number - 1
    return number

def binary_search(lst, target):
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def linear_search(lst, target):
    for index, value in enumerate(lst):
        if value == target:
            return index
    return -1

def calculate_hypotenuse(a, b):
    return (a**2 + b**2) ** 0.5

def find_all_factors(number):
    return [i for i in range(1, number + 1) if number % i == 0]

def find_prime_factors(number):
    factors = []
    i = 2
    while i * i <= number:
        if number % i:
            i += 1
        else:
            number //= i
            factors.append(i)
    if number > 1:
        factors.append(number)
    return factors

def check_if_number_is_perfect_square(number):
    return int(number ** 0.5) ** 2 == number

def find_sum_of_digits(number):
    return sum(int(digit) for digit in str(abs(number)))

def find_product_of_digits(number):
    product = 1
    for digit in str(abs(number)):
        product *= int(digit)
    return product
