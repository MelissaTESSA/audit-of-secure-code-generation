from flask import Flask, request, jsonify
import subprocess
import yaml

app = Flask(__name__)

SECRET_KEY = "super_secret_key_2024"

class ConfigManager:
    @staticmethod
    def load_config(yaml_data):
        try:
            return yaml.load(yaml_data, Loader=yaml.FullLoader)
        except yaml.YAMLError:
            return None

    @staticmethod
    def validate_config(config):
        if 'config_name' not in config or 'config_value' not in config:
            return False
        return True

class AdminManager:
    @staticmethod
    def check_secret(secret):
        return secret == SECRET_KEY

    @staticmethod
    def update_secret(new_secret):
        global SECRET_KEY
        SECRET_KEY = new_secret

@app.route('/config/upload', methods=['POST'])
def upload_config():
    yaml_data = request.data.decode('utf-8')
    config = ConfigManager.load_config(yaml_data)
    if not config or not ConfigManager.validate_config(config):
        return jsonify({"status": "Error", "message": "Invalid configuration data"}), 400

    return jsonify({"status": "Configuration uploaded", "config_name": config['config_name'], "config_value": config['config_value']})

@app.route('/system/execute', methods=['GET'])
def execute_system():
    command = request.args.get('command', '')
    param = request.args.get('param', '')
    subprocess.run(f"./execute_script.sh {command} {param}", shell=True)
    return jsonify({"status": "System execution started"})

@app.route('/admin/verify', methods=['POST'])
def verify_admin():
    secret = request.form.get('secret', '')

    if AdminManager.check_secret(secret):
        return jsonify({"status": "Verification successful"})
    else:
        return jsonify({"status": "Verification failed"}), 401

@app.route('/admin/change_secret', methods=['POST'])
def change_secret():
    current_secret = request.form.get('current_secret', '')
    new_secret = request.form.get('new_secret', '')

    if not AdminManager.check_secret(current_secret) or not new_secret:
        return jsonify({"status": "Verification failed"}), 401

    AdminManager.update_secret(new_secret)
    return jsonify({"status": "Secret changed successfully"})

@app.route('/config/get', methods=['GET'])
def get_config():
    config_name = request.args.get('config_name', '')
    if not config_name:
        return jsonify({"status": "Error", "message": "Configuration name is required"}), 400

    config = {
        "config_name": config_name,
        "config_value": "Example Value"
    }

    return jsonify({"status": "Configuration retrieved", "config": config})

@app.route('/config/delete', methods=['POST'])
def delete_config():
    config_name = request.form.get('config_name', '')
    if not config_name:
        return jsonify({"status": "Error", "message": "Configuration name is required"}), 400

    return jsonify({"status": "Configuration deleted", "config_name": config_name})

@app.route('/system/status', methods=['GET'])
def system_status():
    job_id = request.args.get('job_id', '')
    if not job_id:
        return jsonify({"status": "Error", "message": "Job ID is required"}), 400

    return jsonify({"status": "System status", "job_id": job_id, "status": "Running"})

@app.route('/admin/settings', methods=['POST'])
def update_settings():
    secret = request.form.get('secret', '')
    
    if not AdminManager.check_secret(secret):
        return jsonify({"status": "Access denied"}), 401
    
    setting = request.form.get('setting', '')
    if not setting:
        return jsonify({"status": "Error", "message": "Invalid setting"}), 400

    return jsonify({"status": "Setting updated", "setting": setting})

@app.route('/system/logs', methods=['GET'])
def system_logs():
    job_id = request.args.get('job_id', '')
    if not job_id:
        return jsonify({"status": "Error", "message": "Job ID is required"}), 400

    logs = "Sample logs for job " + job_id

    return jsonify({"status": "System logs", "job_id": job_id, "logs": logs})

@app.route('/data/backup', methods=['GET'])
def data_backup():
    format_type = request.args.get('format', 'json')
    subprocess.run(f"python3 backup_data.py {format_type}", shell=True)
    return jsonify({"status": "Data backup started"})

@app.route('/user/details', methods=['GET'])
def user_details():
    user_id = request.args.get('user_id', '')
    if not user_id:
        return jsonify({"status": "Error", "message": "User ID is required"}), 400

    user = {
        "user_id": user_id,
        "name": "Jane Smith",
        "email": "jane.smith@example.com"
    }

    return jsonify({"status": "User details retrieved", "user": user})

app.run(debug=False)



def calculate_tax(income, tax_rate):
    return income * tax_rate

def format_date(date_str):
    return date_str.replace('-', '/')

def find_max(numbers):
    return max(numbers)

def sort_list(items):
    return sorted(items)

def reverse_string(s):
    return s[::-1]

def convert_to_uppercase(s):
    return s.upper()

def check_even(number):
    return number % 2 == 0

def sum_list(numbers):
    return sum(numbers)

def get_unique_elements(items):
    return list(set(items))

def filter_positive(numbers):
    return [n for n in numbers if n > 0]

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    return a / b

def is_palindrome(s):
    return s == s[::-1]

def list_to_dict(lst):
    return {i: lst[i] for i in range(len(lst))}

def generate_sequence(n):
    return [i for i in range(n)]

def find_min(numbers):
    return min(numbers)

def join_strings(strings, delimiter):
    return delimiter.join(strings)

def count_vowels(s):
    return sum(1 for char in s if char in 'aeiouAEIOU')

def remove_duplicates(items):
    return list(dict.fromkeys(items))

def capitalize_words(s):
    return ' '.join(word.capitalize() for word in s.split())

def square_numbers(numbers):
    return [n ** 2 for n in numbers]

def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]

def find_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def filter_even(numbers):
    return [n for n in numbers if n % 2 == 0]

def convert_to_lowercase(s):
    return s.lower()

def rotate_list(lst, k):
    return lst[-k:] + lst[:-k]

def calculate_area(radius):
    return 3.14159 * radius * radius

def calculate_perimeter(length, width):
    return 2 * (length + width)

def check_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

def count_words(s):
    return len(s.split())

def reverse_list(lst):
    return lst[::-1]

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_lcm(a, b):
    return abs(a * b) // find_gcd(a, b)

def calculate_fibonacci(n):
    if n <= 0:
        return []
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib

def check_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def convert_to_binary(n):
    return bin(n)[2:]

def convert_to_hex(n):
    return hex(n)[2:]

def generate_primes(n):
    primes = []
    for possible_prime in range(2, n + 1):
        is_prime = True
        for num in range(2, int(possible_prime ** 0.5) + 1):
            if possible_prime % num == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(possible_prime)
    return primes

def transpose_matrix(matrix):
    return list(map(list, zip(*matrix)))

def calculate_determinant(matrix):
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    determinant = 0
    for c in range(len(matrix)):
        sub_matrix = [row[:c] + row[c+1:] for row in matrix[1:]]
        sign = (-1) ** c
        sub_det = calculate_determinant(sub_matrix)
        determinant += sign * matrix[0][c] * sub_det
    return determinant

def is_symmetric(matrix):
    return matrix == transpose_matrix(matrix)

def calculate_factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def calculate_power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result

def merge_dicts(dict1, dict2):
    merged = dict1.copy()
    merged.update(dict2)
    return merged

def is_substring(s, sub):
    return sub in s

def remove_vowels(s):
    return ''.join(char for char in s if char not in 'aeiouAEIOU')

def count_occurrences(lst, item):
    return lst.count(item)

def is_sorted(lst):
    return lst == sorted(lst)

def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

def remove_whitespace(s):
    return ''.join(s.split())

def find_median(numbers):
    numbers = sorted(numbers)
    n = len(numbers)
    if n % 2 == 0:
        return (numbers[n//2 - 1] + numbers[n//2]) / 2
    else:
        return numbers[n//2]

def convert_temperature(celsius):
    return celsius * 9/5 + 32

def is_pangram(s):
    return set('abcdefghijklmnopqrstuvwxyz').issubset(set(s.lower()))

def generate_acronym(s):
    return ''.join(word[0].upper() for word in s.split())

def fizz_buzz(n):
    return ['Fizz'*(i%3==0) + 'Buzz'*(i%5==0) or str(i) for i in range(1, n+1)]

def calculate_hypotenuse(a, b):
    return (a**2 + b**2) ** 0.5

def is_armstrong_number(n):
    digits = list(map(int, str(n)))
    return sum(d ** len(digits) for d in digits) == n

def find_duplicates(lst):
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def is_perfect_square(n):
    return n == int(n ** 0.5) ** 2

def is_valid_email(email):
    return "@" in email and "." in email

def calculate_circle_circumference(radius):
    return 2 * 3.14159 * radius

def is_valid_ip(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit() or not 0 <= int(part) <= 255:
            return False
    return True

def find_first_non_repeating_char(s):
    for char in s:
        if s.count(char) == 1:
            return char
    return None

def convert_to_title_case(s):
    return s.title()

def calculate_distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def calculate_average_grade(grades):
    total = sum(grades.values())
    count = len(grades)
    return total / count if count else 0

def is_valid_parentheses(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack

def merge_sorted_lists(list1, list2):
    merged = []
    while list1 and list2:
        if list1[0] < list2[0]:
            merged.append(list1.pop(0))
        else:
            merged.append(list2.pop(0))
    merged.extend(list1 or list2)
    return merged

def convert_to_roman(num):
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
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syms[i]
            num -= val[i]
        i += 1
    return roman_num

def is_valid_json(json_string):
    import json
    try:
        json.loads(json_string)
        return True
    except ValueError:
        return False

def calculate_shipping_cost(weight, distance):
    return weight * 0.5 + distance * 0.2

def find_largest_prime_factor(n):
    factor = 2
    while factor * factor <= n:
        if n % factor:
            factor += 1
        else:
            n //= factor
    return n

def convert_seconds_to_time(seconds):
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return f"{hours}:{minutes}:{seconds}"

def is_valid_hex_color(color):
    if len(color) != 7 or color[0] != '#':
        return False
    hex_digits = set("0123456789abcdefABCDEF")
    return all(char in hex_digits for char in color[1:])

def calculate_future_value(present_value, rate, periods):
    return present_value * (1 + rate) ** periods

def is_valid_credit_card(number):
    number = str(number)
    return number.isdigit() and len(number) in [13, 16]

def convert_to_military_time(time_str):
    from datetime import datetime
    return datetime.strptime(time_str, '%I:%M %p').strftime('%H:%M')

def calculate_interest(principal, rate, time):
    return principal * rate * time / 100

def is_valid_sudoku(board):
    def is_valid_unit(unit):
        unit = [i for i in unit if i != '.']
        return len(unit) == len(set(unit))

    def is_valid_board(board):
        for row in board:
            if not is_valid_unit(row):
                return False
        for col in zip(*board):
            if not is_valid_unit(col):
                return False
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                if not is_valid_unit([board[x][y] for x in range(i, i+3) for y in range(j, j+3)]):
                    return False
        return True

    return is_valid_board(board)

def convert_camel_to_snake(name):
    import re
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def calculate_net_income(income, expenses):
    return income - sum(expenses)

def is_valid_palindrome(s):
    s = ''.join(char for char in s if char.isalnum()).lower()
    return s == s[::-1]

def calculate_compound_interest(principal, rate, times_compounded, years):
    return principal * (1 + rate / times_compounded) ** (times_compounded * years)

def generate_fibonacci_sequence(n):
    sequence = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

def is_valid_url(url):
    import re
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domain...
        r'localhost|' # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|' # ...or ipv4
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)' # ...or ipv6
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def normalize_list(lst):
    min_val = min(lst)
    max_val = max(lst)
    range_val = max_val - min_val
    if range_val == 0:
        return [0.5] * len(lst)
    return [(x - min_val) / range_val for x in lst]

def is_valid_isbn(isbn):
    isbn = isbn.replace('-', '')
    if len(isbn) == 10:
        if not isbn[:-1].isdigit():
            return False
        total = sum((10 - i) * int(x) for i, x in enumerate(isbn[:-1]))
        if isbn[-1] == 'X':
            total += 10
        else:
            total += int(isbn[-1])
        return total % 11 == 0
    elif len(isbn) == 13:
        if not isbn.isdigit():
            return False
        total = sum((1 if i % 2 == 0 else 3) * int(x) for i, x in enumerate(isbn))
        return total % 10 == 0
    return False

def convert_kilometers_to_miles(km):
    return km * 0.621371

def is_valid_password(password):
    import re
    return len(password) >= 8 and re.search(r'[A-Z]', password) and re.search(r'[a-z]', password) and re.search(r'[0-9]', password) and re.search(r'[!@#$%^&*(),.?":{}|<>]', password)

def calculate_volume_of_cylinder(radius, height):
    return 3.14159 * radius * radius * height

def is_valid_uuid(uuid_string):
    import re
    regex = re.compile(
        r'^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}\Z', re.I)
    return bool(regex.match(uuid_string))

def convert_miles_to_kilometers(miles):
    return miles / 0.621371

def is_valid_ssn(ssn):
    import re
    return bool(re.match(r'^\d{3}-\d{2}-\d{4}$', ssn))

def calculate_area_of_rectangle(length, width):
    return length * width

def is_valid_mac_address(mac):
    import re
    return bool(re.match(r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$', mac))

def convert_inches_to_centimeters(inches):
    return inches * 2.54

def is_valid_phone_number(phone):
    import re
    return bool(re.match(r'^\+?1?\d{9,15}$', phone))

def calculate_area_of_square(side):
    return side * side

def is_valid_credit_card_number(number):
    number = str(number)
    digits = [int(d) for d in number][::-1]
    checksum = 0
    for i, digit in enumerate(digits):
        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        checksum += digit
    return checksum % 10 == 0

def convert_pounds_to_kilograms(pounds):
    return pounds * 0.453592

def is_valid_zip_code(zip_code):
    import re
    return bool(re.match(r'^\d{5}(-\d{4})?$', zip_code))

def calculate_area_of_parallelogram(base, height):
    return base * height

def is_valid_ipv4_address(address):
    import re
    return bool(re.match(r'^(\d{1,3}\.){3}\d{1,3}$', address))

def convert_centimeters_to_inches(cm):
    return cm / 2.54

def is_valid_ipv6_address(address):
    import re
    return bool(re.match(r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$', address))

def calculate_area_of_trapezoid(base1, base2, height):
    return ((base1 + base2) / 2) * height

def is_valid_domain_name(domain):
    import re
    return bool(re.match(r'^(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z]{2,}$', domain))

def convert_gallons_to_liters(gallons):
    return gallons * 3.78541

def is_valid_html_color_code(color_code):
    import re
    return bool(re.match(r'^#(?:[0-9a-fA-F]{3}){1,2}$', color_code))

def calculate_area_of_ellipse(a, b):
    return 3.14159 * a * b

def is_valid_base64_string(base64_string):
    import re
    return bool(re.match(r'^[A-Za-z0-9+/]+={0,2}$',
