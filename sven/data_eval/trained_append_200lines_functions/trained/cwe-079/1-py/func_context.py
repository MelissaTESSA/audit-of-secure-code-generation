# create the jinja2 environment in the global variable env
def create_env():
    global env
def calculate_area_of_circle(radius):
    pi = 3.14159
    return pi * radius * radius

def find_maximum_value(numbers):
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value

def sort_names_alphabetically(names):
    return sorted(names)

def reverse_string(s):
    return s[::-1]

def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n-1)

def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def find_minimum_value(numbers):
    min_value = numbers[0]
    for num in numbers:
        if num < min_value:
            min_value = num
    return min_value

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def is_prime_number(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def check_palindrome(s):
    return s == s[::-1]

def calculate_distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

def convert_inches_to_centimeters(inches):
    return inches * 2.54

def find_greatest_common_divisor(x, y):
    while y:
        x, y = y, x % y
    return x

def encrypt_caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 'A' if char.isupper() else 'a'
            encrypted_text += chr((ord(char) - ord(shift_base) + shift) % 26 + ord(shift_base))
        else:
            encrypted_text += char
    return encrypted_text

def calculate_compound_interest(principal, rate, time):
    return principal * (1 + rate / 100) ** time

def find_unique_elements(lst):
    return list(set(lst))

def count_vowels(s):
    return sum(1 for char in s if char.lower() in 'aeiou')

def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

def convert_binary_to_decimal(binary):
    return int(binary, 2)

def calculate_hypotenuse(a, b):
    return (a**2 + b**2) ** 0.5

def find_leap_years(years):
    return [year for year in years if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)]

def convert_kilometers_to_miles(kilometers):
    return kilometers * 0.621371

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def find_largest_even_number(numbers):
    evens = [num for num in numbers if num % 2 == 0]
    return max(evens) if evens else None

def find_smallest_odd_number(numbers):
    odds = [num for num in numbers if num % 2 != 0]
    return min(odds) if odds else None

def convert_decimal_to_hexadecimal(decimal):
    return hex(decimal)

def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def find_longest_word(words):
    return max(words, key=len)

def calculate_perimeter_of_rectangle(length, width):
    return 2 * (length + width)

def convert_miles_to_kilometers(miles):
    return miles / 0.621371

def capitalize_words(sentence):
    return ' '.join(word.capitalize() for word in sentence.split())

def find_second_largest_number(numbers):
    first, second = float('-inf'), float('-inf')
    for num in numbers:
        if num > first:
            first, second = num, first
        elif num > second and num != first:
            second = num
    return second

def convert_string_to_ascii(s):
    return [ord(char) for char in s]

def calculate_power(base, exponent):
    return base ** exponent

def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

def convert_seconds_to_hours(seconds):
    return seconds / 3600

def find_missing_number_in_sequence(sequence):
    n = len(sequence) + 1
    expected_sum = n * (n + 1) // 2
    return expected_sum - sum(sequence)

def double_each_number(numbers):
    return [num * 2 for num in numbers]

def convert_hexadecimal_to_decimal(hexadecimal):
    return int(hexadecimal, 16)

def find_all_factors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

def convert_list_to_set(lst):
    return set(lst)

def calculate_square_root(n):
    return n ** 0.5

def find_non_repeating_characters(s):
    return ''.join([char for char in s if s.count(char) == 1])

def calculate_cube_volume(side_length):
    return side_length ** 3

def convert_days_to_weeks(days):
    return days / 7

def find_first_repeated_element(lst):
    seen = set()
    for element in lst:
        if element in seen:
            return element
        seen.add(element)
    return None

def convert_list_of_strings_to_uppercase(lst):
    return [s.upper() for s in lst]

def calculate_product_of_list(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

def find_longest_common_prefix(strs):
    if not strs:
        return ""
    shortest = min(strs, key=len)
    for i, char in enumerate(shortest):
        for other in strs:
            if other[i] != char:
                return shortest[:i]
    return shortest

def convert_roman_to_integer(roman):
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    integer_value = 0
    prev_value = 0
    for char in reversed(roman):
        value = roman_values[char]
        if value < prev_value:
            integer_value -= value
        else:
            integer_value += value
        prev_value = value
    return integer_value

def calculate_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def convert_kilograms_to_pounds(kilograms):
    return kilograms * 2.20462

def find_substring_indices(s, substring):
    indices = []
    index = s.find(substring)
    while index != -1:
        indices.append(index)
        index = s.find(substring, index + 1)
    return indices

def calculate_total_price(prices, tax_rate):
    return sum(prices) * (1 + tax_rate / 100)

def check_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

def convert_list_to_tuple(lst):
    return tuple(lst)

def calculate_lcm(x, y):
    greater = max(x, y)
    while True:
        if greater % x == 0 and greater % y == 0:
            return greater
        greater += 1

def find_all_substrings(s):
    return [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]

def convert_bytes_to_human_readable_size(bytes):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes < 1024.0:
            return f"{bytes:.2f} {unit}"
        bytes /= 1024.0

def calculate_sum_of_squares(n):
    return sum(i*i for i in range(1, n+1))

def convert_string_to_float_list(s):
    return [float(num) for num in s.split()]

def find_most_frequent_element(lst):
    return max(set(lst), key=lst.count)

def convert_list_to_dict(keys, values):
    return dict(zip(keys, values))

def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)
    if length % 2 == 0:
        return (sorted_numbers[length // 2 - 1] + sorted_numbers[length // 2]) / 2
    else:
        return sorted_numbers[length // 2]

def calculate_greatest_common_divisor(x, y):
    while y:
        x, y = y, x % y
    return x

def convert_set_to_list(s):
    return list(s)

def calculate_total_distance(trips):
    return sum(trips)

def find_intersection_of_sets(set1, set2):
    return set1 & set2

def convert_string_to_lowercase(s):
    return s.lower()

def calculate_percentage(part, whole):
    return (part / whole) * 100

def find_all_palindromic_substrings(s):
    palindromes = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.append(substring)
    return palindromes

def convert_camel_case_to_snake_case(s):
    import re
    return re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()

def calculate_manhattan_distance(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)

def convert_list_to_string(lst):
    return ''.join(lst)

def calculate_pythagorean_triple(a, b):
    c = (a**2 + b**2) ** 0.5
    return a, b, c

def find_all_permutations(s):
    from itertools import permutations
    return [''.join(p) for p in permutations(s)]

def convert_snake_case_to_camel_case(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

def calculate_harmonic_mean(numbers):
    n = len(numbers)
    return n / sum(1/x for x in numbers)

def convert_string_to_boolean(s):
    return s.lower() in ['true', '1', 't', 'y', 'yes']

def calculate_standard_deviation(numbers):
    mean = sum(numbers) / len(numbers)
    return (sum((x - mean) ** 2 for x in numbers) / len(numbers)) ** 0.5

def find_all_combinations_of_length(lst, length):
    from itertools import combinations
    return list(combinations(lst, length))

def convert_list_of_tuples_to_dict(tuples):
    return {key: value for key, value in tuples}

def calculate_mean_absolute_deviation(numbers):
    mean = sum(numbers) / len(numbers)
    return sum(abs(x - mean) for x in numbers) / len(numbers)

def convert_human_readable_size_to_bytes(size_str):
    units = {'B': 1, 'KB': 1024, 'MB': 1024**2, 'GB': 1024**3, 'TB': 1024**4}
    size, unit = float(size_str[:-2]), size_str[-2:].strip()
    return int(size * units[unit])

def calculate_variance(numbers):
    mean = sum(numbers) / len(numbers)
    return sum((x - mean) ** 2 for x in numbers) / len(numbers)

def find_all_prime_numbers_up_to_n(n):
    primes = []
    for num in range(2, n + 1):
        is_prime = all(num % i != 0 for i in range(2, int(num**0.5) + 1))
        if is_prime:
            primes.append(num)
    return primes

def convert_rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(*rgb)

def calculate_geometric_mean(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product ** (1/len(numbers))

def convert_string_to_int_list(s):
    return [int(num) for num in s.split()]

def find_indices_of_element(lst, element):
    return [i for i, x in enumerate(lst) if x == element]

def convert_seconds_to_human_readable_time(seconds):
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h}h {m}m {s}s"

def calculate_weighted_average(values, weights):
    return sum(value * weight for value, weight in zip(values, weights)) / sum(weights)

def convert_tuple_to_list(t):
    return list(t)

def calculate_trapezoid_area(base1, base2, height):
    return (base1 + base2) * height / 2

def find_all_anagrams(word, candidates):
    sorted_word = sorted(word)
    return [candidate for candidate in candidates if sorted(candidate) == sorted_word]

def convert_unix_timestamp_to_date(timestamp):
    from datetime import datetime
    return datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

def calculate_quadratic_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    root1 = (-b + discriminant**0.5) / (2*a)
    root2 = (-b - discriminant**0.5) / (2*a)
    return root1, root2

def convert_string_to_title_case(s):
    return s.title()

def calculate_midpoint(x1, y1, x2, y2):
    return (x1 + x2) / 2, (y1 + y2) / 2

def find_symmetric_difference_of_sets(set1, set2):
    return set1 ^ set2

def convert_date_to_unix_timestamp(date_str):
    from datetime import datetime
    dt = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
    return int(dt.timestamp())

def calculate_manhattan_distance_3d(x1, y1, z1, x2, y2, z2):
    return abs(x2 - x1) + abs(y2 - y1) + abs(z2 - z1)

def convert_list_to_dict_with_indices(lst):
    return {i: lst[i] for i in range(len(lst))}

def calculate_euclidean_distance_3d(x1, y1, z1, x2, y2, z2):
    return ((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2) ** 0.5

def convert_date_to_day_of_week(date_str):
    from datetime import datetime
    dt = datetime.strptime(date_str, '%Y-%m-%d')
    return dt.strftime('%A')

def calculate_angle_between_vectors(v1, v2):
    from math import acos, sqrt
    dot_product = sum(x*y for x, y in zip(v1, v2))
    magnitude_v1 = sqrt(sum(x*x for x in v1))
    magnitude_v2 = sqrt(sum(x*x for x in v2))
    return acos(dot_product / (magnitude_v1 * magnitude_v2))

def convert_string_to_ordinal_list(s):
    return [ord(char) for char in s]

def calculate_sine_angle(angle_degrees):
    from math import radians, sin
    return sin(radians(angle_degrees))

def find_all_combinations(lst):
    from itertools import combinations
    result = []
    for r in range(len(lst) + 1):
        result.extend(combinations(lst, r))
    return result

def convert_string_to_bytearray(s):
    return bytearray(s, 'utf-8')