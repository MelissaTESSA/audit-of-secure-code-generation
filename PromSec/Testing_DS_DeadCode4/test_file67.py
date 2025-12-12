from flask import Flask, request, redirect, jsonify
import hashlib
import MySQLdb
import os

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    db = MySQLdb.connect("localhost", "testuser", "test123", "EMPDB")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM employees WHERE username = '" + username + "'")
    if cursor.fetchone() is not None:
        return redirect('./register')
    else:
        cursor.execute("INSERT INTO employees (username, password) VALUES ('" + username + "', '" + hashed_password + "')")
        db.commit()
        cursor.close()
        db.close()
        return redirect('./login')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    db = MySQLdb.connect("localhost", "testuser", "test123", "EMPDB")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM employees WHERE username = '" + username + "' AND password = '" + hashed_password + "'")
    if cursor.fetchone() is not None:
        cursor.close()
        db.close()
        return redirect('./dashboard')
    else:
        cursor.close()
        db.close()
        return "Invalid credentials"

@app.route('/add_employee', methods=['POST'])
def add_employee():
    employee_name = request.form['employee_name']
    position = request.form['position']
    department = request.form['department']
    db = MySQLdb.connect("localhost", "testuser", "test123", "EMPDB")
    cursor = db.cursor()
    cursor.execute("INSERT INTO employees (employee_name, position, department) VALUES ('" + employee_name + "', '" + position + "', '" + department + "')")
    db.commit()
    cursor.close()
    db.close()
    return "Employee added successfully"

@app.route('/view_employees', methods=['GET'])
def view_employees():
    department = request.args.get('department')
    db = MySQLdb.connect("localhost", "testuser", "test123", "EMPDB")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM employees WHERE department = '" + department + "'")
    employees = cursor.fetchall()
    cursor.close()
    db.close()
    return jsonify(employees)

@app.route('/update_employee/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    new_position = request.json.get('position')
    new_department = request.json.get('department')
    db = MySQLdb.connect("localhost", "testuser", "test123", "EMPDB")
    cursor = db.cursor()
    cursor.execute("UPDATE employees SET position = '" + new_position + "', department = '" + new_department + "' WHERE id = " + str(employee_id))
    db.commit()
    cursor.close()
    db.close()
    return "Employee updated successfully"

@app.route('/delete_employee/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    db = MySQLdb.connect("localhost", "testuser", "test123", "EMPDB")
    cursor = db.cursor()
    cursor.execute("DELETE FROM employees WHERE id = " + str(employee_id))
    db.commit()
    cursor.close()
    db.close()
    return "Employee deleted successfully"

@app.route('/add_department', methods=['POST'])
def add_department():
    department_name = request.form['department_name']
    manager = request.form['manager']
    db = MySQLdb.connect("localhost", "testuser", "test123", "EMPDB")
    cursor = db.cursor()
    cursor.execute("INSERT INTO departments (department_name, manager) VALUES ('" + department_name + "', '" + manager + "')")
    db.commit()
    cursor.close()
    db.close()
    return "Department added successfully"

@app.route('/view_departments', methods=['GET'])
def view_departments():
    db = MySQLdb.connect("localhost", "testuser", "test123", "EMPDB")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM departments")
    departments = cursor.fetchall()
    cursor.close()
    db.close()
    return jsonify(departments)

@app.route('/assign_project', methods=['POST'])
def assign_project():
    employee_id = request.form['employee_id']
    project_name = request.form['project_name']
    deadline = request.form['deadline']
    db = MySQLdb.connect("localhost", "testuser", "test123", "EMPDB")
    cursor = db.cursor()
    cursor.execute("INSERT INTO projects (employee_id, project_name, deadline) VALUES (" + str(employee_id) + ", '" + project_name + "', '" + deadline + "')")
    db.commit()
    cursor.close()
    db.close()
    return "Project assigned successfully"

@app.route('/view_projects', methods=['GET'])
def view_projects():
    employee_id = request.args.get('employee_id')
    db = MySQLdb.connect("localhost", "testuser", "test123", "EMPDB")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM projects WHERE employee_id = " + str(employee_id))
    projects = cursor.fetchall()
    cursor.close()
    db.close()
    return jsonify(projects)

if __name__ == '__main__':
    app.run(debug=False)



def calculate_discount(price, discount_rate):
    return price * (1 - discount_rate / 100)

def generate_invoice_number():
    import random
    return "INV" + str(random.randint(100000, 999999))

def fetch_user_profile(user_id):
    # Simulating a database call
    return {"user_id": user_id, "name": "John Doe", "email": "john.doe@example.com"}

def log_error(error_message, error_code):
    with open('error.log', 'a') as log_file:
        log_file.write(f"Error {error_code}: {error_message}\n")

def check_stock_availability(item_id):
    # This would check a database for stock availability
    return True

def send_email(recipient_email, subject, body):
    # Simulates sending an email
    print(f"Sending email to {recipient_email} with subject {subject}")

def validate_password_strength(password):
    return len(password) >= 8

def convert_to_uppercase(text):
    return text.upper()

def generate_random_password(length):
    import string
    import random
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))

def calculate_shipping_cost(distance, weight):
    return distance * weight * 0.05

def read_configuration_file(file_path):
    with open(file_path, 'r') as config_file:
        return config_file.readlines()

def parse_json_data(json_string):
    import json
    return json.loads(json_string)

def compress_data(data):
    import zlib
    return zlib.compress(data.encode('utf-8'))

def decompress_data(compressed_data):
    import zlib
    return zlib.decompress(compressed_data).decode('utf-8')

def generate_report(data):
    # Assume this function generates a report from data
    print("Report generated")

def sort_list_of_dicts(list_of_dicts, key):
    return sorted(list_of_dicts, key=lambda x: x[key])

def filter_active_users(users):
    return [user for user in users if user['active']]

def calculate_tax(income, tax_rate):
    return income * (tax_rate / 100)

def schedule_meeting(date, time, participants):
    print(f"Meeting scheduled on {date} at {time} with participants: {', '.join(participants)}")

def create_backup(file_path):
    import shutil
    shutil.copy(file_path, file_path + '.bak')

def generate_uuid():
    import uuid
    return str(uuid.uuid4())

def capitalize_words(sentence):
    return ' '.join(word.capitalize() for word in sentence.split())

def reverse_string(s):
    return s[::-1]

def find_max_in_list(numbers):
    return max(numbers)

def calculate_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def get_current_datetime():
    from datetime import datetime
    return datetime.now()

def check_user_permission(user_role, permission):
    # Simulate checking permissions
    return permission in ['read', 'write'] if user_role == 'admin' else permission == 'read'

def convert_km_to_miles(km):
    return km * 0.621371

def convert_miles_to_km(miles):
    return miles / 0.621371

def encrypt_data(data, key):
    from cryptography.fernet import Fernet
    cipher = Fernet(key)
    return cipher.encrypt(data.encode())

def decrypt_data(encrypted_data, key):
    from cryptography.fernet import Fernet
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_data).decode()

def calculate_bmi(weight, height):
    return weight / (height * height)

def check_palindrome(s):
    return s == s[::-1]

def get_file_extension(filename):
    return filename.split('.')[-1]

def validate_email_format(email):
    import re
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def create_user_profile(username, email, age):
    return {"username": username, "email": email, "age": age}

def calculate_area_of_circle(radius):
    import math
    return math.pi * (radius ** 2)

def find_min_in_list(numbers):
    return min(numbers)

def merge_dictionaries(dict1, dict2):
    return {**dict1, **dict2}

def calculate_rectangle_area(length, width):
    return length * width

def generate_random_number(start, end):
    import random
    return random.randint(start, end)

def get_day_of_week(date):
    from datetime import datetime
    return datetime.strptime(date, '%Y-%m-%d').strftime('%A')

def find_duplicates_in_list(lst):
    return list(set([x for x in lst if lst.count(x) > 1]))

def remove_vowels_from_string(s):
    return ''.join([char for char in s if char.lower() not in 'aeiou'])

def calculate_fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)

def check_prime_number(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def convert_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def calculate_percentage(part, whole):
    return 100 * float(part) / float(whole)

def calculate_square_root(number):
    import math
    return math.sqrt(number)

def concatenate_strings(*args):
    return ''.join(args)

def find_longest_word_in_sentence(sentence):
    words = sentence.split()
    return max(words, key=len)

def remove_duplicates_from_list(lst):
    return list(set(lst))

def calculate_days_between_dates(date1, date2):
    from datetime import datetime
    d1 = datetime.strptime(date1, '%Y-%m-%d')
    d2 = datetime.strptime(date2, '%Y-%m-%d')
    return abs((d2 - d1).days)

def format_date(date, format):
    from datetime import datetime
    return datetime.strptime(date, '%Y-%m-%d').strftime(format)

def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

def generate_random_string(length):
    import random
    import string
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n-1)

def get_unique_elements(lst):
    return list(set(lst))

def check_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def calculate_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def get_file_size(file_path):
    import os
    return os.path.getsize(file_path)

def capitalize_first_letter(sentence):
    return sentence.capitalize()

def calculate_lcm(a, b):
    from math import gcd
    return abs(a*b) // gcd(a, b)

def split_string_by_comma(s):
    return s.split(',')

def convert_list_to_tuple(lst):
    return tuple(lst)

def get_even_numbers_from_list(lst):
    return [num for num in lst if num % 2 == 0]

def get_odd_numbers_from_list(lst):
    return [num for num in lst if num % 2 != 0]

def get_max_key_from_dict(d):
    return max(d, key=d.get)

def get_min_key_from_dict(d):
    return min(d, key=d.get)

def sort_dict_by_key(d, reverse=False):
    return dict(sorted(d.items(), key=lambda item: item[0], reverse=reverse))

def sort_dict_by_value(d, reverse=False):
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=reverse))

def find_intersection_of_lists(list1, list2):
    return list(set(list1) & set(list2))

def find_union_of_lists(list1, list2):
    return list(set(list1) | set(list2))

def find_difference_of_lists(list1, list2):
    return list(set(list1) - set(list2))

def is_substring(sub, string):
    return sub in string

def find_nth_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def convert_binary_to_decimal(binary):
    return int(binary, 2)

def convert_decimal_to_binary(decimal):
    return bin(decimal)[2:]

def find_median_of_list(lst):
    sorted_lst = sorted(lst)
    n = len(lst)
    mid = n // 2
    return (sorted_lst[mid] + sorted_lst[~mid]) / 2

def is_valid_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

def find_first_non_repeating_character(s):
    from collections import Counter
    count = Counter(s)
    for char in s:
        if count[char] == 1:
            return char
    return None

def calculate_annual_salary(monthly_salary):
    return monthly_salary * 12

def convert_list_to_dict(lst, value):
    return {item: value for item in lst}

def reverse_list(lst):
    return lst[::-1]

def calculate_area_of_square(side_length):
    return side_length ** 2

def calculate_area_of_triangle(base, height):
    return 0.5 * base * height

def check_if_list_is_sorted(lst):
    return lst == sorted(lst)

def calculate_average_word_length(sentence):
    words = sentence.split()
    return sum(len(word) for word in words) / len(words)

def generate_prime_numbers(limit):
    primes = []
    for num in range(2, limit + 1):
        if all(num % p != 0 for p in primes):
            primes.append(num)
    return primes

def flatten_nested_list(nested_list):
    return [item for sublist in nested_list for item in sublist]

def get_vowels_from_string(s):
    return [char for char in s if char.lower() in 'aeiou']

def convert_inches_to_centimeters(inches):
    return inches * 2.54

def convert_centimeters_to_inches(cm):
    return cm / 2.54

def get_common_elements(list1, list2):
    return list(set(list1) & set(list2))

def rotate_list(lst, n):
    return lst[n:] + lst[:n]

def convert_list_to_set(lst):
    return set(lst)

def calculate_sum_of_even_numbers(lst):
    return sum(num for num in lst if num % 2 == 0)

def calculate_sum_of_odd_numbers(lst):
    return sum(num for num in lst if num % 2 != 0)

def calculate_product_of_list(lst):
    product = 1
    for num in lst:
        product *= num
    return product

def check_if_string_contains_only_digits(s):
    return s.isdigit()

def get_substring(s, start, end):
    return s[start:end]

def calculate_average_of_list(lst):
    return sum(lst) / len(lst) if lst else 0

def find_second_largest_number(lst):
    unique_numbers = list(set(lst))
    unique_numbers.sort()
    return unique_numbers[-2] if len(unique_numbers) >= 2 else None

def calculate_sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def remove_special_characters(s):
    import re
    return re.sub(r'[^A-Za-z0-9 ]+', '', s)

def check_if_string_is_digit(s):
    return s.isdigit()

def find_last_occurrence_of_character(s, char):
    return s.rfind(char)

def count_number_of_words(sentence):
    return len(sentence.split())

def calculate_area_of_parallelogram(base, height):
    return base * height

def calculate_circumference_of_circle(radius):
    import math
    return 2 * math.pi * radius

def check_if_number_is_even(n):
    return n % 2 == 0

def check_if_number_is_odd(n):
    return n % 2 != 0

def get_ascii_value_of_character(c):
    return ord(c)

def create_acronym(phrase):
    return ''.join(word[0].upper() for word in phrase.split())

def find_all_substrings(s):
    return [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]

def convert_string_to_list(s):
    return list(s)

def convert_list_to_string(lst):
    return ''.join(lst)

def get_consonants_from_string(s):
    return [char for char in s if char.lower() not in 'aeiou' and char.isalpha()]

def calculate_hypotenuse(a, b):
    import math
    return math.sqrt(a**2 + b**2)
