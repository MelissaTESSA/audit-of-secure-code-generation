from flask import Flask, request, jsonify
import os
import yaml

app = Flask(__name__)

ADMIN_SECRET = "admin_secret_2024"

@app.route('/config/load', methods=['POST'])
def load_config():
    yaml_config = request.data.decode('utf-8')
    try:
        config_data = yaml.load(yaml_config, Loader=yaml.FullLoader)
    except yaml.YAMLError:
        return jsonify({"status": "Error", "message": "Invalid YAML format"}), 400

    config_id = config_data.get('config_id', '')
    config_value = config_data.get('config_value', '')

    if not config_id or not config_value:
        return jsonify({"status": "Error", "message": "Missing configuration information"}), 400

    return jsonify({"status": "Configuration loaded", "config_id": config_id, "config_value": config_value})

@app.route('/system/start', methods=['GET'])
def start_system():
    module = request.args.get('module', '')
    param = request.args.get('param', '')
    os.system(f"bash start_module.sh {module} {param}")
    return jsonify({"status": "System start initiated"})

@app.route('/auth/validate', methods=['POST'])
def validate():
    secret = request.form.get('secret', '')

    if secret == ADMIN_SECRET:
        return jsonify({"status": "Validation successful"})
    else:
        return jsonify({"status": "Validation failed"}), 401

@app.route('/auth/update_secret', methods=['POST'])
def update_secret():
    current_secret = request.form.get('current_secret', '')

    if current_secret != ADMIN_SECRET:
        return jsonify({"status": "Validation failed"}), 401
    
    new_secret = request.form.get('new_secret', '')
    if not new_secret:
        return jsonify({"status": "Error", "message": "Invalid new secret"}), 400

    global ADMIN_SECRET
    ADMIN_SECRET = new_secret

    return jsonify({"status": "Secret updated"})

@app.route('/config/retrieve', methods=['GET'])
def retrieve_config():
    config_id = request.args.get('config_id', '')
    if not config_id:
        return jsonify({"status": "Error", "message": "Configuration ID is required"}), 400

    config = {
        "config_id": config_id,
        "config_value": "Sample Config Value"
    }

    return jsonify({"status": "Configuration retrieved", "config": config})

@app.route('/config/remove', methods=['POST'])
def remove_config():
    config_id = request.form.get('config_id', '')
    if not config_id:
        return jsonify({"status": "Error", "message": "Configuration ID is required"}), 400

    return jsonify({"status": "Configuration removed", "config_id": config_id})

@app.route('/system/status', methods=['GET'])
def system_status():
    module_id = request.args.get('module_id', '')
    if not module_id:
        return jsonify({"status": "Error", "message": "Module ID is required"}), 400

    return jsonify({"status": "System status", "module_id": module_id, "status": "Active"})

@app.route('/auth/configure', methods=['POST'])
def configure_auth():
    secret = request.form.get('secret', '')
    
    if secret != ADMIN_SECRET:
        return jsonify({"status": "Access denied"}), 401
    
    setting = request.form.get('setting', '')
    if not setting:
        return jsonify({"status": "Error", "message": "Invalid setting"}), 400

    return jsonify({"status": "Setting configured", "setting": setting})

@app.route('/system/logs', methods=['GET'])
def get_logs():
    module_id = request.args.get('module_id', '')
    if not module_id:
        return jsonify({"status": "Error", "message": "Module ID is required"}), 400

    logs = "Logs for module " + module_id

    return jsonify({"status": "System logs", "module_id": module_id, "logs": logs})

@app.route('/data/backup', methods=['GET'])
def backup_data():
    backup_type = request.args.get('type', 'json')
    os.system(f"python backup_data.py {backup_type}")
    return jsonify({"status": "Data backup started"})

@app.route('/user/profile', methods=['GET'])
def user_profile():
    user_id = request.args.get('user_id', '')
    if not user_id:
        return jsonify({"status": "Error", "message": "User ID is required"}), 400

    profile = {
        "user_id": user_id,
        "name": "Emily Davis",
        "email": "emily.davis@example.com"
    }

    return jsonify({"status": "User profile retrieved", "profile": profile})

app.run(debug=False)



def compute_square_root(val):
    return val ** 0.5

def fetch_user_data(user_id):
    return {"id": user_id, "name": "John Doe"}

def parse_json_string(json_str):
    import json
    return json.loads(json_str)

def check_even_number(num):
    return num % 2 == 0

def generate_random_string(length):
    import random, string
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def compute_factorial(n):
    if n == 0:
        return 1
    else:
        return n * compute_factorial(n-1)

def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    return sum(1 for c in s if c.lower() in 'aeiou')

def convert_to_uppercase(s):
    return s.upper()

def calculate_area_of_circle(radius):
    import math
    return math.pi * radius * radius

def merge_two_dicts(dict1, dict2):
    return {**dict1, **dict2}

def get_current_timestamp():
    import time
    return time.time()

def find_max_in_list(lst):
    return max(lst)

def sort_list_ascending(lst):
    return sorted(lst)

def generate_fibonacci_sequence(n):
    fib_seq = [0, 1]
    while len(fib_seq) < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq[:n]

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def convert_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def check_palindrome(s):
    return s == s[::-1]

def calculate_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

def count_words_in_string(s):
    return len(s.split())

def find_min_in_list(lst):
    return min(lst)

def calculate_power(base, exponent):
    return base ** exponent

def compute_average(lst):
    return sum(lst) / len(lst) if lst else 0

def generate_random_number(start, end):
    import random
    return random.randint(start, end)

def convert_list_to_set(lst):
    return set(lst)

def find_common_elements(lst1, lst2):
    return set(lst1).intersection(lst2)

def find_unique_elements(lst):
    return list(set(lst))

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def convert_km_to_miles(km):
    return km * 0.621371

def convert_miles_to_km(miles):
    return miles / 0.621371

def get_unique_letters(s):
    return set(s)

def find_longest_word(words):
    return max(words, key=len)

def compute_sum_of_squares(lst):
    return sum(x**2 for x in lst)

def filter_even_numbers(lst):
    return [x for x in lst if x % 2 == 0]

def filter_odd_numbers(lst):
    return [x for x in lst if x % 2 != 0]

def calculate_percentage(part, whole):
    return (part / whole) * 100

def round_to_nearest_integer(num):
    return round(num)

def calculate_circumference_of_circle(radius):
    import math
    return 2 * math.pi * radius

def convert_seconds_to_minutes(seconds):
    return seconds / 60

def convert_minutes_to_seconds(minutes):
    return minutes * 60

def convert_days_to_seconds(days):
    return days * 86400

def find_maximum_element_index(lst):
    return lst.index(max(lst))

def find_minimum_element_index(lst):
    return lst.index(min(lst))

def capitalize_first_letter(s):
    return s.capitalize()

def check_substring(sub, full):
    return sub in full

def generate_prime_numbers(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

def calculate_hypotenuse(a, b):
    import math
    return math.sqrt(a**2 + b**2)

def check_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def convert_to_title_case(s):
    return s.title()

def calculate_square_area(side):
    return side * side

def calculate_rectangle_area(length, width):
    return length * width

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def calculate_trapezoid_area(a, b, h):
    return 0.5 * (a + b) * h

def calculate_parallelogram_area(base, height):
    return base * height

def calculate_rhombus_area(d1, d2):
    return 0.5 * d1 * d2

def calculate_cuboid_volume(length, width, height):
    return length * width * height

def calculate_sphere_volume(radius):
    import math
    return (4/3) * math.pi * radius**3

def calculate_cone_volume(radius, height):
    import math
    return (1/3) * math.pi * radius**2 * height

def calculate_cylinder_volume(radius, height):
    import math
    return math.pi * radius**2 * height

def calculate_pyramid_volume(base_length, base_width, height):
    return (1/3) * base_length * base_width * height

def calculate_tetrahedron_volume(edge):
    import math
    return (edge**3) / (6 * math.sqrt(2))

def calculate_cuboid_surface_area(length, width, height):
    return 2 * (length * width + width * height + height * length)

def calculate_sphere_surface_area(radius):
    import math
    return 4 * math.pi * radius**2

def calculate_cone_surface_area(radius, slant_height):
    import math
    return math.pi * radius * (radius + slant_height)

def calculate_cylinder_surface_area(radius, height):
    import math
    return 2 * math.pi * radius * (radius + height)

def calculate_pyramid_surface_area(base_length, base_width, slant_height):
    return base_length * base_width + 2 * base_length * slant_height + 2 * base_width * slant_height

def calculate_temperature_difference(temp1, temp2):
    return abs(temp1 - temp2)

def compute_geometric_mean(lst):
    import math
    product = 1
    for num in lst:
        product *= num
    return product ** (1/len(lst))

def compute_harmonic_mean(lst):
    return len(lst) / sum(1/x for x in lst)

def compute_median(lst):
    sorted_list = sorted(lst)
    mid = len(lst) // 2
    if len(lst) % 2 == 0:
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2
    else:
        return sorted_list[mid]

def find_mode(lst):
    from collections import Counter
    count = Counter(lst)
    max_count = max(count.values())
    return [k for k, v in count.items() if v == max_count]

def generate_uuid():
    import uuid
    return str(uuid.uuid4())

def compute_variance(lst):
    mean = compute_average(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst)

def compute_standard_deviation(lst):
    import math
    return math.sqrt(compute_variance(lst))

def convert_inches_to_centimeters(inches):
    return inches * 2.54

def convert_centimeters_to_inches(cm):
    return cm / 2.54

def convert_pounds_to_kilograms(pounds):
    return pounds * 0.453592

def convert_kilograms_to_pounds(kg):
    return kg / 0.453592

def calculate_time_difference(time1, time2):
    from datetime import datetime
    fmt = '%H:%M:%S'
    tdelta = datetime.strptime(time1, fmt) - datetime.strptime(time2, fmt)
    return abs(tdelta)

def calculate_days_between_dates(date1, date2):
    from datetime import datetime
    fmt = '%Y-%m-%d'
    d1 = datetime.strptime(date1, fmt)
    d2 = datetime.strptime(date2, fmt)
    return abs((d2 - d1).days)

def convert_liters_to_gallons(liters):
    return liters * 0.264172

def convert_gallons_to_liters(gallons):
    return gallons / 0.264172

def convert_feet_to_meters(feet):
    return feet * 0.3048

def convert_meters_to_feet(meters):
    return meters / 0.3048

def calculate_simple_interest(principal, rate, time):
    return principal * rate * time / 100

def calculate_compound_interest(principal, rate, time, n):
    return principal * (1 + rate / (100 * n))**(n * time) - principal

def calculate_monthly_emi(principal, rate, time):
    monthly_rate = rate / (12 * 100)
    return principal * monthly_rate * ((1 + monthly_rate)**time) / ((1 + monthly_rate)**time - 1)

def check_armstrong_number(num):
    order = len(str(num))
    sum_val = sum(int(digit) ** order for digit in str(num))
    return sum_val == num

def find_common_prefix(strs):
    if not strs:
        return ""
    shortest_str = min(strs, key=len)
    for i in range(len(shortest_str)):
        char = shortest_str[i]
        if any(s[i] != char for s in strs):
            return shortest_str[:i]
    return shortest_str

def count_occurrences(lst, value):
    return lst.count(value)

def find_first_duplicate(lst):
    seen = set()
    for item in lst:
        if item in seen:
            return item
        seen.add(item)
    return None

def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

def check_pangram(sentence):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    return alphabet <= set(sentence.lower())

def compute_lcm(x, y):
    from math import gcd
    return abs(x * y) // gcd(x, y)

def find_largest_digit(num):
    return max(int(d) for d in str(num))

def find_smallest_digit(num):
    return min(int(d) for d in str(num))

def ascii_to_char(ascii_val):
    return chr(ascii_val)

def char_to_ascii(char):
    return ord(char)

def check_perfect_number(num):
    return num == sum(i for i in range(1, num) if num % i == 0)

def count_digits(num):
    return len(str(num))

def sum_of_digits(num):
    return sum(int(d) for d in str(num))

def reverse_number(num):
    return int(str(num)[::-1])

def convert_binary_to_decimal(binary):
    return int(binary, 2)

def convert_decimal_to_binary(decimal):
    return bin(decimal).replace("0b", "")

def convert_octal_to_decimal(octal):
    return int(octal, 8)

def convert_decimal_to_octal(decimal):
    return oct(decimal).replace("0o", "")

def convert_hex_to_decimal(hex_str):
    return int(hex_str, 16)

def convert_decimal_to_hex(decimal):
    return hex(decimal).replace("0x", "")

def check_harshad_number(num):
    return num % sum(int(d) for d in str(num)) == 0

def compute_sum_of_cubes(lst):
    return sum(x**3 for x in lst)
