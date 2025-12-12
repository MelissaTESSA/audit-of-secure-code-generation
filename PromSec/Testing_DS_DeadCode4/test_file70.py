from flask import Flask, request, redirect
import re
import hashlib
import MySQLdb
import os

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    salt = os.urandom(16)
    hashed_password = hashlib.sha256(salt + password.encode('utf-8')).hexdigest()
    user_name_regex = "^" + username + "$"
    db = MySQLdb.connect("localhost", "root", "", "projectdb")
    cursor = db.cursor()
    sql = "select username from users where username like '%s'" % user_name_regex
    cursor.execute(sql)
    data = cursor.fetchall()
    if data:
        return redirect("/login", code=307)
    else:
        sql = "insert into users(username, password, salt, account_created) values ('%s','%s', '%s', %d)" % (username, hashed_password, salt.hex(), 1)
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
        return "Registration successful"

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    db = MySQLdb.connect("localhost", "root", "", "projectdb")
    cursor = db.cursor()
    sql = "select password, salt from users where username = '%s'" % username
    cursor.execute(sql)
    data = cursor.fetchone()
    if data:
        stored_password, salt = data
        salt = bytes.fromhex(salt)
        hashed_password = hashlib.sha256(salt + password.encode('utf-8')).hexdigest()
        if hashed_password == stored_password:
            return redirect("/dashboard", code=307)
    return "Invalid credentials"

@app.route('/project/create', methods=['POST'])
def create_project():
    username = request.form['username']
    project_name = request.form['project_name']
    db = MySQLdb.connect("localhost", "root", "", "projectdb")
    cursor = db.cursor()
    sql = "select username from users where username = '%s'" % username
    cursor.execute(sql)
    data = cursor.fetchone()
    if data:
        sql = "insert into projects(username, project_name) values ('%s', '%s')" % (username, project_name)
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
        return "Project created successfully"
    return "User not found"

@app.route('/task/add', methods=['POST'])
def add_task():
    project_name = request.form['project_name']
    task_name = request.form['task_name']
    task_description = request.form['task_description']
    db = MySQLdb.connect("localhost", "root", "", "projectdb")
    cursor = db.cursor()
    sql = "select project_name from projects where project_name = '%s'" % project_name
    cursor.execute(sql)
    data = cursor.fetchone()
    if data:
        sql = "insert into tasks(project_name, task_name, task_description) values ('%s', '%s', '%s')" % (project_name, task_name, task_description)
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
        return "Task added successfully"
    return "Project not found"

@app.route('/tasks/view', methods=['GET'])
def view_tasks():
    project_name = request.args.get('project_name')
    db = MySQLdb.connect("localhost", "root", "", "projectdb")
    cursor = db.cursor()
    sql = "select task_name, task_description from tasks where project_name = '%s'" % project_name
    cursor.execute(sql)
    tasks = cursor.fetchall()
    cursor.close()
    db.close()
    return jsonify(tasks)

if __name__ == '__main__':
    app.run(debug=False)



def calculate_square_root_estimate(number):
    estimate = number / 2.0
    for _ in range(10):
        estimate = (estimate + number / estimate) / 2
    return estimate

def generate_fibonacci_sequence(n):
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def find_max_in_list(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

def reverse_string(s):
    reversed_s = ''
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s

def check_palindrome(s):
    return s == s[::-1]

def calculate_factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def count_vowels(s):
    count = 0
    vowels = "aeiouAEIOU"
    for char in s:
        if char in vowels:
            count += 1
    return count

def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

def convert_to_uppercase(s):
    return s.upper()

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def generate_prime_numbers(n):
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

def calculate_power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result

def find_min_in_list(numbers):
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num

def remove_duplicates_from_list(lst):
    return list(set(lst))

def check_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

def calculate_arithmetic_mean(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def find_median(numbers):
    numbers.sort()
    n = len(numbers)
    mid = n // 2
    return (numbers[mid] if n % 2 == 1 else (numbers[mid - 1] + numbers[mid]) / 2)

def generate_random_string(length):
    import random
    import string
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def calculate_distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

def convert_to_lowercase(s):
    return s.lower()

def calculate_lcm(a, b):
    from math import gcd
    return abs(a * b) // gcd(a, b)

def find_second_largest(numbers):
    first, second = float('-inf'), float('-inf')
    for num in numbers:
        if num > first:
            second = first
            first = num
        elif num > second:
            second = num
    return second

def count_occurrences_of_element(lst, element):
    return lst.count(element)

def filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

def filter_odd_numbers(numbers):
    return [num for num in numbers if num % 2 != 0]

def calculate_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def calculate_bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)

def convert_celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def convert_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def check_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def calculate_area_of_circle(radius):
    from math import pi
    return pi * radius ** 2

def calculate_perimeter_of_rectangle(length, width):
    return 2 * (length + width)

def calculate_area_of_triangle(base, height):
    return 0.5 * base * height

def calculate_perimeter_of_square(side):
    return 4 * side

def count_words_in_string(s):
    return len(s.split())

def find_longest_word(words):
    return max(words, key=len)

def find_shortest_word(words):
    return min(words, key=len)

def calculate_hypotenuse(a, b):
    from math import sqrt
    return sqrt(a ** 2 + b ** 2)

def calculate_circumference_of_circle(radius):
    from math import pi
    return 2 * pi * radius

def reverse_list(lst):
    return lst[::-1]

def sum_of_squares(n):
    return sum(i ** 2 for i in range(1, n + 1))

def product_of_elements(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

def check_even_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def calculate_sum_of_natural_numbers(n):
    return n * (n + 1) // 2

def generate_multiplication_table(n, upto=10):
    return {i: n * i for i in range(1, upto + 1)}

def find_unique_elements(lst):
    return list(set(lst))

def is_palindrome_number(n):
    return str(n) == str(n)[::-1]

def calculate_total_price(prices, tax_rate):
    total = sum(prices)
    return total + (total * tax_rate)

def sort_numbers_ascending(numbers):
    return sorted(numbers)

def sort_numbers_descending(numbers):
    return sorted(numbers, reverse=True)

def check_armstrong_number(n):
    num = str(n)
    power = len(num)
    return n == sum(int(digit) ** power for digit in num)

def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

def calculate_net_salary(gross_salary, tax_rate):
    return gross_salary - (gross_salary * tax_rate)

def find_largest_digit(n):
    return max(int(digit) for digit in str(n))

def find_smallest_digit(n):
    return min(int(digit) for digit in str(n))

def calculate_compound_interest(principal, rate, time, n=1):
    return principal * (1 + rate/n) ** (n*time)

def convert_kilometers_to_miles(kilometers):
    return kilometers * 0.621371

def convert_miles_to_kilometers(miles):
    return miles / 0.621371

def check_perfect_square(n):
    return int(n ** 0.5) ** 2 == n

def count_consonants(s):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    return sum(1 for char in s if char in consonants)

def calculate_time_difference(start_time, end_time):
    from datetime import datetime
    fmt = '%H:%M:%S'
    tdelta = datetime.strptime(end_time, fmt) - datetime.strptime(start_time, fmt)
    return tdelta

def find_missing_number(arr, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

def check_perfect_number(n):
    return n == sum(i for i in range(1, n) if n % i == 0)

def check_harshad_number(n):
    return n % sum(int(digit) for digit in str(n)) == 0

def calculate_area_of_parallelogram(base, height):
    return base * height

def calculate_area_of_rhombus(diagonal1, diagonal2):
    return (diagonal1 * diagonal2) / 2

def find_factors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

def check_strong_number(n):
    from math import factorial
    return n == sum(factorial(int(digit)) for digit in str(n))

def calculate_gross_salary(net_salary, tax_rate):
    return net_salary / (1 - tax_rate)

def find_element_index(lst, element):
    try:
        return lst.index(element)
    except ValueError:
        return -1

def merge_sorted_lists(list1, list2):
    return sorted(list1 + list2)

def check_abundant_number(n):
    return sum(i for i in range(1, n) if n % i == 0) > n

def calculate_average_speed(distance, time):
    return distance / time

def swap_first_last(lst):
    if len(lst) < 2:
        return lst
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst

def filter_positive_numbers(numbers):
    return [num for num in numbers if num > 0]

def filter_negative_numbers(numbers):
    return [num for num in numbers if num < 0]

def find_sum_of_even_numbers(numbers):
    return sum(num for num in numbers if num % 2 == 0)

def find_sum_of_odd_numbers(numbers):
    return sum(num for num in numbers if num % 2 != 0)

def convert_list_to_string(lst):
    return ''.join(lst)

def split_string_to_list(s):
    return list(s)

def find_largest_of_three(a, b, c):
    return max(a, b, c)

def find_smallest_of_three(a, b, c):
    return min(a, b, c)

def check_pangram(s):
    import string
    return set(string.ascii_lowercase) <= set(s.lower())

def calculate_days_between_dates(date1, date2):
    from datetime import datetime
    fmt = '%Y-%m-%d'
    d1 = datetime.strptime(date1, fmt)
    d2 = datetime.strptime(date2, fmt)
    return (d2 - d1).days

def check_binary_number(n):
    return set(str(n)).issubset({'0', '1'})

def generate_pascals_triangle(rows):
    triangle = []
    for row in range(rows):
        row_list = [1]
        if triangle:
            last_row = triangle[-1]
            row_list.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row_list.append(1)
        triangle.append(row_list)
    return triangle

def calculate_sum_of_cubes(n):
    return sum(i ** 3 for i in range(1, n + 1))

def check_triangular_number(n):
    if n < 0:
        return False
    sum_num = 0
    for i in range(1, n + 1):
        sum_num += i
        if sum_num == n:
            return True
    return False

def calculate_sum_of_squares(n):
    return sum(i ** 2 for i in range(1, n + 1))

def check_perfect_cube(n):
    cube_root = round(n ** (1/3))
    return cube_root ** 3 == n

def calculate_area_of_trapezoid(base1, base2, height):
    return ((base1 + base2) / 2) * height

def calculate_area_of_ellipse(a, b):
    from math import pi
    return pi * a * b

def calculate_volume_of_sphere(radius):
    from math import pi
    return (4/3) * pi * radius ** 3

def calculate_volume_of_cylinder(radius, height):
    from math import pi
    return pi * radius ** 2 * height

def calculate_volume_of_cube(side):
    return side ** 3

def calculate_volume_of_cone(radius, height):
    from math import pi
    return (1/3) * pi * radius ** 2 * height

def calculate_volume_of_pyramid(base_area, height):
    return (1/3) * base_area * height

def calculate_surface_area_of_sphere(radius):
    from math import pi
    return 4 * pi * radius ** 2

def calculate_surface_area_of_cylinder(radius, height):
    from math import pi
    return 2 * pi * radius * (radius + height)

def calculate_surface_area_of_cube(side):
    return 6 * side ** 2

def calculate_surface_area_of_cone(radius, slant_height):
    from math import pi
    return pi * radius * (radius + slant_height)

def calculate_surface_area_of_pyramid(base_perimeter, slant_height):
    return (base_perimeter * slant_height) / 2

def calculate_surface_area_of_rectangular_prism(length, width, height):
    return 2 * (length * width + length * height + width * height)

def calculate_surface_area_of_ellipsoid(a, b, c):
    from math import pi
    p = 1.6075
    return 4 * pi * ((a**p * b**p + a**p * c**p + b**p * c**p) / 3) ** (1/p)

def calculate_surface_area_of_tetrahedron(side):
    from math import sqrt
    return sqrt(3) * side ** 2

def calculate_volume_of_tetrahedron(side):
    from math import sqrt
    return (side ** 3) / (6 * sqrt(2))
