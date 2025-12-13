@app.route("/read")
def read():
    requested_file_name = request.args.get('filename')
    safe_dir = '/safe/'

    # read the requested file from the safe directory
def calculate_interest_rate(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

def predict_weather_conditions(temperature, humidity, pressure):
    if temperature > 30 and humidity < 50:
        return "Hot and Dry"
    elif temperature < 20 and humidity > 70:
        return "Cool and Humid"
    else:
        return "Moderate"

def process_payment(amount, payment_method):
    if payment_method == "credit_card":
        return amount * 0.98
    elif payment_method == "paypal":
        return amount * 0.97
    else:
        return amount

def generate_fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def format_date_to_string(year, month, day):
    return f"{year}-{month:02d}-{day:02d}"

def compute_factorial(number):
    if number == 0:
        return 1
    else:
        return number * compute_factorial(number - 1)

def find_prime_numbers(limit):
    primes = []
    for num in range(2, limit + 1):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            primes.append(num)
    return primes

def convert_temperature_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def calculate_area_of_circle(radius):
    import math
    return math.pi * radius * radius

def log_user_activity(user_id, activity):
    with open("user_activity.log", "a") as log_file:
        log_file.write(f"User {user_id}: {activity}\n")

def reverse_string(s):
    return s[::-1]

def count_words_in_string(s):
    return len(s.split())

def check_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

def find_greatest_common_divisor(a, b):
    while b:
        a, b = b, a % b
    return a

def simulate_die_rolls(n):
    import random
    return [random.randint(1, 6) for _ in range(n)]

def calculate_bmi(weight, height):
    return weight / (height * height)

def find_unique_elements(lst):
    return list(set(lst))

def convert_seconds_to_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"

def validate_email_address(email):
    import re
    pattern = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
    return re.match(pattern, email)

def compute_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def sort_list_of_strings(strings):
    return sorted(strings)

def calculate_lcm(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    return abs(a * b) // gcd(a, b)

def is_palindrome(s):
    return s == s[::-1]

def generate_random_password(length):
    import string
    import random
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def convert_list_to_string(lst):
    return ', '.join(map(str, lst))

def find_max_in_list(lst):
    return max(lst)

def find_min_in_list(lst):
    return min(lst)

def calculate_median(numbers):
    numbers.sort()
    n = len(numbers)
    mid = n // 2
    if n % 2 == 0:
        return (numbers[mid - 1] + numbers[mid]) / 2
    else:
        return numbers[mid]

def check_if_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def merge_two_dicts(dict1, dict2):
    return {**dict1, **dict2}

def capitalize_words_in_string(s):
    return ' '.join(word.capitalize() for word in s.split())

def convert_km_to_miles(km):
    return km * 0.621371

def convert_miles_to_km(miles):
    return miles / 0.621371

def generate_alphabet_list():
    return [chr(i) for i in range(97, 123)]

def calculate_perimeter_of_rectangle(length, width):
    return 2 * (length + width)

def find_second_largest_in_list(lst):
    unique_lst = list(set(lst))
    unique_lst.sort()
    return unique_lst[-2] if len(unique_lst) > 1 else None

def flatten_nested_list(nested_list):
    return [item for sublist in nested_list for item in sublist]

def count_vowels_in_string(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def find_intersection_of_lists(list1, list2):
    return list(set(list1) & set(list2))

def find_union_of_lists(list1, list2):
    return list(set(list1) | set(list2))

def check_if_perfect_square(number):
    return int(number**0.5) ** 2 == number

def generate_random_numbers(n, start, end):
    import random
    return [random.randint(start, end) for _ in range(n)]

def calculate_total_cost(prices, tax_rate):
    total = sum(prices)
    tax = total * tax_rate
    return total + tax

def find_missing_number_in_sequence(sequence):
    n = len(sequence) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(sequence)
    return expected_sum - actual_sum

def convert_to_uppercase(s):
    return s.upper()

def convert_to_lowercase(s):
    return s.lower()

def compute_square_root(number):
    import math
    return math.sqrt(number)

def find_longest_word_in_string(s):
    words = s.split()
    longest_word = max(words, key=len)
    return longest_word

def filter_even_numbers(lst):
    return [num for num in lst if num % 2 == 0]

def filter_odd_numbers(lst):
    return [num for num in lst if num % 2 != 0]

def compute_power(base, exponent):
    return base ** exponent

def calculate_discounted_price(price, discount):
    return price - (price * discount / 100)

def generate_multiplication_table(number, limit):
    return [number * i for i in range(1, limit + 1)]

def merge_sorted_lists(list1, list2):
    return sorted(list1 + list2)

def find_common_elements_in_lists(list1, list2):
    return list(set(list1) & set(list2))

def calculate_circle_circumference(radius):
    import math
    return 2 * math.pi * radius

def calculate_rectangle_area(length, width):
    return length * width

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def check_if_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def find_most_frequent_element(lst):
    from collections import Counter
    count = Counter(lst)
    return count.most_common(1)[0][0]

def find_least_frequent_element(lst):
    from collections import Counter
    count = Counter(lst)
    return count.most_common()[-1][0]

def compute_degrees_to_radians(degrees):
    import math
    return degrees * (math.pi / 180)

def compute_radians_to_degrees(radians):
    import math
    return radians * (180 / math.pi)

def calculate_compound_interest(principal, rate, time, n):
    return principal * (1 + rate / n) ** (n * time)

def find_duplicates_in_list(lst):
    from collections import Counter
    count = Counter(lst)
    return [item for item, freq in count.items() if freq > 1]

def compute_geometric_mean(numbers):
    product = 1
    for number in numbers:
        product *= number
    return product ** (1/len(numbers))

def generate_random_hex_color():
    import random
    return f"#{random.randint(0, 0xFFFFFF):06x}"

def calculate_hypotenuse(a, b):
    import math
    return math.sqrt(a**2 + b**2)

def convert_binary_to_decimal(binary):
    return int(binary, 2)

def convert_decimal_to_binary(decimal):
    return bin(decimal)[2:]

def calculate_euclidean_distance(x1, y1, x2, y2):
    import math
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def check_if_armstrong_number(number):
    digits = list(map(int, str(number)))
    return number == sum(d ** len(digits) for d in digits)

def calculate_harmonic_mean(numbers):
    return len(numbers) / sum(1 / num for num in numbers)

def convert_hexadecimal_to_decimal(hexadecimal):
    return int(hexadecimal, 16)

def convert_decimal_to_hexadecimal(decimal):
    return hex(decimal)[2:]

def calculate_pythagorean_triplet(a, b):
    import math
    c = math.sqrt(a**2 + b**2)
    return (a, b, int(c)) if c.is_integer() else None

def find_all_factors(number):
    return [i for i in range(1, number + 1) if number % i == 0]

def check_if_perfect_number(number):
    return sum(i for i in range(1, number) if number % i == 0) == number

def calculate_manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def compute_bitwise_and(a, b):
    return a & b

def compute_bitwise_or(a, b):
    return a | b

def compute_bitwise_xor(a, b):
    return a ^ b

def compute_bitwise_not(a):
    return ~a

def compute_bitwise_shift_left(a, n):
    return a << n

def compute_bitwise_shift_right(a, n):
    return a >> n

def find_first_repeating_element(lst):
    seen = set()
    for item in lst:
        if item in seen:
            return item
        seen.add(item)
    return None

def find_first_non_repeating_element(lst):
    from collections import Counter
    count = Counter(lst)
    for item in lst:
        if count[item] == 1:
            return item
    return None

def swap_variables(a, b):
    return b, a

def calculate_gross_salary(basic_salary, hra, da):
    return basic_salary + hra + da

def count_occurrences_of_element(lst, element):
    return lst.count(element)

def generate_prime_numbers_up_to_n(n):
    primes = []
    for num in range(2, n + 1):
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            primes.append(num)
    return primes

def find_most_repeated_char_in_string(s):
    from collections import Counter
    count = Counter(s)
    return count.most_common(1)[0][0]

def sum_of_digits(number):
    return sum(map(int, str(number)))

def product_of_digits(number):
    product = 1
    for digit in str(number):
        product *= int(digit)
    return product

def find_nth_fibonacci_number(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return find_nth_fibonacci_number(n-1) + find_nth_fibonacci_number(n-2)

def calculate_average_word_length(s):
    words = s.split()
    return sum(len(word) for word in words) / len(words)

def find_longest_palindrome_substring(s):
    if not s:
        return ""
    start, end = 0, 0
    for i in range(len(s)):
        len1 = expand_around_center(s, i, i)
        len2 = expand_around_center(s, i, i + 1)
        length = max(len1, len2)
        if length > end - start:
            start = i - (length - 1) // 2
            end = i + length // 2
    return s[start:end + 1]

def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1

def convert_camel_case_to_snake_case(s):
    import re
    return re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()

def convert_snake_case_to_camel_case(s):
    components = s.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

def count_consonants_in_string(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char.isalpha() and char not in vowels)

def calculate_probability_of_event(success, total):
    return success / total if total else 0

def find_all_permutations_of_string(s):
    from itertools import permutations
    return [''.join(p) for p in permutations(s)]

def find_all_combinations_of_string(s, n):
    from itertools import combinations
    return [''.join(c) for c in combinations(s, n)]

def is_substring(s1, s2):
    return s1 in s2

def is_rotation(s1, s2):
    return len(s1) == len(s2) and s2 in s1 + s1

def find_longest_common_prefix(strings):
    if not strings:
        return ""
    shortest = min(strings, key=len)
    for i, char in enumerate(shortest):
        if any(s[i] != char for s in strings):
            return shortest[:i]
    return shortest

def reverse_words_in_string(s):
    return ' '.join(s.split()[::-1])

def find_greatest_product_of_three(lst):
    lst.sort()
    return max(lst[-1] * lst[-2] * lst[-3], lst[0] * lst[1] * lst[-1])

def check_if_valid_parentheses(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack

def convert_roman_to_integer(roman):
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = 0
    for char in reversed(roman):
        current_value = roman_map[char]
        if current_value >= prev_value:
            result += current_value
        else:
            result -= current_value
        prev_value = current_value
    return result

def convert_integer_to_roman(num):
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syms[i]
            num -= val[i]
        i += 1
    return roman_num

def compute_greatest_common_divisor(a, b):
    while b:
        a, b = b, a % b
    return a

def check_if_valid_palindrome(s):
    import re
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return s == s[::-1]

def generate_subsets(lst):
    from itertools import chain, combinations
    return list(chain.from_iterable(combinations(lst, r) for r in range(len(lst) + 1)))

def compute_arithmetic_mean(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def calculate_sine_of_angle(angle):
    import math
    return math.sin(math.radians(angle))

def calculate_cosine_of_angle(angle):
    import math
    return math.cos(math.radians(angle))

def calculate_tangent_of_angle(angle):
    import math
    return math.tan(math.radians(angle))

def check_if_balanced_brackets(s):
    stack = []
    brackets = {"(": ")", "{": "}", "[": "]"}
    for char in s:
        if char in brackets:
            stack.append(char)
        elif char in brackets.values():
            if not stack or brackets[stack.pop()] != char:
                return False
    return not stack

def convert_decimal_to_octal(decimal):
    return oct(decimal)[2:]

def convert_octal_to_decimal(octal):
    return int(octal, 8)

def find_greatest_of_three_numbers(a, b, c):
    return max(a, b, c)

def find_least_of_three_numbers(a, b, c):
    return min(a, b, c)

def calculate_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def calculate_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def find_nth_prime_number(n):
    count = 0
    num = 2
    while count < n:
        if check_if_prime(num):
            count += 1
        num += 1
    return num - 1

def find_factors_of_number(number):