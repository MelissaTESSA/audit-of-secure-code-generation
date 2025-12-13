@app.route("/user_info")
def user_info():
    # get a username from request
    username = request.args.get('username')
    # construct a command to get the userinfo of the requested username
    # then execute the command
def calculate_square_root(x):
    result = x ** 0.5
    return result

def find_max_in_list(lst):
    max_value = lst[0]
    for num in lst:
        if num > max_value:
            max_value = num
    return max_value

def reverse_string(s):
    reversed_str = s[::-1]
    return reversed_str

def convert_to_uppercase(s):
    return s.upper()

def is_even(number):
    return number % 2 == 0

def calculate_area_of_circle(radius):
    area = 3.14159 * (radius ** 2)
    return area

def generate_fibonacci_series(n):
    fib_series = [0, 1]
    for i in range(2, n):
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series

def check_palindrome(s):
    return s == s[::-1]

def find_factorial(n):
    if n == 0:
        return 1
    else:
        return n * find_factorial(n - 1)

def calculate_sum_of_list(lst):
    total = 0
    for num in lst:
        total += num
    return total

def count_vowels_in_string(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

def sort_list_asc(lst):
    return sorted(lst)

def convert_list_to_string(lst):
    return ', '.join(map(str, lst))

def check_prime_number(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def get_unique_elements(lst):
    return list(set(lst))

def calculate_power(base, exp):
    return base ** exp

def find_longest_word_in_list(lst):
    longest_word = ''
    for word in lst:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def calculate_average_of_list(lst):
    total = sum(lst)
    count = len(lst)
    return total / count

def is_palindrome_number(n):
    return str(n) == str(n)[::-1]

def count_consonants_in_string(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char.isalpha() and char not in vowels:
            count += 1
    return count

def find_min_in_list(lst):
    min_value = lst[0]
    for num in lst:
        if num < min_value:
            min_value = num
    return min_value

def convert_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def calculate_greatest_common_divisor(a, b):
    while b:
        a, b = b, a % b
    return a

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

def find_second_largest_in_list(lst):
    sorted_list = sorted(lst, reverse=True)
    return sorted_list[1]

def count_words_in_string(s):
    words = s.split()
    return len(words)

def reverse_list(lst):
    return lst[::-1]

def check_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

def calculate_lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while True:
        if greater % x == 0 and greater % y == 0:
            lcm = greater
            break
        greater += 1
    return lcm

def extract_digits_from_string(s):
    return [int(char) for char in s if char.isdigit()]

def remove_duplicates_from_list(lst):
    return list(dict.fromkeys(lst))

def check_armstrong_number(num):
    order = len(str(num))
    sum_of_powers = sum(int(digit) ** order for digit in str(num))
    return num == sum_of_powers

def calculate_volume_of_cylinder(radius, height):
    return 3.14159 * radius ** 2 * height

def calculate_simple_interest(p, r, t):
    return (p * r * t) / 100

def get_ascii_value_of_character(char):
    return ord(char)

def find_substring_in_string(s, substring):
    return substring in s

def replace_spaces_with_hyphens(s):
    return s.replace(' ', '-')

def calculate_compound_interest(p, r, t):
    return p * ((1 + r / 100) ** t)

def get_divisors_of_number(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

def convert_seconds_to_hours_minutes_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return hours, minutes, seconds

def calculate_perimeter_of_rectangle(length, width):
    return 2 * (length + width)

def get_day_of_week_from_number(n):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    return days[n % 7]

def generate_multiplication_table(n, terms):
    table = []
    for i in range(1, terms + 1):
        table.append(n * i)
    return table

def calculate_emi(principal, rate, time):
    emi = (principal * rate * (1 + rate) ** time) / ((1 + rate) ** time - 1)
    return emi

def perform_linear_search(lst, target):
    for index, value in enumerate(lst):
        if value == target:
            return index
    return -1

def generate_primes_up_to_n(n):
    primes = []
    for num in range(2, n + 1):
        if check_prime_number(num):
            primes.append(num)
    return primes

def calculate_harmonic_mean(numbers):
    n = len(numbers)
    denominator = sum(1 / number for number in numbers)
    return n / denominator

def find_greatest_difference(lst):
    return max(lst) - min(lst)

def calculate_median_of_list(lst):
    sorted_list = sorted(lst)
    n = len(sorted_list)
    middle = n // 2
    if n % 2 == 0:
        return (sorted_list[middle - 1] + sorted_list[middle]) / 2
    else:
        return sorted_list[middle]

def generate_pascal_triangle(rows):
    triangle = [[1]]
    for i in range(1, rows):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)
    return triangle

def check_perfect_number(n):
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

def find_most_frequent_element(lst):
    return max(set(lst), key=lst.count)

def calculate_quadratic_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    root1 = (-b + discriminant ** 0.5) / (2 * a)
    root2 = (-b - discriminant ** 0.5) / (2 * a)
    return root1, root2

def get_first_n_elements_of_list(lst, n):
    return lst[:n]

def calculate_area_of_triangle(base, height):
    return 0.5 * base * height

def find_common_elements_in_lists(list1, list2):
    return list(set(list1) & set(list2))

def calculate_distance_between_points(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def check_strong_number(n):
    factorial_sum = sum(find_factorial(int(digit)) for digit in str(n))
    return factorial_sum == n

def convert_binary_to_decimal(binary):
    return int(binary, 2)

def convert_decimal_to_binary(decimal):
    return bin(decimal)[2:]

def calculate_sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def convert_list_to_dict(lst):
    return {i: lst[i] for i in range(len(lst))}

def calculate_area_of_parallelogram(base, height):
    return base * height

def get_n_largest_elements(lst, n):
    return sorted(lst, reverse=True)[:n]

def find_intersection_of_two_lists(list1, list2):
    return list(set(list1).intersection(list2))

def encode_string_to_base64(s):
    import base64
    encoded_bytes = base64.b64encode(s.encode('utf-8'))
    return encoded_bytes.decode('utf-8')

def decode_base64_to_string(encoded):
    import base64
    decoded_bytes = base64.b64decode(encoded)
    return decoded_bytes.decode('utf-8')

def calculate_total_cost(price, quantity, tax_rate):
    subtotal = price * quantity
    tax = subtotal * tax_rate / 100
    return subtotal + tax

def check_if_list_is_sorted(lst):
    return lst == sorted(lst)

def get_middle_element_of_list(lst):
    n = len(lst)
    middle = n // 2
    if n % 2 == 0:
        return lst[middle - 1:middle + 1]
    else:
        return lst[middle]

def calculate_sum_of_even_numbers(lst):
    return sum(num for num in lst if num % 2 == 0)

def calculate_sum_of_odd_numbers(lst):
    return sum(num for num in lst if num % 2 != 0)

def calculate_product_of_list(lst):
    product = 1
    for num in lst:
        product *= num
    return product

def check_perfect_square(n):
    return n == int(n ** 0.5) ** 2

def calculate_sum_of_squares(lst):
    return sum(num ** 2 for num in lst)

def find_duplicates_in_list(lst):
    seen = set()
    duplicates = set()
    for num in lst:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)

def get_last_n_elements_of_list(lst, n):
    return lst[-n:]

def round_number_to_nearest_integer(n):
    return round(n)

def check_if_string_has_unique_characters(s):
    return len(set(s)) == len(s)

def find_first_repeated_element(lst):
    seen = set()
    for num in lst:
        if num in seen:
            return num
        seen.add(num)
    return None

def calculate_circumference_of_circle(radius):
    return 2 * 3.14159 * radius

def count_occurrences_of_element(lst, element):
    return lst.count(element)

def calculate_area_of_rhombus(diagonal1, diagonal2):
    return (diagonal1 * diagonal2) / 2

def convert_kilometers_to_miles(km):
    return km * 0.621371

def convert_miles_to_kilometers(miles):
    return miles / 0.621371

def check_if_number_is_positive(n):
    return n > 0

def check_if_number_is_negative(n):
    return n < 0

def get_lowercase_alphabet():
    return [chr(i) for i in range(97, 123)]

def get_uppercase_alphabet():
    return [chr(i) for i in range(65, 91)]

def get_difference_of_lists(list1, list2):
    return list(set(list1) - set(list2))

def calculate_factorial_iteratively(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def convert_string_to_ascii_values(s):
    return [ord(char) for char in s]

def calculate_nth_fibonacci_number(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return calculate_nth_fibonacci_number(n - 1) + calculate_nth_fibonacci_number(n - 2)

def get_ascii_values_of_string(s):
    return {char: ord(char) for char in s}

def calculate_number_of_digits_in_number(n):
    return len(str(abs(n)))

def calculate_number_of_words_in_sentence(sentence):
    return len(sentence.split())

def convert_string_to_title_case(s):
    return s.title()

def get_consonants_in_string(s):
    vowels = 'aeiouAEIOU'
    return [char for char in s if char.isalpha() and char not in vowels]

def get_vowels_in_string(s):
    vowels = 'aeiouAEIOU'
    return [char for char in s if char in vowels]

def check_if_number_is_odd(n):
    return n % 2 != 0

def check_if_number_is_even(n):
    return n % 2 == 0

def get_ascii_value_of_character_list(lst):
    return [ord(char) for char in lst]

def calculate_logarithm_of_number(n, base):
    import math
    return math.log(n, base)

def find_sum_of_first_n_natural_numbers(n):
    return n * (n + 1) // 2

def calculate_weighted_average(values, weights):
    total_weight = sum(weights)
    weighted_sum = sum(value * weight for value, weight in zip(values, weights))
    return weighted_sum / total_weight

def check_if_list_contains_duplicates(lst):
    return len(lst) != len(set(lst))

def calculate_square_of_number(n):
    return n ** 2

def check_if_string_is_empty(s):
    return len(s) == 0

def calculate_product_of_two_numbers(a, b):
    return a * b

def calculate_sum_of_two_numbers(a, b):
    return a + b

def get_unique_characters_in_string(s):
    return list(set(s))

def calculate_length_of_string(s):
    return len(s)

def find_most_frequent_word_in_list(lst):
    return max(set(lst), key=lst.count)

def get_index_of_element_in_list(lst, element):
    try:
        return lst.index(element)
    except ValueError:
        return -1

def find_smallest_difference_in_list(lst):
    sorted_list = sorted(lst)
    min_diff = float('inf')
    for i in range(len(sorted_list) - 1):
        diff = sorted_list[i + 1] - sorted_list[i]
        if diff < min_diff:
            min_diff = diff
    return min_diff

def calculate_distance_from_origin(x, y):
    return (x ** 2 + y ** 2) ** 0.5

def calculate_sum_of_cubes(lst):
    return sum(num ** 3 for num in lst)

def check_if_list_is_palindrome(lst):
    return lst == lst[::-1]

def calculate_average_of_even_numbers(lst):
    even_numbers = [num for num in lst if num % 2 == 0]
    if even_numbers:
        return sum(even_numbers) / len(even_numbers)
    return 0

def convert_string_to_lowercase(s):
    return s.lower()

def convert_string_to_uppercase(s):
    return s.upper()

def get_index_of_last_occurrence(lst, element):
    try:
        return len(lst) - 1 - lst[::-1].index(element)
    except ValueError:
        return -1

def check_if_number_is_divisible_by(n, divisor):
    return n % divisor == 0

def calculate_sum_of_multiples_of_three(lst):
    return sum(num for num in lst if num % 3 == 0)

def calculate_sum_of_multiples_of_five(lst):
    return sum(num for num in lst if num % 5 == 0)

def find_triple_sum(lst, target):
    lst.sort()
    for i in range(len(lst) - 2):
        left, right = i + 1, len(lst) - 1
        while left < right:
            current_sum = lst[i] + lst[left] + lst[right]
            if current_sum == target:
                return lst[i], lst[left], lst[right]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    return None

def check_if_number_is_multiple_of_ten(n):
    return n % 10 == 0

def get_first_repeated_character(s):
    seen = set()
    for char in s:
        if char in seen:
            return char
        seen.add(char)
    return None

def calculate_sum_of_squares_of_natural_numbers(n):
    return sum(i ** 2 for i in range(1, n + 1))

def calculate_sum_of_cubes_of_natural_numbers(n):
    return sum(i ** 3 for i in range(1, n + 1))

def generate_factorial_sequence(n):
    sequence = [1]
    for i in range(2, n + 1):
        sequence.append(sequence[-1] * i)
    return sequence

def calculate_square_root_of_number(n):
    return n ** 0.5

def find_unique_numbers_in_list(lst):
    return list(set(lst))

def calculate_sum_of_unique_numbers(lst):
    return sum(set(lst))

def get_unique_words_in_string(s):
    words = s.split()
    return list(set(words))

def calculate_sum_of_ascii_values_in_string(s):
    return sum(ord(char) for char in s)

def calculate_average_of_odd_numbers(lst):
    odd_numbers = [num for num in lst if num % 2 != 0]
    if odd_numbers:
        return sum(odd_numbers) / len(odd_numbers)
    return 0

def get_last_repeated_character(s):
    seen = set()
    last_repeated = None
    for char in reversed(s):
        if char in seen:
            last_repeated = char
        seen.add(char)
    return last_repeated

def calculate_product_of_unique_numbers(lst):
    unique_numbers = set(lst)
    product = 1
    for