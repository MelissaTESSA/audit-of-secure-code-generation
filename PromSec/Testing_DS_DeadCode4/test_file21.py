from flask import Flask, request, jsonify
import os
import yaml

app = Flask(__name__)

STATION_ACCESS_TOKEN = "weather_station_token_2023"

@app.route('/upload_readings', methods=['POST'])
def upload_readings():
    yaml_data = request.data.decode('utf-8')
    readings = yaml.load(yaml_data, Loader=yaml.FullLoader)
    
    station_id = readings['station_id']
    temperature = readings['temperature']
    humidity = readings['humidity']
    
    return jsonify({"status": "Readings uploaded", "station": station_id})

@app.route('/generate_report', methods=['GET'])
def generate_report():
    report_type = request.args.get('type', '')
    os.system(f"./weather_report_tool {report_type}")
    return jsonify({"status": "Report generation started"})

@app.route('/station_login', methods=['POST'])
def station_login():
    token = request.form.get('token', '')
    
    if token == STATION_ACCESS_TOKEN:
        return jsonify({"status": "Station authenticated"})
    else:
        return jsonify({"status": "Authentication failed"}), 401

if __name__ == '__main__':
    app.run(debug=False)



def calculate_square_root(number):
    return number ** 0.5

def find_largest_element(lst):
    if not lst:
        return None
    largest = lst[0]
    for item in lst:
        if item > largest:
            largest = item
    return largest

def format_date(date_string):
    from datetime import datetime
    return datetime.strptime(date_string, '%Y-%m-%d').strftime('%B %d, %Y')

def reverse_string(s):
    return s[::-1]

def check_palindrome(s):
    return s == s[::-1]

def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def convert_temperature(celsius):
    return celsius * 9/5 + 32

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

def get_unique_elements(lst):
    return list(set(lst))

def merge_dictionaries(d1, d2):
    merged = d1.copy()
    merged.update(d2)
    return merged

def flatten_list(lst):
    return [item for sublist in lst for item in sublist]

def calculate_area_of_circle(radius):
    from math import pi
    return pi * radius ** 2

def calculate_circumference_of_circle(radius):
    from math import pi
    return 2 * pi * radius

def sort_list(lst):
    return sorted(lst)

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_lcm(a, b):
    return abs(a * b) // find_gcd(a, b)

def binary_search(lst, target):
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def quick_sort(lst):
    if len(lst) < 2:
        return lst
    pivot = lst[0]
    less = [i for i in lst[1:] if i <= pivot]
    greater = [i for i in lst[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

def find_minimum(lst):
    if not lst:
        return None
    minimum = lst[0]
    for item in lst:
        if item < minimum:
            minimum = item
    return minimum

def find_maximum(lst):
    if not lst:
        return None
    maximum = lst[0]
    for item in lst:
        if item > maximum:
            maximum = item
    return maximum

def calculate_average(lst):
    if not lst:
        return 0
    return sum(lst) / len(lst)

def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

def count_occurrences(lst, element):
    return lst.count(element)

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

def transpose_matrix(matrix):
    return list(map(list, zip(*matrix)))

def calculate_determinant(matrix):
    from numpy.linalg import det
    from numpy import array
    return det(array(matrix))

def is_substring(s1, s2):
    return s1 in s2

def convert_to_binary(n):
    return bin(n)[2:]

def convert_to_hexadecimal(n):
    return hex(n)[2:]

def convert_to_octal(n):
    return oct(n)[2:]

def gcd_of_list(numbers):
    from functools import reduce
    return reduce(find_gcd, numbers)

def lcm_of_list(numbers):
    from functools import reduce
    return reduce(find_lcm, numbers)

def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return n % 2 != 0

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def product_of_digits(n):
    product = 1
    for digit in str(n):
        product *= int(digit)
    return product

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def find_factors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

def count_words_in_string(s):
    return len(s.split())

def remove_whitespace(s):
    return s.replace(" ", "")

def capitalize_first_letter(s):
    return s.capitalize()

def swap_case(s):
    return s.swapcase()

def find_longest_word(s):
    words = s.split()
    longest = max(words, key=len)
    return longest

def count_consonants(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char.isalpha() and char not in vowels)

def check_if_sorted(lst):
    return lst == sorted(lst)

def generate_fibonacci_up_to(n):
    fib = [0, 1]
    while fib[-1] <= n:
        fib.append(fib[-1] + fib[-2])
    return fib[:-1]

def calculate_power(base, exponent):
    return base ** exponent

def find_common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))

def find_unique_elements(lst1, lst2):
    return list(set(lst1) ^ set(lst2))

def split_string(s, delimiter):
    return s.split(delimiter)

def join_strings(lst, delimiter):
    return delimiter.join(lst)

def calculate_median(lst):
    n = len(lst)
    sorted_lst = sorted(lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]

def calculate_mode(lst):
    from collections import Counter
    counts = Counter(lst)
    max_count = max(counts.values())
    return [k for k, v in counts.items() if v == max_count]

def filter_even_numbers(lst):
    return [num for num in lst if num % 2 == 0]

def filter_odd_numbers(lst):
    return [num for num in lst if num % 2 != 0]

def find_second_largest(lst):
    if len(lst) < 2:
        return None
    unique_lst = list(set(lst))
    unique_lst.sort()
    return unique_lst[-2]

def find_second_smallest(lst):
    if len(lst) < 2:
        return None
    unique_lst = list(set(lst))
    unique_lst.sort()
    return unique_lst[1]

def is_pangram(s):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    return alphabet <= set(s.lower())

def count_capital_letters(s):
    return sum(1 for char in s if char.isupper())

def count_lowercase_letters(s):
    return sum(1 for char in s if char.islower())

def generate_primes_up_to(n):
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def generate_combinations(lst, r):
    from itertools import combinations
    return list(combinations(lst, r))

def generate_permutations(lst, r):
    from itertools import permutations
    return list(permutations(lst, r))

def generate_all_subsets(s):
    from itertools import chain, combinations
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s) + 1)))

def calculate_hypotenuse(a, b):
    return (a ** 2 + b ** 2) ** 0.5

def calculate_perimeter_of_rectangle(length, width):
    return 2 * (length + width)

def calculate_area_of_rectangle(length, width):
    return length * width

def calculate_volume_of_cylinder(radius, height):
    from math import pi
    return pi * radius ** 2 * height

def calculate_surface_area_of_cylinder(radius, height):
    from math import pi
    return 2 * pi * radius * (radius + height)

def find_most_frequent_element(lst):
    from collections import Counter
    return Counter(lst).most_common(1)[0][0]

def find_least_frequent_element(lst):
    from collections import Counter
    return Counter(lst).most_common()[-1][0]

def convert_to_title_case(s):
    return s.title()

def check_if_isogram(s):
    s = s.lower().replace(" ", "")
    return len(s) == len(set(s))

def calculate_compound_interest(principal, rate, time, n):
    return principal * (1 + rate / n) ** (n * time)

def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def convert_to_uppercase(s):
    return s.upper()

def convert_to_lowercase(s):
    return s.lower()

def reverse_list(lst):
    return lst[::-1]

def sum_of_list(lst):
    return sum(lst)

def product_of_list(lst):
    product = 1
    for num in lst:
        product *= num
    return product

def remove_element(lst, element):
    return [x for x in lst if x != element]

def is_sublist(lst1, lst2):
    return all(item in lst2 for item in lst1)

def count_substring_occurrences(s, substring):
    return s.count(substring)

def calculate_standard_deviation(lst):
    from statistics import stdev
    return stdev(lst)

def calculate_variance(lst):
    from statistics import variance
    return variance(lst)

def calculate_mean(lst):
    from statistics import mean
    return mean(lst)

def calculate_harmonic_mean(lst):
    from statistics import harmonic_mean
    return harmonic_mean(lst)

def calculate_geometric_mean(lst):
    from statistics import geometric_mean
    return geometric_mean(lst)

def check_if_all_elements_are_unique(lst):
    return len(lst) == len(set(lst))

def find_element_index(lst, element):
    return lst.index(element) if element in lst else -1

def to_base64(s):
    from base64 import b64encode
    return b64encode(s.encode()).decode()

def from_base64(s):
    from base64 import b64decode
    return b64decode(s).decode()

def convert_decimal_to_binary(decimal):
    return bin(decimal)[2:]

def convert_decimal_to_hex(decimal):
    return hex(decimal)[2:]

def convert_decimal_to_octal(decimal):
    return oct(decimal)[2:]

def calculate_euclidean_distance(point1, point2):
    return sum((a - b) ** 2 for a, b in zip(point1, point2)) ** 0.5

def calculate_manhattan_distance(point1, point2):
    return sum(abs(a - b) for a, b in zip(point1, point2))

def calculate_chebyshev_distance(point1, point2):
    return max(abs(a - b) for a, b in zip(point1, point2))

def calculate_jaccard_similarity(set1, set2):
    return len(set1 & set2) / len(set1 | set2)

def calculate_cosine_similarity(vec1, vec2):
    from numpy import dot
    from numpy.linalg import norm
    return dot(vec1, vec2) / (norm(vec1) * norm(vec2))

def find_median_of_two_sorted_arrays(arr1, arr2):
    from heapq import merge
    merged = list(merge(arr1, arr2))
    n = len(merged)
    mid = n // 2
    if n % 2 == 0:
        return (merged[mid - 1] + merged[mid]) / 2
    else:
        return merged[mid]

def is_valid_parentheses(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack

def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while s.find(prefix) != 0:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

def is_balanced_binary_tree(root):
    def height(node):
        if not node:
            return 0
        left_height = height(node.left)
        right_height = height(node.right)
        if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) + 1
    
    return height(root) != -1
