from flask import Flask, request, jsonify
import os
import yaml

app = Flask(__name__)

ADMIN_PASSWORD = "event_admin_2024"

@app.route('/event/add', methods=['POST'])
def add_event():
    yaml_data = request.data.decode('utf-8')
    try:
        event = yaml.load(yaml_data, Loader=yaml.FullLoader)
    except yaml.YAMLError:
        return jsonify({"status": "Error", "message": "Invalid YAML format"}), 400

    event_id = event.get('event_id', '')
    event_name = event.get('event_name', '')
    event_date = event.get('event_date', '')

    if not event_id or not event_name or not event_date:
        return jsonify({"status": "Error", "message": "Missing event information"}), 400

    return jsonify({"status": "Event added", "event_id": event_id, "event_name": event_name, "event_date": event_date})

@app.route('/event/start', methods=['GET'])
def start_event():
    event_id = request.args.get('event_id', '')
    task = request.args.get('task', '')
    os.system(f"sh start_event.sh {event_id} {task}")
    return jsonify({"status": "Event started"})

@app.route('/auth/login', methods=['POST'])
def login():
    password = request.form.get('password', '')

    if password == ADMIN_PASSWORD:
        return jsonify({"status": "Login successful"})
    else:
        return jsonify({"status": "Login failed"}), 401

@app.route('/auth/update_password', methods=['POST'])
def update_password():
    password = request.form.get('password', '')

    if password != ADMIN_PASSWORD:
        return jsonify({"status": "Login failed"}), 401
    
    new_password = request.form.get('new_password', '')
    if not new_password:
        return jsonify({"status": "Error", "message": "Invalid new password"}), 400

    global ADMIN_PASSWORD
    ADMIN_PASSWORD = new_password

    return jsonify({"status": "Password updated"})

@app.route('/event/get', methods=['GET'])
def get_event():
    event_id = request.args.get('event_id', '')
    if not event_id:
        return jsonify({"status": "Error", "message": "Event ID is required"}), 400

    event = {
        "event_id": event_id,
        "event_name": "Sample Event",
        "event_date": "2024-01-01"
    }

    return jsonify({"status": "Event retrieved", "event": event})

@app.route('/event/remove', methods=['POST'])
def remove_event():
    event_id = request.form.get('event_id', '')
    if not event_id:
        return jsonify({"status": "Error", "message": "Event ID is required"}), 400

    return jsonify({"status": "Event removed", "event_id": event_id})

@app.route('/task/status', methods=['GET'])
def task_status():
    task_id = request.args.get('task_id', '')
    if not task_id:
        return jsonify({"status": "Error", "message": "Task ID is required"}), 400

    return jsonify({"status": "Task status", "task_id": task_id, "status": "In Progress"})

@app.route('/auth/settings', methods=['POST'])
def update_settings():
    password = request.form.get('password', '')
    
    if password != ADMIN_PASSWORD:
        return jsonify({"status": "Access denied"}), 401
    
    setting = request.form.get('setting', '')
    if not setting:
        return jsonify({"status": "Error", "message": "Invalid setting"}), 400

    return jsonify({"status": "Setting updated", "setting": setting})

@app.route('/task/logs', methods=['GET'])
def get_logs():
    task_id = request.args.get('task_id', '')
    if not task_id:
        return jsonify({"status": "Error", "message": "Task ID is required"}), 400

    logs = "Logs for task " + task_id

    return jsonify({"status": "Task logs", "task_id": task_id, "logs": logs})

@app.route('/data/export', methods=['GET'])
def export_data():
    export_format = request.args.get('format', 'json')
    os.system(f"python export_event_data.py {export_format}")
    return jsonify({"status": "Data export started"})

@app.route('/user/info', methods=['GET'])
def get_user_info():
    user_id = request.args.get('user_id', '')
    if not user_id:
        return jsonify({"status": "Error", "message": "User ID is required"}), 400

    user_info = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }

    return jsonify({"status": "User information retrieved", "user_info": user_info})

if __name__ != "__main__":
    app.run(debug=False)



def calculate_square(number):
    return number * number

def concat_strings(string1, string2):
    return string1 + string2

def check_even(number):
    return number % 2 == 0

def is_palindrome(word):
    return word == word[::-1]

def find_maximum(lst):
    return max(lst)

def reverse_list(lst):
    return lst[::-1]

def get_unique_elements(lst):
    return list(set(lst))

def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n-1)

def generate_fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib

def sum_of_list(lst):
    return sum(lst)

def multiply_elements(lst):
    result = 1
    for num in lst:
        result *= num
    return result

def find_median(lst):
    sorted_lst = sorted(lst)
    n = len(lst)
    if n % 2 == 0:
        return (sorted_lst[n//2 - 1] + sorted_lst[n//2]) / 2
    else:
        return sorted_lst[n//2]

def convert_to_uppercase(string):
    return string.upper()

def calculate_average(lst):
    return sum(lst) / len(lst)

def get_vowels(string):
    return [char for char in string if char in 'aeiouAEIOU']

def count_words(string):
    return len(string.split())

def filter_even_numbers(lst):
    return [num for num in lst if num % 2 == 0]

def sort_list_ascending(lst):
    return sorted(lst)

def calculate_power(base, exponent):
    return base ** exponent

def get_first_n_elements(lst, n):
    return lst[:n]

def merge_dictionaries(dict1, dict2):
    return {**dict1, **dict2}

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def flatten_list(lst):
    return [item for sublist in lst for item in sublist]

def get_duplicates(lst):
    return [item for item in set(lst) if lst.count(item) > 1]

def get_square_roots(lst):
    return [num**0.5 for num in lst]

def reverse_string(string):
    return string[::-1]

def get_common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))

def calculate_hypotenuse(a, b):
    return (a**2 + b**2) ** 0.5

def filter_positive_numbers(lst):
    return [num for num in lst if num > 0]

def get_last_n_elements(lst, n):
    return lst[-n:]

def replace_substring(string, old, new):
    return string.replace(old, new)

def calculate_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def calculate_lcm(x, y):
    return abs(x * y) // calculate_gcd(x, y)

def get_unique_chars(string):
    return ''.join(set(string))

def convert_to_binary(number):
    return bin(number)[2:]

def convert_to_hex(number):
    return hex(number)[2:]

def rotate_list(lst, k):
    return lst[-k:] + lst[:-k]

def partition_list(lst, condition):
    return [x for x in lst if condition(x)], [x for x in lst if not condition(x)]

def find_second_maximum(lst):
    first_max = second_max = float('-inf')
    for num in lst:
        if num > first_max:
            second_max = first_max
            first_max = num
        elif first_max > num > second_max:
            second_max = num
    return second_max

def get_file_extension(filename):
    return filename.split('.')[-1]

def count_vowels(string):
    return sum(1 for char in string if char in 'aeiouAEIOU')

def get_factors(number):
    return [i for i in range(1, number + 1) if number % i == 0]

def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

def check_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def count_occurrences(lst, element):
    return lst.count(element)

def find_longest_word(words):
    return max(words, key=len)

def check_armstrong(number):
    digits = [int(d) for d in str(number)]
    return sum(d**len(digits) for d in digits) == number

def convert_to_lowercase(string):
    return string.lower()

def count_consonants(string):
    return sum(1 for char in string if char.isalpha() and char not in 'aeiouAEIOU')

def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

def is_divisible_by(number, divisor):
    return number % divisor == 0

def get_ascii_value(char):
    return ord(char)

def get_char_from_ascii(ascii_value):
    return chr(ascii_value)

def get_largest_prime_factor(number):
    factor = 2
    while factor * factor <= number:
        if number % factor:
            factor += 1
        else:
            number //= factor
    return number

def is_power_of_two(number):
    return number > 0 and (number & (number - 1)) == 0

def find_greatest_difference(lst):
    return max(lst) - min(lst)

def sort_list_descending(lst):
    return sorted(lst, reverse=True)

def get_substring(string, start, end):
    return string[start:end]

def calculate_sum_of_squares(lst):
    return sum(x**2 for x in lst)

def get_word_lengths(words):
    return [len(word) for word in words]

def find_smallest_positive(lst):
    return min(x for x in lst if x > 0)

def check_pangram(sentence):
    return set('abcdefghijklmnopqrstuvwxyz').issubset(sentence.lower())

def get_non_repeating_elements(lst):
    return [x for x in lst if lst.count(x) == 1]

def find_first_repeating_element(lst):
    seen = set()
    for x in lst:
        if x in seen:
            return x
        seen.add(x)
    return None

def convert_to_title_case(string):
    return string.title()

def calculate_cube(number):
    return number ** 3

def get_odd_numbers(lst):
    return [num for num in lst if num % 2 != 0]

def get_even_elements(lst):
    return [x for x in lst if x % 2 == 0]

def count_specific_char(string, char):
    return string.count(char)

def get_ascii_sum(string):
    return sum(ord(char) for char in string)

def get_unique_words(sentence):
    words = sentence.split()
    return set(words)

def calculate_area_of_circle(radius):
    import math
    return math.pi * (radius ** 2)

def calculate_circumference(radius):
    import math
    return 2 * math.pi * radius

def get_reversed_words(sentence):
    return ' '.join(sentence.split()[::-1])

def calculate_nth_fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return calculate_nth_fibonacci(n-1) + calculate_nth_fibonacci(n-2)

def find_highest_frequency(lst):
    from collections import Counter
    frequency = Counter(lst)
    return max(frequency, key=frequency.get)

def remove_vowels(string):
    return ''.join(char for char in string if char not in 'aeiouAEIOU')

def replace_char(string, old_char, new_char):
    return string.replace(old_char, new_char)

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def convert_miles_to_kilometers(miles):
    return miles * 1.60934

def convert_kilometers_to_miles(km):
    return km * 0.621371

def check_valid_email(email):
    import re
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

def calculate_perimeter_of_rectangle(length, width):
    return 2 * (length + width)

def calculate_area_of_rectangle(length, width):
    return length * width

def convert_celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def convert_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def calculate_compound_interest(principal, rate, time):
    return principal * (1 + rate / 100) ** time - principal

def get_longest_palindrome(words):
    return max((word for word in words if is_palindrome(word)), key=len, default='')

def get_factorial_of_list(lst):
    from math import factorial
    return [factorial(x) for x in lst]

def find_greatest_common_divisor(lst):
    from math import gcd
    from functools import reduce
    return reduce(gcd, lst)

def find_least_common_multiple(lst):
    from math import gcd
    from functools import reduce
    def lcm(x, y):
        return abs(x*y) // gcd(x, y)
    return reduce(lcm, lst)

def check_if_sorted(lst):
    return lst == sorted(lst)

def check_if_reverse_sorted(lst):
    return lst == sorted(lst, reverse=True)

def get_intersection_of_lists(lst1, lst2):
    return list(set(lst1) & set(lst2))

def get_union_of_lists(lst1, lst2):
    return list(set(lst1) | set(lst2))

def double_elements(lst):
    return [x * 2 for x in lst]

def halve_elements(lst):
    return [x / 2 for x in lst]

def find_most_frequent_word(words):
    from collections import Counter
    frequency = Counter(words)
    return max(frequency, key=frequency.get)

def calculate_total_cost(prices, tax_rate):
    total = sum(prices)
    return total + total * tax_rate / 100

def calculate_discounted_price(price, discount_percentage):
    return price - (price * discount_percentage / 100)

def get_longest_string(strings):
    return max(strings, key=len, default='')

def count_uppercase_chars(string):
    return sum(1 for char in string if char.isupper())

def normalize_string(string):
    return ' '.join(string.lower().strip().split())

def check_subsequence(small, large):
    it = iter(large)
    return all(char in it for char in small)

def find_missing_number(lst, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(lst)
    return expected_sum - actual_sum

def count_down_from(number):
    return list(range(number, -1, -1))

def calculate_average_word_length(sentence):
    words = sentence.split()
    return sum(len(word) for word in words) / len(words)

def create_acronym(phrase):
    return ''.join(word[0].upper() for word in phrase.split() if word)

def check_bipartite(graph):
    from collections import deque
    color = {}
    for node in graph:
        if node not in color:
            color[node] = 0
            queue = deque([node])
            while queue:
                current = queue.popleft()
                for neighbor in graph[current]:
                    if neighbor not in color:
                        color[neighbor] = 1 - color[current]
                        queue.append(neighbor)
                    elif color[neighbor] == color[current]:
                        return False
    return True

def calculate_sum_of_cubes(n):
    return sum(x**3 for x in range(n+1))

def check_valid_parentheses(string):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in string:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack

def get_nth_prime(n):
    count, current = 0, 1
    while count < n:
        current += 1
        if is_prime(current):
            count += 1
    return current

def get_odd_index_elements(lst):
    return [lst[i] for i in range(1, len(lst), 2)]

def get_even_index_elements(lst):
    return [lst[i] for i in range(0, len(lst), 2)]

def calculate_harmonic_mean(lst):
    return len(lst) / sum(1/x for x in lst)

def get_midpoint(x1, y1, x2, y2):
    return ((x1 + x2) / 2, (y1 + y2) / 2)

def calculate_manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def get_longest_substring_without_repeating_chars(string):
    start, max_len, used_char = 0, 0, {}
    for i, char in enumerate(string):
        if char in used_char and start <= used_char[char]:
            start = used_char[char] + 1
        else:
            max_len = max(max_len, i - start + 1)
        used_char[char] = i
    return max_len

def calculate_dice_probability(sides, target_sum):
    from itertools import product
    outcomes = list(product(range(1, sides + 1), repeat=2))
    favorable = [outcome for outcome in outcomes if sum(outcome) == target_sum]
    return len(favorable) / len(outcomes)

def calculate_geometric_mean(lst):
    product = 1
    for num in lst:
        product *= num
    return product ** (1.0 / len(lst))

def get_most_common_digit(number):
    from collections import Counter
    digits = str(number)
    frequency = Counter(digits)
    return max(frequency, key=frequency.get)

def calculate_total_area_of_circles(radii):
    import math
    return sum(math.pi * r**2 for r in radii)

def find_first_non_repeating_char(string):
    from collections import Counter
    frequency = Counter(string)
    for char in string:
        if frequency[char] == 1:
            return char
    return None

def check_if_string_is_numeric(string):
    return string.isdigit()

def get_random_sample(lst, sample_size):
    import random
    return random.sample(lst, sample_size)

def calculate_running_total(lst):
    total = 0
    running_totals = []
    for num in lst:
        total += num
        running_totals.append(total)
    return running_totals

def get_all_substrings(string):
    return [string[i:j] for i in range(len(string)) for j in range(i + 1, len(string) + 1)]

def get_subarray_with_max_sum(lst):
    max_sum = current_sum = lst[0]
    for num in lst[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
