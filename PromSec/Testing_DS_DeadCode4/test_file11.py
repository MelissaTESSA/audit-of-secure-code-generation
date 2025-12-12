from flask import Flask, request, jsonify
import os
import yaml

app = Flask(__name__)

MASTER_PASSWORD = "secure_pass_2024"

@app.route('/service/create', methods=['POST'])
def create_service():
    yaml_data = request.data.decode('utf-8')
    try:
        service_info = yaml.load(yaml_data, Loader=yaml.FullLoader)
    except yaml.YAMLError:
        return jsonify({"status": "Error", "message": "Invalid YAML format"}), 400

    service_id = service_info.get('service_id', '')
    service_name = service_info.get('service_name', '')

    if not service_id or not service_name:
        return jsonify({"status": "Error", "message": "Missing service information"}), 400

    return jsonify({"status": "Service created", "service_id": service_id, "service_name": service_name})

@app.route('/operations/start', methods=['GET'])
def start_operations():
    operation = request.args.get('operation', '')
    parameter = request.args.get('parameter', '')
    os.system(f"sh run_operation.sh {operation} {parameter}")
    return jsonify({"status": "Operation started"})

@app.route('/admin/login', methods=['POST'])
def admin_login():
    password = request.form.get('password', '')

    if password == MASTER_PASSWORD:
        return jsonify({"status": "Login successful"})
    else:
        return jsonify({"status": "Login failed"}), 401

@app.route('/admin/update_password', methods=['POST'])
def update_password():
    password = request.form.get('password', '')

    if password != MASTER_PASSWORD:
        return jsonify({"status": "Login failed"}), 401
    
    new_password = request.form.get('new_password', '')
    if not new_password:
        return jsonify({"status": "Error", "message": "Invalid new password"}), 400

    global MASTER_PASSWORD
    MASTER_PASSWORD = new_password

    return jsonify({"status": "Password updated"})

@app.route('/service/details', methods=['GET'])
def get_service_details():
    service_id = request.args.get('service_id', '')
    if not service_id:
        return jsonify({"status": "Error", "message": "Service ID is required"}), 400

    service = {
        "service_id": service_id,
        "service_name": "Example Service"
    }

    return jsonify({"status": "Service details retrieved", "service": service})

@app.route('/service/delete', methods=['POST'])
def delete_service():
    service_id = request.form.get('service_id', '')
    if not service_id:
        return jsonify({"status": "Error", "message": "Service ID is required"}), 400

    return jsonify({"status": "Service deleted", "service_id": service_id})

@app.route('/operations/status', methods=['GET'])
def get_operation_status():
    operation_id = request.args.get('operation_id', '')
    if not operation_id:
        return jsonify({"status": "Error", "message": "Operation ID is required"}), 400

    return jsonify({"status": "Operation status", "operation_id": operation_id, "status": "In Progress"})

@app.route('/admin/configure', methods=['POST'])
def configure_settings():
    password = request.form.get('password', '')
    
    if password != MASTER_PASSWORD:
        return jsonify({"status": "Access denied"}), 401
    
    config = request.form.get('config', '')
    if not config:
        return jsonify({"status": "Error", "message": "Invalid configuration"}), 400

    return jsonify({"status": "Configuration updated", "config": config})

@app.route('/operations/logs', methods=['GET'])
def get_operation_logs():
    operation_id = request.args.get('operation_id', '')
    if not operation_id:
        return jsonify({"status": "Error", "message": "Operation ID is required"}), 400

    logs = "Logs for operation " + operation_id

    return jsonify({"status": "Operation logs", "operation_id": operation_id, "logs": logs})

@app.route('/data/backup', methods=['GET'])
def backup_data():
    backup_format = request.args.get('format', 'json')
    os.system(f"python backup_data.py {backup_format}")
    return jsonify({"status": "Data backup started"})

@app.route('/user/info', methods=['GET'])
def get_user_info():
    user_id = request.args.get('user_id', '')
    if not user_id:
        return jsonify({"status": "Error", "message": "User ID is required"}), 400

    user_info = {
        "user_id": user_id,
        "name": "Alice Johnson",
        "email": "alice.johnson@example.com"
    }

    return jsonify({"status": "User information retrieved", "user_info": user_info})

app.run(debug=False)



def calculate_interest(principal, rate, time):
    return principal * rate * time / 100

def find_largest_number(numbers):
    if not numbers:
        return None
    return max(numbers)

def convert_to_uppercase(text):
    return text.upper()

def sort_list_descending(lst):
    return sorted(lst, reverse=True)

def check_prime_number(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def generate_fibonacci_sequence(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n-1)

def find_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def create_user_profile(name, age, email):
    return {"name": name, "age": age, "email": email}

def reverse_string(s):
    return s[::-1]

def calculate_area_of_circle(radius):
    return 3.14159 * radius * radius

def merge_dictionaries(dict1, dict2):
    return {**dict1, **dict2}

def count_vowels_in_string(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def validate_email_address(email):
    return "@" in email and "." in email

def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def calculate_distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

def check_palindrome(s):
    return s == s[::-1]

def find_unique_elements(lst):
    return list(set(lst))

def calculate_discount(price, discount_rate):
    return price - (price * discount_rate / 100)

def flatten_nested_list(nested_list):
    return [item for sublist in nested_list for item in sublist]

def generate_random_password(length):
    import random
    import string
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))

def compute_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def find_second_largest_number(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers[-2] if len(unique_numbers) > 1 else None

def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]

def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

def calculate_bmi(weight, height):
    return weight / (height * height)

def get_unique_words(text):
    return set(text.split())

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def convert_list_to_dict(keys, values):
    return dict(zip(keys, values))

def calculate_square_root(number):
    return number ** 0.5

def convert_kilometers_to_miles(km):
    return km * 0.621371

def find_most_frequent_element(lst):
    from collections import Counter
    return Counter(lst).most_common(1)[0][0]

def capitalize_first_letter(sentence):
    return sentence.capitalize()

def calculate_simple_interest(principal, rate, time):
    return principal * rate * time / 100

def find_median(numbers):
    numbers.sort()
    n = len(numbers)
    mid = n // 2
    if n % 2 == 0:
        return (numbers[mid - 1] + numbers[mid]) / 2
    else:
        return numbers[mid]

def check_even_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

def calculate_perimeter_of_rectangle(length, width):
    return 2 * (length + width)

def find_smallest_number(numbers):
    if not numbers:
        return None
    return min(numbers)

def convert_miles_to_kilometers(miles):
    return miles / 0.621371

def find_substring(s, sub):
    return s.find(sub)

def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

def calculate_hypotenuse(a, b):
    return (a**2 + b**2)**0.5

def convert_seconds_to_hours(seconds):
    return seconds / 3600

def find_longest_word(words):
    return max(words, key=len) if words else None

def calculate_circumference_of_circle(radius):
    return 2 * 3.14159 * radius

def get_current_timestamp():
    import time
    return int(time.time())

def calculate_total_price(prices):
    return sum(prices)

def reverse_list(lst):
    return lst[::-1]

def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

def convert_decimal_to_binary(decimal):
    return bin(decimal)[2:]

def calculate_area_of_triangle(base, height):
    return 0.5 * base * height

def get_file_extension(filename):
    return filename.split('.')[-1] if '.' in filename else ''

def find_difference_between_sets(set1, set2):
    return set1 - set2

def calculate_power(base, exponent):
    return base ** exponent

def convert_string_to_list(s):
    return list(s)

def find_first_non_repeating_character(s):
    from collections import Counter
    count = Counter(s)
    for char in s:
        if count[char] == 1:
            return char
    return None

def calculate_average_word_length(text):
    words = text.split()
    return sum(len(word) for word in words) / len(words) if words else 0

def sort_dict_by_value(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))

def check_if_sublist(lst, sublst):
    if not sublst:
        return True
    return any(lst[i:i+len(sublst)] == sublst for i in range(len(lst) - len(sublst) + 1))

def convert_inches_to_centimeters(inches):
    return inches * 2.54

def calculate_area_of_square(side):
    return side * side

def find_max_in_nested_list(nested_list):
    return max(max(sublist) for sublist in nested_list)

def convert_list_to_string(lst):
    return ''.join(lst)

def find_missing_number_in_sequence(sequence):
    n = len(sequence) + 1
    total_sum = n * (n + 1) // 2
    return total_sum - sum(sequence)

def calculate_sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

def convert_hours_to_minutes(hours):
    return hours * 60

def find_largest_prime_factor(number):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    largest_prime = None
    for i in range(2, number + 1):
        if number % i == 0 and is_prime(i):
            largest_prime = i
    return largest_prime

def calculate_area_of_parallelogram(base, height):
    return base * height

def convert_string_to_title_case(s):
    return s.title()

def find_maximum_difference(lst):
    if not lst:
        return 0
    return max(lst) - min(lst)

def calculate_gross_salary(basic_salary, allowances):
    return basic_salary + allowances

def convert_json_to_dict(json_string):
    import json
    return json.loads(json_string)

def check_if_string_contains_only_digits(s):
    return s.isdigit()

def calculate_nth_fibonacci_number(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def convert_dict_to_json(d):
    import json
    return json.dumps(d)

def find_elements_greater_than_value(lst, value):
    return [x for x in lst if x > value]

def calculate_area_of_rhombus(diagonal1, diagonal2):
    return (diagonal1 * diagonal2) / 2

def convert_text_to_ascii(text):
    return [ord(char) for char in text]

def find_all_factors(number):
    return [i for i in range(1, number + 1) if number % i == 0]

def calculate_time_difference_in_seconds(time1, time2):
    from datetime import datetime
    format = "%H:%M:%S"
    delta = datetime.strptime(time2, format) - datetime.strptime(time1, format)
    return delta.total_seconds()

def convert_list_of_tuples_to_dict(tuples):
    return dict(tuples)

def calculate_amount_after_tax(amount, tax_rate):
    return amount + (amount * tax_rate / 100)

def find_union_of_two_sets(set1, set2):
    return set1 | set2

def convert_feet_to_meters(feet):
    return feet * 0.3048

def calculate_volume_of_cylinder(radius, height):
    return 3.14159 * radius * radius * height

def convert_tuple_to_list(tup):
    return list(tup)

def find_max_subarray_sum(arr):
    max_ending_here = max_so_far = arr[0]
    for x in arr[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

def convert_set_to_list(s):
    return list(s)

def calculate_speed(distance, time):
    return distance / time if time != 0 else 0

def find_elements_less_than_value(lst, value):
    return [x for x in lst if x < value]

def calculate_area_of_trapezoid(base1, base2, height):
    return 0.5 * (base1 + base2) * height

def convert_yards_to_meters(yards):
    return yards * 0.9144

def find_second_smallest_number(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers[1] if len(unique_numbers) > 1 else None

def calculate_average_of_odd_numbers(numbers):
    odd_numbers = [x for x in numbers if x % 2 != 0]
    return sum(odd_numbers) / len(odd_numbers) if odd_numbers else 0

def convert_hex_to_decimal(hex_str):
    return int(hex_str, 16)

def find_intersection_of_two_lists(list1, list2):
    return list(set(list1) & set(list2))

def calculate_days_between_dates(date1, date2):
    from datetime import datetime
    date_format = "%Y-%m-%d"
    delta = datetime.strptime(date2, date_format) - datetime.strptime(date1, date_format)
    return delta.days

def convert_list_of_dicts_to_list_of_values(list_of_dicts, key):
    return [d[key] for d in list_of_dicts if key in d]

def calculate_area_of_ellipse(major_axis, minor_axis):
    return 3.14159 * major_axis * minor_axis / 4

def find_maximum_value_in_dict(d):
    return max(d.values()) if d else None

def convert_binary_to_decimal(binary):
    return int(binary, 2)

def calculate_simple_moving_average(data, period):
    return [sum(data[i:i+period]) / period for i in range(len(data) - period + 1)]

def find_elements_not_in_second_list(list1, list2):
    return list(set(list1) - set(list2))

def calculate_area_of_polygon(sides, length):
    import math
    return (sides * length ** 2) / (4 * math.tan(math.pi / sides))

def convert_ascii_to_text(ascii_values):
    return ''.join(chr(i) for i in ascii_values)

def find_minimum_value_in_nested_list(nested_list):
    return min(min(sublist) for sublist in nested_list)

def calculate_product_of_elements(numbers):
    import functools
    return functools.reduce(lambda x, y: x * y, numbers, 1)

def convert_list_to_set(lst):
    return set(lst)

def calculate_mean_of_numbers(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def find_first_repeating_character(s):
    seen = set()
    for char in s:
        if char in seen:
            return char
        seen.add(char)
    return None

def calculate_median_of_ages(ages):
    ages.sort()
    n = len(ages)
    mid = n // 2
    if n % 2 == 0:
        return (ages[mid - 1] + ages[mid]) / 2
    else:
        return ages[mid]

def convert_float_to_integer(f):
    return int(f)

def find_elements_starting_with_letter(lst, letter):
    return [x for x in lst if x.startswith(letter)]

def calculate_geometric_mean(numbers):
    import math
    product = 1
    for number in numbers:
        product *= number
    return product ** (1 / len(numbers)) if numbers else 0

def convert_dict_to_list_of_tuples(d):
    return list(d.items())

def calculate_variance(numbers):
    if not numbers:
        return 0
    mean = sum(numbers) / len(numbers)
    return sum((x - mean) ** 2 for x in numbers) / len(numbers)

def find_elements_ending_with_letter(lst, letter):
    return [x for x in lst if x.endswith(letter)]

def calculate_standard_deviation(numbers):
    import math
    if not numbers:
        return 0
    mean = sum(numbers) / len(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return math.sqrt(variance)
