@app.route("/read")
def read():
    requested_file_name = request.args.get('filename')
    safe_dir = '/safe/'

    # read the requested file from the safe directory
def calculate_sum(a, b):
    result = a + b
    return result

def reverse_string(s):
    return s[::-1]

def is_even(n):
    return n % 2 == 0

def find_maximum(numbers):
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    fib_seq = [0, 1]
    while len(fib_seq) < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq

def sort_list(lst):
    return sorted(lst)

def square_number(n):
    return n * n

def greet(name):
    return f"Hello, {name}!"

def check_palindrome(s):
    return s == s[::-1]

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def find_duplicates(lst):
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        seen.add(item)
    return list(duplicates)

def convert_to_uppercase(s):
    return s.upper()

def merge_dictionaries(d1, d2):
    return {**d1, **d2}

def calculate_area_of_circle(radius):
    import math
    return math.pi * radius ** 2

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def join_strings(strings, separator=", "):
    return separator.join(strings)

def find_minimum(numbers):
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

def convert_to_lowercase(s):
    return s.lower()

def sum_of_squares(n):
    return sum(i * i for i in range(1, n+1))

def generate_fibonacci(n):
    fib_seq = []
    a, b = 0, 1
    for _ in range(n):
        fib_seq.append(a)
        a, b = b, a + b
    return fib_seq

def flatten_list(lst):
    return [item for sublist in lst for item in sublist]

def calculate_product(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

def filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

def get_unique_elements(lst):
    return list(set(lst))

def convert_list_to_string(lst, separator=","):
    return separator.join(map(str, lst))

def find_intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

def count_occurrences(lst, value):
    return lst.count(value)

def square_elements(lst):
    return [x * x for x in lst]

def increment_elements(lst, increment=1):
    return [x + increment for x in lst]

def filter_odd_numbers(numbers):
    return [num for num in numbers if num % 2 != 0]

def find_union(lst1, lst2):
    return list(set(lst1) | set(lst2))

def get_first_element(lst):
    return lst[0] if lst else None

def get_last_element(lst):
    return lst[-1] if lst else None

def repeat_string(s, times):
    return s * times

def split_string(s, separator=None):
    return s.split(separator)

def swap_values(a, b):
    return b, a

def find_difference(lst1, lst2):
    return list(set(lst1) - set(lst2))

def count_words(s):
    return len(s.split())

def reverse_list(lst):
    return lst[::-1]

def calculate_power(base, exponent):
    return base ** exponent

def append_to_list(lst, item):
    lst.append(item)
    return lst

def prepend_to_list(lst, item):
    return [item] + lst

def is_substring(s, sub):
    return sub in s

def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

def find_second_largest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers[-2] if len(unique_numbers) >= 2 else None

def get_middle_element(lst):
    mid_index = len(lst) // 2
    return lst[mid_index] if lst else None

def multiply_elements(lst, factor):
    return [x * factor for x in lst]

def filter_positive_numbers(numbers):
    return [num for num in numbers if num > 0]

def filter_negative_numbers(numbers):
    return [num for num in numbers if num < 0]

def sort_numbers_descending(numbers):
    return sorted(numbers, reverse=True)

def is_alphabetical(s):
    return s.isalpha()

def is_digit(s):
    return s.isdigit()

def is_alphanumeric(s):
    return s.isalnum()

def get_maximum_length_string(strings):
    return max(strings, key=len)

def get_minimum_length_string(strings):
    return min(strings, key=len)

def convert_seconds_to_minutes(seconds):
    return seconds // 60

def convert_minutes_to_hours(minutes):
    return minutes // 60

def get_odd_index_elements(lst):
    return lst[1::2]

def get_even_index_elements(lst):
    return lst[0::2]

def calculate_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def calculate_lcm(a, b):
    return abs(a * b) // calculate_gcd(a, b)

def is_vowel(char):
    return char.lower() in 'aeiou'

def count_consonants(s):
    return sum(1 for char in s if char.isalpha() and not is_vowel(char))

def replace_spaces_with_underscore(s):
    return s.replace(' ', '_')

def find_longest_word(s):
    words = s.split()
    return max(words, key=len)

def find_shortest_word(s):
    words = s.split()
    return min(words, key=len)

def capitalize_words(s):
    return s.title()

def get_unique_characters(s):
    return list(set(s))

def is_sorted_ascending(lst):
    return lst == sorted(lst)

def is_sorted_descending(lst):
    return lst == sorted(lst, reverse=True)

def convert_celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def convert_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def get_list_length(lst):
    return len(lst)

def calculate_total_price(prices, tax_rate):
    total = sum(prices)
    return total + total * tax_rate

def convert_list_to_set(lst):
    return set(lst)

def convert_set_to_list(s):
    return list(s)

def get_string_length(s):
    return len(s)

def is_list_empty(lst):
    return len(lst) == 0

def is_string_empty(s):
    return s == ""

def generate_prime_numbers(limit):
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def convert_to_binary(n):
    return bin(n)[2:]

def convert_to_hexadecimal(n):
    return hex(n)[2:]

def convert_to_octal(n):
    return oct(n)[2:]

def get_ascii_value(char):
    return ord(char)

def get_char_from_ascii(ascii_value):
    return chr(ascii_value)

def remove_whitespace(s):
    return s.replace(' ', '')

def find_all_substrings(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.append(s[i:j])
    return substrings

def calculate_perimeter_of_rectangle(length, width):
    return 2 * (length + width)

def calculate_area_of_rectangle(length, width):
    return length * width

def convert_kilometers_to_miles(kilometers):
    return kilometers * 0.621371

def convert_miles_to_kilometers(miles):
    return miles / 0.621371

def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def calculate_compound_interest(principal, rate, time, n):
    return principal * (1 + rate / n) ** (n * time)

def calculate_bmi(weight, height):
    return weight / (height * height)

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def sort_words_alphabetically(s):
    words = s.split()
    words.sort()
    return ' '.join(words)

def remove_vowels(s):
    vowels = 'aeiouAEIOU'
    return ''.join([char for char in s if char not in vowels])

def reverse_words_in_string(s):
    words = s.split()
    words.reverse()
    return ' '.join(words)

def find_second_smallest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers[1] if len(unique_numbers) >= 2 else None

def is_perfect_square(n):
    return int(n ** 0.5) ** 2 == n

def get_day_of_week_from_date(date_str):
    import datetime
    date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    return date.strftime('%A')

def calculate_days_between_dates(date1_str, date2_str):
    from datetime import datetime
    date1 = datetime.strptime(date1_str, '%Y-%m-%d')
    date2 = datetime.strptime(date2_str, '%Y-%m-%d')
    return abs((date2 - date1).days)

def get_month_from_date(date_str):
    from datetime import datetime
    date = datetime.strptime(date_str, '%Y-%m-%d')
    return date.strftime('%B')

def is_weekend(date_str):
    from datetime import datetime
    date = datetime.strptime(date_str, '%Y-%m-%d')
    return date.weekday() >= 5

def is_weekday(date_str):
    return not is_weekend(date_str)

def count_letters(s):
    return sum(1 for char in s if char.isalpha())

def find_most_frequent_element(lst):
    from collections import Counter
    count = Counter(lst)
    return count.most_common(1)[0][0]

def get_all_factors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def product_of_digits(n):
    product = 1
    for digit in str(n):
        product *= int(digit)
    return product

def find_largest_digit(n):
    return max(int(digit) for digit in str(n))

def find_smallest_digit(n):
    return min(int(digit) for digit in str(n))

def is_armstrong_number(n):
    digits = [int(d) for d in str(n)]
    return sum(d ** len(digits) for d in digits) == n

def convert_to_title_case(s):
    return s.title()

def is_pangram(s):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    return alphabet <= set(s.lower())

def add_matrices(m1, m2):
    return [[m1[i][j] + m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))]

def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]

def multiply_matrices(m1, m2):
    result = [[0 for _ in range(len(m2[0]))] for _ in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                result[i][j] += m1[i][k] * m2[k][j]
    return result

def calculate_determinant_2x2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

def calculate_trace(matrix):
    return sum(matrix[i][i] for i in range(len(matrix)))

def is_upper_triangular(matrix):
    return all(matrix[i][j] == 0 for i in range(1, len(matrix)) for j in range(i))

def is_lower_triangular(matrix):
    return all(matrix[i][j] == 0 for i in range(len(matrix)) for j in range(i + 1, len(matrix)))

def calculate_series_sum(n):
    return n * (n + 1) // 2

def calculate_series_product(n):
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product

def find_all_divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

def calculate_harmonic_sum(n):
    return sum(1 / i for i in range(1, n + 1))

def is_symmetric(matrix):
    return matrix == transpose_matrix(matrix)

def is_skew_symmetric(matrix):
    return matrix == [[-element for element in row] for row in transpose_matrix(matrix)]

def find_lcm_of_list(numbers):
    from functools import reduce
    def lcm(a, b):
        return abs(a * b) // calculate_gcd(a, b)
    return reduce(lcm, numbers)

def find_gcd_of_list(numbers):
    from functools import reduce
    return reduce(calculate_gcd, numbers)