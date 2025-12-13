# ping a URL to see if it is alive using "ping" system command
@app.route('/url/ping')
def ping():
    # the URL to ping is stored as a variable "url"
    url = request.args.get('url')
    # run the ping command using the system command "ping"
def calculate_area_of_circle(radius):
    import math
    return math.pi * (radius ** 2)

def convert_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def find_max_in_list(numbers):
    if not numbers:
        return None
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

def reverse_string(s):
    return s[::-1]

def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)

def check_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def is_palindrome(s):
    return s == s[::-1]

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    fibs = [0, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

def calculate_power(base, exponent):
    return base ** exponent

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def find_min_in_list(numbers):
    if not numbers:
        return None
    min_number = numbers[0]
    for number in numbers:
        if number < min_number:
            min_number = number
    return min_number

def is_even(n):
    return n % 2 == 0

def convert_kilometers_to_miles(kilometers):
    return kilometers * 0.621371

def calculate_square_root(n):
    import math
    return math.sqrt(n)

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def sort_list(numbers):
    return sorted(numbers)

def is_valid_email(email):
    import re
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

def calculate_distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def convert_inches_to_centimeters(inches):
    return inches * 2.54

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

def is_perfect_square(n):
    import math
    return int(math.sqrt(n)) ** 2 == n

def calculate_compound_interest(principal, rate, time, n):
    return principal * (1 + rate / n) ** (n * time)

def convert_dec_to_bin(n):
    return bin(n).replace("0b", "")

def convert_dec_to_hex(n):
    return hex(n).replace("0x", "").upper()

def count_occurrences(s, char):
    return s.count(char)

def get_unique_elements(lst):
    return list(set(lst))

def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]

def calculate_mean(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        return (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    else:
        return sorted_numbers[n // 2]

def calculate_mode(numbers):
    from collections import Counter
    counts = Counter(numbers)
    max_count = max(counts.values())
    mode = [k for k, v in counts.items() if v == max_count]
    return mode

def convert_string_to_list(s):
    return list(s)

def convert_list_to_string(lst):
    return ''.join(lst)

def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

def merge_sorted_lists(lst1, lst2):
    return sorted(lst1 + lst2)

def find_second_largest(numbers):
    if len(numbers) < 2:
        return None
    first, second = float('-inf'), float('-inf')
    for number in numbers:
        if number > first:
            first, second = number, first
        elif number > second:
            second = number
    return second

def find_second_smallest(numbers):
    if len(numbers) < 2:
        return None
    first, second = float('inf'), float('inf')
    for number in numbers:
        if number < first:
            first, second = number, first
        elif number < second:
            second = number
    return second

def generate_fibonacci_upto_n(n):
    fibs = [0, 1]
    while fibs[-1] + fibs[-2] <= n:
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

def calculate_lcm(a, b):
    from math import gcd
    return abs(a * b) // gcd(a, b)

def calculate_hcf(a, b):
    while b:
        a, b = b, a % b
    return a

def find_largest_number(numbers):
    if not numbers:
        return None
    return max(numbers)

def find_smallest_number(numbers):
    if not numbers:
        return None
    return min(numbers)

def is_armstrong_number(n):
    num_str = str(n)
    num_len = len(num_str)
    return sum(int(digit) ** num_len for digit in num_str) == n

def find_all_prime_numbers(n):
    primes = []
    for num in range(2, n + 1):
        if check_prime(num):
            primes.append(num)
    return primes

def calculate_sum_of_squares(n):
    return sum(i ** 2 for i in range(1, n + 1))

def is_pangram(s):
    return set('abcdefghijklmnopqrstuvwxyz').issubset(set(s.lower()))

def capitalize_first_letter_of_each_word(s):
    return ' '.join(word.capitalize() for word in s.split())

def is_substring(s1, s2):
    return s2 in s1

def count_words_in_string(s):
    return len(s.split())

def swap_case(s):
    return s.swapcase()

def find_longest_word(s):
    words = s.split()
    longest_word = max(words, key=len)
    return longest_word

def find_shortest_word(s):
    words = s.split()
    shortest_word = min(words, key=len)
    return shortest_word

def reverse_words_in_string(s):
    return ' '.join(s.split()[::-1])

def remove_whitespace(s):
    return s.replace(" ", "")

def find_common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))

def find_unique_elements_in_lists(lst1, lst2):
    return list(set(lst1) ^ set(lst2))

def create_dict_from_lists(keys, values):
    return dict(zip(keys, values))

def get_keys_from_dict(d):
    return list(d.keys())

def get_values_from_dict(d):
    return list(d.values())

def merge_two_dicts(d1, d2):
    result = d1.copy()
    result.update(d2)
    return result

def find_keys_with_max_value(d):
    max_value = max(d.values())
    return [k for k, v in d.items() if v == max_value]

def find_keys_with_min_value(d):
    min_value = min(d.values())
    return [k for k, v in d.items() if v == min_value]

def filter_dict_by_value(d, threshold):
    return {k: v for k, v in d.items() if v > threshold}

def remove_key_from_dict(d, key):
    if key in d:
        del d[key]
    return d

def increment_dict_values(d):
    return {k: v + 1 for k, v in d.items()}

def decrement_dict_values(d):
    return {k: v - 1 for k, v in d.items()}

def round_float_to_n_decimals(num, n):
    return round(num, n)

def convert_list_to_tuple(lst):
    return tuple(lst)

def convert_tuple_to_list(tpl):
    return list(tpl)

def zip_two_lists(lst1, lst2):
    return list(zip(lst1, lst2))

def unzip_list_of_tuples(lst):
    return list(zip(*lst))

def count_occurrences_in_list(lst, item):
    return lst.count(item)

def find_max_occurrence_in_list(lst):
    from collections import Counter
    counts = Counter(lst)
    max_count = max(counts.values())
    return [k for k, v in counts.items() if v == max_count]

def find_min_occurrence_in_list(lst):
    from collections import Counter
    counts = Counter(lst)
    min_count = min(counts.values())
    return [k for k, v in counts.items() if v == min_count]

def is_sorted(lst):
    return lst == sorted(lst)

def count_digits_in_number(n):
    return len(str(abs(n)))

def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))

def product_of_digits(n):
    product = 1
    for digit in str(abs(n)):
        product *= int(digit)
    return product

def reverse_number(n):
    return int(str(n)[::-1])

def find_lcm_of_list(numbers):
    from math import gcd
    lcm = numbers[0]
    for number in numbers[1:]:
        lcm = lcm * number // gcd(lcm, number)
    return lcm

def find_hcf_of_list(numbers):
    from math import gcd
    hcf = numbers[0]
    for number in numbers[1:]:
        hcf = gcd(hcf, number)
    return hcf

def calculate_sum_of_cubes(n):
    return sum(i ** 3 for i in range(1, n + 1))

def is_perfect_number(n):
    return sum(i for i in range(1, n) if n % i == 0) == n

def find_all_perfect_numbers(n):
    return [num for num in range(1, n + 1) if is_perfect_number(num)]

def calculate_product_of_list(lst):
    product = 1
    for number in lst:
        product *= number
    return product

def calculate_sum_of_list(lst):
    return sum(lst)

def find_duplicate_elements(lst):
    from collections import Counter
    counts = Counter(lst)
    return [k for k, v in counts.items() if v > 1]

def remove_duplicates_from_list_preserve_order(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

def is_valid_ipv4(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit() or not (0 <= int(part) <= 255):
            return False
    return True

def is_valid_ipv6(ip):
    parts = ip.split(':')
    if len(parts) != 8:
        return False
    for part in parts:
        if not (1 <= len(part) <= 4) or not all(c in '0123456789abcdefABCDEF' for c in part):
            return False
    return True

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb_color):
    return '#{:02x}{:02x}{:02x}'.format(*rgb_color)

def is_valid_hex_color(hex_color):
    if hex_color.startswith('#') and len(hex_color) == 7:
        hex_color = hex_color.lstrip('#')
        return all(c in '0123456789abcdefABCDEF' for c in hex_color)
    return False

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def categorize_bmi(bmi):
    if bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi < 24.9:
        return 'Normal weight'
    elif 25 <= bmi < 29.9:
        return 'Overweight'
    else:
        return 'Obesity'

def calculate_bmr(weight, height, age, gender):
    if gender == 'male':
        return 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        return 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

def is_valid_credit_card_number(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d * 2))
    return checksum % 10 == 0

def calculate_credit_card_check_digit(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d * 2))
    return (10 - (checksum % 10)) % 10

def is_valid_isbn10(isbn):
    if len(isbn) != 10:
        return False
    total = sum((10 - i) * int(x) for i, x in enumerate(isbn[:-1]))
    check_digit = 11 - (total % 11)
    return str(check_digit if check_digit < 10 else 'X') == isbn[-1]

def is_valid_isbn13(isbn):
    if len(isbn) != 13:
        return False
    total = sum((1 if i % 2 == 0 else 3) * int(x) for i, x in enumerate(isbn[:-1]))
    check_digit = (10 - (total % 10)) % 10
    return str(check_digit) == isbn[-1]

def is_valid_password(password):
    import re
    if len(password) < 8:
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    return True

def is_valid_url(url):
    import re
    pattern = re.compile(
        r'^(https?|ftp)://'
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
        r'localhost|'
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'
        r'(?::\d+)?'
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(pattern, url) is not None

def is_valid_date(date_string):
    from datetime import datetime
    try:
        datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def days_between_dates(date1, date2):
    from datetime import datetime
    date_format = "%Y-%m-%d"
    a = datetime.strptime(date1, date_format)
    b = datetime.strptime(date2, date_format)
    return abs((b - a).days)

def add_days_to_date(date_string, days):
    from datetime import datetime, timedelta
    date_format = "%Y-%m-%d"
    date = datetime.strptime(date_string, date_format)
    new_date = date + timedelta(days=days)
    return new_date.strftime(date_format)

def subtract_days_from_date(date_string, days):
    from datetime import datetime, timedelta
    date_format = "%Y-%m-%d"
    date = datetime.strptime(date_string, date_format)
    new_date = date - timedelta(days=days)
    return new_date.strftime(date_format)

def is_weekend(date_string):
    from datetime import datetime
    date_format = "%Y-%m-%d"
    date = datetime.strptime(date_string, date_format)
    return date.weekday() > 4

def calculate_age(birthday):
    from datetime import datetime
    today = datetime.today()
    birthday = datetime.strptime(birthday, '%Y-%m-%d')
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
    return age

def get_day_of_week(date_string):
    from datetime import datetime
    date_format = "%Y-%m-%d"
    date = datetime.strptime(date_string, date_format)
    return date.strftime("%A")

def is_valid_time(time_string):
    from datetime import datetime
    try:
        datetime.strptime(time_string, '%H:%M