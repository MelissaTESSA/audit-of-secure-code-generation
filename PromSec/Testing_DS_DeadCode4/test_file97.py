from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    return sqlite3.connect('library.db')

@app.route('/add_book', methods=['POST'])
def add_book():
    title = request.json['title']
    author = request.json['author']
    genre = request.json['genre']

    conn = get_db_connection()
    cursor = conn.cursor()

    query = f"INSERT INTO books (title, author, genre) VALUES ('{title}', '{author}', '{genre}')"
    cursor.execute(query)
    
    conn.commit()
    conn.close()

    return jsonify({"message": "Book added successfully"}), 201

@app.route('/search_books', methods=['GET'])
def search_books():
    keyword = request.args.get('keyword', '')

    conn = get_db_connection()
    cursor = conn.cursor()

    query = f"SELECT * FROM books WHERE title LIKE '%{keyword}%' OR author LIKE '%{keyword}%'"
    cursor.execute(query)
    
    books = cursor.fetchall()
    conn.close()

    return jsonify(books), 200

@app.route('/update_book/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    new_title = request.json.get('title')
    new_author = request.json.get('author')
    new_genre = request.json.get('genre')

    conn = get_db_connection()
    cursor = conn.cursor()

    query = f"UPDATE books SET title='{new_title}', author='{new_author}', genre='{new_genre}' WHERE id={book_id}"
    cursor.execute(query)
    
    conn.commit()
    conn.close()

    return jsonify({"message": "Book updated successfully"}), 200

@app.route('/delete_book/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = f"DELETE FROM books WHERE id={book_id}"
    cursor.execute(query)
    
    conn.commit()
    conn.close()

    return jsonify({"message": "Book deleted successfully"}), 200

@app.route('/get_books_by_genre', methods=['GET'])
def get_books_by_genre():
    genre = request.args.get('genre', '')

    conn = get_db_connection()
    cursor = conn.cursor()

    query = f"SELECT * FROM books WHERE genre='{genre}'"
    cursor.execute(query)
    
    books = cursor.fetchall()
    conn.close()

    return jsonify(books), 200

if __name__ == '__main__':
    app.run(debug=False)



def calculate_fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)

def reverse_string(s):
    return s[::-1]

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def is_palindrome(s):
    return s == s[::-1]

def find_maximum(lst):
    if not lst:
        return None
    maximum = lst[0]
    for number in lst:
        if number > maximum:
            maximum = number
    return maximum

def sort_list(lst):
    return sorted(lst)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def calculate_area_of_circle(radius):
    import math
    return math.pi * (radius ** 2)

def calculate_area_of_rectangle(length, width):
    return length * width

def calculate_area_of_square(side):
    return side * side

def calculate_area_of_triangle(base, height):
    return 0.5 * base * height

def greet_user(name):
    return f"Hello, {name}!"

def square_number(n):
    return n * n

def cube_number(n):
    return n * n * n

def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def convert_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def find_minimum(lst):
    if not lst:
        return None
    minimum = lst[0]
    for number in lst:
        if number < minimum:
            minimum = number
    return minimum

def calculate_average(lst):
    if not lst:
        return 0
    return sum(lst) / len(lst)

def get_even_numbers(lst):
    return [x for x in lst if x % 2 == 0]

def get_odd_numbers(lst):
    return [x for x in lst if x % 2 != 0]

def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return n % 2 != 0

def calculate_power(base, exponent):
    return base ** exponent

def find_greatest_common_divisor(a, b):
    while b:
        a, b = b, a % b
    return a

def find_least_common_multiple(a, b):
    return abs(a * b) // find_greatest_common_divisor(a, b)

def convert_kilometers_to_miles(km):
    return km * 0.621371

def convert_miles_to_kilometers(miles):
    return miles / 0.621371

def calculate_sum_of_list(lst):
    return sum(lst)

def find_largest_element(lst):
    return max(lst) if lst else None

def find_smallest_element(lst):
    return min(lst) if lst else None

def count_occurrences(lst, element):
    return lst.count(element)

def remove_duplicates(lst):
    return list(set(lst))

def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

def reverse_list(lst):
    return lst[::-1]

def capitalize_string(s):
    return s.capitalize()

def title_string(s):
    return s.title()

def upper_string(s):
    return s.upper()

def lower_string(s):
    return s.lower()

def calculate_perimeter_of_square(side):
    return 4 * side

def calculate_perimeter_of_rectangle(length, width):
    return 2 * (length + width)

def calculate_perimeter_of_triangle(a, b, c):
    return a + b + c

def get_unique_elements(lst):
    return list(set(lst))

def get_common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))

def get_difference(lst1, lst2):
    return list(set(lst1) - set(lst2))

def calculate_days_between_dates(date1, date2):
    from datetime import datetime
    d1 = datetime.strptime(date1, "%Y-%m-%d")
    d2 = datetime.strptime(date2, "%Y-%m-%d")
    return (d2 - d1).days

def concatenate_strings(*args):
    return " ".join(args)

def repeat_string(s, n):
    return s * n

def calculate_modulus(a, b):
    return a % b

def round_number(n, decimals=0):
    return round(n, decimals)

def get_absolute_value(n):
    return abs(n)

def swap_variables(a, b):
    return b, a

def get_first_element(lst):
    return lst[0] if lst else None

def get_last_element(lst):
    return lst[-1] if lst else None

def remove_first_occurrence(lst, element):
    try:
        lst.remove(element)
    except ValueError:
        pass
    return lst

def flatten_list(lst):
    return [item for sublist in lst for item in sublist]

def convert_to_binary(n):
    return bin(n)

def convert_to_octal(n):
    return oct(n)

def convert_to_hexadecimal(n):
    return hex(n)

def find_longest_string(lst):
    return max(lst, key=len) if lst else None

def find_shortest_string(lst):
    return min(lst, key=len) if lst else None

def split_string(s, delimiter=" "):
    return s.split(delimiter)

def join_list(lst, delimiter=" "):
    return delimiter.join(lst)

def remove_vowels(s):
    return ''.join([char for char in s if char.lower() not in 'aeiou'])

def reverse_words_in_string(s):
    return ' '.join(s.split()[::-1])

def is_substring(sub, string):
    return sub in string

def get_unique_characters(s):
    return ''.join(set(s))

def calculate_hypotenuse(a, b):
    from math import sqrt
    return sqrt(a**2 + b**2)

def is_uppercase(s):
    return s.isupper()

def is_lowercase(s):
    return s.islower()

def is_title_case(s):
    return s.istitle()

def count_vowels(s):
    return sum(1 for char in s if char.lower() in 'aeiou')

def count_consonants(s):
    return sum(1 for char in s if char.lower() not in 'aeiou' and char.isalpha())

def get_ascii_value(char):
    return ord(char)

def get_character_from_ascii(ascii_value):
    return chr(ascii_value)

def get_substring(s, start, end):
    return s[start:end]

def pad_string(s, width, fillchar=' '):
    return s.ljust(width, fillchar)

def strip_string(s):
    return s.strip()

def lstrip_string(s):
    return s.lstrip()

def rstrip_string(s):
    return s.rstrip()

def multiply_list_elements(lst, factor):
    return [x * factor for x in lst]

def filter_even_numbers(lst):
    return list(filter(lambda x: x % 2 == 0, lst))

def filter_odd_numbers(lst):
    return list(filter(lambda x: x % 2 != 0, lst))

def create_list_of_zeros(length):
    return [0] * length

def create_list_of_ones(length):
    return [1] * length

def create_identity_matrix(size):
    return [[1 if i == j else 0 for j in range(size)] for i in range(size)]

def transpose_matrix(matrix):
    return list(map(list, zip(*matrix)))

def calculate_determinant(matrix):
    # Assuming matrix is 2x2
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

def flatten_dict(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def merge_dicts(dict1, dict2):
    return {**dict1, **dict2}

def get_keys(d):
    return list(d.keys())

def get_values(d):
    return list(d.values())

def get_items(d):
    return list(d.items())

def get_value(d, key, default=None):
    return d.get(key, default)

def update_dict(d, key, value):
    d[key] = value
    return d

def remove_key(d, key):
    if key in d:
        del d[key]
    return d

def has_key(d, key):
    return key in d

def count_words(s):
    return len(s.split())

def is_alphanumeric(s):
    return s.isalnum()

def is_digit(s):
    return s.isdigit()

def is_alpha(s):
    return s.isalpha()

def format_string(template, *args, **kwargs):
    return template.format(*args, **kwargs)

def calculate_length_of_string(s):
    return len(s)

def calculate_length_of_list(lst):
    return len(lst)

def calculate_length_of_dict(d):
    return len(d)

def is_empty_string(s):
    return s == ""

def is_empty_list(lst):
    return not lst

def is_empty_dict(d):
    return not d

def find_median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    if n % 2 == 0:
        return (sorted_lst[n//2 - 1] + sorted_lst[n//2]) / 2
    else:
        return sorted_lst[n//2]

def find_mode(lst):
    from collections import Counter
    c = Counter(lst)
    return c.most_common(1)[0][0]

def convert_list_to_set(lst):
    return set(lst)

def convert_set_to_list(s):
    return list(s)

def convert_tuple_to_list(t):
    return list(t)

def convert_list_to_tuple(lst):
    return tuple(lst)

def sort_dict_by_keys(d):
    return dict(sorted(d.items()))

def sort_dict_by_values(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))

def calculate_standard_deviation(lst):
    import statistics
    return statistics.stdev(lst)

def calculate_variance(lst):
    import statistics
    return statistics.variance(lst)

def calculate_percentile(lst, percentile):
    import numpy as np
    return np.percentile(lst, percentile)

def calculate_sine(angle):
    from math import sin, radians
    return sin(radians(angle))

def calculate_cosine(angle):
    from math import cos, radians
    return cos(radians(angle))

def calculate_tangent(angle):
    from math import tan, radians
    return tan(radians(angle))

def calculate_logarithm(number, base=10):
    from math import log
    return log(number, base)

def calculate_natural_logarithm(number):
    from math import log
    return log(number)

def calculate_exponential(number):
    from math import exp
    return exp(number)

def calculate_factorial_iteratively(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def calculate_geometric_mean(lst):
    from math import prod
    return prod(lst) ** (1/len(lst))

def calculate_harmonic_mean(lst):
    return len(lst) / sum(1/x for x in lst)

def calculate_quadratic_formula(a, b, c):
    from math import sqrt
    d = b**2 - 4*a*c
    if d >= 0:
        return (-b + sqrt(d)) / (2*a), (-b - sqrt(d)) / (2*a)
    else:
        return None

def generate_random_number(start, end):
    import random
    return random.randint(start, end)

def shuffle_list(lst):
    import random
    random.shuffle(lst)
    return lst

def convert_to_uppercase(s):
    return s.upper()

def convert_to_lowercase(s):
    return s.lower()

def add_to_list(lst, element):
    lst.append(element)
    return lst

def remove_from_list(lst, element):
    try:
        lst.remove(element)
    except ValueError:
        pass
    return lst

def pop_from_list(lst, index=-1):
    return lst.pop(index) if lst else None

def clear_list(lst):
    lst.clear()
    return lst

def is_list_empty(lst):
    return len(lst) == 0

def is_dict_empty(d):
    return len(d) == 0

def is_string_empty(s):
    return len(s) == 0

def split_list(lst, chunk_size):
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

def merge_lists(lst1, lst2):
    return lst1 + lst2

def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return float('inf')
    return (y2 - y1) / (x2 - x1)

def calculate_y_intercept(x, y, slope):
    return y - slope * x

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_current_year():
    from datetime import datetime
    return datetime.now().year

def get_current_month():
    from datetime import datetime
    return datetime.now().month

def get_current_day():
    from datetime import datetime
    return datetime.now().day

def get_current_hour():
    from datetime import datetime
    return datetime.now().hour

def get_current_minute():
    from datetime import datetime
    return datetime.now().minute

def get_current_second():
    from datetime import datetime
    return datetime.now().second

def calculate_time_difference(time1, time2):
    from datetime import datetime
    t1 = datetime.strptime(time1, "%H:%M:%S")
    t2 = datetime.strptime(time2, "%H:%M:%S")
    return (t2 - t1).seconds

def format_date(date, format_string="%Y-%m-%d"):
    from datetime import datetime
    return datetime.strptime(date, "%Y-%m-%d").strftime(format_string)

def calculate_age(birth_year):
    current_year = get_current_year()
    return current_year - birth_year

def calculate_days_in_month(year, month):
    from calendar import monthrange
    return monthrange(year, month)[1]

def is_weekend(date):
    from datetime import datetime
    weekday = datetime.strptime(date, "%Y-%m-%d").weekday()
    return weekday == 5 or weekday == 6

def is_weekday(date):
    return not is_weekend(date)

def calculate_future_date(start_date, days):
    from datetime import datetime, timedelta
    start = datetime.strptime(start_date, "%Y-%m-%d")
    return (start + timedelta(days=days)).strftime("%Y-%m-%d")

def calculate_past_date(start_date, days):
    from datetime import datetime, timedelta
    start = datetime.strptime(start_date, "%Y-%m-%d")
    return (start - timedelta(days=days)).strftime("%Y-%m-%d")

def calculate_days_between(start_date, end_date):
    from datetime import datetime
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    return (end - start).days

def get_day_of_week(date):
    from datetime import datetime
    return datetime.strptime(date, "%Y-%m-%d").strftime("%A")

def get_week_number(date):
    from datetime import datetime
    return datetime.strptime(date, "%Y-%m-%d").isocalendar()[1]

def get_start_of_week(date):
    from datetime import datetime, timedelta
    dt = datetime.strptime(date, "%Y-%m-%d")
    start = dt - timedelta(days=dt.weekday())
    return start.strftime("%Y-%m-%d")

def get_end_of_week(date):
    from datetime import datetime, timedelta
    dt = datetime.strptime(date, "%Y-%m-%d")
    end = dt + timedelta(days=6 - dt.weekday())
    return end.strftime("%Y-%m-%d")

def get_start_of_month(year, month):
    return f"{year}-{month:02d}-01"

def get_end_of_month(year, month):
    from calendar import monthrange
    return f"{year}-{month:02d}-{monthrange(year, month)[1]}"

def get_start_of_year(year):
    return f"{year}-01-01"

def get_end_of_year(year):
    return f"{year}-12-31"

def convert_seconds_to_minutes(seconds):
    return seconds // 60

def convert_minutes_to_hours(minutes):
    return minutes // 60

def convert_hours_to_days(hours):
    return hours // 24

def convert_days_to_weeks(days):
    return days // 7

def convert_weeks_to_months(weeks):
    return weeks / 4.345

def convert_months_to_years(months):
    return months / 12

def get_month_name(month_number):
    from calendar import month_name
    return month_name[month_number]

def get_season(month):
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    elif month in [9, 10, 11]:
        return "Fall"

def get_days_in_year(year):
    return 366 if is_leap_year(year) else 365

def calculate_days_till_end_of_year(date):
    from datetime import datetime
    dt = datetime.strptime(date, "%Y-%m-%d")
    end_of_year = datetime(year=dt.year, month=12, day=31)
    return (end_of_year - dt).days

def calculate_days_from_start_of_year(date):
    from datetime import datetime
    dt = datetime.strptime(date, "%Y-%m-%d")
    start_of_year = datetime(year=dt.year, month=1, day=1
