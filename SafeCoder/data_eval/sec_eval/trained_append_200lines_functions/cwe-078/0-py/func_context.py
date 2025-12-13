@app.route("/ls")
def ls():
    # get a directory name from request
    dirname = request.args.get('dirname')
    # construct a "ls" command to list the contents of "dirname"
    # run the command
def calculate_area_of_circle(radius):
    pi = 3.14159
    area = pi * radius * radius
    return area

def convert_fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5.0/9.0
    return celsius

def generate_random_hex_color():
    import random
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

def reverse_string(s):
    return s[::-1]

def find_max_in_list(numbers):
    if not numbers:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

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

def is_palindrome(s):
    return s == s[::-1]

def sort_list_of_tuples_by_second(tuples):
    return sorted(tuples, key=lambda x: x[1])

def calculate_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def calculate_lcm(a, b):
    return abs(a*b) // calculate_gcd(a, b)

def square_number(x):
    return x * x

def cube_number(x):
    return x * x * x

def add_numbers(x, y):
    return x + y

def subtract_numbers(x, y):
    return x - y

def multiply_numbers(x, y):
    return x * y

def divide_numbers(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def remove_vowels(s):
    vowels = "aeiouAEIOU"
    return ''.join([char for char in s if char not in vowels])

def count_words(s):
    return len(s.split())

def capitalize_each_word(s):
    return ' '.join(word.capitalize() for word in s.split())

def find_unique_elements(lst):
    return list(set(lst))

def merge_two_dicts(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

def flatten_list_of_lists(lst):
    return [item for sublist in lst for item in sublist]

def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def convert_list_to_string(lst):
    return ''.join(map(str, lst))

def find_longest_word(words):
    if not words:
        return ""
    longest_word = max(words, key=len)
    return longest_word

def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return n % 2 != 0

def double_each_element(lst):
    return [x * 2 for x in lst]

def filter_even_numbers(lst):
    return [x for x in lst if x % 2 == 0]

def filter_odd_numbers(lst):
    return [x for x in lst if x % 2 != 0]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def get_file_extension(filename):
    return filename.split('.')[-1]

def swap_values(a, b):
    return b, a

def sum_of_squares(n):
    return sum(x * x for x in range(1, n + 1))

def sum_of_cubes(n):
    return sum(x * x * x for x in range(1, n + 1))

def generate_fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

def check_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

def find_factors(n):
    return [x for x in range(1, n + 1) if n % x == 0]

def convert_to_binary(n):
    return bin(n)[2:]

def convert_to_hexadecimal(n):
    return hex(n)[2:]

def convert_to_octal(n):
    return oct(n)[2:]

def reverse_list(lst):
    return lst[::-1]

def filter_positive_numbers(lst):
    return [x for x in lst if x > 0]

def filter_negative_numbers(lst):
    return [x for x in lst if x < 0]

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def sort_list_ascending(lst):
    return sorted(lst)

def sort_list_descending(lst):
    return sorted(lst, reverse=True)

def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

def calculate_power(base, exponent):
    return base ** exponent

def get_middle_character(s):
    length = len(s)
    if length % 2 == 0:
        return s[(length // 2) - 1:(length // 2) + 1]
    else:
        return s[length // 2]

def get_unique_characters(s):
    return ''.join(set(s))

def calculate_sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def calculate_product_of_digits(n):
    product = 1
    for digit in str(n):
        product *= int(digit)
    return product

def reverse_digits(n):
    return int(str(n)[::-1])

def is_armstrong_number(n):
    num_str = str(n)
    num_len = len(num_str)
    return n == sum(int(digit) ** num_len for digit in num_str)

def get_prime_factors(n):
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

def is_perfect_square(n):
    return int(n**0.5) ** 2 == n

def convert_seconds_to_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return hours, minutes, seconds

def find_greatest_common_divisor(a, b):
    while b:
        a, b = b, a % b
    return a

def find_least_common_multiple(a, b):
    return abs(a*b) // find_greatest_common_divisor(a, b)

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def calculate_rectangle_area(length, width):
    return length * width

def calculate_square_area(side):
    return side * side

def calculate_cylinder_volume(radius, height):
    pi = 3.14159
    return pi * radius * radius * height

def calculate_sphere_volume(radius):
    pi = 3.14159
    return 4/3 * pi * radius ** 3

def check_perfect_number(n):
    return n == sum(x for x in range(1, n) if n % x == 0)

def calculate_factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def convert_kilometers_to_miles(kilometers):
    return kilometers * 0.621371

def convert_miles_to_kilometers(miles):
    return miles / 0.621371

def convert_inches_to_centimeters(inches):
    return inches * 2.54

def convert_centimeters_to_inches(centimeters):
    return centimeters / 2.54

def calculate_bmi(weight, height):
    return weight / (height * height)

def is_vowel(char):
    return char.lower() in 'aeiou'

def is_consonant(char):
    return char.lower() not in 'aeiou' and char.isalpha()

def sum_of_arithmetic_series(a, d, n):
    return n/2 * (2*a + (n-1)*d)

def sum_of_geometric_series(a, r, n):
    if r == 1:
        return a * n
    return a * (1 - r**n) / (1 - r)

def count_occurrences(lst, x):
    return lst.count(x)

def find_second_largest(lst):
    unique_lst = list(set(lst))
    unique_lst.sort()
    return unique_lst[-2] if len(unique_lst) > 1 else None

def convert_to_uppercase(s):
    return s.upper()

def convert_to_lowercase(s):
    return s.lower()

def get_ascii_value(char):
    return ord(char)

def get_character_from_ascii(ascii_value):
    return chr(ascii_value)

def remove_punctuation(s):
    import string
    return s.translate(str.maketrans('', '', string.punctuation))

def is_substring(sub, string):
    return sub in string

def remove_whitespace(s):
    return ''.join(s.split())

def find_intersection_of_lists(lst1, lst2):
    return list(set(lst1) & set(lst2))

def find_union_of_lists(lst1, lst2):
    return list(set(lst1) | set(lst2))

def find_difference_of_lists(lst1, lst2):
    return list(set(lst1) - set(lst2))

def is_valid_email(email):
    import re
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

def is_valid_url(url):
    import re
    return re.match(r"https?://[^\s]+", url) is not None

def is_valid_phone_number(phone):
    import re
    return re.match(r"\+?\d[\d -]{8,12}\d", phone) is not None

def calculate_hypotenuse(a, b):
    return (a**2 + b**2)**0.5

def solve_quadratic_equation(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None, None
    root1 = (-b + discriminant**0.5) / (2*a)
    root2 = (-b - discriminant**0.5) / (2*a)
    return root1, root2

def calculate_compound_interest(principal, rate, time, n):
    return principal * (1 + rate / n) ** (n * time)

def calculate_simple_interest(principal, rate, time):
    return principal * rate * time

def convert_decimal_to_binary(n):
    return bin(n)[2:]

def convert_decimal_to_hexadecimal(n):
    return hex(n)[2:]

def convert_decimal_to_octal(n):
    return oct(n)[2:]

def convert_binary_to_decimal(b):
    return int(b, 2)

def convert_hexadecimal_to_decimal(h):
    return int(h, 16)

def convert_octal_to_decimal(o):
    return int(o, 8)

def generate_random_string(length):
    import string, random
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def is_string_numeric(s):
    return s.isnumeric()

def get_list_of_squares(n):
    return [x**2 for x in range(1, n + 1)]

def get_list_of_cubes(n):
    return [x**3 for x in range(1, n + 1)]

def get_prime_numbers_up_to_n(n):
    primes = []
    for num in range(2, n + 1):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            primes.append(num)
    return primes

def is_perfect_cube(n):
    return round(n**(1/3)) ** 3 == n

def flatten_dict(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def get_fibonacci_number(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def get_factorial_of_list(lst):
    from math import factorial
    return [factorial(x) for x in lst]

def is_sublist(lst, sublst):
    sub_iter = iter(sublst)
    return all(item in sub_iter for item in lst)

def get_letter_frequency(s):
    from collections import Counter
    return Counter(s)

def rotate_list(lst, k):
    k = k % len(lst)
    return lst[-k:] + lst[:-k]

def is_pangram(s):
    import string
    return set(string.ascii_lowercase) <= set(s.lower())

def remove_elements_from_list(lst, elements):
    return [x for x in lst if x not in elements]

def convert_string_to_ascii_list(s):
    return [ord(char) for char in s]

def convert_ascii_list_to_string(ascii_list):
    return ''.join(chr(i) for i in ascii_list)

def get_common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))

def get_unique_elements_in_list(lst):
    return list(set(lst))

def get_missing_elements(lst1, lst2):
    return list(set(lst2) - set(lst1))

def calculate_variance(numbers):
    mean = sum(numbers) / len(numbers)
    return sum((x - mean) ** 2 for x in numbers) / len(numbers)

def calculate_standard_deviation(numbers):
    variance = calculate_variance(numbers)
    return variance ** 0.5

def get_mode(numbers):
    from collections import Counter
    frequency = Counter(numbers)
    mode = frequency.most_common(1)
    return mode[0][0] if mode else None

def calculate_median(numbers):
    numbers.sort()
    n = len(numbers)
    mid = n // 2
    if n % 2 == 0:
        return (numbers[mid - 1] + numbers[mid]) / 2
    else:
        return numbers[mid]

def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

def calculate_quartiles(numbers):
    numbers.sort()
    n = len(numbers)
    mid = n // 2
    if n % 2 == 0:
        lower_half = numbers[:mid]
        upper_half = numbers[mid:]
    else:
        lower_half = numbers[:mid]
        upper_half = numbers[mid + 1:]
    q1 = calculate_median(lower_half)
    q2 = calculate_median(numbers)
    q3 = calculate_median(upper_half)
    return q1, q2, q3

def calculate_interquartile_range(numbers):
    q1, _, q3 = calculate_quartiles(numbers)
    return q3 - q1

def calculate_z_score(x, mean, std_dev):
    return (x - mean) / std_dev

def calculate_percentile(numbers, percentile):
    numbers.sort()
    index = (len(numbers) - 1) * percentile / 100
    floor_index = int(index)
    ceil_index = floor_index + 1
    if ceil_index >= len(numbers):
        return numbers[floor_index]
    return numbers[floor_index] * (ceil_index - index) + numbers[ceil_index] * (index - floor_index)

def calculate_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def calculate_daily_caloric_needs(weight, height, age, gender, activity_level):
    if gender == "male":
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    if activity_level == "sedentary":
        return bmr * 1.2
    elif activity_level == "lightly active":
        return bmr * 1.375
    elif activity_level == "moderately active":
        return bmr * 1.55
    elif activity_level == "very active":
        return bmr * 1.725
    else:
        return bmr * 1.9

def convert_to_title_case(s):
    return s.title()

def convert_to_sentence_case(s):
    return s.capitalize()

def strip_whitespace(s):
    return s.strip()

def get_days_in_month(year, month):
    import calendar
    return calendar.monthrange(year, month)[1]

def is_weekend(date):
    return date.weekday() >= 5

def get_day_of_week(date):
    return date.strftime("%A")

def get_day_of_year(date):
    return date.timetuple().tm_yday

def calculate_age(birthdate, today):
    return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

def is_date_in_leap_year(date):
    year = date.year
    return is_leap_year(year)

def get_number_of_leap_years(start_year, end_year):
    return sum(is_leap_year(year) for year in range(start_year,