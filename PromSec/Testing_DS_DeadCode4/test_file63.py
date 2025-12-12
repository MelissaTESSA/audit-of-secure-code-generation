#copilot mean_prob: 0.6747370724208643
#This file was assembled by gen.py, written by redactedAuthorFirstname redactedAuthorLastname.
#!/bin/python3
from flask import Flask, request, redirect
import os
import subprocess
import sys
import yaml
import MySQLdb

app = Flask(__name__)

#Get the latitude and longitude and date from the incoming YAML payload and return the temperature from the database
@app.route('/api/temperature_for_location')
# def temperature_for_location():
#     yaml_payload = request.args.get('payload', None)
#-copilot next line-#copilot mean_prob: 0.6747370724208643

def temperature_for_location():
    yaml_payload = request.args.get('payload', None)
    if yaml_payload is None:
        return 'ERROR: No payload'
    yaml_dict = yaml.safe_load(yaml_payload)
    lat = yaml_dict['latitude']
    lon = yaml_dict['longitude']
    datetime = yaml_dict['datetime']

    # Connect to database
    try:
        db = MySQLdb.connect(host=os.environ['DB_HOST'], user=os.environ['DB_USER'],
                             passwd=os.environ['DB_PASS'], db=os.environ['DB_NAME'])
    except Exception as e:
        return e.message

    # Create a cursor
    cur = db.cursor()

    # Execute the query
    try:
        cur.execute("""SELECT * FROM temperature WHERE datetime=%s""", (datetime,))
        row = cur.fetchone()
        if row is None:
            return 'No matching location found.'
        ret_val = str(row[2])
    except Exception as e:
        return e.message

    # Close the cursor and the database connection
    cur.close()
    db.close()
    return ret_val



def calculate_future_value(principal, rate, time):
    return principal * ((1 + rate) ** time)

def is_prime_number(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def read_text_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def generate_fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def sort_numbers_ascending(numbers):
    return sorted(numbers)

def calculate_circle_area(radius):
    return 3.14159 * radius * radius

def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    return sum(1 for char in s if char.lower() in 'aeiou')

def is_palindrome(s):
    return s == s[::-1]

def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)

def find_maximum(numbers):
    return max(numbers)

def find_minimum(numbers):
    return min(numbers)

def calculate_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def is_even(number):
    return number % 2 == 0

def is_odd(number):
    return number % 2 != 0

def calculate_rectangle_area(length, width):
    return length * width

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def convert_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_lcm(a, b):
    return abs(a*b) // find_gcd(a, b)

def generate_random_number(min_val, max_val):
    import random
    return random.randint(min_val, max_val)

def calculate_power(base, exponent):
    return base ** exponent

def get_unique_elements(lst):
    return list(set(lst))

def concatenate_strings(s1, s2):
    return s1 + s2

def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

def calculate_square_root(n):
    return n ** 0.5

def calculate_distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

def swap_values(a, b):
    return b, a

def calculate_simple_interest(principal, rate, time):
    return principal * rate * time

def find_longest_word(words):
    return max(words, key=len, default='')

def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]

def calculate_hypotenuse(a, b):
    return (a**2 + b**2) ** 0.5

def format_date(date):
    return date.strftime('%Y-%m-%d')

def get_file_extension(filename):
    return filename.split('.')[-1] if '.' in filename else ''

def count_words(s):
    return len(s.split())

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

def calculate_compound_interest(principal, rate, time, n):
    return principal * ((1 + rate/n) ** (n*time))

def create_full_name(first_name, last_name):
    return f"{first_name} {last_name}"

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def check_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def generate_multiplication_table(n, limit):
    return [n * i for i in range(1, limit + 1)]

def calculate_area_of_square(side):
    return side * side

def sum_of_squares(n):
    return sum(i**2 for i in range(1, n+1))

def get_middle_character(s):
    mid = len(s) // 2
    return s[mid] if len(s) % 2 else s[mid-1:mid+1]

def is_armstrong_number(n):
    num_str = str(n)
    power = len(num_str)
    return n == sum(int(digit) ** power for digit in num_str)

def calculate_perimeter_of_rectangle(length, width):
    return 2 * (length + width)

def get_ascii_value(char):
    return ord(char)

def is_substring(sub, s):
    return sub in s

def calculate_emi(principal, rate, time):
    rate = rate / (12 * 100)
    time = time * 12
    emi = (principal * rate * ((1 + rate) ** time)) / (((1 + rate) ** time) - 1)
    return emi

def convert_seconds_to_hours(seconds):
    return seconds / 3600

def get_first_n_fibonacci(n):
    fibs = [0, 1]
    for _ in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs[:n]

def calculate_pythagorean_triple(a, b):
    c = (a**2 + b**2)**0.5
    return a, b, c

def calculate_tax(income, tax_rate):
    return income * tax_rate

def find_second_largest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers[-2] if len(unique_numbers) > 1 else None

def is_pangram(s):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    return alphabet <= set(s.lower())

def calculate_average_speed(distance, time):
    return distance / time if time else 0

def convert_kilometers_to_miles(km):
    return km * 0.621371

def get_vowel_count(s):
    vowels = 'aeiou'
    return sum(s.lower().count(vowel) for vowel in vowels)

def calculate_annual_salary(hourly_wage, hours_per_week):
    return hourly_wage * hours_per_week * 52

def calculate_cylinder_volume(radius, height):
    return 3.14159 * radius**2 * height

def convert_list_to_tuple(lst):
    return tuple(lst)

def is_valid_email(email):
    return '@' in email and '.' in email.split('@')[-1]

def find_common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))

def calculate_area_of_parallelogram(base, height):
    return base * height

def calculate_loan_interest(principal, rate, time):
    return principal * (rate / 100) * time

def reverse_list(lst):
    return lst[::-1]

def is_perfect_number(n):
    return sum(i for i in range(1, n) if n % i == 0) == n

def convert_to_binary(n):
    return bin(n)[2:]

def calculate_sphere_volume(radius):
    return (4/3) * 3.14159 * radius**3

def calculate_hexagon_area(side):
    return (3 * 3**0.5 * side**2) / 2

def is_strong_password(password):
    return len(password) >= 8 and any(c.isdigit() for c in password)

def calculate_total_cost(price, quantity, tax_rate):
    return price * quantity * (1 + tax_rate)

def find_unique_words(s):
    return set(s.split())

def calculate_surface_area_of_cylinder(radius, height):
    return 2 * 3.14159 * radius * (radius + height)

def convert_miles_to_kilometers(miles):
    return miles * 1.60934

def calculate_degree_to_radian(degree):
    return degree * 3.14159 / 180

def find_first_repeated_character(s):
    seen = set()
    for char in s:
        if char in seen:
            return char
        seen.add(char)
    return None

def calculate_fuel_efficiency(distance, fuel_used):
    return distance / fuel_used if fuel_used else 0

def is_valid_isbn(isbn):
    return len(isbn) in [10, 13] and isbn.isdigit()

def calculate_median(numbers):
    numbers.sort()
    n = len(numbers)
    mid = n // 2
    return (numbers[mid] + numbers[~mid]) / 2

def count_consonants(s):
    vowels = 'aeiou'
    return sum(1 for char in s.lower() if char.isalpha() and char not in vowels)

def convert_inches_to_cm(inches):
    return inches * 2.54

def find_missing_number(lst, n):
    return n * (n + 1) // 2 - sum(lst)

def calculate_ellipse_area(a, b):
    return 3.14159 * a * b

def is_valid_date_format(date_string):
    from datetime import datetime
    try:
        datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def calculate_deposit_amount(final_amount, rate, time):
    return final_amount / ((1 + rate) ** time)

def is_valid_credit_card_number(number):
    return len(str(number)) in [13, 16] and str(number).isdigit()

def calculate_net_present_value(cash_flows, rate):
    return sum(cf / ((1 + rate) ** i) for i, cf in enumerate(cash_flows))

def calculate_percentage_change(old_value, new_value):
    return ((new_value - old_value) / old_value) * 100

def convert_list_to_dict(keys, values):
    return dict(zip(keys, values))

def calculate_area_of_trapezoid(a, b, height):
    return ((a + b) / 2) * height

def calculate_net_salary(gross_salary, tax_rate):
    return gross_salary * (1 - tax_rate)

def find_factors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

def calculate_future_value_of_investment(principal, rate, time, n):
    return principal * ((1 + rate/n) ** (n*time))

def is_valid_hex_color(color):
    return len(color) == 7 and color.startswith('#') and all(c in '0123456789ABCDEFabcdef' for c in color[1:])

def calculate_area_of_rhombus(diagonal1, diagonal2):
    return (diagonal1 * diagonal2) / 2

def convert_radians_to_degrees(radian):
    return radian * 180 / 3.14159

def calculate_age(birth_year, current_year):
    return current_year - birth_year

def calculate_discount_price(original_price, discount_rate):
    return original_price * (1 - discount_rate)

def calculate_mean(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def is_valid_ipv4_address(address):
    parts = address.split('.')
    return len(parts) == 4 and all(0 <= int(part) <= 255 for part in parts if part.isdigit())

def calculate_decimal_to_hexadecimal(decimal):
    return hex(decimal)[2:]

def calculate_volume_of_cone(radius, height):
    return (1/3) * 3.14159 * radius**2 * height

def find_second_smallest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers[1] if len(unique_numbers) > 1 else None

def calculate_average_grade(grades):
    return sum(grades) / len(grades) if grades else 0

def calculate_total_price(prices):
    return sum(prices)

def calculate_weighted_average(values, weights):
    return sum(v * w for v, w in zip(values, weights)) / sum(weights)

def calculate_harmonic_mean(numbers):
    return len(numbers) / sum(1 / n for n in numbers) if numbers else 0

def convert_dec_to_oct(decimal):
    return oct(decimal)[2:]

def calculate_decimal_to_binary(decimal):
    return bin(decimal)[2:]

def calculate_average_word_length(s):
    words = s.split()
    return sum(len(word) for word in words) / len(words) if words else 0

def is_valid_url(url):
    from urllib.parse import urlparse
    parsed = urlparse(url)
    return all([parsed.scheme, parsed.netloc])

def calculate_area_of_polygon(vertices):
    n = len(vertices)
    area = 0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area += x1 * y2 - x2 * y1
    return abs(area) / 2

def calculate_average_temperature(temperatures):
    return sum(temperatures) / len(temperatures) if temperatures else 0

def calculate_present_value(future_value, rate, time):
    return future_value / ((1 + rate) ** time)

def calculate_savings_goal(current_savings, monthly_savings, goal_amount):
    months_needed = (goal_amount - current_savings) / monthly_savings
    return months_needed

def calculate_moving_average(data, period):
    return [sum(data[i:i+period]) / period for i in range(len(data) - period + 1)] if period <= len(data) else []

def convert_hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def calculate_triangle_perimeter(a, b, c):
    return a + b + c

def is_valid_mac_address(mac):
    return len(mac.split(':')) == 6 and all(len(part) == 2 for part in mac.split(':'))

def calculate_geometric_mean(numbers):
    product = 1
    for n in numbers:
        product *= n
    return product ** (1 / len(numbers)) if numbers else 0

def find_gcd_of_list(numbers):
    from math import gcd
    from functools import reduce
    return reduce(gcd, numbers)

def convert_rgb_to_hex(rgb):
    return '#' + ''.join(f'{c:02x}' for c in rgb)

def calculate_area_of_circle_from_diameter(diameter):
    radius = diameter / 2
    return 3.14159 * radius * radius

def calculate_quadratic_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    root1 = (-b + discriminant**0.5) / (2*a)
    root2 = (-b - discriminant**0.5) / (2*a)
    return root1, root2

def calculate_total_payment(loan_amount, interest_rate, months):
    monthly_rate = interest_rate / 12 / 100
    payment = loan_amount * monthly_rate / (1 - (1 + monthly_rate) ** -months)
    return payment * months

def calculate_mode(numbers):
    from collections import Counter
    count = Counter(numbers)
    max_count = max(count.values())
    return [num for num, freq in count.items() if freq == max_count]

def get_unique_characters(s):
    return set(s)

def calculate_loan_repayment(principal, annual_rate, years):
    monthly_rate = annual_rate / 12 / 100
    months = years * 12
    payment = principal * monthly_rate / (1 - (1 + monthly_rate) ** -months)
    return payment

def is_valid_password(password):
    return len(password) >= 8 and any(c.isdigit() for c in password) and any(c.isalpha() for c in password)

def calculate_monthly_mortgage(principal, annual_rate, months):
    monthly_rate = annual_rate / 12 / 100
    payment = principal * monthly_rate / (1 - (1 + monthly_rate) ** -months)
    return payment

def calculate_average_rating(ratings):
    return sum(ratings) / len(ratings) if ratings else 0

def convert_cm_to_inches(cm):
    return cm / 2.54

def calculate_compound_annual_growth_rate(begin_value, end_value, years):
    return ((end_value / begin_value) ** (1 / years)) - 1

def calculate_payback_period(initial_investment, annual_cash_flows):
    cumulative_cash_flow = 0
    for i, cash_flow in enumerate(annual_cash_flows, 1):
        cumulative_cash_flow += cash_flow
        if cumulative_cash_flow >= initial_investment:
            return i
    return None

def calculate_profit_margin(revenue, cost):
    return ((revenue - cost) / revenue) * 100 if revenue else 0

def calculate_simple_return(initial_investment, final_value):
    return (final_value - initial_investment) / initial_investment

def calculate_breakeven_point(fixed_costs, price_per_unit, variable_cost_per_unit):
    return fixed_costs / (price_per_unit - variable_cost_per_unit)

def convert_kg_to_pounds(kg):
    return kg * 2.20462

def calculate_annual_growth_rate(start_value, end_value, years):
    return ((end_value / start_value) ** (1 / years)) - 1

def calculate_average_daily_balance(balances, days):
    return sum(balances) / days if days else 0

def calculate_weight_on_moon(weight_on_earth):
    return weight_on_earth * 0.165

def calculate_weight_on_mars(weight_on_earth):
    return weight_on_earth * 0.38

def calculate_weight_on_jupiter(weight_on_earth):
    return weight_on_earth * 2.34

def find_largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

def calculate_wind_chill(temperature, wind_speed):
    return 35.74 + 0.6215 * temperature - 35.75 * wind_speed**0.16 + 0.4275 * temperature * wind_speed**0.16

def is_valid_postal_code(postal_code):
    return len(postal_code) ==
