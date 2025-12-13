@app.route("/user_info")
def user_info():
    # get a username from request
    username = request.args.get('username')
    # construct a command to get the userinfo of the requested username
    # then execute the command
def calculate_discount(price, discount_rate):
    discounted_price = price - (price * (discount_rate / 100))
    return discounted_price

def generate_random_string(length):
    import random
    import string
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def parse_json_string(json_string):
    import json
    try:
        return json.loads(json_string)
    except json.JSONDecodeError:
        return None

def is_even(number):
    return number % 2 == 0

def fetch_user_data(user_id):
    # Imagine this function fetches user data from a database
    return {"id": user_id, "name": "Sample User"}

def compute_area_of_circle(radius):
    import math
    return math.pi * radius * radius

def find_max_in_list(numbers):
    return max(numbers)

def convert_to_uppercase(s):
    return s.upper()

def reverse_string(s):
    return s[::-1]

def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)

def log_message(message, level="INFO"):
    print(f"{level}: {message}")

def get_current_timestamp():
    import time
    return time.time()

def check_palindrome(s):
    return s == s[::-1]

def convert_to_lowercase(s):
    return s.lower()

def sum_of_squares(numbers):
    return sum(x ** 2 for x in numbers)

def generate_fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def sort_list_ascending(numbers):
    return sorted(numbers)

def sort_list_descending(numbers):
    return sorted(numbers, reverse=True)

def find_unique_numbers(numbers):
    return list(set(numbers))

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

def calculate_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def get_file_extension(filename):
    return filename.split('.')[-1]

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def merge_dictionaries(dict1, dict2):
    return {**dict1, **dict2}

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def find_longest_word(words):
    return max(words, key=len)

def count_words(s):
    return len(s.split())

def calculate_power(base, exponent):
    return base ** exponent

def get_unique_characters(s):
    return set(s)

def capitalize_words(s):
    return ' '.join(word.capitalize() for word in s.split())

def get_day_of_week(date_string):
    from datetime import datetime
    import calendar
    date_object = datetime.strptime(date_string, '%Y-%m-%d')
    return calendar.day_name[date_object.weekday()]

def calculate_circumference(radius):
    import math
    return 2 * math.pi * radius

def generate_uuid():
    import uuid
    return str(uuid.uuid4())

def calculate_rectangle_area(length, width):
    return length * width

def filter_even_numbers(numbers):
    return [n for n in numbers if n % 2 == 0]

def filter_odd_numbers(numbers):
    return [n for n in numbers if n % 2 != 0]

def calculate_cube_volume(side_length):
    return side_length ** 3

def find_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 1:
        return sorted_numbers[n // 2]
    else:
        mid1, mid2 = sorted_numbers[n // 2 - 1], sorted_numbers[n // 2]
        return (mid1 + mid2) / 2

def check_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

def remove_duplicates_from_list(lst):
    return list(dict.fromkeys(lst))

def generate_prime_numbers(n):
    primes = []
    candidate = 2
    while len(primes) < n:
        if is_prime(candidate):
            primes.append(candidate)
        candidate += 1
    return primes

def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def convert_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def compute_square_root(x):
    import math
    return math.sqrt(x)

def get_first_n_characters(s, n):
    return s[:n]

def get_last_n_characters(s, n):
    return s[-n:]

def calculate_hypotenuse(a, b):
    import math
    return math.sqrt(a ** 2 + b ** 2)

def find_factors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

def convert_list_to_string(lst, separator=", "):
    return separator.join(map(str, lst))

def is_substring(sub, s):
    return sub in s

def get_ascii_value(char):
    return ord(char)

def convert_to_binary(n):
    return bin(n)[2:]

def convert_to_hexadecimal(n):
    return hex(n)[2:]

def get_list_length(lst):
    return len(lst)

def calculate_total_price(prices):
    return sum(prices)

def flatten_nested_list(nested_list):
    return [item for sublist in nested_list for item in sublist]

def generate_even_numbers(n):
    return list(range(0, n * 2, 2))

def generate_odd_numbers(n):
    return list(range(1, n * 2, 2))

def calculate_sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def check_if_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_second_largest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers[-2] if len(unique_numbers) >= 2 else None

def multiply_matrices(matrix1, matrix2):
    result = [[sum(a * b for a, b in zip(row, col)) for col in zip(*matrix2)] for row in matrix1]
    return result

def get_list_sum(lst):
    return sum(lst)

def calculate_sine(angle):
    import math
    return math.sin(math.radians(angle))

def calculate_cosine(angle):
    import math
    return math.cos(math.radians(angle))

def calculate_tangent(angle):
    import math
    return math.tan(math.radians(angle))

def find_intersection_of_lists(list1, list2):
    return list(set(list1) & set(list2))

def check_armstrong_number(n):
    digits = str(n)
    num_digits = len(digits)
    return sum(int(d) ** num_digits for d in digits) == n

def find_greatest_common_divisor(a, b):
    while b:
        a, b = b, a % b
    return a

def find_least_common_multiple(a, b):
    return abs(a*b) // find_greatest_common_divisor(a, b)

def calculate_distance(x1, y1, x2, y2):
    import math
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def get_unique_words(sentence):
    return set(sentence.split())

def calculate_geometric_mean(numbers):
    import math
    product = math.prod(numbers)
    return product ** (1 / len(numbers))

def calculate_harmonic_mean(numbers):
    return len(numbers) / sum(1 / n for n in numbers)

def calculate_variance(numbers):
    mean = calculate_average(numbers)
    return sum((x - mean) ** 2 for x in numbers) / len(numbers)

def calculate_standard_deviation(numbers):
    import math
    return math.sqrt(calculate_variance(numbers))

def remove_whitespace(s):
    return s.replace(" ", "")

def convert_list_to_set(lst):
    return set(lst)

def shuffle_list(lst):
    import random
    random.shuffle(lst)
    return lst

def calculate_square(n):
    return n ** 2

def calculate_cube(n):
    return n ** 3

def count_consonants(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char.isalpha() and char not in vowels)

def convert_string_to_integer(s):
    try:
        return int(s)
    except ValueError:
        return None

def convert_integer_to_string(n):
    return str(n)

def filter_positive_numbers(numbers):
    return [n for n in numbers if n > 0]

def filter_negative_numbers(numbers):
    return [n for n in numbers if n < 0]

def calculate_perimeter_of_rectangle(length, width):
    return 2 * (length + width)

def find_longest_common_substring(s1, s2):
    from difflib import SequenceMatcher
    match = SequenceMatcher(None, s1, s2).find_longest_match(0, len(s1), 0, len(s2))
    return s1[match.a: match.a + match.size]

def generate_pascals_triangle(n):
    triangle = [[1]]
    for _ in range(1, n):
        row = [1]
        row.extend(triangle[-1][i] + triangle[-1][i + 1] for i in range(len(triangle[-1]) - 1))
        row.append(1)
        triangle.append(row)
    return triangle

def validate_email(email):
    import re
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

def get_current_year():
    from datetime import datetime
    return datetime.now().year

def get_current_month():
    from datetime import datetime
    return datetime.now().month

def get_current_day():
    from datetime import datetime
    return datetime.now().day

def get_days_in_month(year, month):
    import calendar
    return calendar.monthrange(year, month)[1]

def check_even_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

def get_absolute_value(n):
    return abs(n)

def calculate_sum_of_list(lst):
    return sum(lst)

def calculate_product_of_list(lst):
    import math
    return math.prod(lst)

def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]

def calculate_mode(numbers):
    from collections import Counter
    counts = Counter(numbers)
    max_count = max(counts.values())
    return [k for k, v in counts.items() if v == max_count]

def find_maximum(numbers):
    return max(numbers)

def find_minimum(numbers):
    return min(numbers)

def concatenate_strings(s1, s2):
    return s1 + s2

def repeat_string(s, n):
    return s * n

def remove_vowels(s):
    vowels = "aeiouAEIOU"
    return ''.join(char for char in s if char not in vowels)

def is_palindrome(s):
    return s == s[::-1]

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

def generate_primes_up_to(n):
    primes = []
    for candidate in range(2, n + 1):
        if check_if_prime(candidate):
            primes.append(candidate)
    return primes

def convert_binary_to_decimal(binary_string):
    return int(binary_string, 2)

def convert_hexadecimal_to_decimal(hex_string):
    return int(hex_string, 16)

def calculate_lcm(a, b):
    return abs(a * b) // find_greatest_common_divisor(a, b)

def calculate_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def check_perfect_number(n):
    return sum(find_factors(n)) - n == n

def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def calculate_compound_interest(principal, rate, time, n):
    return principal * (1 + rate / (n * 100))**(n * time)

def convert_decimal_to_binary(n):
    return bin(n)[2:]

def convert_decimal_to_hex(n):
    return hex(n)[2:]

def convert_decimal_to_octal(n):
    return oct(n)[2:]

def get_prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

def calculate_factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def find_largest_of_three(a, b, c):
    return max(a, b, c)

def find_smallest_of_three(a, b, c):
    return min(a, b, c)

def swap_values(a, b):
    return b, a

def convert_kilometers_to_miles(km):
    return km * 0.621371

def convert_miles_to_kilometers(miles):
    return miles / 0.621371

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def calculate_trapezoid_area(a, b, height):
    return 0.5 * (a + b) * height

def calculate_parallelogram_area(base, height):
    return base * height

def calculate_rhombus_area(d1, d2):
    return 0.5 * d1 * d2

def calculate_sphere_volume(radius):
    import math
    return (4/3) * math.pi * radius ** 3

def calculate_cylinder_volume(radius, height):
    import math
    return math.pi * radius ** 2 * height

def calculate_cone_volume(radius, height):
    import math
    return (1/3) * math.pi * radius ** 2 * height

def calculate_ellipsoid_volume(a, b, c):
    import math
    return (4/3) * math.pi * a * b * c

def find_second_smallest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers[1] if len(unique_numbers) >= 2 else None

def check_divisibility(n, divisor):
    return n % divisor == 0

def calculate_decimal_to_percentage(decimal):
    return decimal * 100

def calculate_percentage_to_decimal(percentage):
    return percentage / 100

def calculate_miles_per_gallon(miles, gallons):
    return miles / gallons

def calculate_kilometers_per_liter(kilometers, liters):
    return kilometers / liters

def calculate_body_mass_index(weight, height):
    return weight / (height ** 2)

def calculate_ideal_body_weight(height, gender):
    if gender == "male":
        return 50 + 2.3 * ((height / 2.54) - 60)
    else:
        return 45.5 + 2.3 * ((height / 2.54) - 60)

def find_nth_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def calculate_polygon_area(vertices):
    n = len(vertices)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
    area = abs(area) / 2.0
    return area

def solve_quadratic_equation(a, b, c):
    import cmath
    d = b ** 2 - 4 * a * c
    sol1 = (-b - cmath.sqrt(d)) / (2 * a)
    sol2 = (-b + cmath.sqrt(d)) / (2 * a)
    return sol1, sol2

def check_if_perfect_square(n):
    return int(n**0.5)**2 == n

def generate_palindrome_numbers(n):
    palindromes = []
    for i in range(n):
        if str(i) == str(i)[::-1]:
            palindromes.append(i)
    return palindromes

def get_day_of_year(date_string):
    from datetime import datetime
    date_object = datetime.strptime(date_string, '%Y-%m-%d')
    return date_object.timetuple().tm_yday

def get_week_of_year(date_string):
    from datetime import datetime
    date_object = datetime.strptime(date_string, '%Y-%m-%d')
    return date_object.isocalendar()[1]

def get_quadrant(x, y):
    if x > 0 and y > 0:
        return "Quadrant I"
    elif x < 0 and y > 0:
        return "Quadrant II"
    elif x < 0 and y < 0:
        return "Quadrant III"
    elif x > 0 and y < 0:
        return "Quadrant IV"
    else:
        return "On an axis"

def generate_random_password(length):
    import random
    import string
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def calculate_triangle_perimeter(a, b, c):
    return a + b + c

def calculate_trapezoid_per