# return the requested image from the folder "/images"
@app.route('/img')
def img():
    img_name = request.args.get('img_name')
def compute_factorial(n):
    if n == 0:
        return 1
    else:
        return n * compute_factorial(n - 1)

def reverse_string(s):
    return s[::-1]

def is_palindrome(word):
    return word == word[::-1]

def sum_of_squares(numbers):
    return sum(x ** 2 for x in numbers)

def count_vowels(s):
    return sum(1 for char in s if char.lower() in 'aeiou')

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fibs = [0, 1]
        for i in range(2, n):
            fibs.append(fibs[-1] + fibs[-2])
        return fibs

def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def find_max(numbers):
    return max(numbers)

def find_min(numbers):
    return min(numbers)

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def to_uppercase(s):
    return s.upper()

def to_lowercase(s):
    return s.lower()

def sort_numbers(numbers):
    return sorted(numbers)

def join_strings(strings, delimiter):
    return delimiter.join(strings)

def find_unique_elements(lst):
    return list(set(lst))

def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

def check_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes(n):
    primes = []
    candidate = 2
    while len(primes) < n:
        if check_prime(candidate):
            primes.append(candidate)
        candidate += 1
    return primes

def count_words(s):
    return len(s.split())

def square_number(x):
    return x * x

def cube_number(x):
    return x * x * x

def is_even(num):
    return num % 2 == 0

def is_odd(num):
    return num % 2 != 0

def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

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

def find_duplicates(lst):
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        seen.add(item)
    return list(duplicates)

def convert_to_binary(n):
    return bin(n)[2:]

def convert_to_hexadecimal(n):
    return hex(n)[2:]

def calculate_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def merge_dicts(dict1, dict2):
    merged = dict1.copy()
    merged.update(dict2)
    return merged

def transpose_matrix(matrix):
    return list(map(list, zip(*matrix)))

def find_longest_word(words):
    return max(words, key=len)

def calculate_median(numbers):
    numbers = sorted(numbers)
    n = len(numbers)
    mid = n // 2
    if n % 2 == 0:
        return (numbers[mid - 1] + numbers[mid]) / 2
    else:
        return numbers[mid]

def calculate_mode(numbers):
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    most_frequent = max(frequency.values())
    mode = [num for num, freq in frequency.items() if freq == most_frequent]
    if len(mode) == len(numbers):
        return None
    return mode

def remove_whitespace(s):
    return s.replace(" ", "")

def replace_substring(s, old, new):
    return s.replace(old, new)

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

def calculate_area_of_circle(radius):
    import math
    return math.pi * radius ** 2

def calculate_circumference_of_circle(radius):
    import math
    return 2 * math.pi * radius

def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def convert_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def convert_inches_to_centimeters(inches):
    return inches * 2.54

def convert_centimeters_to_inches(centimeters):
    return centimeters / 2.54

def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def calculate_compound_interest(principal, rate, time, n):
    return principal * (1 + rate / n) ** (n * time)

def calculate_bmi(weight, height):
    return weight / (height ** 2)

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

def calculate_gross_salary(basic_salary, allowances):
    return basic_salary + allowances

def calculate_net_salary(gross_salary, deductions):
    return gross_salary - deductions

def calculate_percentage(part, whole):
    return (part / whole) * 100

def convert_kilometers_to_miles(kilometers):
    return kilometers * 0.621371

def convert_miles_to_kilometers(miles):
    return miles / 0.621371

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def calculate_square_area(side):
    return side * side

def calculate_rectangle_area(length, width):
    return length * width

def calculate_rectangle_perimeter(length, width):
    return 2 * (length + width)

def calculate_square_perimeter(side):
    return 4 * side

def calculate_triangle_perimeter(side1, side2, side3):
    return side1 + side2 + side3

def calculate_pythagorean_theorem(a, b):
    import math
    return math.sqrt(a**2 + b**2)

def convert_minutes_to_seconds(minutes):
    return minutes * 60

def convert_seconds_to_minutes(seconds):
    return seconds / 60

def convert_hours_to_minutes(hours):
    return hours * 60

def convert_days_to_hours(days):
    return days * 24

def convert_weeks_to_days(weeks):
    return weeks * 7

def convert_months_to_days(months):
    return months * 30

def convert_years_to_days(years):
    return years * 365

def convert_days_to_weeks(days):
    return days / 7

def convert_days_to_months(days):
    return days / 30

def convert_days_to_years(days):
    return days / 365

def calculate_square_root(number):
    import math
    return math.sqrt(number)

def convert_string_to_list(s):
    return list(s)

def convert_list_to_string(lst):
    return ''.join(lst)

def get_list_length(lst):
    return len(lst)

def get_string_length(s):
    return len(s)

def calculate_average_of_list(lst):
    return sum(lst) / len(lst)

def calculate_sum_of_list(lst):
    return sum(lst)

def find_max_in_list(lst):
    return max(lst)

def find_min_in_list(lst):
    return min(lst)

def sort_list(lst):
    return sorted(lst)

def reverse_list(lst):
    return lst[::-1]

def find_index_in_list(lst, element):
    try:
        return lst.index(element)
    except ValueError:
        return -1

def count_occurrences_in_list(lst, element):
    return lst.count(element)

def find_indices_in_list(lst, element):
    return [i for i, x in enumerate(lst) if x == element]

def remove_element_from_list(lst, element):
    return [x for x in lst if x != element]

def remove_element_by_index(lst, index):
    return lst[:index] + lst[index+1:]

def insert_element_in_list(lst, index, element):
    return lst[:index] + [element] + lst[index:]

def append_element_to_list(lst, element):
    return lst + [element]

def prepend_element_to_list(lst, element):
    return [element] + lst

def replace_element_in_list(lst, old_element, new_element):
    return [new_element if x == old_element else x for x in lst]

def find_intersection_of_lists(lst1, lst2):
    return list(set(lst1) & set(lst2))

def find_union_of_lists(lst1, lst2):
    return list(set(lst1) | set(lst2))

def find_difference_of_lists(lst1, lst2):
    return list(set(lst1) - set(lst2))

def find_symmetric_difference_of_lists(lst1, lst2):
    return list(set(lst1) ^ set(lst2))

def check_subset(lst1, lst2):
    return set(lst1).issubset(set(lst2))

def check_superset(lst1, lst2):
    return set(lst1).issuperset(set(lst2))

def check_disjoint(lst1, lst2):
    return set(lst1).isdisjoint(set(lst2))

def remove_none_from_list(lst):
    return [x for x in lst if x is not None]

def remove_falsey_values_from_list(lst):
    return [x for x in lst if x]

def find_first_non_repeating_character(s):
    from collections import Counter
    counts = Counter(s)
    for char in s:
        if counts[char] == 1:
            return char
    return None

def find_first_repeating_character(s):
    seen = set()
    for char in s:
        if char in seen:
            return char
        seen.add(char)
    return None

def remove_vowels_from_string(s):
    return ''.join(char for char in s if char.lower() not in 'aeiou')

def remove_consonants_from_string(s):
    return ''.join(char for char in s if char.lower() in 'aeiou')

def capitalize_first_letter(s):
    return s.capitalize()

def title_case_string(s):
    return s.title()

def swap_case_string(s):
    return s.swapcase()

def is_uppercase(s):
    return s.isupper()

def is_lowercase(s):
    return s.islower()

def convert_to_title_case(s):
    return s.title()

def check_if_string_contains_digit(s):
    return any(char.isdigit() for char in s)

def check_if_string_is_alpha(s):
    return s.isalpha()

def check_if_string_is_digit(s):
    return s.isdigit()

def check_if_string_is_alphanumeric(s):
    return s.isalnum()

def check_if_string_is_space(s):
    return s.isspace()

def split_string(s, delimiter=' '):
    return s.split(delimiter)

def join_list(lst, delimiter=' '):
    return delimiter.join(lst)

def find_last_occurrence_of_substring(s, sub):
    return s.rfind(sub)

def find_first_occurrence_of_substring(s, sub):
    return s.find(sub)

def remove_first_occurrence_of_substring(s, sub):
    return s.replace(sub, '', 1)

def remove_last_occurrence_of_substring(s, sub):
    pos = s.rfind(sub)
    if pos != -1:
        return s[:pos] + s[pos+len(sub):]
    return s

def check_if_substring_exists(s, sub):
    return sub in s

def convert_string_to_bytes(s, encoding='utf-8'):
    return s.encode(encoding)

def convert_bytes_to_string(b, encoding='utf-8'):
    return b.decode(encoding)

def check_if_key_in_dict(d, key):
    return key in d

def check_if_value_in_dict(d, value):
    return value in d.values()

def get_value_from_dict(d, key, default=None):
    return d.get(key, default)

def set_value_in_dict(d, key, value):
    d[key] = value

def remove_key_from_dict(d, key):
    if key in d:
        del d[key]

def get_keys_from_dict(d):
    return list(d.keys())

def get_values_from_dict(d):
    return list(d.values())

def get_items_from_dict(d):
    return list(d.items())

def update_dict(d, other):
    d.update(other)

def clear_dict(d):
    d.clear()

def create_dict_from_keys_values(keys, values):
    return dict(zip(keys, values))

def invert_dict(d):
    return {v: k for k, v in d.items()}

def merge_lists(lst1, lst2):
    return lst1 + lst2

def zip_lists(lst1, lst2):
    return list(zip(lst1, lst2))

def unzip_list_of_tuples(lst):
    return list(zip(*lst))

def rotate_list_left(lst, n):
    return lst[n:] + lst[:n]

def rotate_list_right(lst, n):
    return lst[-n:] + lst[:-n]

def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

def is_power_of_three(n):
    if n <= 0:
        return False
    while n % 3 == 0:
        n //= 3
    return n == 1

def is_power_of_four(n):
    if n <= 0:
        return False
    while n % 4 == 0:
        n //= 4
    return n == 1

def is_power_of_five(n):
    if n <= 0:
        return False
    while n % 5 == 0:
        n //= 5
    return n == 1

def calculate_power(base, exponent):
    return base ** exponent

def calculate_nth_root(number, n):
    return number ** (1 / n)

def calculate_logarithm_base_10(x):
    import math
    return math.log10(x)

def calculate_logarithm_base_2(x):
    import math
    return math.log2(x)

def calculate_natural_logarithm(x):
    import math
    return math.log(x)

def calculate_exponential(x):
    import math
    return math.exp(x)

def calculate_sine(angle):
    import math
    return math.sin(math.radians(angle))

def calculate_cosine(angle):
    import math
    return math.cos(math.radians(angle))

def calculate_tangent(angle):
    import math
    return math.tan(math.radians(angle))

def calculate_arcsine(value):
    import math
    return math.degrees(math.asin(value))

def calculate_arccosine(value):
    import math
    return math.degrees(math.acos(value))

def calculate_arctangent(value):
    import math
    return math.degrees(math.atan(value))

def generate_random_integer(min_value, max_value):
    import random
    return random.randint(min_value, max_value)

def generate_random_float(min_value, max_value):
    import random
    return random.uniform(min_value, max_value)

def shuffle_list(lst):
    import random
    random.shuffle(lst)
    return lst

def select_random_element(lst):
    import random
    return random.choice(lst)

def select_random_sample(lst, n):
    import random
    return random.sample(lst, n)

def generate_random_string(length):
    import random
    import string
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def generate_uuid():
    import uuid
    return str(uuid.uuid4())

def calculate_hypotenuse(a, b):
    import math
    return math.hypot(a, b)

def calculate_distance_between_points(x1, y1, x2, y2):
    import math
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def calculate_chebyshev_distance(x1, y1, x2, y2):
    return max(abs(x1 - x2), abs(y1 - y2))

def calculate_hamming_distance(s1, s2):
    return sum(el1 != el2 for el1, el2 in zip(s1, s2))

def calculate_jaccard_similarity(set1, set2):
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    return len(intersection) / len(union)

def calculate_euclidean_norm(vector):
    import math
    return math.sqrt(sum(x**2 for x in vector))

def calculate_magnitude_of_vector(vector):
    import math
    return math.sqrt(sum(x**2 for x in vector))

def normalize_vector(vector):
    magnitude = calculate_magnitude_of_vector(vector)
    return [x / magnitude for x in vector]

def dot_product(vector1, vector2):
    return sum(x * y for x, y in zip(vector1, vector2))

def cross_product(vector1, vector2):
    return [
        vector1[1] * vector2[2] - vector1[2] * vector2[1],
        vector1[2] * vector2[0] - vector1[0] * vector2[2],
        vector1[0] * vector2[1] - vector1[1] * vector2[0]
    ]

def calculate_angle_between_vectors(vector1, vector2):
    import math
    dot_prod = dot_product(vector1, vector2)
    magnitude1 = calculate_magnitude_of_vector(vector1)
    magnitude2 = calculate_magnitude_of_vector(vector2)
    return math.degrees(math.acos(dot_prod / (magnitude1 * magnitude2)))

def calculate_determinant_of_2x2_matrix(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

def calculate_determinant_of_3x3_matrix(matrix):