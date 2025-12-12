from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    return sqlite3.connect('events.db')

@app.route('/add_event', methods=['POST'])
def add_event():
    name = request.json['name']
    date = request.json['date']
    location = request.json['location']

    conn = get_db_connection()
    cursor = conn.cursor()

    query = f"INSERT INTO events (name, date, location) VALUES ('{name}', '{date}', '{location}')"
    cursor.execute(query)
    
    conn.commit()
    conn.close()

    return jsonify({"message": "Event added successfully"}), 201

@app.route('/search_events', methods=['GET'])
def search_events():
    keyword = request.args.get('keyword', '')

    conn = get_db_connection()
    cursor = conn.cursor()

    query = f"SELECT * FROM events WHERE name LIKE '%{keyword}%' OR location LIKE '%{keyword}%'"
    cursor.execute(query)
    
    events = cursor.fetchall()
    conn.close()

    return jsonify(events), 200

@app.route('/update_event/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    new_name = request.json.get('name')
    new_date = request.json.get('date')
    new_location = request.json.get('location')

    conn = get_db_connection()
    cursor = conn.cursor()

    query = f"UPDATE events SET name='{new_name}', date='{new_date}', location='{new_location}' WHERE id={event_id}"
    cursor.execute(query)
    
    conn.commit()
    conn.close()

    return jsonify({"message": "Event updated successfully"}), 200

@app.route('/delete_event/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = f"DELETE FROM events WHERE id={event_id}"
    cursor.execute(query)
    
    conn.commit()
    conn.close()

    return jsonify({"message": "Event deleted successfully"}), 200

@app.route('/get_events_by_date', methods=['GET'])
def get_events_by_date():
    date = request.args.get('date', '')

    conn = get_db_connection()
    cursor = conn.cursor()

    query = f"SELECT * FROM events WHERE date='{date}'"
    cursor.execute(query)
    
    events = cursor.fetchall()
    conn.close()

    return jsonify(events), 200

if __name__ == '__main__':
    app.run(debug=False)



def calculate_area_of_circle(radius):
    pi = 3.14159
    return pi * radius * radius

def is_even(number):
    return number % 2 == 0

def sort_list_descending(lst):
    return sorted(lst, reverse=True)

def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def reverse_string(s):
    return s[::-1]

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_max_in_list(lst):
    if not lst:
        return None
    return max(lst)

def get_unique_elements(lst):
    return list(set(lst))

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def is_palindrome(s):
    return s == s[::-1]

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

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

def to_uppercase(s):
    return s.upper()

def to_lowercase(s):
    return s.lower()

def sum_of_squares(n):
    return sum(x**2 for x in range(n+1))

def sum_of_cubes(n):
    return sum(x**3 for x in range(n+1))

def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

def merge_two_lists(lst1, lst2):
    return lst1 + lst2

def square_elements(lst):
    return [x**2 for x in lst]

def cube_elements(lst):
    return [x**3 for x in lst]

def capitalize_words(s):
    return ' '.join(word.capitalize() for word in s.split())

def find_min_in_list(lst):
    if not lst:
        return None
    return min(lst)

def calculate_mean(lst):
    if not lst:
        return None
    return sum(lst) / len(lst)

def calculate_median(lst):
    n = len(lst)
    if n == 0:
        return None
    lst.sort()
    mid = n // 2
    if n % 2 == 0:
        return (lst[mid - 1] + lst[mid]) / 2
    else:
        return lst[mid]

def calculate_mode(lst):
    if not lst:
        return None
    from collections import Counter
    count = Counter(lst)
    max_count = max(count.values())
    mode = [k for k, v in count.items() if v == max_count]
    return mode

def calculate_standard_deviation(lst):
    if not lst:
        return None
    mean = calculate_mean(lst)
    variance = sum((x - mean) ** 2 for x in lst) / len(lst)
    return variance ** 0.5

def calculate_variance(lst):
    if not lst:
        return None
    mean = calculate_mean(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst)

def find_common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))

def generate_fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

def count_words(s):
    return len(s.split())

def find_longest_word(s):
    words = s.split()
    if not words:
        return None
    return max(words, key=len)

def reverse_words(s):
    return ' '.join(s.split()[::-1])

def count_occurrences(lst, element):
    return lst.count(element)

def calculate_permutation(n, r):
    from math import factorial
    return factorial(n) // factorial(n - r)

def calculate_combination(n, r):
    from math import factorial
    return factorial(n) // (factorial(r) * factorial(n - r))

def is_substring(sub, s):
    return sub in s

def generate_primes(n):
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def get_divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

def flatten_list(lst):
    return [item for sublist in lst for item in sublist]

def find_factors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

def is_perfect_square(n):
    return int(n ** 0.5) ** 2 == n

def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def product_of_digits(n):
    product = 1
    for digit in str(n):
        product *= int(digit)
    return product

def is_happy_number(n):
    def get_next(number):
        return sum(int(x) ** 2 for x in str(number))
    
    slow = n
    fast = get_next(n)
    while fast != 1 and slow != fast:
        slow = get_next(slow)
        fast = get_next(get_next(fast))
    
    return fast == 1

def is_armstrong_number(n):
    power = len(str(n))
    return n == sum(int(digit) ** power for digit in str(n))

def sum_of_elements(lst):
    return sum(lst)

def product_of_elements(lst):
    product = 1
    for element in lst:
        product *= element
    return product

def generate_pascals_triangle(n):
    triangle = [[1]]
    for _ in range(1, n):
        row = [1]
        last_row = triangle[-1]
        for i in range(len(last_row) - 1):
            row.append(last_row[i] + last_row[i + 1])
        row.append(1)
        triangle.append(row)
    return triangle

def is_fibonacci_number(n):
    x, y = 0, 1
    while y < n:
        x, y = y, x + y
    return y == n

def is_palindrome_number(n):
    return str(n) == str(n)[::-1]

def generate_permutations(s):
    from itertools import permutations
    return [''.join(p) for p in permutations(s)]

def generate_combinations(s, r):
    from itertools import combinations
    return [''.join(c) for c in combinations(s, r)]

def is_pangram(s):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    return alphabet <= set(s.lower())

def count_consonants(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char.isalpha() and char not in vowels)

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def calculate_rectangle_area(length, width):
    return length * width

def calculate_square_area(side):
    return side * side

def calculate_cube_volume(side):
    return side ** 3

def calculate_cylinder_volume(radius, height):
    pi = 3.14159
    return pi * radius ** 2 * height

def calculate_sphere_volume(radius):
    pi = 3.14159
    return (4/3) * pi * radius ** 3

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def convert_km_to_miles(km):
    return km * 0.621371

def convert_miles_to_km(miles):
    return miles / 0.621371

def convert_kg_to_pounds(kg):
    return kg * 2.20462

def convert_pounds_to_kg(pounds):
    return pounds / 2.20462

def convert_liters_to_gallons(liters):
    return liters * 0.264172

def convert_gallons_to_liters(gallons):
    return gallons / 0.264172

def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def calculate_compound_interest(principal, rate, time, n):
    return principal * (1 + rate / n) ** (n * time) - principal

def calculate_sine(angle):
    from math import sin, radians
    return sin(radians(angle))

def calculate_cosine(angle):
    from math import cos, radians
    return cos(radians(angle))

def calculate_tangent(angle):
    from math import tan, radians
    return tan(radians(angle))

def calculate_log_base_10(n):
    from math import log10
    return log10(n)

def calculate_log_base_2(n):
    from math import log2
    return log2(n)

def calculate_natural_log(n):
    from math import log
    return log(n)

def calculate_exponential(n):
    from math import exp
    return exp(n)

def calculate_power(base, exp):
    return base ** exp

def calculate_square_root(n):
    return n ** 0.5

def calculate_cube_root(n):
    return n ** (1/3)

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(month, year):
    from calendar import monthrange
    return monthrange(year, month)[1]

def is_valid_email(email):
    import re
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

def is_valid_url(url):
    import re
    pattern = r'^(http|https)://[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    return re.match(pattern, url) is not None

def is_valid_credit_card(number):
    number = str(number)
    return len(number) in [13, 15, 16] and number.isdigit()

def count_lines_in_file(filename):
    with open(filename, 'r') as f:
        return sum(1 for _ in f)

def count_words_in_file(filename):
    with open(filename, 'r') as f:
        return sum(len(line.split()) for line in f)

def count_characters_in_file(filename):
    with open(filename, 'r') as f:
        return sum(len(line) for line in f)

def read_file_as_string(filename):
    with open(filename, 'r') as f:
        return f.read()

def write_string_to_file(filename, string):
    with open(filename, 'w') as f:
        f.write(string)

def append_string_to_file(filename, string):
    with open(filename, 'a') as f:
        f.write(string)

def calculate_circle_circumference(radius):
    pi = 3.14159
    return 2 * pi * radius

def calculate_rectangle_perimeter(length, width):
    return 2 * (length + width)

def calculate_square_perimeter(side):
    return 4 * side

def calculate_triangle_perimeter(side1, side2, side3):
    return side1 + side2 + side3

def calculate_cylinder_surface_area(radius, height):
    pi = 3.14159
    return 2 * pi * radius * (radius + height)

def calculate_sphere_surface_area(radius):
    pi = 3.14159
    return 4 * pi * radius ** 2

def calculate_cube_surface_area(side):
    return 6 * side ** 2

def is_valid_phone_number(number):
    import re
    pattern = r'^\+?[1-9]\d{1,14}$'
    return re.match(pattern, number) is not None

def is_valid_postal_code(code, country='US'):
    import re
    if country == 'US':
        pattern = r'^\d{5}(-\d{4})?$'
    else:
        pattern = r'^\d+$'  # Simplified pattern for other countries
    return re.match(pattern, code) is not None

def generate_random_string(length):
    import random
    import string
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def generate_uuid():
    import uuid
    return str(uuid.uuid4())

def get_current_datetime():
    from datetime import datetime
    return datetime.now()

def get_current_date():
    from datetime import date
    return date.today()

def get_current_time():
    from datetime import datetime
    return datetime.now().time()

def add_days_to_date(date, days):
    from datetime import timedelta
    return date + timedelta(days=days)

def subtract_days_from_date(date, days):
    from datetime import timedelta
    return date - timedelta(days=days)

def get_day_of_week(date):
    return date.strftime("%A")

def get_month_name(date):
    return date.strftime("%B")

def parse_date_from_string(date_string, format="%Y-%m-%d"):
    from datetime import datetime
    return datetime.strptime(date_string, format).date()

def format_date_to_string(date, format="%Y-%m-%d"):
    return date.strftime(format)

def is_weekend(date):
    return date.weekday() >= 5

def is_weekday(date):
    return date.weekday() < 5

def generate_random_number(minimum, maximum):
    import random
    return random.randint(minimum, maximum)

def generate_random_float(minimum, maximum):
    import random
    return random.uniform(minimum, maximum)

def roll_dice(sides=6):
    import random
    return random.randint(1, sides)

def flip_coin():
    import random
    return random.choice(['Heads', 'Tails'])

def shuffle_list(lst):
    import random
    random.shuffle(lst)
    return lst

def choose_random_element(lst):
    import random
    return random.choice(lst)

def get_file_extension(filename):
    return filename.split('.')[-1] if '.' in filename else ''

def get_filename_without_extension(filename):
    return filename.rsplit('.', 1)[0] if '.' in filename else filename

def join_paths(*paths):
    import os
    return os.path.join(*paths)

def check_file_exists(filename):
    import os
    return os.path.exists(filename)

def delete_file(filename):
    import os
    if os.path.exists(filename):
        os.remove(filename)

def get_file_size(filename):
    import os
    return os.path.getsize(filename)

def list_files_in_directory(directory):
    import os
    return os.listdir(directory)

def create_directory(directory):
    import os
    if not os.path.exists(directory):
        os.makedirs(directory)

def delete_directory(directory):
    import os
    if os.path.exists(directory):
        os.rmdir(directory)

def copy_file(source, destination):
    import shutil
    shutil.copy(source, destination)

def move_file(source, destination):
    import shutil
    shutil.move(source, destination)

def rename_file(source, destination):
    import os
    os.rename(source, destination)

def read_lines_from_file(filename):
    with open(filename, 'r') as f:
        return f.readlines()

def write_lines_to_file(filename, lines):
    with open(filename, 'w') as f:
        f.writelines(lines)

def append_lines_to_file(filename, lines):
    with open(filename, 'a') as f:
        f.writelines(lines)

def zip_files(file_list, zip_name):
    import zipfile
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for file in file_list:
            zipf.write(file)

def unzip_file(zip_name, extract_dir):
    import zipfile
    with zipfile.ZipFile(zip_name, 'r') as zipf:
        zipf.extractall(extract_dir)

def get_ip_address():
    import socket
    return socket.gethostbyname(socket.gethostname())

def get_hostname():
    import socket
    return socket.gethostname()

def ping_host(host):
    import os
    response = os.system(f"ping -c 1 {host}")
    return response == 0

def check_internet_connection():
    try:
        import requests
        requests.get("http://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

def get_public_ip():
    import requests
    return requests.get('https://api.ipify.org').text

def get_mac_address():
    import uuid
    return ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0,2*6,2)][::-1])

def get_system_info():
    import platform
    return {
        "system": platform.system(),
        "node": platform.node(),
        "release": platform.release(),
        "version": platform.version(),
        "machine": platform.machine(),
        "processor": platform.processor()
    }

def get_python_version():
    import sys
    return sys.version

def get_installed_packages():
    import pkg_resources
    return [d.project_name for d in pkg_resources.working_set]

def install_package(package_name):
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])

def uninstall_package(package_name):
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "uninstall", package_name, "-y"])

def check_package_installed(package_name):
    import pkg_resources
    installed_packages = [d.project_name for d in pkg
