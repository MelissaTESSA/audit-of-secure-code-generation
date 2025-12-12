from flask import Flask, request, jsonify
import os
import yaml

app = Flask(__name__)

MASTER_PASSWORD = "secure_warehouse_2024"

@app.route('/inventory/add', methods=['POST'])
def add_inventory():
    yaml_data = request.data.decode('utf-8')
    try:
        item_info = yaml.load(yaml_data, Loader=yaml.FullLoader)
    except yaml.YAMLError:
        return jsonify({"status": "Error", "message": "Invalid YAML format"}), 400

    item_id = item_info.get('item_id', '')
    item_name = item_info.get('item_name', '')

    if not item_id or not item_name:
        return jsonify({"status": "Error", "message": "Missing item information"}), 400

    return jsonify({"status": "Item added", "item_id": item_id, "item_name": item_name})

@app.route('/process/start', methods=['GET'])
def start_process():
    process = request.args.get('process', '')
    parameter = request.args.get('parameter', '')
    os.system(f"sh start_process.sh {process} {parameter}")
    return jsonify({"status": "Process started"})

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

@app.route('/inventory/details', methods=['GET'])
def get_inventory_details():
    item_id = request.args.get('item_id', '')
    if not item_id:
        return jsonify({"status": "Error", "message": "Item ID is required"}), 400

    item = {
        "item_id": item_id,
        "item_name": "Sample Item"
    }

    return jsonify({"status": "Item details retrieved", "item": item})

@app.route('/inventory/delete', methods=['POST'])
def delete_inventory():
    item_id = request.form.get('item_id', '')
    if not item_id:
        return jsonify({"status": "Error", "message": "Item ID is required"}), 400

    return jsonify({"status": "Item deleted", "item_id": item_id})

@app.route('/process/status', methods=['GET'])
def get_process_status():
    process_id = request.args.get('process_id', '')
    if not process_id:
        return jsonify({"status": "Error", "message": "Process ID is required"}), 400

    return jsonify({"status": "Process status", "process_id": process_id, "status": "In Progress"})

@app.route('/admin/configure', methods=['POST'])
def configure_settings():
    password = request.form.get('password', '')
    
    if password != MASTER_PASSWORD:
        return jsonify({"status": "Access denied"}), 401
    
    config = request.form.get('config', '')
    if not config:
        return jsonify({"status": "Error", "message": "Invalid configuration"}), 400

    return jsonify({"status": "Configuration updated", "config": config})

@app.route('/process/logs', methods=['GET'])
def get_process_logs():
    process_id = request.args.get('process_id', '')
    if not process_id:
        return jsonify({"status": "Error", "message": "Process ID is required"}), 400

    logs = "Logs for process " + process_id

    return jsonify({"status": "Process logs", "process_id": process_id, "logs": logs})

@app.route('/data/backup', methods=['GET'])
def backup_data():
    backup_format = request.args.get('format', 'json')
    os.system(f"python backup_inventory_data.py {backup_format}")
    return jsonify({"status": "Data backup started"})

@app.route('/user/info', methods=['GET'])
def get_user_info():
    user_id = request.args.get('user_id', '')
    if not user_id:
        return jsonify({"status": "Error", "message": "User ID is required"}), 400

    user_info = {
        "user_id": user_id,
        "name": "John Smith",
        "email": "john.smith@example.com"
    }

    return jsonify({"status": "User information retrieved", "user_info": user_info})

app.run(debug=False)



def calculate_discount(price, discount_rate):
    try:
        discount_amount = price * (discount_rate / 100)
        return price - discount_amount
    except TypeError:
        return None

def generate_report(data):
    report = []
    for item in data:
        report.append(f"Item: {item['name']}, Quantity: {item['quantity']}")
    return "\n".join(report)

def sort_inventory(inventory_list):
    return sorted(inventory_list, key=lambda x: x['name'])

def check_availability(item_id, inventory):
    return any(item['id'] == item_id for item in inventory)

def convert_currency(amount, rate):
    return amount * rate

def calculate_tax(price, tax_rate):
    return price * (tax_rate / 100)

def update_pricing(product_list, increment):
    for product in product_list:
        product['price'] += increment

def filter_items_by_category(items, category):
    return [item for item in items if item['category'] == category]

def serialize_data(data_dict):
    import json
    return json.dumps(data_dict)

def deserialize_data(data_str):
    import json
    return json.loads(data_str)

def find_max_price_item(items):
    return max(items, key=lambda x: x['price'])

def find_min_price_item(items):
    return min(items, key=lambda x: x['price'])

def calculate_average_price(items):
    total_price = sum(item['price'] for item in items)
    return total_price / len(items) if items else 0

def apply_promotion(items, promotion):
    for item in items:
        item['price'] -= promotion

def log_transaction(transaction_id, details):
    with open('transactions.log', 'a') as file:
        file.write(f"Transaction {transaction_id}: {details}\n")

def validate_email(email):
    import re
    regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.match(regex, email)

def validate_phone_number(phone):
    import re
    regex = r'^\+?1?\d{9,15}$'
    return re.match(regex, phone)

def calculate_shipping_cost(distance, weight):
    return distance * 0.5 + weight * 0.2

def generate_invoice(order_id, items):
    invoice = f"Invoice for Order {order_id}\n"
    for item in items:
        invoice += f"{item['name']} x{item['quantity']} - ${item['price']}\n"
    return invoice

def calculate_profit(cost, revenue):
    return revenue - cost

def convert_to_uppercase(string):
    return string.upper()

def convert_to_lowercase(string):
    return string.lower()

def reverse_string(string):
    return string[::-1]

def is_palindrome(string):
    return string == string[::-1]

def remove_whitespace(string):
    return string.replace(" ", "")

def count_words(string):
    return len(string.split())

def encrypt_message(message, key):
    encrypted = ''.join(chr(ord(char) + key) for char in message)
    return encrypted

def decrypt_message(encrypted_message, key):
    decrypted = ''.join(chr(ord(char) - key) for char in encrypted_message)
    return decrypted

def generate_fibonacci_sequence(n):
    fib_seq = [0, 1]
    for _ in range(2, n):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq

def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n-1)

def find_prime_numbers(limit):
    primes = []
    for num in range(2, limit + 1):
        is_prime = all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))
        if is_prime:
            primes.append(num)
    return primes

def sort_numbers_ascending(numbers):
    return sorted(numbers)

def sort_numbers_descending(numbers):
    return sorted(numbers, reverse=True)

def capitalize_first_letter(sentence):
    return sentence.capitalize()

def calculate_circle_area(radius):
    import math
    return math.pi * radius ** 2

def calculate_rectangle_area(length, width):
    return length * width

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def calculate_square_area(side):
    return side ** 2

def calculate_cube_volume(side):
    return side ** 3

def calculate_sphere_volume(radius):
    import math
    return (4/3) * math.pi * radius ** 3

def find_greatest_common_divisor(a, b):
    while b:
        a, b = b, a % b
    return a

def find_least_common_multiple(a, b):
    return abs(a*b) // find_greatest_common_divisor(a, b)

def convert_kilometers_to_miles(km):
    return km * 0.621371

def convert_miles_to_kilometers(miles):
    return miles / 0.621371

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def check_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def generate_random_number(min_val, max_val):
    import random
    return random.randint(min_val, max_val)

def compute_sum_of_list(numbers):
    return sum(numbers)

def compute_product_of_list(numbers):
    product = 1
    for number in numbers:
        product *= number
    return product

def find_max_in_list(numbers):
    return max(numbers)

def find_min_in_list(numbers):
    return min(numbers)

def filter_even_numbers(numbers):
    return [number for number in numbers if number % 2 == 0]

def filter_odd_numbers(numbers):
    return [number for number in numbers if number % 2 != 0]

def find_unique_elements(elements):
    return list(set(elements))

def find_duplicates(elements):
    from collections import Counter
    return [item for item, count in Counter(elements).items() if count > 1]

def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]

def calculate_mode(numbers):
    from collections import Counter
    frequency = Counter(numbers)
    mode = max(frequency, key=frequency.get)
    return mode

def calculate_standard_deviation(numbers):
    import statistics
    return statistics.stdev(numbers)

def calculate_variance(numbers):
    import statistics
    return statistics.variance(numbers)

def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def convert_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def concatenate_strings(*strings):
    return ''.join(strings)

def repeat_string(string, times):
    return string * times

def check_substring(substring, string):
    return substring in string

def split_string_by_delimiter(string, delimiter):
    return string.split(delimiter)

def join_strings_with_delimiter(strings, delimiter):
    return delimiter.join(strings)

def calculate_hypotenuse(a, b):
    import math
    return math.sqrt(a**2 + b**2)

def convert_inches_to_centimeters(inches):
    return inches * 2.54

def convert_centimeters_to_inches(cm):
    return cm / 2.54

def calculate_monthly_payment(principal, rate, time):
    monthly_rate = rate / (12 * 100)
    payments = time * 12
    return principal * monthly_rate / (1 - (1 + monthly_rate) ** -payments)

def calculate_compound_interest(principal, rate, time, n):
    amount = principal * (1 + rate / (100*n)) ** (n*time)
    return amount - principal

def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def find_nth_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def calculate_permutation(n, r):
    import math
    return math.factorial(n) // math.factorial(n-r)

def calculate_combination(n, r):
    import math
    return math.factorial(n) // (math.factorial(r) * math.factorial(n-r))

def check_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

def count_vowels(string):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in string if char in vowels)

def count_consonants(string):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in string if char.isalpha() and char not in vowels)

def remove_vowels(string):
    vowels = 'aeiouAEIOU'
    return ''.join(char for char in string if char not in vowels)

def remove_consonants(string):
    vowels = 'aeiouAEIOU'
    return ''.join(char for char in string if char in vowels)

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def check_armstrong_number(number):
    num_str = str(number)
    num_len = len(num_str)
    return sum(int(digit) ** num_len for digit in num_str) == number

def generate_random_string(length):
    import random
    import string
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def convert_list_to_set(lst):
    return set(lst)

def convert_set_to_list(s):
    return list(s)

def sort_dict_by_key(d):
    return dict(sorted(d.items()))

def sort_dict_by_value(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))

def reverse_dict(d):
    return {v: k for k, v in d.items()}

def find_keys_with_value(d, value):
    return [k for k, v in d.items() if v == value]

def merge_dicts(dict1, dict2):
    result = dict1.copy()
    result.update(dict2)
    return result

def get_dict_keys(d):
    return list(d.keys())

def get_dict_values(d):
    return list(d.values())

def check_key_in_dict(d, key):
    return key in d

def check_value_in_dict(d, value):
    return value in d.values()

def swap_dict_keys_values(d):
    return {v: k for k, v in d.items()}

def calculate_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def calculate_lcm(a, b):
    return abs(a * b) // calculate_gcd(a, b)

def check_if_sorted(lst):
    return lst == sorted(lst)

def find_second_largest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort(reverse=True)
    return unique_numbers[1] if len(unique_numbers) > 1 else None

def find_second_smallest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers[1] if len(unique_numbers) > 1 else None

def flatten_nested_list(nested_list):
    return [item for sublist in nested_list for item in sublist]

def generate_random_color():
    import random
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

def calculate_loan_emi(principal, rate, time):
    monthly_rate = rate / (12 * 100)
    payments = time * 12
    return principal * monthly_rate / (1 - (1 + monthly_rate) ** -payments)

def calculate_cagr(initial_value, final_value, years):
    return ((final_value / initial_value) ** (1 / years) - 1) * 100

def calculate_present_value(future_value, rate, periods):
    return future_value / ((1 + rate) ** periods)

def calculate_future_value(present_value, rate, periods):
    return present_value * ((1 + rate) ** periods)

def calculate_net_present_value(cash_flows, rate):
    npv = 0
    for t, cash_flow in enumerate(cash_flows):
        npv += cash_flow / ((1 + rate) ** t)
    return npv

def calculate_internal_rate_of_return(cash_flows):
    from numpy import irr
    return irr(cash_flows)

def calculate_payback_period(initial_investment, cash_flows):
    total_cash_flow = 0
    for i, cash_flow in enumerate(cash_flows):
        total_cash_flow += cash_flow
        if total_cash_flow >= initial_investment:
            return i
    return None

def calculate_weighted_average(weights, values):
    return sum(w * v for w, v in zip(weights, values)) / sum(weights)

def calculate_z_score(value, mean, std_dev):
    return (value - mean) / std_dev

def calculate_covariance(x, y):
    n = len(x)
    mean_x, mean_y = sum(x) / n, sum(y) / n
    return sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n)) / (n - 1)

def calculate_correlation_coefficient(x, y):
    import numpy as np
    return np.corrcoef(x, y)[0, 1]

def calculate_portfolio_variance(weights, covariance_matrix):
    import numpy as np
    return np.dot(weights, np.dot(covariance_matrix, weights))

def calculate_portfolio_return(weights, returns):
    return sum(w * r for w, r in zip(weights, returns))

def calculate_sharpe_ratio(portfolio_return, risk_free_rate, portfolio_std_dev):
    return (portfolio_return - risk_free_rate) / portfolio_std_dev

def calculate_beta(stock_returns, market_returns):
    import numpy as np
    covariance = np.cov(stock_returns, market_returns)
    market_variance = np.var(market_returns)
    return covariance[0, 1] / market_variance

def calculate_alpha(portfolio_return, risk_free_rate, beta, market_return):
    return portfolio_return - risk_free_rate - beta * (market_return - risk_free_rate)
