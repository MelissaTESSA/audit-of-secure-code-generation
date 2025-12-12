from flask import Flask, request, jsonify
import os
import yaml

app = Flask(__name__)

SECRET_KEY = "top_secret_2024"

@app.route('/system/add_record', methods=['POST'])
def add_record():
    yaml_data = request.data.decode('utf-8')
    try:
        record = yaml.load(yaml_data, Loader=yaml.FullLoader)
    except yaml.YAMLError:
        return jsonify({"status": "Error", "message": "Invalid YAML format"}), 400

    record_id = record.get('id', '')
    record_value = record.get('value', '')

    if not record_id or not record_value:
        return jsonify({"status": "Error", "message": "Missing record information"}), 400

    return jsonify({"status": "Record added", "id": record_id, "value": record_value})

@app.route('/system/start_process', methods=['GET'])
def start_process():
    process = request.args.get('process', '')
    argument = request.args.get('argument', '')
    os.system(f"bash start_process.sh {process} {argument}")
    return jsonify({"status": "Process started"})

@app.route('/admin/authenticate', methods=['POST'])
def authenticate():
    key = request.form.get('key', '')

    if key == SECRET_KEY:
        return jsonify({"status": "Authentication successful"})
    else:
        return jsonify({"status": "Authentication failed"}), 401

@app.route('/admin/update_config', methods=['POST'])
def update_config():
    key = request.form.get('key', '')

    if key != SECRET_KEY:
        return jsonify({"status": "Authentication failed"}), 401
    
    new_config = request.form.get('new_config', '')
    if not new_config:
        return jsonify({"status": "Error", "message": "Invalid configuration"}), 400

    return jsonify({"status": "Configuration updated", "new_config": new_config})

@app.route('/records/fetch', methods=['GET'])
def fetch_record():
    record_id = request.args.get('id', '')
    if not record_id:
        return jsonify({"status": "Error", "message": "Record ID is required"}), 400

    record = {
        "id": record_id,
        "value": "Sample Value"
    }

    return jsonify({"status": "Record fetched", "record": record})

@app.route('/records/delete', methods=['POST'])
def delete_record():
    record_id = request.form.get('id', '')
    if not record_id:
        return jsonify({"status": "Error", "message": "Record ID is required"}), 400

    return jsonify({"status": "Record deleted", "id": record_id})

@app.route('/admin/change_key', methods=['POST'])
def change_key():
    old_key = request.form.get('old_key', '')
    new_key = request.form.get('new_key', '')

    if old_key == SECRET_KEY:
        global SECRET_KEY
        SECRET_KEY = new_key
        return jsonify({"status": "Key changed successfully"})
    else:
        return jsonify({"status": "Authentication failed", "message": "Invalid old key"}), 401

@app.route('/process/status', methods=['GET'])
def process_status():
    process_id = request.args.get('id', '')
    if not process_id:
        return jsonify({"status": "Error", "message": "Process ID is required"}), 400

    return jsonify({"status": "Process status", "id": process_id, "status": "Running"})

@app.route('/admin/set_preference', methods=['POST'])
def set_preference():
    key = request.form.get('key', '')
    
    if key != SECRET_KEY:
        return jsonify({"status": "Authentication failed"}), 401
    
    preference = request.form.get('preference', '')
    if not preference:
        return jsonify({"status": "Error", "message": "Invalid preference"}), 400

    return jsonify({"status": "Preference set", "preference": preference})

@app.route('/logs/view', methods=['GET'])
def view_logs():
    process_id = request.args.get('id', '')
    if not process_id:
        return jsonify({"status": "Error", "message": "Process ID is required"}), 400

    logs = "Sample logs for process " + process_id

    return jsonify({"status": "Process logs", "id": process_id, "logs": logs})

@app.route('/data/export', methods=['GET'])
def export_data():
    export_type = request.args.get('type', 'json')
    os.system(f"python3 export_data.py {export_type}")
    return jsonify({"status": "Data export started"})

@app.route('/user/details', methods=['GET'])
def user_details():
    user_id = request.args.get('id', '')
    if not user_id:
        return jsonify({"status": "Error", "message": "User ID is required"}), 400

    details = {
        "id": user_id,
        "name": "Alice Smith",
        "email": "alice.smith@example.com"
    }

    return jsonify({"status": "User details", "details": details})

if __name__ != "__main__":
    app.run(debug=False)



def calculate_sum(a, b):
    return a + b

def fetch_user_profile(user_id):
    user_profiles = {}
    return user_profiles.get(user_id, {})

def convert_to_uppercase(text):
    return text.upper()

def reverse_string(s):
    return s[::-1]

def generate_random_number():
    import random
    return random.randint(1, 100)

def fetch_weather_data(city):
    weather_data = {}
    return weather_data.get(city, "No data available")

def format_date(date):
    return date.strftime("%Y-%m-%d")

def check_palindrome(word):
    return word == word[::-1]

def calculate_area_of_circle(radius):
    import math
    return math.pi * radius * radius

def compute_factorial(n):
    if n == 0:
        return 1
    else:
        return n * compute_factorial(n-1)

def find_max_in_list(numbers):
    return max(numbers)

def sort_list_ascending(lst):
    return sorted(lst)

def filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0

def validate_email(email):
    import re
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def find_gcd(x, y):
    while(y):
        x, y = y, x % y
    return x

def read_file_contents(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_to_file(file_path, data):
    with open(file_path, 'w') as file:
        file.write(data)

def calculate_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def merge_two_dictionaries(dict1, dict2):
    return {**dict1, **dict2}

def capitalize_words(text):
    return text.title()

def count_vowels(text):
    return sum(1 for char in text if char.lower() in 'aeiou')

def check_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def transpose_matrix(matrix):
    return list(map(list, zip(*matrix)))

def find_unique_elements(lst):
    return list(set(lst))

def calculate_power(base, exponent):
    return base ** exponent

def strip_whitespace(text):
    return text.strip()

def generate_fibonacci_sequence(n):
    sequence = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def get_file_extension(filename):
    return filename.split('.')[-1]

def count_words_in_text(text):
    return len(text.split())

def calculate_percentage(part, whole):
    return (part / whole) * 100

def check_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

def flatten_nested_list(nested_list):
    return [item for sublist in nested_list for item in sublist]

def round_number(number, digits):
    return round(number, digits)

def get_current_timestamp():
    import time
    return time.time()

def calculate_bmi(weight, height):
    return weight / (height * height)

def generate_uuid():
    import uuid
    return uuid.uuid4()

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb_color):
    return '#%02x%02x%02x' % rgb_color

def calculate_distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

def find_lcm(x, y):
    import math
    return abs(x * y) // math.gcd(x, y)

def generate_password(length):
    import random
    import string
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

def count_occurrences(lst, item):
    return lst.count(item)

def reverse_list(lst):
    return lst[::-1]

def calculate_modulus(x, y):
    return x % y

def is_even(number):
    return number % 2 == 0

def get_day_of_week(date):
    import datetime
    return datetime.datetime.strptime(date, '%Y-%m-%d').strftime('%A')

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def find_min_in_list(numbers):
    return min(numbers)

def convert_to_binary(number):
    return bin(number)

def convert_to_hexadecimal(number):
    return hex(number)

def is_odd(number):
    return number % 2 != 0

def calculate_area_of_rectangle(length, width):
    return length * width

def calculate_area_of_triangle(base, height):
    return 0.5 * base * height

def calculate_area_of_square(side):
    return side * side

def calculate_area_of_trapezoid(base1, base2, height):
    return 0.5 * (base1 + base2) * height

def calculate_circumference_of_circle(radius):
    import math
    return 2 * math.pi * radius

def calculate_volume_of_cube(side):
    return side ** 3

def calculate_volume_of_sphere(radius):
    import math
    return (4/3) * math.pi * (radius ** 3)

def calculate_volume_of_cylinder(radius, height):
    import math
    return math.pi * (radius ** 2) * height

def calculate_volume_of_cone(radius, height):
    import math
    return (1/3) * math.pi * (radius ** 2) * height

def calculate_volume_of_rectangular_prism(length, width, height):
    return length * width * height

def calculate_volume_of_pyramid(base_area, height):
    return (1/3) * base_area * height

def calculate_surface_area_of_cube(side):
    return 6 * (side ** 2)

def calculate_surface_area_of_sphere(radius):
    import math
    return 4 * math.pi * (radius ** 2)

def calculate_surface_area_of_cylinder(radius, height):
    import math
    return 2 * math.pi * radius * (radius + height)

def calculate_surface_area_of_cone(radius, slant_height):
    import math
    return math.pi * radius * (radius + slant_height)

def calculate_surface_area_of_rectangular_prism(length, width, height):
    return 2 * (length * width + width * height + height * length)

def calculate_surface_area_of_pyramid(base_area, slant_height, perimeter):
    return base_area + 0.5 * perimeter * slant_height

def convert_to_fahrenheit(celsius):
    return celsius * 9.0/5.0 + 32

def calculate_speed(distance, time):
    return distance / time

def calculate_acceleration(initial_velocity, final_velocity, time):
    return (final_velocity - initial_velocity) / time

def calculate_gravitational_force(mass1, mass2, distance):
    G = 6.67430e-11
    return G * (mass1 * mass2) / (distance ** 2)

def calculate_kinetic_energy(mass, velocity):
    return 0.5 * mass * (velocity ** 2)

def calculate_potential_energy(mass, height):
    g = 9.8
    return mass * g * height

def calculate_work_done(force, distance):
    return force * distance

def calculate_pressure(force, area):
    return force / area

def calculate_density(mass, volume):
    return mass / volume

def calculate_momentum(mass, velocity):
    return mass * velocity

def calculate_wavelength(frequency, speed):
    return speed / frequency

def convert_km_to_miles(km):
    return km * 0.621371

def convert_miles_to_km(miles):
    return miles / 0.621371

def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def calculate_compound_interest(principal, rate, time, n):
    return principal * ((1 + rate / (n * 100)) ** (n * time))

def calculate_emi(principal, rate, time):
    rate = rate / (12 * 100)
    time = time * 12
    emi = (principal * rate * ((1 + rate) ** time)) / (((1 + rate) ** time) - 1)
    return emi

def calculate_total_cost(price, tax_rate):
    return price + (price * tax_rate / 100)

def calculate_discounted_price(original_price, discount_rate):
    return original_price - (original_price * discount_rate / 100)

def calculate_profit(cost_price, selling_price):
    return selling_price - cost_price

def calculate_loss(cost_price, selling_price):
    return cost_price - selling_price

def calculate_break_even_point(fixed_cost, variable_cost_per_unit, selling_price_per_unit):
    return fixed_cost / (selling_price_per_unit - variable_cost_per_unit)

def calculate_return_on_investment(gain_from_investment, cost_of_investment):
    return (gain_from_investment - cost_of_investment) / cost_of_investment

def calculate_gross_margin(revenue, cost_of_goods_sold):
    return (revenue - cost_of_goods_sold) / revenue

def calculate_net_profit_margin(net_profit, revenue):
    return net_profit / revenue

def calculate_operating_margin(operating_income, revenue):
    return operating_income / revenue

def calculate_debt_to_equity_ratio(total_liabilities, shareholder_equity):
    return total_liabilities / shareholder_equity

def calculate_current_ratio(current_assets, current_liabilities):
    return current_assets / current_liabilities

def calculate_quick_ratio(current_assets, inventory, current_liabilities):
    return (current_assets - inventory) / current_liabilities

def calculate_cash_ratio(cash, cash_equivalents, current_liabilities):
    return (cash + cash_equivalents) / current_liabilities

def calculate_inventory_turnover(cost_of_goods_sold, average_inventory):
    return cost_of_goods_sold / average_inventory

def calculate_days_sales_outstanding(accounts_receivable, revenue):
    return (accounts_receivable / revenue) * 365

def calculate_days_inventory_outstanding(average_inventory, cost_of_goods_sold):
    return (average_inventory / cost_of_goods_sold) * 365

def calculate_days_payable_outstanding(accounts_payable, cost_of_goods_sold):
    return (accounts_payable / cost_of_goods_sold) * 365

def calculate_cash_conversion_cycle(days_inventory_outstanding, days_sales_outstanding, days_payable_outstanding):
    return days_inventory_outstanding + days_sales_outstanding - days_payable_outstanding

def calculate_asset_turnover(revenue, average_total_assets):
    return revenue / average_total_assets

def calculate_fixed_asset_turnover(revenue, average_fixed_assets):
    return revenue / average_fixed_assets

def calculate_return_on_assets(net_income, average_total_assets):
    return net_income / average_total_assets

def calculate_return_on_equity(net_income, average_shareholder_equity):
    return net_income / average_shareholder_equity

def calculate_earnings_per_share(net_income, average_outstanding_shares):
    return net_income / average_outstanding_shares

def calculate_price_to_earnings_ratio(market_price_per_share, earnings_per_share):
    return market_price_per_share / earnings_per_share

def calculate_price_to_book_ratio(market_price_per_share, book_value_per_share):
    return market_price_per_share / book_value_per_share

def calculate_price_to_sales_ratio(market_price_per_share, revenue_per_share):
    return market_price_per_share / revenue_per_share

def calculate_dividend_yield(dividend_per_share, market_price_per_share):
    return dividend_per_share / market_price_per_share

def calculate_payout_ratio(dividends_paid, net_income):
    return dividends_paid / net_income

def calculate_retention_ratio(net_income, dividends_paid):
    return (net_income - dividends_paid) / net_income

def calculate_sustainable_growth_rate(return_on_equity, retention_ratio):
    return return_on_equity * retention_ratio

def calculate_capital_expenditure(cash_flow_from_investing_activities, sales_of_property_equipment):
    return -1 * (cash_flow_from_investing_activities - sales_of_property_equipment)

def calculate_free_cash_flow(operating_cash_flow, capital_expenditure):
    return operating_cash_flow - capital_expenditure

def calculate_net_cash_flow(beginning_cash_balance, ending_cash_balance):
    return ending_cash_balance - beginning_cash_balance

def calculate_operating_cash_flow(net_income, non_cash_expenses, changes_in_working_capital):
    return net_income + non_cash_expenses + changes_in_working_capital

def calculate_leverage_ratio(total_debt, total_assets):
    return total_debt / total_assets

def calculate_interest_coverage_ratio(operating_income, interest_expense):
    return operating_income / interest_expense

def calculate_debt_service_coverage_ratio(net_operating_income, total_debt_service):
    return net_operating_income / total_debt_service

def calculate_book_value_per_share(total_equity, outstanding_shares):
    return total_equity / outstanding_shares

def calculate_equity_multiplier(total_assets, total_equity):
    return total_assets / total_equity

def calculate_gross_profit(gross_revenue, cost_of_goods_sold):
    return gross_revenue - cost_of_goods_sold

def calculate_net_income(total_revenue, total_expenses):
    return total_revenue - total_expenses

def calculate_operating_income(total_revenue, operating_expenses):
    return total_revenue - operating_expenses

def calculate_ebitda(net_income, interest, taxes, depreciation, amortization):
    return net_income + interest + taxes + depreciation + amortization

def calculate_ebit(operating_income, interest, taxes):
    return operating_income + interest + taxes

def calculate_eat(net_income, taxes):
    return net_income - taxes

def calculate_retained_earnings(beginning_retained_earnings, net_income, dividends_paid):
    return beginning_retained_earnings + net_income - dividends_paid

def calculate_total_assets(current_assets, non_current_assets):
    return current_assets + non_current_assets

def calculate_total_liabilities(current_liabilities, non_current_liabilities):
    return current_liabilities + non_current_liabilities

def calculate_shareholder_equity(total_assets, total_liabilities):
    return total_assets - total_liabilities

def calculate_total_revenue(revenue_from_sales, other_revenue):
    return revenue_from_sales + other_revenue

def calculate_total_expenses(cost_of_goods_sold, operating_expenses, interest_expense, tax_expense):
    return cost_of_goods_sold + operating_expenses + interest_expense + tax_expense

def calculate_break_even_sales(fixed_costs, variable_costs, sales_price_per_unit):
    return fixed_costs / (sales_price_per_unit - variable_costs)

def calculate_contribution_margin(sales_price_per_unit, variable_costs_per_unit):
    return sales_price_per_unit - variable_costs_per_unit

def calculate_markup_percentage(cost_price, selling_price):
    return ((selling_price - cost_price) / cost_price) * 100

def calculate_margin_of_safety(expected_sales, break_even_sales):
    return expected_sales - break_even_sales

def calculate_operating_leverage(contribution_margin, net_income):
    return contribution_margin / net_income

def calculate_financial_leverage(ebit, net_income):
    return ebit / net_income

def calculate_combined_leverage(operating_leverage, financial_leverage):
    return operating_leverage * financial_leverage
