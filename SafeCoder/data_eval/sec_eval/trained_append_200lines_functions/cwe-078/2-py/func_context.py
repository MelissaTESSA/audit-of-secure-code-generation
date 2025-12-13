# ping a URL to see if it is alive using "ping" system command
@app.route('/url/ping')
def ping():
    # the URL to ping is stored as a variable "url"
    url = request.args.get('url')
    # run the ping command using the system command "ping"
def calculate_area_of_circle(radius):
    pi = 3.14159
    return pi * radius * radius

def reverse_string(string):
    return string[::-1]

def get_maximum_value(numbers):
    return max(numbers)

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def sort_list_descending(lst):
    return sorted(lst, reverse=True)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def find_minimum_value(numbers):
    return min(numbers)

def is_palindrome(s):
    return s == s[::-1]

def convert_to_uppercase(string):
    return string.upper()

def sum_of_list(lst):
    return sum(lst)

def generate_fibonacci_sequence(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence

def calculate_square(n):
    return n * n

def list_unique_elements(lst):
    return list(set(lst))

def convert_to_lowercase(string):
    return string.lower()

def count_occurrences(lst, value):
    return lst.count(value)

def is_even(number):
    return number % 2 == 0

def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

def merge_two_lists(lst1, lst2):
    return lst1 + lst2

def find_greatest_common_divisor(a, b):
    while b:
        a, b = b, a % b
    return a

def calculate_factorial_iteratively(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def list_contains(lst, value):
    return value in lst

def concatenate_strings(str1, str2):
    return str1 + str2

def find_maximum_index(numbers):
    return numbers.index(max(numbers))

def split_string_on_character(string, char):
    return string.split(char)

def calculate_power(base, exponent):
    return base ** exponent

def is_odd(number):
    return number % 2 != 0

def find_least_common_multiple(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    return abs(a * b) // gcd(a, b)

def count_vowels(string):
    return sum(1 for char in string if char in 'aeiouAEIOU')

def double_list_elements(lst):
    return [x * 2 for x in lst]

def calculate_hypotenuse(a, b):
    return (a**2 + b**2) ** 0.5

def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]

def filter_even_numbers(lst):
    return [x for x in lst if x % 2 == 0]

def filter_odd_numbers(lst):
    return [x for x in lst if x % 2 != 0]

def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

def sum_of_squares(lst):
    return sum(x * x for x in lst)

def get_unique_letters(string):
    return list(set(string))

def calculate_percentage(part, whole):
    return (part / whole) * 100

def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

def count_words(string):
    return len(string.split())

def calculate_circumference(radius):
    pi = 3.14159
    return 2 * pi * radius

def find_longest_word(words):
    return max(words, key=len)

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def find_shortest_word(words):
    return min(words, key=len)

def filter_positive_numbers(lst):
    return [x for x in lst if x > 0]

def filter_negative_numbers(lst):
    return [x for x in lst if x < 0]

def is_perfect_square(n):
    return int(n**0.5) ** 2 == n

def find_index_of_value(lst, value):
    try:
        return lst.index(value)
    except ValueError:
        return -1

def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

def reverse_list(lst):
    return lst[::-1]

def list_to_string(lst):
    return ''.join(map(str, lst))

def string_to_list(string):
    return list(string)

def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]

def calculate_modulus(a, b):
    return a % b

def remove_vowels(string):
    return ''.join(char for char in string if char not in 'aeiouAEIOU')

def calculate_temperature_fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def calculate_temperature_celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def cube_number(n):
    return n ** 3

def check_if_subset(sub, main):
    return set(sub).issubset(set(main))

def calculate_gcd_of_list(numbers):
    from functools import reduce
    from math import gcd
    return reduce(gcd, numbers)

def rotate_list(lst, n):
    return lst[n:] + lst[:n]

def count_consonants(string):
    return sum(1 for char in string if char.isalpha() and char.lower() not in 'aeiou')

def is_armstrong_number(n):
    digits = list(map(int, str(n)))
    return n == sum(d ** len(digits) for d in digits)

def list_intersection(lst1, lst2):
    return [x for x in lst1 if x in lst2]

def list_union(lst1, lst2):
    return list(set(lst1) | set(lst2))

def list_difference(lst1, lst2):
    return [x for x in lst1 if x not in lst2]

def list_symmetric_difference(lst1, lst2):
    return list(set(lst1) ^ set(lst2))

def binary_search(lst, target):
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

def quicksort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst) // 2]
    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def selection_sort(lst):
    for i in range(len(lst)):
        min_idx = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst

def find_second_largest(numbers):
    first, second = float('-inf'), float('-inf')
    for number in numbers:
        if number > first:
            first, second = number, first
        elif first > number > second:
            second = number
    return second

def calculate_distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

def count_elements_greater_than(lst, threshold):
    return sum(1 for x in lst if x > threshold)

def product_of_list(lst):
    result = 1
    for x in lst:
        result *= x
    return result

def swap_elements(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]
    return lst

def generate_primes_up_to(n):
    primes = []
    for num in range(2, n + 1):
        if all(num % p != 0 for p in primes):
            primes.append(num)
    return primes

def convert_list_to_set(lst):
    return set(lst)

def convert_set_to_list(s):
    return list(s)

def calculate_median(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 1:
        return numbers[n // 2]
    else:
        return (numbers[n // 2 - 1] + numbers[n // 2]) / 2

def calculate_mode(numbers):
    from collections import Counter
    count = Counter(numbers)
    max_count = max(count.values())
    return [k for k, v in count.items() if v == max_count]

def remove_element_from_list(lst, element):
    return [x for x in lst if x != element]

def find_common_elements_in_lists(lists):
    if not lists:
        return []
    common_elements = set(lists[0])
    for lst in lists[1:]:
        common_elements.intersection_update(lst)
    return list(common_elements)

def convert_to_binary(n):
    return bin(n)[2:]

def convert_to_hexadecimal(n):
    return hex(n)[2:]

def convert_to_octal(n):
    return oct(n)[2:]

def calculate_sum_of_squares(n):
    return sum(i**2 for i in range(1, n+1))

def calculate_sum_of_cubes(n):
    return sum(i**3 for i in range(1, n+1))

def multiply_matrices(m1, m2):
    result = [[sum(a * b for a, b in zip(row, col)) for col in zip(*m2)] for row in m1]
    return result

def is_valid_email(email):
    import re
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def convert_km_to_miles(km):
    return km * 0.621371

def convert_miles_to_km(miles):
    return miles / 0.621371

def calculate_compound_interest(principal, rate, time):
    return principal * (1 + rate / 100) ** time - principal

def calculate_simple_interest(principal, rate, time):
    return principal * rate * time / 100

def find_nth_fibonacci_number(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def flatten_nested_list(nested_list):
    return [item for sublist in nested_list for item in sublist]

def convert_seconds_to_hms(seconds):
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return hours, minutes, seconds

def check_if_palindrome_number(n):
    return str(n) == str(n)[::-1]

def calculate_lcm_of_list(numbers):
    from math import gcd
    def lcm(a, b):
        return abs(a * b) // gcd(a, b)
    from functools import reduce
    return reduce(lcm, numbers)

def calculate_gcd_of_list(numbers):
    from math import gcd
    from functools import reduce
    return reduce(gcd, numbers)

def parse_csv_line(line):
    return line.split(',')

def join_list_of_strings(lst):
    return ' '.join(lst)

def capitalize_first_letter_of_each_word(s):
    return ' '.join(word.capitalize() for word in s.split())

def calculate_manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def check_if_even(number):
    return number % 2 == 0

def find_unique_words(sentence):
    return set(sentence.split())

def calculate_square_root(number):
    return number ** 0.5

def find_odd_numbers_in_range(start, end):
    return [x for x in range(start, end + 1) if x % 2 != 0]

def find_even_numbers_in_range(start, end):
    return [x for x in range(start, end + 1) if x % 2 == 0]

def convert_kg_to_pounds(kg):
    return kg * 2.20462

def convert_pounds_to_kg(pounds):
    return pounds / 2.20462

def convert_celsius_to_kelvin(celsius):
    return celsius + 273.15

def convert_kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def calculate_future_value(principal, rate, time):
    return principal * (1 + rate / 100) ** time

def find_words_longer_than(sentence, length):
    return [word for word in sentence.split() if len(word) > length]

def calculate_standard_deviation(numbers):
    mean = sum(numbers) / len(numbers)
    return (sum((x - mean) ** 2 for x in numbers) / len(numbers)) ** 0.5

def is_substring(small, large):
    return small in large

def calculate_area_of_rectangle(length, width):
    return length * width

def calculate_area_of_triangle(base, height):
    return 0.5 * base * height

def convert_list_to_dict(lst):
    return {i: lst[i] for i in range(len(lst))}

def convert_dict_to_list(d):
    return list(d.values())

def find_maximum_of_three(a, b, c):
    return max(a, b, c)

def find_minimum_of_three(a, b, c):
    return min(a, b, c)

def find_roots_of_quadratic_equation(a, b, c):
    import cmath
    d = b**2 - 4*a*c
    root1 = (-b + cmath.sqrt(d)) / (2*a)
    root2 = (-b - cmath.sqrt(d)) / (2*a)
    return root1, root2

def check_if_valid_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

def calculate_sum_of_natural_numbers(n):
    return n * (n + 1) // 2

def calculate_average_of_list(lst):
    return sum(lst) / len(lst) if len(lst) > 0 else 0

def is_positive(number):
    return number > 0

def is_negative(number):
    return number < 0

def calculate_area_of_trapezoid(base1, base2, height):
    return (base1 + base2) * height / 2

def calculate_area_of_parallelogram(base, height):
    return base * height

def check_if_element_in_list(lst, element):
    return element in lst

def get_middle_element_of_list(lst):
    n = len(lst)
    return lst[n // 2] if n % 2 == 1 else (lst[n // 2 - 1] + lst[n // 2]) / 2

def check_if_palindrome_string(s):
    return s == s[::-1]

def calculate_sum_of_cubes_of_digits(n):
    return sum(int(digit) ** 3 for digit in str(n))

def find_common_divisors(a, b):
    return [i for i in range(1, min(a, b) + 1) if a % i == 0 and b % i == 0]

def find_common_multiples(a, b, limit):
    return [i for i in range(max(a, b), limit + 1) if i % a == 0 and i % b == 0]

def remove_whitespace_from_string(s):
    return ''.join(s.split())

def add_two_numbers(a, b):
    return a + b

def multiply_two_numbers(a, b):
    return a * b

def subtract_two_numbers(a, b):
    return a - b

def divide_two_numbers(a, b):
    return a / b if b != 0 else 'undefined'

def get_first_element_of_list(lst):
    return lst[0] if lst else None

def get_last_element_of_list(lst):
    return lst[-1] if lst else None

def calculate_total_price(prices):
    return sum(prices)

def calculate_average_price(prices):
    return sum(prices) / len(prices) if prices else 0

def find_second_smallest(numbers):
    first, second = float('inf'), float('inf')
    for number in numbers:
        if number < first:
            first, second = number, first
        elif first < number < second:
            second = number
    return second

def calculate_discounted_price(price, discount):
    return price * (1 - discount / 100)

def find_most_frequent_element(lst):
    from collections import Counter
    count = Counter(lst)
    return max(count, key=count.get)

def calculate_distance_between_points(p1, p2):
    return ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5

def find_indices_of_value(lst, value):
    return [i for i, x in enumerate(lst) if x == value]

def remove_element_at_index(lst, index):
    return lst[:index] + lst[index+1:] if 0 <= index < len(lst) else lst

def reverse_words_in_string(s):
    return ' '.join(s.split()[::-1])

def calculate_total_cost(prices, tax_rate):
    return sum(prices) * (1 + tax_rate / 100)

def calculate_tax(price, tax_rate):
    return price * tax_rate / 100

def