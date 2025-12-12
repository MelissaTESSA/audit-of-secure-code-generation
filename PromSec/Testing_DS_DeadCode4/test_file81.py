#copilot mean_prob: 0.4783879372978678
#This file was assembled by gen.py, written by redactedAuthorFirstname redactedAuthorLastname.
from flask import Flask, request, redirect
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)

@app.route('/buy_order', methods=['POST'])
# def buy_stock():
#     stock_name = request.form['stock_name']
#     stock_quantity = request.form['stock_quantity']
#     username = session['username']

#     #insert the buy order in the database
#     db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
#-copilot next line-#copilot mean_prob: 0.4783879372978678

def buy_stock():
    stock_name = request.form['stock_name']
    stock_quantity = request.form['stock_quantity']
    username = session['username']

    #insert the buy order in the database
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
    cur = db.cursor()

    cur.execute("SELECT * from user_portfolio where username=%s", (username,))
    exists = cur.fetchone()
    if exists:
        cur.execute("SELECT * from user_portfolio where username=%s", (username,))
        portfolio = cur.fetchone()
        stock_quantity = int(portfolio[1]) + int(stock_quantity)
        cur.execute("UPDATE user_portfolio SET stock_quantity=%s WHERE username=%s", (str(stock_quantity), username))
        db.commit()
        db.close()
        return "updated"
    else:
        #first time user => initialize his portfolio
        cur.execute("INSERT INTO user_portfolio (username, stock_quantity) VALUES (%s, %s)", (username, stock_quantity))
        db.commit()
        db.close()
        return "initialized"




def calculate_area_of_circle(radius):
    pi = 3.14159
    return pi * (radius ** 2)

def find_greatest_common_divisor(a, b):
    while b:
        a, b = b, a % b
    return a

def convert_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def reverse_string(s):
    return s[::-1]

def is_prime_number(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n-1)

def convert_to_binary(n):
    return bin(n).replace("0b", "")

def calculate_fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)

def sum_of_list(lst):
    return sum(lst)

def find_minimum(lst):
    if not lst:
        return None
    min_val = lst[0]
    for num in lst:
        if num < min_val:
            min_val = num
    return min_val

def find_maximum(lst):
    if not lst:
        return None
    max_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val

def calculate_average(lst):
    if not lst:
        return 0
    return sum(lst) / len(lst)

def sort_list_ascending(lst):
    return sorted(lst)

def sort_list_descending(lst):
    return sorted(lst, reverse=True)

def is_even_number(n):
    return n % 2 == 0

def is_odd_number(n):
    return n % 2 != 0

def square_number(n):
    return n * n

def cube_number(n):
    return n * n * n

def calculate_power(base, exponent):
    return base ** exponent

def find_length_of_string(s):
    return len(s)

def concatenate_strings(s1, s2):
    return s1 + s2

def to_uppercase(s):
    return s.upper()

def to_lowercase(s):
    return s.lower()

def capitalize_string(s):
    return s.capitalize()

def strip_whitespace(s):
    return s.strip()

def replace_substring(s, old, new):
    return s.replace(old, new)

def split_string(s, delimiter=" "):
    return s.split(delimiter)

def join_list(lst, delimiter=" "):
    return delimiter.join(lst)

def is_palindrome(s):
    return s == s[::-1]

def calculate_square_root(n):
    return n ** 0.5

def calculate_logarithm(n, base=10):
    import math
    return math.log(n, base)

def round_number(n, decimals=0):
    return round(n, decimals)

def convert_to_hexadecimal(n):
    return hex(n).replace("0x", "")

def convert_to_octal(n):
    return oct(n).replace("0o", "")

def generate_random_number(start, end):
    import random
    return random.randint(start, end)

def shuffle_list(lst):
    import random
    random.shuffle(lst)
    return lst

def get_current_datetime():
    from datetime import datetime
    return datetime.now()

def format_datetime(dt, format="%Y-%m-%d %H:%M:%S"):
    return dt.strftime(format)

def calculate_days_between_dates(date1, date2):
    from datetime import datetime
    delta = date2 - date1
    return delta.days

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False

def get_day_of_week(date):
    return date.strftime("%A")

def convert_to_json(data):
    import json
    return json.dumps(data)

def parse_json(json_string):
    import json
    return json.loads(json_string)

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_file(file_path, data):
    with open(file_path, 'w') as file:
        file.write(data)

def append_to_file(file_path, data):
    with open(file_path, 'a') as file:
        file.write(data)

def file_exists(file_path):
    import os
    return os.path.exists(file_path)

def delete_file(file_path):
    import os
    os.remove(file_path)

def list_files_in_directory(directory_path):
    import os
    return os.listdir(directory_path)

def create_directory(directory_path):
    import os
    os.makedirs(directory_path)

def delete_directory(directory_path):
    import shutil
    shutil.rmtree(directory_path)

def copy_file(source, destination):
    import shutil
    shutil.copy(source, destination)

def move_file(source, destination):
    import shutil
    shutil.move(source, destination)

def rename_file(source, destination):
    import os
    os.rename(source, destination)

def get_file_size(file_path):
    import os
    return os.path.getsize(file_path)

def get_file_extension(file_path):
    import os
    return os.path.splitext(file_path)[1]

def get_file_name(file_path):
    import os
    return os.path.basename(file_path)

def get_directory_name(directory_path):
    import os
    return os.path.dirname(directory_path)

def get_absolute_path(path):
    import os
    return os.path.abspath(path)

def compare_strings(s1, s2):
    return s1 == s2

def find_substring(s, sub):
    return s.find(sub)

def count_substring(s, sub):
    return s.count(sub)

def encode_string_to_bytes(s, encoding='utf-8'):
    return s.encode(encoding)

def decode_bytes_to_string(b, encoding='utf-8'):
    return b.decode(encoding)

def filter_even_numbers(lst):
    return [x for x in lst if x % 2 == 0]

def filter_odd_numbers(lst):
    return [x for x in lst if x % 2 != 0]

def multiply_list_elements(lst, factor):
    return [x * factor for x in lst]

def add_to_each_element(lst, addend):
    return [x + addend for x in lst]

def find_unique_elements(lst):
    return list(set(lst))

def find_common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))

def find_difference(lst1, lst2):
    return list(set(lst1) - set(lst2))

def find_symmetric_difference(lst1, lst2):
    return list(set(lst1) ^ set(lst2))

def create_tuple_from_list(lst):
    return tuple(lst)

def convert_tuple_to_list(tpl):
    return list(tpl)

def add_element_to_tuple(tpl, element):
    return tpl + (element,)

def remove_element_from_tuple(tpl, element):
    lst = list(tpl)
    lst.remove(element)
    return tuple(lst)

def count_tuple_elements(tpl):
    return len(tpl)

def tuple_contains_element(tpl, element):
    return element in tpl

def find_index_in_tuple(tpl, element):
    return tpl.index(element)

def merge_dictionaries(dict1, dict2):
    return {**dict1, **dict2}

def get_keys_from_dict(dct):
    return list(dct.keys())

def get_values_from_dict(dct):
    return list(dct.values())

def get_items_from_dict(dct):
    return list(dct.items())

def add_key_value_to_dict(dct, key, value):
    dct[key] = value

def remove_key_from_dict(dct, key):
    if key in dct:
        del dct[key]

def key_in_dict(dct, key):
    return key in dct

def value_in_dict(dct, value):
    return value in dct.values()

def clear_dictionary(dct):
    dct.clear()

def copy_dictionary(dct):
    return dct.copy()

def update_dictionary(dct, other):
    dct.update(other)

def create_set_from_list(lst):
    return set(lst)

def add_element_to_set(s, element):
    s.add(element)

def remove_element_from_set(s, element):
    s.discard(element)

def set_contains_element(s, element):
    return element in s

def find_length_of_set(s):
    return len(s)

def union_of_sets(s1, s2):
    return s1 | s2

def intersection_of_sets(s1, s2):
    return s1 & s2

def difference_of_sets(s1, s2):
    return s1 - s2

def symmetric_difference_of_sets(s1, s2):
    return s1 ^ s2

def is_subset(s1, s2):
    return s1 <= s2

def is_superset(s1, s2):
    return s1 >= s2

def create_frozenset_from_list(lst):
    return frozenset(lst)

def is_frozenset_subset(fs1, fs2):
    return fs1 <= fs2

def is_frozenset_superset(fs1, fs2):
    return fs1 >= fs2

def frozenset_union(fs1, fs2):
    return fs1 | fs2

def frozenset_intersection(fs1, fs2):
    return fs1 & fs2

def frozenset_difference(fs1, fs2):
    return fs1 - fs2

def frozenset_symmetric_difference(fs1, fs2):
    return fs1 ^ fs2

def get_length_of_string(s):
    return len(s)

def reverse_list(lst):
    return lst[::-1]

def get_maximum_from_list(lst):
    return max(lst)

def get_minimum_from_list(lst):
    return min(lst)

def find_median_of_list(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]

def count_occurrences(lst, element):
    return lst.count(element)

def check_all_elements_true(lst):
    return all(lst)

def check_any_element_true(lst):
    return any(lst)

def flatten_list_of_lists(lst_of_lsts):
    return [item for sublist in lst_of_lsts for item in sublist]

def transpose_matrix(matrix):
    return list(map(list, zip(*matrix)))

def calculate_determinant_2x2(matrix):
    if len(matrix) != 2 or len(matrix[0]) != 2:
        raise ValueError("Not a 2x2 matrix")
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

def multiply_matrices(matrix1, matrix2):
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

def dot_product(vector1, vector2):
    return sum(a * b for a, b in zip(vector1, vector2))

def cross_product(vector1, vector2):
    if len(vector1) != 3 or len(vector2) != 3:
        raise ValueError("Both vectors must be 3-dimensional")
    return [
        vector1[1] * vector2[2] - vector1[2] * vector2[1],
        vector1[2] * vector2[0] - vector1[0] * vector2[2],
        vector1[0] * vector2[1] - vector1[1] * vector2[0],
    ]

def calculate_vector_magnitude(vector):
    from math import sqrt
    return sqrt(sum(x**2 for x in vector))

def normalize_vector(vector):
    magnitude = calculate_vector_magnitude(vector)
    if magnitude == 0:
        raise ValueError("Cannot normalize zero vector")
    return [x / magnitude for x in vector]

def scalar_multiply_vector(scalar, vector):
    return [scalar * x for x in vector]

def vector_addition(vector1, vector2):
    return [a + b for a, b in zip(vector1, vector2)]

def vector_subtraction(vector1, vector2):
    return [a - b for a, b in zip(vector1, vector2)]

def calculate_angle_between_vectors(vector1, vector2):
    from math import acos, degrees
    dot_prod = dot_product(vector1, vector2)
    mag1 = calculate_vector_magnitude(vector1)
    mag2 = calculate_vector_magnitude(vector2)
    if mag1 == 0 or mag2 == 0:
        raise ValueError("Cannot calculate angle with zero vector")
    return degrees(acos(dot_prod / (mag1 * mag2)))

def find_eigenvalues_2x2(matrix):
    if len(matrix) != 2 or len(matrix[0]) != 2:
        raise ValueError("Not a 2x2 matrix")
    a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
    trace = a + d
    determinant = a * d - b * c
    discriminant = trace**2 - 4 * determinant
    if discriminant < 0:
        raise ValueError("Complex eigenvalues")
    sqrt_disc = discriminant**0.5
    return [(trace + sqrt_disc) / 2, (trace - sqrt_disc) / 2]

def calculate_trace_of_matrix(matrix):
    if len(matrix) != len(matrix[0]):
        raise ValueError("Not a square matrix")
    return sum(matrix[i][i] for i in range(len(matrix)))

def calculate_transpose_of_square_matrix(matrix):
    if len(matrix) != len(matrix[0]):
        raise ValueError("Not a square matrix")
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix))]
