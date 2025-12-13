int getIdFromArray(int index) {
    // given the array of ids, return the value at the given index and -1 if the index is out of bounds
def calculate_area_of_triangle(base, height):
    return 0.5 * base * height

def find_greatest_common_divisor(a, b):
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

def reverse_string(s):
    return s[::-1]

def convert_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def generate_fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n-1)

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

def find_largest_number_in_list(numbers):
    return max(numbers)

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def flatten_nested_list(nested_list):
    flat_list = []
    for element in nested_list:
        if isinstance(element, list):
            flat_list.extend(flatten_nested_list(element))
        else:
            flat_list.append(element)
    return flat_list

def remove_duplicates_from_list(items):
    return list(set(items))

def get_unique_elements_from_list(items):
    return list(set(items))

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def convert_to_binary(n):
    return bin(n)[2:]

def check_palindrome(s):
    return s == s[::-1]

def merge_two_sorted_lists(list1, list2):
    result = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    result.extend(list1[i:])
    result.extend(list2[j:])
    return result

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def remove_whitespace(s):
    return ''.join(s.split())

def find_second_largest_number(numbers):
    first = second = float('-inf')
    for number in numbers:
        if number > first:
            second = first
            first = number
        elif number > second:
            second = number
    return second

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

def calculate_power(base, exponent):
    return base ** exponent

def convert_list_to_dict(keys, values):
    return dict(zip(keys, values))

def get_middle_character(s):
    length = len(s)
    if length % 2 == 0:
        return s[length//2 - 1:length//2 + 1]
    else:
        return s[length//2]

def calculate_sum_of_squares(n):
    return sum(i**2 for i in range(1, n+1))

def count_words_in_string(s):
    return len(s.split())

def get_day_of_week_from_date(year, month, day):
    import datetime
    return datetime.date(year, month, day).strftime("%A")

def find_missing_number_in_sequence(sequence):
    n = len(sequence) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(sequence)
    return expected_sum - actual_sum

def rotate_list(lst, k):
    k = k % len(lst)
    return lst[-k:] + lst[:-k]

def get_factors_of_number(n):
    return [i for i in range(1, n+1) if n % i == 0]

def count_occurrences_of_element(lst, element):
    return lst.count(element)

def convert_seconds_to_hours_minutes_seconds(seconds):
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return hours, minutes, seconds

def remove_punctuation(s):
    import string
    return s.translate(str.maketrans('', '', string.punctuation))

def get_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

def get_odd_numbers(numbers):
    return [num for num in numbers if num % 2 != 0]

def calculate_distance_between_points(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def get_maximum_value_from_dict(d):
    return max(d.values())

def get_minimum_value_from_dict(d):
    return min(d.values())

def convert_string_to_title_case(s):
    return s.title()

def calculate_hypotenuse(a, b):
    return (a**2 + b**2) ** 0.5

def get_unique_characters(s):
    return set(s)

def sum_of_list(numbers):
    return sum(numbers)

def multiply_elements_of_list(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

def get_first_n_elements_of_list(lst, n):
    return lst[:n]

def reverse_list(lst):
    return lst[::-1]

def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return n % 2 != 0

def get_longest_word(words):
    return max(words, key=len)

def calculate_gross_salary(basic, hra, da):
    return basic + hra + da

def get_ascii_value_of_character(c):
    return ord(c)

def convert_list_to_tuple(lst):
    return tuple(lst)

def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def get_lcm_of_two_numbers(a, b):
    from math import gcd
    return abs(a*b) // gcd(a, b)

def get_hcf_of_two_numbers(a, b):
    from math import gcd
    return gcd(a, b)

def get_substring(s, start, end):
    return s[start:end]

def calculate_compound_interest(principal, rate, time, n):
    return principal * (1 + rate/n) ** (n*time)

def binary_search(lst, target):
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] < target:
            low = mid + 1
        elif lst[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1

def find_intersection_of_lists(list1, list2):
    return list(set(list1) & set(list2))

def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

def calculate_median(numbers):
    numbers.sort()
    n = len(numbers)
    mid = n // 2
    if n % 2 == 0:
        return (numbers[mid - 1] + numbers[mid]) / 2
    else:
        return numbers[mid]

def calculate_mode(numbers):
    from collections import Counter
    count = Counter(numbers)
    max_count = max(count.values())
    return [num for num in count if count[num] == max_count]

def get_last_n_elements_of_list(lst, n):
    return lst[-n:]

def calculate_variance(numbers):
    mean = calculate_mean(numbers)
    return sum((x - mean) ** 2 for x in numbers) / len(numbers)

def calculate_standard_deviation(numbers):
    variance = calculate_variance(numbers)
    return variance ** 0.5

def calculate_permutation(n, r):
    from math import factorial
    return factorial(n) // factorial(n - r)

def calculate_combination(n, r):
    from math import factorial
    return factorial(n) // (factorial(r) * factorial(n - r))

def convert_decimal_to_hexadecimal(n):
    return hex(n)[2:]

def convert_hexadecimal_to_decimal(hex_str):
    return int(hex_str, 16)

def convert_decimal_to_octal(n):
    return oct(n)[2:]

def convert_octal_to_decimal(octal_str):
    return int(octal_str, 8)

def convert_decimal_to_binary(n):
    return bin(n)[2:]

def convert_binary_to_decimal(binary_str):
    return int(binary_str, 2)

def get_cube_of_number(n):
    return n ** 3

def get_square_of_number(n):
    return n ** 2

def get_square_root_of_number(n):
    return n ** 0.5

def get_cube_root_of_number(n):
    return n ** (1/3)

def convert_kilometers_to_miles(kilometers):
    return kilometers * 0.621371

def convert_miles_to_kilometers(miles):
    return miles / 0.621371

def convert_celsius_to_kelvin(celsius):
    return celsius + 273.15

def convert_kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def convert_fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def convert_kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def get_ascii_values_of_string(s):
    return [ord(char) for char in s]

def convert_tuple_to_list(t):
    return list(t)

def convert_list_to_set(lst):
    return set(lst)

def convert_set_to_list(s):
    return list(s)

def get_min_max_of_list(lst):
    return min(lst), max(lst)

def get_second_smallest_number(numbers):
    first = second = float('inf')
    for number in numbers:
        if number < first:
            second = first
            first = number
        elif number < second:
            second = number
    return second

def calculate_sum_of_cubes(n):
    return sum(i**3 for i in range(1, n+1))

def is_pangram(s):
    return set('abcdefghijklmnopqrstuvwxyz') <= set(s.lower())

def calculate_gcd_of_list(numbers):
    from math import gcd
    from functools import reduce
    return reduce(gcd, numbers)

def calculate_lcm_of_list(numbers):
    from math import gcd
    from functools import reduce
    def lcm(a, b):
        return abs(a*b) // gcd(a, b)
    return reduce(lcm, numbers)

def get_fibonacci_number(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def find_nth_prime(n):
    prime_count = 0
    num = 2
    while prime_count < n:
        if is_prime(num):
            prime_count += 1
        num += 1
    return num - 1

def is_armstrong_number(n):
    num_str = str(n)
    num_len = len(num_str)
    return sum(int(digit) ** num_len for digit in num_str) == n

def get_prime_factors_of_number(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

def get_all_substrings(s):
    return [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]

def count_consonants(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char.isalpha() and char not in vowels)

def is_substring(s1, s2):
    return s1 in s2

def get_nth_fibonacci_number(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return get_nth_fibonacci_number(n-1) + get_nth_fibonacci_number(n-2)

def get_unique_words_from_string(s):
    return set(s.split())

def count_occurrences_of_word(s, word):
    return s.split().count(word)

def get_first_repeating_character(s):
    seen = set()
    for char in s:
        if char in seen:
            return char
        seen.add(char)
    return None

def get_first_non_repeating_character(s):
    from collections import Counter
    count = Counter(s)
    for char in s:
        if count[char] == 1:
            return char
    return None

def sort_list_of_dicts_by_key(lst, key):
    return sorted(lst, key=lambda d: d[key])

def group_anagrams(words):
    from collections import defaultdict
    anagrams = defaultdict(list)
    for word in words:
        anagrams[tuple(sorted(word))].append(word)
    return list(anagrams.values())

def get_combinations_of_string(s, n):
    from itertools import combinations
    return [''.join(comb) for comb in combinations(s, n)]

def get_permutations_of_string(s):
    from itertools import permutations
    return [''.join(perm) for perm in permutations(s)]

def find_max_subarray_sum(numbers):
    max_ending_here = max_so_far = numbers[0]
    for num in numbers[1:]:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

def flatten_list_of_lists(lst):
    return [item for sublist in lst for item in sublist]

def get_all_palindromic_substrings(s):
    result = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                result.append(substring)
    return result

def is_perfect_number(n):
    return sum(i for i in range(1, n) if n % i == 0) == n

def is_happy_number(n):
    def get_next(number):
        return sum(int(char) ** 2 for char in str(number))
    seen_numbers = set()
    while n != 1 and n not in seen_numbers:
        seen_numbers.add(n)
        n = get_next(n)
    return n == 1

def find_longest_increasing_subsequence(sequence):
    if not sequence:
        return []
    lengths = [1] * len(sequence)
    for i in range(1, len(sequence)):
        for j in range(i):
            if sequence[i] > sequence[j]:
                lengths[i] = max(lengths[i], lengths[j] + 1)
    max_length = max(lengths)
    result = []
    for i in range(len(sequence) - 1, -1, -1):
        if lengths[i] == max_length:
            result.append(sequence[i])
            max_length -= 1
    return result[::-1]

def is_palindrome_number(n):
    return str(n) == str(n)[::-1]

def sum_of_first_n_natural_numbers(n):
    return n * (n + 1) // 2

def get_number_of_digits(n):
    return len(str(n))

def get_number_of_words_in_paragraph(paragraph):
    return len(paragraph.split())

def get_longest_common_prefix(strs):
    if not strs:
        return ""
    shortest = min(strs, key=len)
    for i, char in enumerate(shortest):
        for other in strs:
            if other[i] != char:
                return shortest[:i]
    return shortest

def is_valid_email(email):
    import re
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

def get_most_frequent_word(s):
    from collections import Counter
    words = s.split()
    if not words:
        return None
    count = Counter(words)
    return max(count, key=count.get)

def is_valid_password(password):
    import re
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    return True

def get_prime_numbers_up_to_n(n):
    primes = []
    for num in range(2, n+1):
        if is_prime(num):
            primes.append(num)
    return primes

def get_sum_of_even_numbers_up_to_n(n):
    return sum(num for num in range(2, n+1, 2))

def get_sum_of_odd_numbers_up_to_n(n):
    return sum(num for num in range(1, n+1, 2))

def generate_pascal_triangle(n):
    result = [[1]]
    for _ in range(1, n):
        last_row = result[-1]
        current_row = [1]
        for i in range(len(last_row) - 1):
            current_row.append(last_row[i] + last_row[i + 1])
        current_row.append(1)
        result.append(current_row)
    return result

def find_first_missing_positive_integer(nums):
    nums = [num for num in nums if num > 0]
    nums_set = set(nums)
    smallest_missing = 1
    while smallest_missing in nums_set:
        smallest_missing += 1
    return smallest_missing

def get_factors_of_number(n):
    return [i for i in range(1, n + 1) if n % i == 0]