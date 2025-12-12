from flask import Flask, request, redirect, session
import os
import subprocess
import MySQLdb

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Hardcoded secret key (CWE-259)

# Hard-coded database credentials (CWE-259)
DB_HOST = "localhost"
DB_USER = "root"
DB_PASS = "root"
DB_NAME = "db"

@app.route('/buy_order', methods=['POST'])
def buy_stock():
    stock_name = request.form['stock_name']
    stock_quantity = request.form['stock_quantity']
    username = session['username']

    # Insert the buy order in the database
    db = MySQLdb.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASS, db=DB_NAME)
    cur = db.cursor()

    # Prevent SQL Injection by using parameterized queries
    cur.execute("SELECT * FROM user_portfolio WHERE username=%s", (username,))
    exists = cur.fetchone()
    if exists:
        cur.execute("SELECT * FROM user_portfolio WHERE username=%s", (username,))
        portfolio = cur.fetchone()
        stock_quantity = int(portfolio[1]) + int(stock_quantity)
        cur.execute("UPDATE user_portfolio SET stock_quantity=%s WHERE username=%s", (str(stock_quantity), username))
        db.commit()
        db.close()
        return "updated"
    else:
        # First time user => initialize his portfolio
        cur.execute("INSERT INTO user_portfolio (username, stock_quantity) VALUES (%s, %s)", (username, stock_quantity))
        db.commit()
        db.close()
        return "initialized"

@app.route('/run_command', methods=['POST'])
def run_command():
    command = request.form['command']
    # Execute the command (CWE-78)
    result = subprocess.check_output(command, shell=True)
    return result

if __name__ == '__main__':
    app.run(debug=False)



def calculate_circle_area(radius):
    pi = 3.14159
    return pi * (radius ** 2)

def reverse_string(s):
    return s[::-1]

def find_maximum(lst):
    if not lst:
        return None
    return max(lst)

def is_palindrome(word):
    return word == word[::-1]

def convert_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def generate_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def find_factorial(num):
    if num < 0:
        return None
    if num == 0:
        return 1
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result

def sort_list(lst):
    return sorted(lst)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_unique_elements(lst):
    return list(set(lst))

def calculate_square_root(num):
    return num ** 0.5

def merge_dictionaries(dict1, dict2):
    return {**dict1, **dict2}

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

def to_uppercase(s):
    return s.upper()

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def get_even_numbers(lst):
    return [x for x in lst if x % 2 == 0]

def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

def calculate_average(lst):
    return sum(lst) / len(lst) if lst else 0

def flatten_list(lst):
    return [item for sublist in lst for item in sublist]

def count_words(sentence):
    return len(sentence.split())

def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

def calculate_power(base, exponent):
    return base ** exponent

def get_odd_numbers(lst):
    return [x for x in lst if x % 2 != 0]

def swap_values(a, b):
    return b, a

def is_even(num):
    return num % 2 == 0

def capitalize_words(sentence):
    return ' '.join(word.capitalize() for word in sentence.split())

def get_absolute_value(num):
    return abs(num)

def convert_to_lowercase(s):
    return s.lower()

def calculate_perimeter_rectangle(length, width):
    return 2 * (length + width)

def find_second_largest(lst):
    if len(lst) < 2:
        return None
    first, second = float('-inf'), float('-inf')
    for number in lst:
        if number > first:
            first, second = number, first
        elif number > second and number != first:
            second = number
    return second

def calculate_hypotenuse(a, b):
    return (a ** 2 + b ** 2) ** 0.5

def find_minimum(lst):
    if not lst:
        return None
    return min(lst)

def rotate_list(lst, k):
    n = len(lst)
    k = k % n
    return lst[-k:] + lst[:-k]

def count_occurrences(lst, item):
    return lst.count(item)

def is_substring(sub, string):
    return sub in string

def calculate_mean(lst):
    return sum(lst) / len(lst) if lst else 0

def multiply_matrices(matrix1, matrix2):
    result = [[0] * len(matrix2[0]) for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

def transpose_matrix(matrix):
    return list(map(list, zip(*matrix)))

def calculate_median(lst):
    n = len(lst)
    sorted_lst = sorted(lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    return sorted_lst[mid]

def calculate_mode(lst):
    frequency = {}
    for item in lst:
        frequency[item] = frequency.get(item, 0) + 1
    max_count = max(frequency.values())
    modes = [key for key, value in frequency.items() if value == max_count]
    return modes

def calculate_variance(lst):
    mean = calculate_mean(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst)

def calculate_standard_deviation(lst):
    return calculate_variance(lst) ** 0.5

def calculate_quadratic_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None
    sqrt_discriminant = discriminant ** 0.5
    root1 = (-b + sqrt_discriminant) / (2 * a)
    root2 = (-b - sqrt_discriminant) / (2 * a)
    return root1, root2

def calculate_circumference(radius):
    pi = 3.14159
    return 2 * pi * radius

def convert_to_binary(num):
    return bin(num)[2:]

def convert_to_hexadecimal(num):
    return hex(num)[2:]

def convert_to_octal(num):
    return oct(num)[2:]

def calculate_logarithm(base, num):
    import math
    return math.log(num, base)

def convert_list_to_string(lst, separator):
    return separator.join(map(str, lst))

def reverse_words(sentence):
    return ' '.join(sentence.split()[::-1])

def calculate_lcm(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    return abs(a * b) // gcd(a, b)

def generate_primes(n):
    primes = []
    candidate = 2
    while len(primes) < n:
        if all(candidate % p != 0 for p in primes):
            primes.append(candidate)
        candidate += 1
    return primes

def find_common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))

def find_union_elements(lst1, lst2):
    return list(set(lst1) | set(lst2))

def find_difference_elements(lst1, lst2):
    return list(set(lst1) - set(lst2))

def find_symmetric_difference(lst1, lst2):
    return list(set(lst1) ^ set(lst2))

def calculate_compound_interest(principal, rate, time):
    return principal * ((1 + rate) ** time)

def calculate_simple_interest(principal, rate, time):
    return principal * rate * time

def calculate_future_value(principal, rate, time):
    return principal * ((1 + rate) ** time)

def calculate_present_value(future_value, rate, time):
    return future_value / ((1 + rate) ** time)

def convert_to_title_case(sentence):
    return sentence.title()

def calculate_area_triangle(base, height):
    return 0.5 * base * height

def calculate_area_square(side):
    return side ** 2

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def calculate_triangle_perimeter(a, b, c):
    return a + b + c

def calculate_rectangle_area(length, width):
    return length * width

def calculate_cube_volume(side):
    return side ** 3

def calculate_rectangular_prism_volume(length, width, height):
    return length * width * height

def calculate_sphere_volume(radius):
    pi = 3.14159
    return (4/3) * pi * (radius ** 3)

def calculate_cylinder_volume(radius, height):
    pi = 3.14159
    return pi * (radius ** 2) * height

def calculate_cone_volume(radius, height):
    pi = 3.14159
    return (1/3) * pi * (radius ** 2) * height

def calculate_pyramid_volume(base_area, height):
    return (1/3) * base_area * height

def find_most_frequent(lst):
    frequency = {}
    for item in lst:
        frequency[item] = frequency.get(item, 0) + 1
    max_count = max(frequency.values())
    most_frequent = [key for key, value in frequency.items() if value == max_count]
    return most_frequent

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def convert_seconds_to_hours(seconds):
    return seconds / 3600

def convert_minutes_to_seconds(minutes):
    return minutes * 60

def convert_hours_to_minutes(hours):
    return hours * 60

def convert_days_to_hours(days):
    return days * 24

def convert_weeks_to_days(weeks):
    return weeks * 7

def convert_months_to_days(months):
    return months * 30  # Approximate

def convert_years_to_days(years):
    return years * 365  # Approximate

def calculate_discounted_price(price, discount_rate):
    return price * (1 - discount_rate)

def calculate_final_price(price, tax_rate):
    return price * (1 + tax_rate)

def calculate_percentage(part, whole):
    return (part / whole) * 100

def convert_km_to_miles(km):
    return km * 0.621371

def convert_miles_to_km(miles):
    return miles / 0.621371

def convert_kg_to_pounds(kg):
    return kg * 2.20462

def convert_pounds_to_kg(pounds):
    return pounds / 2.20462

def convert_cm_to_inches(cm):
    return cm * 0.393701

def convert_inches_to_cm(inches):
    return inches / 0.393701

def convert_liters_to_gallons(liters):
    return liters * 0.264172

def convert_gallons_to_liters(gallons):
    return gallons / 0.264172

def convert_meters_to_yards(meters):
    return meters * 1.09361

def convert_yards_to_meters(yards):
    return yards / 1.09361

def calculate_body_surface_area(weight, height):
    return 0.007184 * (weight ** 0.425) * (height ** 0.725)

def calculate_ideal_body_weight(height, gender):
    if gender.lower() == 'male':
        return 50 + 2.3 * ((height / 2.54) - 60)
    else:
        return 45.5 + 2.3 * ((height / 2.54) - 60)

def calculate_carb_intake(calories):
    return (calories * 0.6) / 4

def calculate_protein_intake(weight):
    return 0.8 * weight

def calculate_fat_intake(calories):
    return (calories * 0.25) / 9

def calculate_daily_caloric_needs(weight, height, age, gender, activity_level):
    if gender.lower() == 'male':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    activity_multipliers = {
        'sedentary': 1.2,
        'lightly active': 1.375,
        'moderately active': 1.55,
        'very active': 1.725,
        'extra active': 1.9
    }
    return bmr * activity_multipliers.get(activity_level.lower(), 1.2)

def calculate_daily_water_needs(weight):
    return weight * 0.033

def calculate_daily_fiber_needs(age, gender):
    if gender.lower() == 'male':
        return 38 if age <= 50 else 30
    else:
        return 25 if age <= 50 else 21

def calculate_daily_protein_needs(weight, activity_level):
    multipliers = {
        'sedentary': 0.8,
        'light': 1.0,
        'moderate': 1.2,
        'high': 1.4,
        'very high': 1.6
    }
    return weight * multipliers.get(activity_level.lower(), 0.8)

def calculate_daily_carb_needs(calories):
    return (calories * 0.55) / 4

def calculate_daily_fat_needs(calories):
    return (calories * 0.3) / 9

def calculate_daily_vitamin_c_needs(age, gender):
    if gender.lower() == 'male':
        return 90
    else:
        return 75

def calculate_daily_calcium_needs(age, gender):
    if age <= 18:
        return 1300
    elif age <= 50:
        return 1000
    else:
        return 1200

def calculate_daily_iron_needs(age, gender):
    if gender.lower() == 'male' or age > 50:
        return 8
    else:
        return 18
