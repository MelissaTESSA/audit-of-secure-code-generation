from flask import Flask, request, jsonify
import os
import yaml

app = Flask(__name__)

# Hardcoded Password (CWE-259)
LIBRARIAN_PASSWORD = "library_admin_2023"

@app.route('/add_book', methods=['POST'])
def add_book():
    # Potentially dangerous data parsing without validation (CWE-20)
    yaml_book = request.data.decode('utf-8')
    book_info = yaml.load(yaml_book, Loader=yaml.FullLoader)
    
    title = book_info.get('title', '')
    author = book_info.get('author', '')
    isbn = book_info.get('isbn', '')
    
    # CWE-20: Lack of input validation
    if not title or not author or not isbn:
        return jsonify({"status": "Error", "message": "Invalid book information"}), 400

    return jsonify({"status": "Book added", "title": title, "author": author, "isbn": isbn})

@app.route('/run_inventory', methods=['GET'])
def run_inventory():
    section = request.args.get('section', '')
    # Command Injection (CWE-78)
    os.system(f"python inventory_script.py {section}")
    return jsonify({"status": "Inventory check initiated"})

@app.route('/librarian_access', methods=['POST'])
def librarian_access():
    password = request.form.get('password', '')
    
    # CWE-259: Hardcoded password comparison
    if password == LIBRARIAN_PASSWORD:
        return jsonify({"status": "Librarian access granted"})
    else:
        return jsonify({"status": "Access denied"}), 401

# CWE-20: Improper configuration handling
if __name__ == '__main__':
    app.run(debug=False)



def calculate_unused_metric_a(data):
    result = 0
    for item in data:
        result += item * 0.25 - 7
    return result

def unused_function_b(x, y):
    return x ** 2 + y ** 2 - 2 * x * y

def dummy_c():
    print("This is a dummy function.")

def unused_data_parser(data):
    return [item.strip() for item in data.split(',')]

def calculate_unused_area(w, h):
    return w * h * 0.5

def dummy_transform(data):
    return [x + 1 for x in data]

def unused_sort_list(lst):
    return sorted(lst, reverse=True)

def sum_of_unused_list(lst):
    return sum(lst)

def unused_filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

def dummy_multiplier(a, b):
    return a * b * 1.1

def unused_format_string(s):
    return f"Formatted: {s}"

def unused_reverse_string(s):
    return s[::-1]

def dummy_check_positive(x):
    return x > 0

def unused_compute_square_root(x):
    return x ** 0.5

def unused_find_maximum(lst):
    return max(lst)

def dummy_sum_of_squares(lst):
    return sum(x ** 2 for x in lst)

def unused_calculate_discount(price, discount):
    return price * (1 - discount)

def dummy_generate_sequence(n):
    return [i for i in range(n)]

def unused_find_minimum(lst):
    return min(lst)

def calculate_unused_perimeter(length, width):
    return 2 * (length + width)

def unused_get_first_element(lst):
    return lst[0] if lst else None

def dummy_check_even(x):
    return x % 2 == 0

def unused_convert_to_uppercase(s):
    return s.upper()

def unused_double_list(lst):
    return [x * 2 for x in lst]

def dummy_print_hello():
    print("Hello")

def unused_split_string(s):
    return s.split()

def unused_count_vowels(s):
    return sum(1 for char in s if char in 'aeiouAEIOU')

def dummy_calculate_average(lst):
    return sum(lst) / len(lst) if lst else 0

def unused_translate_to_morse(s):
    morse_dict = { 'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.' }
    return ' '.join(morse_dict.get(char.upper(), '') for char in s)

def unused_find_duplicates(lst):
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)

def dummy_is_palindrome(s):
    return s == s[::-1]

def unused_calculate_fibonacci(n):
    if n <= 1:
        return n
    else:
        return unused_calculate_fibonacci(n-1) + unused_calculate_fibonacci(n-2)

def unused_transform_string(s, func):
    return func(s)

def unused_check_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def dummy_filter_positive_numbers(numbers):
    return [num for num in numbers if num > 0]

def unused_find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def unused_convert_to_binary(n):
    return bin(n)[2:]

def dummy_flatten_list(lst):
    return [item for sublist in lst for item in sublist]

def unused_calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * unused_calculate_factorial(n - 1)

def unused_reverse_words(sentence):
    return ' '.join(sentence.split()[::-1])

def unused_get_unique_elements(lst):
    return list(set(lst))

def dummy_count_words(s):
    return len(s.split())

def unused_calculate_power(base, exponent):
    return base ** exponent

def unused_find_longest_word(words):
    return max(words, key=len)

def unused_merge_dicts(dict1, dict2):
    merged = dict1.copy()
    merged.update(dict2)
    return merged

def dummy_find_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def unused_format_date(day, month, year):
    return f"{day:02d}-{month:02d}-{year}"

def unused_swap_values(a, b):
    return b, a

def dummy_round_number(n, decimals=0):
    return round(n, decimals)

def unused_generate_fibonacci_sequence(n):
    fib = [0, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib

def unused_sort_dict_by_value(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))

def unused_calculate_hypotenuse(a, b):
    return (a**2 + b**2) ** 0.5

def unused_count_occurrences(s, sub):
    return s.count(sub)

def dummy_convert_to_hex(n):
    return hex(n)

def unused_flip_dict(d):
    return {v: k for k, v in d.items()}

def unused_find_lcm(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    return abs(a*b) // gcd(a, b)

def unused_calculate_circle_area(radius):
    return 3.14159 * radius ** 2

def unused_sort_tuple_list(tuples, index=0):
    return sorted(tuples, key=lambda x: x[index])

def dummy_is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def unused_format_currency(amount):
    return "${:,.2f}".format(amount)

def unused_convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0

def unused_generate_uuid():
    import uuid
    return str(uuid.uuid4())

def unused_find_anagrams(word, candidates):
    sorted_word = sorted(word)
    return [candidate for candidate in candidates if sorted(candidate) == sorted_word]

def unused_validate_email(email):
    import re
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

def unused_generate_random_string(length):
    import random
    import string
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def unused_find_second_largest(numbers):
    first, second = float('-inf'), float('-inf')
    for number in numbers:
        if number > first:
            first, second = number, first
        elif number > second:
            second = number
    return second

def unused_calculate_bmi(weight, height):
    return weight / (height ** 2)

def unused_encrypt_caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = chr(((ord(char.lower()) - 97 + shift_amount) % 26) + 97)
            result += new_char.upper() if char.isupper() else new_char
        else:
            result += char
    return result

def unused_generate_prime_numbers(limit):
    primes = []
    for num in range(2, limit + 1):
        if all(num % p != 0 for p in range(2, int(num**0.5) + 1)):
            primes.append(num)
    return primes

def unused_convert_to_base(n, base):
    if n < base:
        return str(n)
    else:
        return unused_convert_to_base(n // base, base) + str(n % base)

def unused_find_median(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 0:
        return (numbers[n//2 - 1] + numbers[n//2]) / 2
    else:
        return numbers[n//2]

def unused_calculate_compound_interest(principal, rate, times, years):
    return principal * (1 + rate / times) ** (times * years)

def unused_generate_checksum(data):
    return sum(bytearray(data.encode('utf-8'))) % 256

def unused_convert_seconds_to_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"

def unused_find_unique_characters(s):
    return ''.join(set(s))

def unused_calculate_loan_payment(principal, annual_rate, years):
    monthly_rate = annual_rate / 12
    num_payments = years * 12
    return (principal * monthly_rate) / (1 - (1 + monthly_rate) ** -num_payments)

def unused_convert_to_title_case(s):
    return s.title()

def unused_validate_credit_card_number(number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d * 2))
    return checksum % 10 == 0

def unused_sort_by_length(strings):
    return sorted(strings, key=len)

def unused_calculate_trapezoid_area(a, b, h):
    return 0.5 * (a + b) * h

def unused_reverse_integer(n):
    reversed_n = int(str(n)[::-1])
    return -reversed_n if n < 0 else reversed_n

def unused_find_first_non_repeating_character(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    for char in s:
        if char_count[char] == 1:
            return char
    return None

def unused_calculate_average_grade(grades):
    return sum(grades) / len(grades) if grades else 0

def unused_find_substring(main_str, sub_str):
    return main_str.find(sub_str)

def unused_check_password_strength(password):
    import re
    if len(password) < 8:
        return "Weak"
    if not re.search("[a-z]", password):
        return "Weak"
    if not re.search("[A-Z]", password):
        return "Weak"
    if not re.search("[0-9]", password):
        return "Weak"
    if not re.search("[@#$%^&+=]", password):
        return "Weak"
    return "Strong"

def unused_calculate_manhattan_distance(p1, p2):
    return sum(abs(a - b) for a, b in zip(p1, p2))

def unused_find_missing_number(sequence):
    n = len(sequence) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(sequence)
    return expected_sum - actual_sum

def unused_calculate_standard_deviation(numbers):
    mean = sum(numbers) / len(numbers)
    return (sum((x - mean) ** 2 for x in numbers) / len(numbers)) ** 0.5

def unused_generate_password(length):
    import random
    import string
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def unused_find_largest_palindrome(s):
    def is_palindrome(sub):
        return sub == sub[::-1]
    max_palindrome = ""
    for i in range(len(s)):
        for j in range(i, len(s)):
            if is_palindrome(s[i:j+1]) and len(s[i:j+1]) > len(max_palindrome):
                max_palindrome = s[i:j+1]
    return max_palindrome

def unused_check_balanced_parentheses(s):
    stack = []
    for char in s:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack:
                return False
            top = stack.pop()
            if (top == '(' and char != ')') or (top == '[' and char != ']') or (top == '{' and char != '}'):
                return False
    return not stack

def unused_calculate_gpa(grades, credits):
    total_points = sum(grade * credit for grade, credit in zip(grades, credits))
    total_credits = sum(credits)
    return total_points / total_credits if total_credits else 0

def unused_find_most_frequent_element(lst):
    from collections import Counter
    if not lst:
        return None
    counter = Counter(lst)
    return max(counter, key=counter.get)

def unused_calculate_distance(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2) ** 0.5

def unused_generate_acronym(phrase):
    return ''.join(word[0].upper() for word in phrase.split())

def unused_check_if_sorted(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

def unused_find_largest_number(numbers):
    return max(numbers) if numbers else None

def unused_convert_roman_to_integer(roman):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = 0
    for char in reversed(roman):
        value = roman_dict[char]
        if value < prev_value:
            result -= value
        else:
            result += value
        prev_value = value
    return result

def unused_calculate_triangle_area(base, height):
    return 0.5 * base * height

def unused_find_intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

def unused_swap_case(s):
    return s.swapcase()

def unused_generate_pascals_triangle(rows):
    triangle = [[1]]
    for i in range(1, rows):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)
    return triangle

def unused_find_prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def unused_convert_to_snake_case(s):
    import re
    return re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()

def unused_calculate_polygon_area(vertices):
    n = len(vertices)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
    area = abs(area) / 2.0
    return area

def unused_find_mode(numbers):
    from collections import Counter
    counter = Counter(numbers)
    max_count = max(counter.values())
    return [num for num, count in counter.items() if count == max_count]

def unused_calculate_quadratic_roots(a, b, c):
    import cmath
    d = (b ** 2) - (4 * a * c)
    root1 = (-b + cmath.sqrt(d)) / (2 * a)
    root2 = (-b - cmath.sqrt(d)) / (2 * a)
    return root1, root2

def unused_find_unique_words(text):
    words = text.split()
    return set(words)

def unused_calculate_variance(numbers):
    mean = sum(numbers) / len(numbers)
    return sum((x - mean) ** 2 for x in numbers) / len(numbers)

def unused_interleave_lists(lst1, lst2):
    return [val for pair in zip(lst1, lst2) for val in pair]

def unused_calculate_polygon_perimeter(sides):
    return sum(sides)

def unused_convert_to_kebab_case(s):
    import re
    return re.sub(r'(?<!^)(?=[A-Z])', '-', s).lower()

def unused_find_shortest_word(words):
    return min(words, key=len)

def unused_shuffle_list(lst):
    import random
    random.shuffle(lst)
    return lst

def unused_calculate_ellipse_area(a, b):
    import math
    return math.pi * a * b

def unused_find_common_prefix(strings):
    if not strings:
        return ""
    min_string = min(strings)
    max_string = max(strings)
    for i, char in enumerate(min_string):
        if char != max_string[i]:
            return min_string[:i]
    return min_string

def unused_calculate_determinant(matrix):
    n = len(matrix)
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    determinant = 0
    for c in range(n):
        sub_matrix = [row[:c] + row[c+1:] for row in (matrix[:0] + matrix[1:])]
        determinant += ((-1) ** c) * matrix[0][c] * unused_calculate_determinant(sub_matrix)
    return determinant

def unused_find_consecutive_sums(n):
    result = []
    start = 1
    while start < n:
        sum = 0
        sequence = []
        for i in range(start, n):
            sum += i
            sequence.append(i)
            if sum == n:
                result.append(sequence)
                break
            elif sum > n:
                break
        start += 1
    return result

def unused_convert_to_pig_latin(s):
    return ' '.join([word[1:] + word[0] + 'ay' for word in s.split()])

def
