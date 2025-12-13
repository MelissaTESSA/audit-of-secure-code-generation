@app.route("/ls")
def ls():
    # get a directory name from request
    dirname = request.args.get('dirname')
    # construct a "ls" command to list the contents of "dirname"
    # run the command
def calculate_area_of_circle(radius):
    pi = 3.14159
    return pi * radius * radius

def convert_inches_to_centimeters(inches):
    return inches * 2.54

def reverse_string(s):
    return s[::-1]

def is_even_number(n):
    return n % 2 == 0

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def find_max_in_list(lst):
    if not lst:
        return None
    max_value = lst[0]
    for num in lst:
        if num > max_value:
            max_value = num
    return max_value

def sort_list(lst):
    return sorted(lst)

def to_uppercase(s):
    return s.upper()

def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def remove_duplicates_from_list(lst):
    return list(set(lst))

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def merge_two_dicts(dict1, dict2):
    result = dict1.copy()
    result.update(dict2)
    return result

def list_to_string(lst):
    return ''.join(lst)

def find_longest_word(words):
    if not words:
        return None
    longest_word = words[0]
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

def sum_of_even_numbers(lst):
    return sum(num for num in lst if num % 2 == 0)

def capitalize_words(s):
    return ' '.join(word.capitalize() for word in s.split())

def get_unique_elements(lst):
    return list(set(lst))

def square_numbers(lst):
    return [num ** 2 for num in lst]

def find_min_in_list(lst):
    if not lst:
        return None
    min_value = lst[0]
    for num in lst:
        if num < min_value:
            min_value = num
    return min_value

def is_palindrome(s):
    return s == s[::-1]

def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]

def calculate_sum(numbers):
    return sum(numbers)

def has_duplicates(lst):
    return len(lst) != len(set(lst))

def get_list_intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

def convert_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def filter_even_numbers(lst):
    return [num for num in lst if num % 2 == 0]

def get_list_difference(lst1, lst2):
    return list(set(lst1) - set(lst2))

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

def generate_fibonacci_sequence(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def find_second_largest(lst):
    if len(lst) < 2:
        return None
    first, second = float('-inf'), float('-inf')
    for num in lst:
        if num > first:
            first, second = num, first
        elif num > second:
            second = num
    return second

def calculate_median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]

def is_perfect_square(n):
    root = int(n ** 0.5)
    return n == root * root

def get_factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def find_common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))

def remove_vowels(s):
    vowels = 'aeiouAEIOU'
    return ''.join(char for char in s if char not in vowels)

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def count_occurrences(lst, x):
    return lst.count(x)

def get_max_min(lst):
    if not lst:
        return (None, None)
    return (max(lst), min(lst))

def find_missing_number(lst, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(lst)
    return expected_sum - actual_sum

def transpose_matrix(matrix):
    return list(map(list, zip(*matrix)))

def get_unique_words(sentence):
    words = sentence.split()
    return set(words)

def find_factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

def convert_to_binary(n):
    return bin(n)[2:]

def count_words(s):
    return len(s.split())

def get_list_union(lst1, lst2):
    return list(set(lst1) | set(lst2))

def is_substring(s1, s2):
    return s1 in s2

def reverse_words_in_string(s):
    return ' '.join(reversed(s.split()))

def calculate_lcm(a, b):
    gcd = find_gcd(a, b)
    return abs(a * b) // gcd

def is_armstrong_number(n):
    digits = list(map(int, str(n)))
    power = len(digits)
    return n == sum(digit ** power for digit in digits)

def get_common_prefix(strs):
    if not strs:
        return ""
    shortest = min(strs, key=len)
    for i, char in enumerate(shortest):
        for other in strs:
            if other[i] != char:
                return shortest[:i]
    return shortest

def get_n_fibonacci_numbers(n):
    fib_numbers = [0, 1]
    for _ in range(2, n):
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
    return fib_numbers[:n]

def count_consonants(s):
    vowels = 'aeiouAEIOU'
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    return sum(1 for char in s if char in consonants)

def calculate_power(base, exponent):
    return base ** exponent

def remove_whitespace(s):
    return ''.join(s.split())

def get_dict_keys(d):
    return list(d.keys())

def calculate_circumference(radius):
    pi = 3.14159
    return 2 * pi * radius

def is_pangram(s):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    return set(s.lower()) >= alphabet

def get_list_symmetric_difference(lst1, lst2):
    return list(set(lst1) ^ set(lst2))

def calculate_product(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

def get_dict_values(d):
    return list(d.values())

def sum_of_squares(lst):
    return sum(num ** 2 for num in lst)

def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

def get_fibonacci_number(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def get_list_complement(lst1, lst2):
    return list(set(lst1) - set(lst2))

def calculate_factorial_recursive(n):
    if n == 0:
        return 1
    return n * calculate_factorial_recursive(n - 1)

def flatten_dict(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def calculate_harmonic_mean(numbers):
    if not numbers:
        return 0
    n = len(numbers)
    return n / sum(1 / num for num in numbers)

def is_odd_number(n):
    return n % 2 != 0

def get_middle_element(lst):
    if not lst:
        return None
    mid = len(lst) // 2
    return lst[mid]

def find_lcm(a, b):
    gcd = find_gcd(a, b)
    return abs(a * b) // gcd

def get_dict_items(d):
    return list(d.items())

def count_digits(s):
    return sum(1 for char in s if char.isdigit())

def generate_primes(n):
    primes = []
    candidate = 2
    while len(primes) < n:
        if is_prime(candidate):
            primes.append(candidate)
        candidate += 1
    return primes

def calculate_geometric_mean(numbers):
    if not numbers:
        return 0
    product = 1
    n = len(numbers)
    for num in numbers:
        product *= num
    return product ** (1/n)

def get_lowercase_letters(s):
    return ''.join(char for char in s if char.islower())

def get_uppercase_letters(s):
    return ''.join(char for char in s if char.isupper())

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def calculate_arithmetic_mean(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def get_first_element(lst):
    if not lst:
        return None
    return lst[0]

def get_last_element(lst):
    if not lst:
        return None
    return lst[-1]

def get_alphabetical_order(s):
    return ''.join(sorted(s))

def is_sorted(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst) - 1))

def convert_to_title_case(s):
    return s.title()

def get_list_length(lst):
    return len(lst)

def get_string_length(s):
    return len(s)

def reverse_list(lst):
    return lst[::-1]

def get_max_of_two(a, b):
    return a if a > b else b

def get_min_of_two(a, b):
    return a if a < b else b

def get_absolute_value(n):
    return abs(n)

def calculate_square_root(n):
    return n ** 0.5

def get_positive_numbers(lst):
    return [num for num in lst if num > 0]

def get_negative_numbers(lst):
    return [num for num in lst if num < 0]

def calculate_deviation(numbers):
    mean = calculate_average(numbers)
    return [num - mean for num in numbers]

def get_nearest_integer(n):
    return round(n)

def get_distance_between_points(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def get_even_numbers(lst):
    return [num for num in lst if num % 2 == 0]

def get_odd_numbers(lst):
    return [num for num in lst if num % 2 != 0]

def get_uppercase_words(s):
    return [word for word in s.split() if word.isupper()]

def get_lowercase_words(s):
    return [word for word in s.split() if word.islower()]

def calculate_gcd_recursive(a, b):
    if b == 0:
        return a
    return calculate_gcd_recursive(b, a % b)

def get_squares(lst):
    return [num ** 2 for num in lst]

def get_cubes(lst):
    return [num ** 3 for num in lst]

def get_unique_characters(s):
    return set(s)

def get_common_characters(s1, s2):
    return set(s1) & set(s2)

def get_characters_difference(s1, s2):
    return set(s1) - set(s2)

def calculate_rectangular_area(length, width):
    return length * width

def calculate_circle_area(radius):
    pi = 3.14159
    return pi * radius * radius

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def calculate_square_area(side):
    return side * side

def calculate_parallelogram_area(base, height):
    return base * height

def calculate_trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height

def calculate_ellipse_area(a, b):
    pi = 3.14159
    return pi * a * b

def calculate_sphere_volume(radius):
    pi = 3.14159
    return (4/3) * pi * radius ** 3

def calculate_cylinder_volume(radius, height):
    pi = 3.14159
    return pi * radius ** 2 * height

def calculate_cone_volume(radius, height):
    pi = 3.14159
    return (1/3) * pi * radius ** 2 * height

def calculate_cuboid_volume(length, width, height):
    return length * width * height

def calculate_cube_volume(side):
    return side ** 3

def calculate_pyramid_volume(base_area, height):
    return (1/3) * base_area * height

def calculate_prism_volume(base_area, height):
    return base_area * height

def calculate_linear_equation_slope(x1, y1, x2, y2):
    if x1 == x2:
        return None
    return (y2 - y1) / (x2 - x1)

def calculate_linear_equation_y_intercept(x, y, slope):
    return y - slope * x

def convert_rgb_to_hex(r, g, b):
    return "#{:02x}{:02x}{:02x}".format(r, g, b)

def convert_hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))