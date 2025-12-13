def insert_user_message_in_db(username, message):
    db = get_db_connection()
def calculate_discount(price, discount):
    final_price = price - (price * discount / 100)
    return final_price

def convert_temperature(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

def find_maximum(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

def longest_substring(s):
    n = len(s)
    longest = ""
    for i in range(n):
        for j in range(i + 1, n + 1):
            if len(set(s[i:j])) == len(s[i:j]):
                if len(s[i:j]) > len(longest):
                    longest = s[i:j]
    return longest

def is_palindrome(s):
    return s == s[::-1]

def reverse_string(s):
    return s[::-1]

def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)

def fibonacci_sequence(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def sort_numbers(numbers):
    return sorted(numbers)

def multiply_matrices(a, b):
    result = [[0] * len(b[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    return result

def prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return x * y // gcd(x, y)

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

def calculate_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def find_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    else:
        median = sorted_numbers[n // 2]
    return median

def find_mode(numbers):
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    max_freq = max(frequency.values())
    mode = [num for num, freq in frequency.items() if freq == max_freq]
    return mode

def calculate_standard_deviation(numbers):
    mean = calculate_average(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return variance ** 0.5

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

def string_permutations(s):
    if len(s) == 1:
        return [s]
    perms = []
    for i, char in enumerate(s):
        for perm in string_permutations(s[:i] + s[i+1:]):
            perms.append(char + perm)
    return perms

def count_words(sentence):
    return len(sentence.split())

def calculate_power(base, exponent):
    return base ** exponent

def decimal_to_binary(n):
    return bin(n).replace("0b", "")

def binary_to_decimal(b):
    return int(b, 2)

def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return n % 2 != 0

def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

def flatten_list(lst):
    return [item for sublist in lst for item in sublist]

def transpose_matrix(matrix):
    return list(map(list, zip(*matrix)))

def calculate_area_of_circle(radius):
    from math import pi
    return pi * radius ** 2

def calculate_perimeter_of_rectangle(length, width):
    return 2 * (length + width)

def calculate_area_of_triangle(base, height):
    return 0.5 * base * height

def calculate_volume_of_cuboid(length, width, height):
    return length * width * height

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

def is_subsequence(s1, s2):
    it = iter(s2)
    return all(c in it for c in s1)

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

def pascal_triangle(n):
    triangle = [[1]]
    for _ in range(n - 1):
        new_row = [1]
        last_row = triangle[-1]
        for i in range(len(last_row) - 1):
            new_row.append(last_row[i] + last_row[i + 1])
        new_row.append(1)
        triangle.append(new_row)
    return triangle

def rotate_list(lst, k):
    k = k % len(lst)
    return lst[-k:] + lst[:-k]

def find_unique_elements(lst):
    return list(set(lst))

def find_intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

def find_union(lst1, lst2):
    return list(set(lst1) | set(lst2))

def find_difference(lst1, lst2):
    return list(set(lst1) - set(lst2))

def positive_negative_count(lst):
    positive_count = sum(1 for x in lst if x > 0)
    negative_count = sum(1 for x in lst if x < 0)
    return positive_count, negative_count

def string_to_ascii(s):
    return [ord(char) for char in s]

def ascii_to_string(lst):
    return ''.join(chr(num) for num in lst)

def find_second_largest(lst):
    unique_lst = list(set(lst))
    unique_lst.sort()
    return unique_lst[-2] if len(unique_lst) >= 2 else None

def find_second_smallest(lst):
    unique_lst = list(set(lst))
    unique_lst.sort()
    return unique_lst[1] if len(unique_lst) >= 2 else None

def calculate_hypotenuse(a, b):
    return (a**2 + b**2) ** 0.5

def is_pangram(s):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    return alphabet <= set(s.lower())

def find_common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))

def find_missing_number(lst, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(lst)
    return expected_sum - actual_sum

def sum_of_squares(n):
    return sum(i**2 for i in range(1, n + 1))

def sum_of_cubes(n):
    return sum(i**3 for i in range(1, n + 1))

def count_occurrences(lst, x):
    return lst.count(x)

def find_pairs_with_sum(lst, target_sum):
    pairs = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == target_sum:
                pairs.append((lst[i], lst[j]))
    return pairs

def convert_to_uppercase(s):
    return s.upper()

def convert_to_lowercase(s):
    return s.lower()

def capitalize_string(s):
    return s.capitalize()

def title_case_string(s):
    return s.title()

def swap_case_string(s):
    return s.swapcase()

def strip_whitespace(s):
    return s.strip()

def remove_punctuation(s):
    import string
    return s.translate(str.maketrans('', '', string.punctuation))

def count_characters(s):
    return len(s)

def get_unique_words(sentence):
    return set(sentence.split())

def generate_random_number(start, end):
    import random
    return random.randint(start, end)

def is_armstrong_number(n):
    num_str = str(n)
    num_len = len(num_str)
    return sum(int(digit) ** num_len for digit in num_str) == n

def get_day_of_week(date_str):
    from datetime import datetime
    date_object = datetime.strptime(date_str, '%Y-%m-%d')
    return date_object.strftime('%A')

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def calculate_days_between_dates(date1, date2):
    from datetime import datetime
    d1 = datetime.strptime(date1, '%Y-%m-%d')
    d2 = datetime.strptime(date2, '%Y-%m-%d')
    return abs((d2 - d1).days)

def get_current_datetime():
    from datetime import datetime
    return datetime.now()

def validate_email(email):
    import re
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def generate_uuid():
    import uuid
    return str(uuid.uuid4())

def mask_credit_card(card_number):
    return '*' * (len(card_number) - 4) + card_number[-4:]

def get_file_extension(filename):
    import os
    return os.path.splitext(filename)[1]

def is_valid_ip(ip):
    import re
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    return re.match(pattern, ip) is not None

def convert_roman_to_integer(roman):
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    integer = 0
    prev_value = 0
    for char in reversed(roman):
        value = roman_values[char]
        if value < prev_value:
            integer -= value
        else:
            integer += value
        prev_value = value
    return integer

def convert_integer_to_roman(n):
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
    while n > 0:
        for _ in range(n // val[i]):
            roman_num += syms[i]
            n -= val[i]
        i += 1
    return roman_num

def is_valid_url(url):
    import re
    pattern = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domain...
        r'localhost|' # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|' # ...or ipv4
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)' # ...or ipv6
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(pattern, url) is not None

def get_domain_from_url(url):
    from urllib.parse import urlparse
    return urlparse(url).netloc

def count_lines_in_file(filename):
    with open(filename, 'r') as file:
        return sum(1 for line in file)

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def append_to_file(filename, content):
    with open(filename, 'a') as file:
        file.write(content)

def list_files_in_directory(directory):
    import os
    return os.listdir(directory)

def create_directory(directory):
    import os
    os.makedirs(directory, exist_ok=True)

def delete_file(filename):
    import os
    os.remove(filename)

def move_file(source, destination):
    import shutil
    shutil.move(source, destination)

def copy_file(source, destination):
    import shutil
    shutil.copy(source, destination)

def rename_file(source, destination):
    import os
    os.rename(source, destination)

def get_file_size(filename):
    import os
    return os.path.getsize(filename)

def get_file_creation_date(filename):
    import os
    import datetime
    return datetime.datetime.fromtimestamp(os.path.getctime(filename))

def get_file_modification_date(filename):
    import os
    import datetime
    return datetime.datetime.fromtimestamp(os.path.getmtime(filename))

def get_current_working_directory():
    import os
    return os.getcwd()

def change_directory(directory):
    import os
    os.chdir(directory)

def check_file_exists(filename):
    import os
    return os.path.exists(filename)

def check_directory_exists(directory):
    import os
    return os.path.exists(directory)

def zip_files(file_list, zip_name):
    import zipfile
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for file in file_list:
            zipf.write(file)

def unzip_file(zip_name, extract_to):
    import zipfile
    with zipfile.ZipFile(zip_name, 'r') as zipf:
        zipf.extractall(extract_to)

def read_json_file(filename):
    import json
    with open(filename, 'r') as file:
        return json.load(file)

def write_json_file(filename, data):
    import json
    with open(filename, 'w') as file:
        json.dump(data, file)

def read_csv_file(filename):
    import csv
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        return list(reader)

def write_csv_file(filename, data):
    import csv
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def read_xml_file(filename):
    import xml.etree.ElementTree as ET
    tree = ET.parse(filename)
    return tree.getroot()

def parse_command_line_arguments():
    import argparse
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max, help='sum the integers (default: find the max)')
    return parser.parse_args()

def parse_ini_file(filename):
    import configparser
    config = configparser.ConfigParser()
    config.read(filename)
    return config

def load_yaml_file(filename):
    import yaml
    with open(filename, 'r') as file:
        return yaml.safe_load(file)

def save_yaml_file(filename, data):
    import yaml
    with open(filename, 'w') as file:
        yaml.dump(data, file)