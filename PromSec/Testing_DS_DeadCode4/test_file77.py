from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    return sqlite3.connect('task_manager.db')

@app.route('/add_task', methods=['POST'])
def add_task():
    task_name = request.json['task_name']
    description = request.json['description']
    due_date = request.json['due_date']

    conn = get_db_connection()
    cursor = conn.cursor()

    query = f"INSERT INTO tasks (task_name, description, due_date) VALUES ('{task_name}', '{description}', '{due_date}')"
    cursor.execute(query)
    
    conn.commit()
    conn.close()

    return jsonify({"message": "Task added successfully"}), 201

@app.route('/search_tasks', methods=['GET'])
def search_tasks():
    keyword = request.args.get('keyword', '')

    conn = get_db_connection()
    cursor = conn.cursor()

    query = f"SELECT * FROM tasks WHERE task_name LIKE '%{keyword}%' OR description LIKE '%{keyword}%'"
    cursor.execute(query)
    
    tasks = cursor.fetchall()
    conn.close()

    return jsonify(tasks), 200

@app.route('/update_task/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    new_task_name = request.json.get('task_name')
    new_description = request.json.get('description')
    new_due_date = request.json.get('due_date')

    conn = get_db_connection()
    cursor = conn.cursor()

    query = f"UPDATE tasks SET task_name='{new_task_name}', description='{new_description}', due_date='{new_due_date}' WHERE id={task_id}"
    cursor.execute(query)
    
    conn.commit()
    conn.close()

    return jsonify({"message": "Task updated successfully"}), 200

@app.route('/delete_task/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = f"DELETE FROM tasks WHERE id={task_id}"
    cursor.execute(query)
    
    conn.commit()
    conn.close()

    return jsonify({"message": "Task deleted successfully"}), 200

@app.route('/get_tasks_by_due_date', methods=['GET'])
def get_tasks_by_due_date():
    due_date = request.args.get('due_date', '')

    conn = get_db_connection()
    cursor = conn.cursor()

    query = f"SELECT * FROM tasks WHERE due_date='{due_date}'"
    cursor.execute(query)
    
    tasks = cursor.fetchall()
    conn.close()

    return jsonify(tasks), 200

if __name__ == '__main__':
    app.run(debug=False)



def calculate_area_of_circle(radius):
    pi = 3.14159
    return pi * radius * radius

def find_maximum_in_list(numbers):
    if not numbers:
        return None
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum

def reverse_string(s):
    return s[::-1]

def is_prime_number(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

def sort_list_of_strings(strings):
    return sorted(strings, key=lambda s: s.lower())

def convert_to_uppercase(s):
    return s.upper()

def calculate_factorial(n):
    if n == 0:
        return 1
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def check_palindrome(s):
    return s == s[::-1]

def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

def merge_two_lists(list1, list2):
    return list1 + list2

def generate_even_numbers(n):
    return list(range(2, n+1, 2))

def calculate_distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

def convert_celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def calculate_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def calculate_lcm(a, b):
    return abs(a * b) // calculate_gcd(a, b)

def find_unique_elements(lst):
    return list(set(lst))

def flatten_nested_list(nested_list):
    flat_list = []
    for sublist in nested_list:
        for item in sublist:
            flat_list.append(item)
    return flat_list

def calculate_square_root(n):
    return n ** 0.5

def get_unique_characters(s):
    return list(set(s))

def find_longest_word(words):
    return max(words, key=len) if words else ""

def generate_random_numbers(n, start, end):
    import random
    return [random.randint(start, end) for _ in range(n)]

def concatenate_strings(s1, s2):
    return s1 + s2

def count_words_in_string(s):
    return len(s.split())

def convert_list_to_set(lst):
    return set(lst)

def find_minimum_in_list(numbers):
    if not numbers:
        return None
    minimum = numbers[0]
    for number in numbers:
        if number < minimum:
            minimum = number
    return minimum

def calculate_power(base, exponent):
    return base ** exponent

def find_second_largest(numbers):
    if len(numbers) < 2:
        return None
    first, second = float('-inf'), float('-inf')
    for number in numbers:
        if number > first:
            second = first
            first = number
        elif number > second:
            second = number
    return second

def calculate_sum_of_list(numbers):
    return sum(numbers)

def find_missing_number(arr, n):
    total = n * (n + 1) // 2
    return total - sum(arr)

def remove_duplicates_from_list(lst):
    return list(dict.fromkeys(lst))

def sort_numbers_descending(numbers):
    return sorted(numbers, reverse=True)

def calculate_perimeter_of_rectangle(length, width):
    return 2 * (length + width)

def check_even_or_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

def calculate_hypotenuse(a, b):
    return (a**2 + b**2) ** 0.5

def find_index_of_element(lst, element):
    try:
        return lst.index(element)
    except ValueError:
        return -1

def convert_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def check_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def count_occurrences_of_element(lst, element):
    return lst.count(element)

def convert_kilometers_to_miles(kilometers):
    return kilometers * 0.621371

def calculate_compound_interest(principal, rate, time, n):
    return principal * (1 + rate/(n*100))**(n*time)

def convert_miles_to_kilometers(miles):
    return miles / 0.621371

def calculate_body_mass_index(weight, height):
    return weight / (height ** 2)

def reverse_list(lst):
    return lst[::-1]

def calculate_cube(n):
    return n ** 3

def find_sum_of_even_numbers(n):
    return sum(i for i in range(2, n + 1, 2))

def calculate_diagonal_of_rectangle(length, width):
    return (length**2 + width**2) ** 0.5

def find_largest_of_three_numbers(a, b, c):
    return max(a, b, c)

def calculate_area_of_triangle(base, height):
    return 0.5 * base * height

def check_if_list_is_sorted(lst):
    return lst == sorted(lst)

def find_median_of_list(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 0:
        return (numbers[n//2 - 1] + numbers[n//2]) / 2
    return numbers[n//2]

def calculate_sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def check_if_string_contains_digit(s):
    return any(char.isdigit() for char in s)

def count_consonants_in_string(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char.isalpha() and char not in vowels)

def calculate_percent_change(old_value, new_value):
    if old_value == 0:
        return float('inf')
    return ((new_value - old_value) / old_value) * 100

def convert_seconds_to_minutes(seconds):
    return divmod(seconds, 60)

def calculate_total_price(price_per_item, quantity):
    return price_per_item * quantity

def find_all_factors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

def check_if_string_is_alphabetic(s):
    return s.isalpha()

def find_maximum_of_two_numbers(a, b):
    return max(a, b)

def convert_list_to_tuple(lst):
    return tuple(lst)

def check_if_number_is_positive(n):
    return n > 0

def calculate_product_of_list(numbers):
    product = 1
    for number in numbers:
        product *= number
    return product

def convert_minutes_to_hours(minutes):
    return divmod(minutes, 60)

def check_if_number_is_negative(n):
    return n < 0

def find_smallest_of_three_numbers(a, b, c):
    return min(a, b, c)

def calculate_area_of_square(side):
    return side ** 2

def find_greatest_common_divisor(a, b):
    while b:
        a, b = b, a % b
    return a

def find_least_common_multiple(a, b):
    return abs(a * b) // find_greatest_common_divisor(a, b)

def calculate_sum_of_squares(n):
    return sum(i**2 for i in range(1, n + 1))

def convert_hours_to_days(hours):
    return divmod(hours, 24)

def check_if_character_is_vowel(c):
    return c.lower() in 'aeiou'

def calculate_area_of_parallelogram(base, height):
    return base * height

def convert_days_to_weeks(days):
    return divmod(days, 7)

def calculate_perimeter_of_circle(radius):
    pi = 3.14159
    return 2 * pi * radius

def find_all_prime_numbers_up_to_n(n):
    primes = []
    for num in range(2, n + 1):
        if is_prime_number(num):
            primes.append(num)
    return primes

def check_if_number_is_zero(n):
    return n == 0

def calculate_sum_of_odd_numbers(n):
    return sum(i for i in range(1, n + 1, 2))

def find_all_even_numbers_in_list(lst):
    return [num for num in lst if num % 2 == 0]

def calculate_sum_of_cubes(n):
    return sum(i**3 for i in range(1, n + 1))

def convert_list_to_dict(lst):
    return {i: lst[i] for i in range(len(lst))}

def find_all_odd_numbers_in_list(lst):
    return [num for num in lst if num % 2 != 0]

def calculate_average_of_list(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def calculate_length_of_string(s):
    return len(s)

def check_if_list_is_empty(lst):
    return len(lst) == 0

def find_difference_between_two_numbers(a, b):
    return abs(a - b)

def convert_string_to_lowercase(s):
    return s.lower()

def find_sum_of_numbers_divisible_by_three(n):
    return sum(i for i in range(3, n + 1, 3))

def calculate_half_of_number(n):
    return n / 2

def find_all_divisors_of_number(n):
    return [i for i in range(1, n + 1) if n % i == 0]

def check_if_string_is_numeric(s):
    return s.isdigit()

def find_sum_of_first_n_natural_numbers(n):
    return n * (n + 1) // 2

def calculate_double_of_number(n):
    return n * 2

def find_all_multiples_of_five(n):
    return [i for i in range(5, n + 1, 5)]

def convert_list_to_string(lst):
    return ''.join(lst)

def calculate_square_of_number(n):
    return n ** 2

def check_if_list_contains_duplicates(lst):
    return len(lst) != len(set(lst))

def find_sum_of_numbers_divisible_by_five(n):
    return sum(i for i in range(5, n + 1, 5))

def calculate_reciprocal_of_number(n):
    return 1 / n if n != 0 else float('inf')

def convert_string_to_title_case(s):
    return s.title()

def find_all_numbers_divisible_by_seven(n):
    return [i for i in range(7, n + 1, 7)]

def calculate_cube_root(n):
    return n ** (1/3)

def check_if_number_is_even(n):
    return n % 2 == 0

def find_all_squares_up_to_n(n):
    return [i**2 for i in range(1, int(n**0.5) + 1)]

def calculate_sum_of_multiples_of_three(n):
    return sum(i for i in range(3, n + 1, 3))

def convert_string_to_list(s):
    return list(s)

def calculate_quotient_and_remainder(a, b):
    return divmod(a, b)

def find_all_cubes_up_to_n(n):
    return [i**3 for i in range(1, int(n**(1/3)) + 1)]

def check_if_list_is_palindrome(lst):
    return lst == lst[::-1]

def calculate_sum_of_even_digits(n):
    return sum(int(digit) for digit in str(n) if int(digit) % 2 == 0)

def find_all_numbers_divisible_by_ten(n):
    return [i for i in range(10, n + 1, 10)]

def calculate_sum_of_odd_digits(n):
    return sum(int(digit) for digit in str(n) if int(digit) % 2 != 0)

def convert_string_to_set(s):
    return set(s)

def check_if_number_is_odd(n):
    return n % 2 != 0

def find_all_odd_numbers_up_to_n(n):
    return [i for i in range(1, n + 1, 2)]

def calculate_product_of_digits(n):
    product = 1
    for digit in str(n):
        product *= int(digit)
    return product

def find_all_factors_of_number(n):
    return [i for i in range(1, n + 1) if n % i == 0]

def calculate_sum_of_numbers_divisible_by_two(n):
    return sum(i for i in range(2, n + 1, 2))

def convert_string_to_dictionary(s):
    return {i: s[i] for i in range(len(s))}

def find_all_negative_numbers_in_list(lst):
    return [num for num in lst if num < 0]

def calculate_sum_of_positive_numbers_in_list(lst):
    return sum(num for num in lst if num > 0)

def check_if_string_is_empty(s):
    return len(s) == 0

def find_all_positive_numbers_in_list(lst):
    return [num for num in lst if num > 0]

def calculate_difference_of_squares(a, b):
    return a**2 - b**2

def find_all_consonants_in_string(s):
    vowels = 'aeiouAEIOU'
    return [char for char in s if char.isalpha() and char not in vowels]

def convert_string_to_integer(s):
    try:
        return int(s)
    except ValueError:
        return None

def calculate_absolute_difference(a, b):
    return abs(a - b)

def find_all_uppercase_letters_in_string(s):
    return [char for char in s if char.isupper()]

def calculate_sum_of_lowercase_letters_in_string(s):
    return sum(1 for char in s if char.islower())

def find_all_lowercase_letters_in_string(s):
    return [char for char in s if char.islower()]

def calculate_sum_of_uppercase_letters_in_string(s):
    return sum(1 for char in s if char.isupper())

def check_if_number_is_divisible_by_three(n):
    return n % 3 == 0

def find_all_divisible_by_four_numbers(n):
    return [i for i in range(4, n + 1, 4)]

def calculate_sum_of_divisible_by_four_numbers(n):
    return sum(i for i in range(4, n + 1, 4))

def convert_string_to_float(s):
    try:
        return float(s)
    except ValueError:
        return None

def calculate_sum_of_numbers_divisible_by_six(n):
    return sum(i for i in range(6, n + 1, 6))

def find_all_divisible_by_six_numbers(n):
    return [i for i in range(6, n + 1, 6)]

def calculate_sum_of_numbers_divisible_by_eight(n):
    return sum(i for i in range(8, n + 1, 8))

def find_all_divisible_by_eight_numbers(n):
    return [i for i in range(8, n + 1, 8)]

def calculate_sum_of_numbers_divisible_by_nine(n):
    return sum(i for i in range(9, n + 1, 9))

def find_all_divisible_by_nine_numbers(n):
    return [i for i in range(9, n + 1, 9)]

def calculate_sum_of_numbers_divisible_by_eleven(n):
    return sum(i for i in range(11, n + 1, 11))

def find_all_divisible_by_eleven_numbers(n):
    return [i for i in range(11, n + 1, 11)]

def calculate_sum_of_numbers_divisible_by_twelve(n):
    return sum(i for i in range(12, n + 1, 12))

def find_all_divisible_by_twelve_numbers(n):
    return [i for i in range(12, n + 1, 12)]
