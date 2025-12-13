@app.route('/buy_order', methods=['POST'])
def buy_stock():
    stock_name = request.form['stock_name']
    stock_quantity = request.form['stock_quantity']
    username = session['username']

    #insert the buy order in the database
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
def calculate_area_of_circle(radius):
    pi = 3.14159
    return pi * (radius ** 2)

def find_maximum_value_in_list(numbers):
    if not numbers:
        return None
    return max(numbers)

def reverse_string(s):
    return s[::-1]

def check_palindrome(s):
    return s == s[::-1]

def sort_numbers_ascending(numbers):
    return sorted(numbers)

def generate_fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

def count_vowels_in_string(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def find_factorial(n):
    if n == 0:
        return 1
    return n * find_factorial(n - 1)

def convert_celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def convert_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def calculate_compound_interest(principal, rate, time):
    return principal * ((1 + rate / 100) ** time) - principal

def find_largest_prime_factor(n):
    factor = 2
    while factor * factor <= n:
        if n % factor:
            factor += 1
        else:
            n //= factor
    return n

def find_least_common_multiple(a, b):
    if a > b:
        greater = a
    else:
        greater = b
    while True:
        if greater % a == 0 and greater % b == 0:
            return greater
        greater += 1

def find_greatest_common_divisor(a, b):
    while b:
        a, b = b, a % b
    return a

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_factors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

def calculate_perimeter_of_square(side_length):
    return 4 * side_length

def calculate_area_of_rectangle(length, width):
    return length * width

def calculate_perimeter_of_rectangle(length, width):
    return 2 * (length + width)

def get_unique_elements_in_list(lst):
    return list(set(lst))

def sum_of_squares(n):
    return sum(i ** 2 for i in range(1, n + 1))

def find_second_largest_number(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers[-2] if len(unique_numbers) > 1 else None

def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

def to_lowercase(s):
    return s.lower()

def to_uppercase(s):
    return s.upper()

def find_longest_word_in_sentence(sentence):
    words = sentence.split()
    longest_word = max(words, key=len)
    return longest_word

def count_words_in_sentence(sentence):
    words = sentence.split()
    return len(words)

def calculate_average_of_numbers(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def count_occurrences_of_element(lst, element):
    return lst.count(element)

def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return n % 2 != 0

def list_multiples_of_number(number, count):
    return [number * i for i in range(1, count + 1)]

def find_median_of_list(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]
    
def is_substring(sub, main):
    return sub in main

def remove_whitespace(s):
    return s.replace(" ", "")

def capitalize_first_letter_of_each_word(s):
    return s.title()

def is_armstrong_number(n):
    num_str = str(n)
    num_len = len(num_str)
    return n == sum(int(digit) ** num_len for digit in num_str)

def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def find_intersection_of_lists(list1, list2):
    return list(set(list1) & set(list2))

def find_union_of_lists(list1, list2):
    return list(set(list1) | set(list2))

def is_valid_email(email):
    return "@" in email and "." in email

def count_consonants_in_string(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char.isalpha() and char not in vowels)

def sort_words_in_sentence(sentence):
    words = sentence.split()
    words.sort()
    return ' '.join(words)

def generate_random_password(length):
    import random
    import string
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

def calculate_hypotenuse(a, b):
    return (a ** 2 + b ** 2) ** 0.5

def convert_kilometers_to_miles(km):
    return km * 0.621371

def convert_miles_to_kilometers(miles):
    return miles / 0.621371

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def check_leap_year(year):
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

def get_current_datetime():
    from datetime import datetime
    return datetime.now()

def convert_to_binary(n):
    return bin(n)[2:]

def convert_to_hexadecimal(n):
    return hex(n)[2:]

def is_pangram(s):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    return set(s.lower()) >= alphabet

def get_day_of_week(date_str):
    from datetime import datetime
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    return days[date_obj.weekday()]

def calculate_power(base, exponent):
    return base ** exponent

def fizz_buzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

def find_common_elements_in_lists(list1, list2):
    return list(set(list1) & set(list2))

def find_difference_of_lists(list1, list2):
    return list(set(list1) - set(list2))

def convert_list_to_string(lst):
    return ''.join(map(str, lst))

def calculate_gross_salary(basic, hra, da):
    return basic + hra + da

def calculate_net_salary(gross, tax):
    return gross - tax

def is_valid_url(url):
    import re
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None

def calculate_sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def convert_seconds_to_hours_minutes_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return hours, minutes, seconds

def check_if_sorted_ascending(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

def flatten_nested_list(nested_list):
    return [item for sublist in nested_list for item in sublist]

def generate_prime_numbers_up_to_n(n):
    primes = []
    for num in range(2, n + 1):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            primes.append(num)
    return primes

def remove_duplicates_from_list(lst):
    return list(dict.fromkeys(lst))

def square_of_number(n):
    return n * n

def cube_of_number(n):
    return n * n * n

def convert_string_to_list(s):
    return list(s)

def convert_list_to_tuple(lst):
    return tuple(lst)

def convert_tuple_to_list(tpl):
    return list(tpl)

def filter_even_numbers_from_list(lst):
    return [num for num in lst if num % 2 == 0]

def filter_odd_numbers_from_list(lst):
    return [num for num in lst if num % 2 != 0]

def merge_two_dicts(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

def remove_key_from_dict(d, key):
    if key in d:
        del d[key]
    return d

def update_dict_with_another(d1, d2):
    d1.update(d2)
    return d1

def find_keys_with_value(d, value):
    return [k for k, v in d.items() if v == value]

def calculate_average_of_dict_values(d):
    return sum(d.values()) / len(d) if d else 0

def calculate_sum_of_dict_values(d):
    return sum(d.values())

def count_keys_in_dict(d):
    return len(d)

def check_if_key_exists_in_dict(d, key):
    return key in d

def find_minimum_value_in_dict(d):
    return min(d.values()) if d else None

def find_maximum_value_in_dict(d):
    return max(d.values()) if d else None

def get_list_of_dict_values(d):
    return list(d.values())

def get_list_of_dict_keys(d):
    return list(d.keys())

def create_dict_from_two_lists(keys, values):
    return dict(zip(keys, values))

def swap_keys_and_values_in_dict(d):
    return {v: k for k, v in d.items()}

def filter_dict_by_value(d, filter_value):
    return {k: v for k, v in d.items() if v > filter_value}

def find_longest_string_in_list(lst):
    return max(lst, key=len) if lst else None

def find_shortest_string_in_list(lst):
    return min(lst, key=len) if lst else None

def check_if_all_elements_are_equal(lst):
    return all(x == lst[0] for x in lst)

def check_if_any_element_is_true(lst):
    return any(lst)

def convert_list_of_strings_to_int(lst):
    return [int(item) for item in lst if item.isdigit()]

def replace_vowels_with_character(s, char):
    vowels = "aeiouAEIOU"
    return ''.join(char if c in vowels else c for c in s)

def repeat_string_n_times(s, n):
    return s * n

def find_substring_positions(main_string, sub_string):
    start = 0
    positions = []
    while start < len(main_string):
        pos = main_string.find(sub_string, start)
        if pos == -1:
            break
        positions.append(pos)
        start = pos + 1
    return positions

def sum_of_elements_in_list(lst):
    return sum(lst)

def product_of_elements_in_list(lst):
    product = 1
    for num in lst:
        product *= num
    return product

def calculate_standard_deviation(numbers):
    if len(numbers) < 2:
        return 0
    mean = sum(numbers) / len(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / (len(numbers) - 1)
    return variance ** 0.5

def find_largest_number_in_list(lst):
    return max(lst) if lst else None

def find_smallest_number_in_list(lst):
    return min(lst) if lst else None

def check_if_string_contains_only_digits(s):
    return s.isdigit()

def check_if_string_contains_only_letters(s):
    return s.isalpha()

def remove_duplicates_from_string(s):
    return ''.join(sorted(set(s), key=s.index))

def find_unique_characters_in_string(s):
    return ''.join(set(s))

def find_most_frequent_character_in_string(s):
    from collections import Counter
    counter = Counter(s)
    return counter.most_common(1)[0][0]

def check_if_two_lists_have_common_elements(lst1, lst2):
    return bool(set(lst1) & set(lst2))

def find_common_elements_in_multiple_lists(*lists):
    return set.intersection(*map(set, lists))

def sum_of_squares_of_digits(n):
    return sum(int(digit) ** 2 for digit in str(n))

def find_longest_consecutive_sequence(lst):
    longest, current = 0, 0
    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1] + 1:
            current += 1
            longest = max(longest, current)
        else:
            current = 0
    return longest + 1

def find_missing_number_in_sequence(seq):
    n = len(seq) + 1
    total = n * (n + 1) // 2
    return total - sum(seq)

def find_first_non_repeating_character(s):
    from collections import Counter
    counter = Counter(s)
    for char in s:
        if counter[char] == 1:
            return char
    return None

def check_if_two_strings_are_isomorphic(s1, s2):
    if len(s1) != len(s2):
        return False
    mapping1, mapping2 = {}, {}
    for c1, c2 in zip(s1, s2):
        if mapping1.get(c1, c2) != c2 or mapping2.get(c2, c1) != c1:
            return False
        mapping1[c1] = c2
        mapping2[c2] = c1
    return True

def count_occurrences_of_each_character(s):
    from collections import Counter
    return dict(Counter(s))

def check_if_string_starts_with_vowel(s):
    return s[0].lower() in "aeiou" if s else False

def check_if_string_ends_with_vowel(s):
    return s[-1].lower() in "aeiou" if s else False

def find_all_perfect_numbers_up_to_n(n):
    perfect_numbers = []
    for num in range(2, n + 1):
        if sum(i for i in range(1, num) if num % i == 0) == num:
            perfect_numbers.append(num)
    return perfect_numbers

def calculate_nth_triangular_number(n):
    return n * (n + 1) // 2

def find_longest_palindromic_substring(s):
    n = len(s)
    if n == 0:
        return ""
    if n == 1:
        return s
    longest = s[0]
    for i in range(n):
        for j in range(i + 1, n + 1):
            sub = s[i:j]
            if sub == sub[::-1] and len(sub) > len(longest):
                longest = sub
    return longest

def convert_number_to_words(n):
    from num2words import num2words
    return num2words(n)

def check_if_list_is_palindrome(lst):
    return lst == lst[::-1]

def find_first_duplicate_in_list(lst):
    seen = set()
    for item in lst:
        if item in seen:
            return item
        seen.add(item)
    return None

def calculate_nth_fibonacci_number(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def find_maximum_subarray_sum(lst):
    max_so_far = lst[0]
    max_ending_here = lst[0]
    for x in lst[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

def check_if_string_is_balanced(s):
    stack = []
    mapping = {")": "(", "]": "[", "}": "{"}
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack

def calculate_digital_root(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

def find_minimum_positive_integer_missing(lst):
    positive_ints = set(range(1, len(lst) + 2))
    return min(positive_ints - set(lst))

def find_most_frequent_element_in_list(lst):
    from collections import Counter
    counter = Counter(lst)
    return counter.most_common(1)[0][