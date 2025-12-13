int getValueFromArray(int* array, int size, int index) {
    // given the array of integers, return the value at the given index and -1 if the index is out of bounds
def calculate_area_of_square(length):
    return length * length

def find_largest_even_number(numbers):
    return max([n for n in numbers if n % 2 == 0], default=None)

def convert_to_uppercase(string):
    return string.upper()

def reverse_list(elements):
    return elements[::-1]

def check_prime_number(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_even_numbers(numbers):
    return sum(n for n in numbers if n % 2 == 0)

def multiply_elements_in_list(numbers):
    result = 1
    for n in numbers:
        result *= n
    return result

def find_longest_word(words):
    return max(words, key=len, default='')

def is_palindrome(string):
    return string == string[::-1]

def count_vowels(string):
    return sum(1 for char in string.lower() if char in 'aeiou')

def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n-1)

def find_minimum_value(numbers):
    return min(numbers, default=None)

def concatenate_strings(str1, str2):
    return str1 + str2

def calculate_distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

def convert_to_binary(n):
    return bin(n)[2:]

def calculate_sum_of_squares(numbers):
    return sum(n**2 for n in numbers)

def get_unique_elements(elements):
    return list(set(elements))

def calculate_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def find_missing_number(numbers, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(numbers)
    return expected_sum - actual_sum

def count_words_in_string(string):
    return len(string.split())

def sort_numbers_descending(numbers):
    return sorted(numbers, reverse=True)

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def find_second_largest_number(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers[-2] if len(unique_numbers) > 1 else None

def calculate_hypotenuse(a, b):
    return (a**2 + b**2)**0.5

def generate_fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

def count_occurrences(element, elements):
    return elements.count(element)

def convert_to_lowercase(string):
    return string.lower()

def calculate_rectangle_perimeter(length, width):
    return 2 * (length + width)

def count_consonants(string):
    return sum(1 for char in string.lower() if char in 'bcdfghjklmnpqrstvwxyz')

def find_greatest_common_divisor(a, b):
    while b:
        a, b = b, a % b
    return a

def convert_to_hexadecimal(n):
    return hex(n)[2:]

def check_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def calculate_power(base, exponent):
    return base ** exponent

def find_shortest_word(words):
    return min(words, key=len, default='')

def remove_duplicates(elements):
    return list(dict.fromkeys(elements))

def check_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

def calculate_circumference(radius):
    import math
    return 2 * math.pi * radius

def find_middle_element(elements):
    return elements[len(elements) // 2] if elements else None

def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def convert_list_to_string(elements):
    return ''.join(map(str, elements))

def find_sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def reverse_string(string):
    return string[::-1]

def find_unique_characters(string):
    return ''.join(sorted(set(string)))

def calculate_exponent(base, exp):
    return base ** exp

def find_most_frequent_element(elements):
    from collections import Counter
    if elements:
        return Counter(elements).most_common(1)[0][0]
    return None

def convert_to_title_case(string):
    return string.title()

def calculate_cube_volume(side):
    return side ** 3

def remove_vowels_from_string(string):
    return ''.join(char for char in string if char.lower() not in 'aeiou')

def find_pairs_with_sum(numbers, target_sum):
    result = []
    seen = set()
    for number in numbers:
        if target_sum - number in seen:
            result.append((number, target_sum - number))
        seen.add(number)
    return result

def check_if_sorted(elements):
    return elements == sorted(elements)

def calculate_gross_salary(basic, hra, da):
    return basic + hra + da

def find_largest_prime_factor(n):
    def is_prime(k):
        if k <= 1:
            return False
        for i in range(2, int(k**0.5) + 1):
            if k % i == 0:
                return False
        return True
    largest_prime = None
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            largest_prime = i
    return largest_prime

def calculate_modulus(a, b):
    return a % b

def convert_to_octal(n):
    return oct(n)[2:]

def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

def calculate_body_mass_index(weight, height):
    return weight / (height ** 2)

def find_least_common_multiple(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    return abs(a * b) // gcd(a, b)

def check_if_palindrome_permutation(string):
    from collections import Counter
    count = Counter(string.replace(" ", "").lower())
    odd_count = sum(1 for val in count.values() if val % 2 == 1)
    return odd_count <= 1

def calculate_total_price(prices):
    return sum(prices)

def find_unique_words(sentence):
    words = sentence.split()
    unique_words = set(words)
    return list(unique_words)

def calculate_square_root(n):
    return n ** 0.5

def find_first_non_repeating_character(string):
    from collections import Counter
    count = Counter(string)
    for char in string:
        if count[char] == 1:
            return char
    return None

def convert_to_roman_numerals(number):
    numerals = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    result = ''
    for value, numeral in sorted(numerals.items(), reverse=True):
        while number >= value:
            result += numeral
            number -= value
    return result

def calculate_rectangle_area(length, width):
    return length * width

def find_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        return (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    else:
        return sorted_numbers[n // 2]

def get_vowel_count(string):
    return sum(1 for char in string if char.lower() in 'aeiou')

def calculate_speed(distance, time):
    return distance / time if time else 0

def find_largest_number(numbers):
    return max(numbers, default=None)

def calculate_discount(price, discount_percent):
    return price * (1 - discount_percent / 100)

def check_if_pangram(sentence):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    return alphabet <= set(sentence.lower())

def calculate_total_distance(distances):
    return sum(distances)

def find_second_smallest_number(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers[1] if len(unique_numbers) > 1 else None

def calculate_sphere_volume(radius):
    import math
    return (4/3) * math.pi * (radius ** 3)

def count_uppercase_letters(string):
    return sum(1 for char in string if char.isupper())

def find_pairs_with_product(numbers, target_product):
    result = []
    seen = set()
    for number in numbers:
        if target_product % number == 0 and (target_product // number) in seen:
            result.append((number, target_product // number))
        seen.add(number)
    return result

def calculate_weekly_salary(hours_worked, hourly_rate):
    return hours_worked * hourly_rate

def check_if_all_elements_unique(elements):
    return len(elements) == len(set(elements))

def find_largest_palindrome(string):
    n = len(string)
    if n == 0:
        return ""
    longest = string[0]
    for i in range(n):
        for j in range(i + 1, n + 1):
            substr = string[i:j]
            if substr == substr[::-1] and len(substr) > len(longest):
                longest = substr
    return longest

def calculate_circle_area(radius):
    import math
    return math.pi * (radius ** 2)

def find_smallest_even_number(numbers):
    even_numbers = [n for n in numbers if n % 2 == 0]
    return min(even_numbers, default=None)

def convert_list_to_set(elements):
    return set(elements)

def calculate_mean(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def find_unique_integers(numbers):
    return list(set(numbers))

def count_lowercase_letters(string):
    return sum(1 for char in string if char.islower())

def check_if_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def calculate_time_difference(time1, time2):
    from datetime import datetime
    fmt = '%H:%M:%S'
    tdelta = datetime.strptime(time2, fmt) - datetime.strptime(time1, fmt)
    return tdelta.seconds

def find_missing_elements(sequence, n):
    full_set = set(range(1, n + 1))
    return list(full_set - set(sequence))

def calculate_geometric_mean(numbers):
    import math
    product = 1
    for n in numbers:
        product *= n
    return product ** (1 / len(numbers)) if numbers else 0

def find_largest_odd_number(numbers):
    odd_numbers = [n for n in numbers if n % 2 != 0]
    return max(odd_numbers, default=None)

def convert_string_to_list(string):
    return list(string)

def calculate_sum_of_cubes(numbers):
    return sum(n ** 3 for n in numbers)

def find_all_factors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

def check_if_substring(string, substring):
    return substring in string

def calculate_final_velocity(initial_velocity, acceleration, time):
    return initial_velocity + (acceleration * time)

def find_common_characters(str1, str2):
    return ''.join(sorted(set(str1) & set(str2)))

def calculate_equilateral_triangle_area(side):
    import math
    return (math.sqrt(3) / 4) * side ** 2

def find_unique_numbers(numbers):
    return list(set(numbers))

def count_digits_in_string(string):
    return sum(1 for char in string if char.isdigit())

def check_if_even(n):
    return n % 2 == 0

def find_second_largest_element(elements):
    unique_elements = list(set(elements))
    unique_elements.sort()
    return unique_elements[-2] if len(unique_elements) > 1 else None

def calculate_prism_volume(base_area, height):
    return base_area * height

def find_all_substrings(string):
    n = len(string)
    return [string[i:j] for i in range(n) for j in range(i + 1, n + 1)]

def calculate_total_weight(weights):
    return sum(weights)

def find_largest_unique_number(numbers):
    from collections import Counter
    count = Counter(numbers)
    unique_numbers = [n for n in numbers if count[n] == 1]
    return max(unique_numbers, default=None)

def convert_string_to_tuple(string):
    return tuple(string)

def calculate_seconds_in_hours(hours):
    return hours * 3600

def find_all_permutations(string):
    from itertools import permutations
    return [''.join(p) for p in permutations(string)]

def calculate_cylinder_surface_area(radius, height):
    import math
    return 2 * math.pi * radius * (radius + height)

def count_occurrences_of_substring(string, substring):
    return string.count(substring)

def check_if_odd(n):
    return n % 2 != 0

def find_maximum_subarray_sum(numbers):
    max_sum = current_sum = numbers[0]
    for n in numbers[1:]:
        current_sum = max(n, current_sum + n)
        max_sum = max(max_sum, current_sum)
    return max_sum

def calculate_hexagon_area(side):
    import math
    return (3 * math.sqrt(3) / 2) * side ** 2

def find_unique_characters_in_string(string):
    return ''.join(sorted(set(string)))

def count_words_in_sentence(sentence):
    return len(sentence.split())

def check_if_divisible(a, b):
    return a % b == 0

def find_maximum_value(numbers):
    return max(numbers, default=None)

def calculate_percentage(part, whole):
    return (part / whole) * 100 if whole else 0

def check_if_alphabetic(string):
    return string.isalpha()

def find_smallest_number(numbers):
    return min(numbers, default=None)

def calculate_pyramid_volume(base_area, height):
    return (1/3) * base_area * height

def find_all_palindromic_substrings(string):
    n = len(string)
    return [string[i:j] for i in range(n) for j in range(i + 1, n + 1) if string[i:j] == string[i:j][::-1]]

def calculate_sum_of_natural_numbers(n):
    return n * (n + 1) // 2

def find_largest_three_numbers(numbers):
    return sorted(numbers, reverse=True)[:3] if len(numbers) >= 3 else None

def convert_tuple_to_list(tpl):
    return list(tpl)

def calculate_seconds_in_days(days):
    return days * 86400

def find_all_combinations(elements):
    from itertools import combinations
    result = []
    for r in range(len(elements) + 1):
        result.extend(combinations(elements, r))
    return result

def calculate_cone_surface_area(radius, height):
    import math
    return math.pi * radius * (radius + (height ** 2 + radius ** 2) ** 0.5)

def count_vowels_in_list(strings):
    return sum(sum(1 for char in string if char.lower() in 'aeiou') for string in strings)

def check_if_multiple(a, b):
    return a % b == 0

def find_highest_scoring_word(words, scores):
    score_dict = dict(zip(words, scores))
    return max(score_dict, key=score_dict.get, default='')

def calculate_circle_circumference(radius):
    import math
    return 2 * math.pi * radius

def find_all_anagrams(word, words):
    from collections import Counter
    word_counter = Counter(word)
    return [w for w in words if Counter(w) == word_counter]

def calculate_loan_payment(principal, rate, time):
    return principal * (rate / 100) * time

def convert_set_to_list(s):
    return list(s)

def calculate_surface_area_of_cube(side):
    return 6 * (side ** 2)

def check_if_armstrong_number(n):
    digits = list(map(int, str(n)))
    return n == sum(d ** len(digits) for d in digits)

def find_pairs_with_difference(numbers, target_difference):
    result = []
    seen = set()
    for number in numbers:
        if (number - target_difference) in seen:
            result.append((number, number - target_difference))
        if (number + target_difference) in seen:
            result.append((number + target_difference, number))
        seen.add(number)
    return result

def calculate_triangle_perimeter(a, b, c):
    return a + b + c

def find_all_fibonacci_numbers_below(n):
    fibonacci = [0, 1]
    while fibonacci[-1] < n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci[:-1]

def count_even_numbers(numbers):
    return sum(1 for n in numbers if n % 2 == 0)

def check_if_palindrome_number(n):
    return str(n) == str(n)[::-1]

def find_minimum_value_in_matrix(matrix):
    return min(min(row) for row in matrix)

def calculate_discounted_price(price, discount):
    return price * ((100 - discount) / 100)

def find_longest_increasing_subsequence_length(numbers):
    if not numbers:
        return 0
    lis = [1] * len(numbers)
    for i in range(1, len(numbers)):
        for j in range(i):
            if numbers[i] > numbers[j]:
                lis[i] = max(lis[i], lis[j] + 1)
    return max(lis)

def calculate_greatest_common_divisor(a, b):
    while b:
        a, b = b, a % b
    return a

def convert_kilometers_to_miles(kilometers):
    return kilometers * 0.621371