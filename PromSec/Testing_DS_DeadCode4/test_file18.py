from flask import Flask, request, jsonify
import os
import yaml

app = Flask(__name__)

SUPER_SECRET_KEY = "1234_secret_key_5678"

@app.route('/process_order', methods=['POST'])
def process_order():
    yaml_order = request.data.decode('utf-8')
    order_data = yaml.load(yaml_order)
    
    product_id = order_data['product_id']
    quantity = order_data['quantity']
    shipping_address = order_data['shipping_address']
    
    return jsonify({"status": "Order processed", 
                    "product": product_id, 
                    "quantity": quantity,
                    "shipping_to": shipping_address})

@app.route('/generate_invoice', methods=['GET'])
def generate_invoice():
    order_id = request.args.get('id', '')
    os.system(f"./invoice_generator {order_id}")
    return jsonify({"status": "Invoice generation initiated"})

@app.route('/admin_panel', methods=['POST'])
def admin_panel():
    provided_key = request.form.get('key', '')
    
    if provided_key == SUPER_SECRET_KEY:
        return jsonify({"status": "Admin access granted"})
    else:
        return jsonify({"status": "Access denied"}), 401

@app.route('/update_inventory', methods=['POST'])
def update_inventory():
    yaml_inventory = request.data.decode('utf-8')
    inventory_data = yaml.load(yaml_inventory)
    return jsonify({"status": "Inventory updated", 
                    "new_inventory": inventory_data})

if __name__ == '__main__':
    app.run(debug=False)


def calculate_discount(price, discount_rate):
    discounted_price = price - (price * discount_rate / 100)
    return discounted_price

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def find_maximum(numbers):
    if not numbers:
        return None
    max_number = numbers[0]
    for num in numbers:
        if num > max_number:
            max_number = num
    return max_number

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def reverse_string(s):
    return s[::-1]

def calculate_area_of_circle(radius):
    pi = 3.14159
    return pi * radius * radius

def fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def is_palindrome(s):
    return s == s[::-1]

def flatten_list(nested_list):
    flat_list = []
    for sublist in nested_list:
        for item in sublist:
            flat_list.append(item)
    return flat_list

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a*b) // gcd(a, b)

def merge_dicts(dict1, dict2):
    result = dict1.copy()
    result.update(dict2)
    return result

def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def generate_random_string(length):
    import string, random
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def sort_numbers(numbers):
    return sorted(numbers)

def transpose_matrix(matrix):
    return list(map(list, zip(*matrix)))

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def find_unique_elements(lst):
    return list(set(lst))

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def calculate_power(base, exponent):
    return base ** exponent

def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

def get_file_extension(filename):
    return filename.split('.')[-1]

def rotate_list(lst, k):
    k = k % len(lst)
    return lst[-k:] + lst[:-k]

def find_intersection(list1, list2):
    return list(set(list1) & set(list2))

def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 1:
        return sorted_numbers[n // 2]
    else:
        mid1 = n // 2
        mid2 = mid1 - 1
        return (sorted_numbers[mid1] + sorted_numbers[mid2]) / 2

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

def calculate_mode(numbers):
    from collections import Counter
    frequency = Counter(numbers)
    mode = frequency.most_common(1)
    return mode[0][0] if mode else None

def generate_fibonacci_until(n):
    sequence = [0, 1]
    while sequence[-1] < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:-1]

def get_unique_words(text):
    words = text.split()
    return set(words)

def calculate_sum_of_squares(n):
    return sum(i**2 for i in range(1, n+1))

def remove_whitespace(s):
    return s.replace(' ', '')

def find_greatest_difference(numbers):
    if not numbers:
        return 0
    return max(numbers) - min(numbers)

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def get_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

def merge_sorted_lists(list1, list2):
    result = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    result.extend(list1[i:])
    result.extend(list2[j:])
    return result

def calculate_hypotenuse(a, b):
    return (a**2 + b**2) ** 0.5

def is_substring(s1, s2):
    return s1 in s2

def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def find_first_repeating_element(lst):
    seen = set()
    for item in lst:
        if item in seen:
            return item
        seen.add(item)
    return None

def count_occurrences(lst, element):
    return lst.count(element)

def check_brackets_balance(s):
    stack = []
    for char in s:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack:
                return False
            top = stack.pop()
            if not ((top == '(' and char == ')') or
                    (top == '{' and char == '}') or
                    (top == '[' and char == ']')):
                return False
    return not stack

def convert_to_binary(n):
    return bin(n)[2:]

def reverse_words(sentence):
    words = sentence.split()
    return ' '.join(reversed(words))

def find_smallest_missing_positive(nums):
    nums = [num for num in nums if num > 0]
    nums.sort()
    smallest_missing = 1
    for num in nums:
        if num == smallest_missing:
            smallest_missing += 1
    return smallest_missing

def is_perfect_square(n):
    return int(n**0.5) ** 2 == n

def find_longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

def find_factors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def is_valid_palindrome(s):
    alphanumeric_s = ''.join(char for char in s if char.isalnum()).lower()
    return alphanumeric_s == alphanumeric_s[::-1]

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def is_armstrong_number(n):
    num_str = str(n)
    num_len = len(num_str)
    return n == sum(int(digit) ** num_len for digit in num_str)

def convert_to_uppercase(s):
    return s.upper()

def generate_multiplication_table(n, up_to=10):
    return [n * i for i in range(1, up_to + 1)]

def is_even(number):
    return number % 2 == 0

def is_odd(number):
    return number % 2 != 0

def convert_to_lowercase(s):
    return s.lower()

def square_numbers(numbers):
    return [num ** 2 for num in numbers]

def cube_numbers(numbers):
    return [num ** 3 for num in numbers]

def remove_vowels(s):
    vowels = "aeiouAEIOU"
    return ''.join(char for char in s if char not in vowels)

def count_consonants(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char.isalpha() and char not in vowels)

def calculate_permutation(n, r):
    return factorial_iterative(n) // factorial_iterative(n - r)

def calculate_combination(n, r):
    return factorial_iterative(n) // (factorial_iterative(r) * factorial_iterative(n - r))

def find_second_largest(numbers):
    first, second = float('-inf'), float('-inf')
    for number in numbers:
        if number > first:
            first, second = number, first
        elif first > number > second:
            second = number
    return second

def convert_list_to_string(lst):
    return ''.join(map(str, lst))

def remove_punctuation(s):
    import string
    return s.translate(str.maketrans('', '', string.punctuation))

def generate_prime_numbers(n):
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def reverse_integer(n):
    sign = -1 if n < 0 else 1
    reversed_n = int(str(abs(n))[::-1])
    return sign * reversed_n

def calculate_sum_of_naturals(n):
    return n * (n + 1) // 2

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def find_most_frequent_element(lst):
    from collections import Counter
    frequency = Counter(lst)
    most_common = frequency.most_common(1)
    return most_common[0][0] if most_common else None

def convert_inches_to_centimeters(inches):
    return inches * 2.54

def calculate_time_difference(start, end):
    from datetime import datetime
    fmt = '%H:%M:%S'
    tdelta = datetime.strptime(end, fmt) - datetime.strptime(start, fmt)
    return tdelta

def replace_spaces_with_underscore(s):
    return s.replace(' ', '_')

def calculate_total_price(prices):
    return sum(prices)

def reverse_list(lst):
    return lst[::-1]

def get_divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

def calculate_circle_circumference(radius):
    pi = 3.14159
    return 2 * pi * radius

def find_all_substrings(s):
    return [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]

def calculate_daily_interest(principal, rate, days):
    return principal * (rate / 100) * (days / 365)

def find_missing_number(nums):
    n = len(nums) + 1
    total = n * (n + 1) // 2
    return total - sum(nums)

def is_pangram(s):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    return set(s.lower()) >= alphabet

def count_words(s):
    return len(s.split())

def calculate_speed(distance, time):
    return distance / time

def is_subsequence(s1, s2):
    it = iter(s2)
    return all(char in it for char in s1)

def calculate_annual_salary(hourly_wage, hours_per_week):
    return hourly_wage * hours_per_week * 52

def calculate_deposit_amount(principal, rate, time):
    return principal * (1 + rate / 100) ** time

def calculate_grade_percentage(marks_obtained, total_marks):
    return (marks_obtained / total_marks) * 100

def count_occurrences_of_char(s, char):
    return s.count(char)

def calculate_trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height

def find_longest_common_prefix(strings):
    if not strings:
        return ""
    shortest = min(strings, key=len)
    for i, char in enumerate(shortest):
        for other in strings:
            if other[i] != char:
                return shortest[:i]
    return shortest

def get_ascii_value(char):
    return ord(char)

def find_second_smallest(numbers):
    first, second = float('inf'), float('inf')
    for number in numbers:
        if number < first:
            first, second = number, first
        elif first < number < second:
            second = number
    return second

def calculate_emi(principal, rate, time):
    rate = rate / (12 * 100)
    time = time * 12
    emi = (principal * rate * (1 + rate) ** time) / ((1 + rate) ** time - 1)
    return emi

def convert_kilometers_to_miles(km):
    return km * 0.621371

def convert_miles_to_kilometers(miles):
    return miles / 0.621371

def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def check_if_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0
