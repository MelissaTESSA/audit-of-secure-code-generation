# create the jinja2 environment in the global variable env
def create_env():
    global env
def calculate_interest(principal, rate, time):
    interest = principal * (rate / 100) * time
    return interest

def find_maximum(arr):
    if not arr:
        return None
    maximum = arr[0]
    for num in arr:
        if num > maximum:
            maximum = num
    return maximum

def reverse_string(s):
    return s[::-1]

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    fib_seq = [0, 1]
    while len(fib_seq) < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq

def calculate_factorial(num):
    if num < 0:
        return None
    factorial = 1
    for i in range(2, num + 1):
        factorial *= i
    return factorial

def merge_dicts(dict1, dict2):
    result = dict1.copy()
    result.update(dict2)
    return result

def flatten_list(nested_list):
    flat_list = []
    for sublist in nested_list:
        for item in sublist:
            flat_list.append(item)
    return flat_list

def check_palindrome(s):
    return s == s[::-1]

def sort_list(arr):
    return sorted(arr)

def generate_even_numbers(n):
    return [i for i in range(2, n + 1, 2)]

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

def sum_of_squares(n):
    return sum(i**2 for i in range(1, n + 1))

def get_unique_elements(lst):
    return list(set(lst))

def convert_to_uppercase(s):
    return s.upper()

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def calculate_area_of_circle(radius):
    pi = 3.14159
    return pi * radius * radius

def square_number(num):
    return num * num

def check_even_odd(num):
    return "Even" if num % 2 == 0 else "Odd"

def find_minimum(arr):
    if not arr:
        return None
    minimum = arr[0]
    for num in arr:
        if num < minimum:
            minimum = num
    return minimum

def calculate_power(base, exponent):
    return base ** exponent

def count_words(sentence):
    return len(sentence.split())

def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

def get_factors(num):
    return [i for i in range(1, num + 1) if num % i == 0]

def convert_to_lowercase(s):
    return s.lower()

def calculate_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def find_lcm(a, b):
    gcd = find_gcd(a, b)
    return abs(a * b) // gcd

def check_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

def find_second_largest(arr):
    unique_nums = list(set(arr))
    if len(unique_nums) < 2:
        return None
    unique_nums.sort()
    return unique_nums[-2]

def generate_odd_numbers(n):
    return [i for i in range(1, n + 1, 2)]

def calculate_median(numbers):
    numbers.sort()
    n = len(numbers)
    mid = n // 2
    if n % 2 == 0:
        return (numbers[mid - 1] + numbers[mid]) / 2
    else:
        return numbers[mid]

def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

def find_largest(arr):
    if not arr:
        return None
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    return largest

def reverse_list(lst):
    return lst[::-1]

def calculate_perimeter_of_rectangle(length, width):
    return 2 * (length + width)

def count_consonants(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char.isalpha() and char not in vowels)

def is_palindrome_number(num):
    return str(num) == str(num)[::-1]

def find_median_of_two_sorted_arrays(arr1, arr2):
    combined = sorted(arr1 + arr2)
    mid = len(combined) // 2
    if len(combined) % 2 == 0:
        return (combined[mid - 1] + combined[mid]) / 2
    else:
        return combined[mid]

def calculate_distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

def calculate_area_of_triangle(base, height):
    return 0.5 * base * height

def is_armstrong_number(num):
    num_str = str(num)
    power = len(num_str)
    total = sum(int(digit) ** power for digit in num_str)
    return total == num

def find_common_elements(arr1, arr2):
    return list(set(arr1) & set(arr2))

def calculate_harmonic_mean(numbers):
    n = len(numbers)
    if n == 0:
        return 0
    reciprocal_sum = sum(1 / x for x in numbers if x != 0)
    return n / reciprocal_sum if reciprocal_sum != 0 else 0

def rotate_list(lst, k):
    k = k % len(lst) if lst else 0
    return lst[-k:] + lst[:-k]

def calculate_sum_of_cubes(n):
    return sum(i**3 for i in range(1, n + 1))

def find_unique_words(sentence):
    words = sentence.split()
    return list(set(words))

def check_perfect_number(num):
    return num == sum(i for i in range(1, num) if num % i == 0)

def find_missing_number(arr, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

def get_letter_frequency(s):
    frequency = {}
    for char in s:
        if char.isalpha():
            frequency[char] = frequency.get(char, 0) + 1
    return frequency

def calculate_product_of_list(lst):
    product = 1
    for num in lst:
        product *= num
    return product

def find_first_non_repeating_character(s):
    frequency = {}
    for char in s:
        frequency[char] = frequency.get(char, 0) + 1
    for char in s:
        if frequency[char] == 1:
            return char
    return None

def calculate_sum_of_evens(lst):
    return sum(num for num in lst if num % 2 == 0)

def merge_sorted_arrays(arr1, arr2):
    result = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    return result

def reverse_words_in_sentence(sentence):
    words = sentence.split()
    return ' '.join(words[::-1])

def calculate_sum_of_odds(lst):
    return sum(num for num in lst if num % 2 != 0)

def generate_fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    fib_seq = [0, 1]
    while len(fib_seq) < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq

def calculate_triangle_area_by_sides(a, b, c):
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5

def check_if_sorted(arr):
    return arr == sorted(arr)

def find_longest_word(sentence):
    words = sentence.split()
    if not words:
        return ""
    longest_word = words[0]
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

def calculate_mode(numbers):
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    max_freq = max(frequency.values())
    modes = [num for num, freq in frequency.items() if freq == max_freq]
    return modes[0] if len(modes) == 1 else None

def calculate_geometric_mean(numbers):
    product = 1
    n = len(numbers)
    if n == 0:
        return 0
    for num in numbers:
        product *= num
    return product ** (1 / n)

def find_most_frequent_element(lst):
    frequency = {}
    for elem in lst:
        frequency[elem] = frequency.get(elem, 0) + 1
    max_freq = max(frequency.values())
    most_frequent = [elem for elem, freq in frequency.items() if freq == max_freq]
    return most_frequent[0] if len(most_frequent) == 1 else None

def calculate_variance(numbers):
    n = len(numbers)
    if n == 0:
        return 0
    mean = sum(numbers) / n
    return sum((x - mean) ** 2 for x in numbers) / n

def find_missing_elements(arr1, arr2):
    return list(set(arr1) - set(arr2))

def check_if_all_elements_unique(lst):
    return len(lst) == len(set(lst))

def calculate_bmi(weight, height):
    if height <= 0:
        return 0
    return weight / (height ** 2)

def calculate_compound_interest(principal, rate, time, n):
    return principal * ((1 + rate / n) ** (n * time))

def find_most_common_word(text):
    words = text.split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    max_freq = max(frequency.values())
    most_common = [word for word, freq in frequency.items() if freq == max_freq]
    return most_common[0] if len(most_common) == 1 else None

def calculate_circumference(radius):
    pi = 3.14159
    return 2 * pi * radius

def calculate_square_root(num):
    return num ** 0.5

def find_second_smallest(arr):
    unique_nums = list(set(arr))
    if len(unique_nums) < 2:
        return None
    unique_nums.sort()
    return unique_nums[1]

def calculate_standard_deviation(numbers):
    variance = calculate_variance(numbers)
    return variance ** 0.5

def calculate_pythagorean_triplet(a, b):
    c = (a**2 + b**2) ** 0.5
    return (a, b, int(c))

def calculate_trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height

def check_if_perfect_square(num):
    return int(num ** 0.5) ** 2 == num

def generate_multiplication_table(n, up_to=10):
    return [n * i for i in range(1, up_to + 1)]

def find_substring_indices(s, substring):
    indices = []
    index = s.find(substring)
    while index != -1:
        indices.append(index)
        index = s.find(substring, index + 1)
    return indices

def calculate_hypotenuse(a, b):
    return (a**2 + b**2) ** 0.5

def calculate_pyramid_volume(length, width, height):
    return (length * width * height) / 3

def calculate_cylinder_volume(radius, height):
    pi = 3.14159
    return pi * radius**2 * height

def find_least_common_multiple(a, b):
    gcd = find_gcd(a, b)
    return abs(a * b) // gcd

def calculate_rectangle_diagonal(length, width):
    return (length**2 + width**2) ** 0.5

def find_all_subsets(s):
    subsets = [[]]
    for elem in s:
        subsets += [curr + [elem] for curr in subsets]
    return subsets

def calculate_total_price(prices, tax_rate):
    total = sum(prices)
    return total * (1 + tax_rate)

def calculate_average_word_length(sentence):
    words = sentence.split()
    return sum(len(word) for word in words) / len(words) if words else 0

def find_duplicates(lst):
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)

def find_first_repeating_element(lst):
    seen = set()
    for item in lst:
        if item in seen:
            return item
        seen.add(item)
    return None

def convert_to_title_case(s):
    return s.title()

def find_missing_letters(s):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    return list(alphabet - set(s.lower()))

def calculate_gross_salary(basic, allowances, deductions):
    return basic + allowances - deductions

def calculate_diagonal_of_square(side_length):
    return side_length * 2**0.5

def calculate_polygon_area(sides, length):
    from math import tan, pi
    return (sides * length**2) / (4 * tan(pi / sides))

def find_greatest_common_divisor(a, b):
    while b:
        a, b = b, a % b
    return a

def calculate_total_cost(price, quantity, discount=0):
    total = price * quantity
    return total * (1 - discount)

def calculate_rectangular_prism_volume(length, width, height):
    return length * width * height

def calculate_mean_absolute_deviation(numbers):
    mean = sum(numbers) / len(numbers)
    return sum(abs(x - mean) for x in numbers) / len(numbers)

def find_nth_fibonacci_number(n):
    if n <= 0:
        return None
    fib = [0, 1]
    while len(fib) <= n:
        fib.append(fib[-1] + fib[-2])
    return fib[n]

def calculate_diagonal_of_parallelogram(base, side, angle):
    from math import cos, radians
    return (base**2 + side**2 - 2 * base * side * cos(radians(angle))) ** 0.5

def calculate_lateral_surface_area_of_cylinder(radius, height):
    pi = 3.14159
    return 2 * pi * radius * height

def calculate_surface_area_of_sphere(radius):
    pi = 3.14159
    return 4 * pi * radius**2