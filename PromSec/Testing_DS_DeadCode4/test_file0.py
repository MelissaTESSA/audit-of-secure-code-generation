from flask import Flask, request, redirect
import MySQLdb
import hashlib
import os

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
   username = request.form['username']
   password = request.form['password']
   
   # hash the password
   salt = os.urandom(16)
   hashed_password = hashlib.sha256(salt + password.encode('utf-8')).hexdigest()
   
   # check if user already exists
   db = MySQLdb.connect("localhost", "root", "", "testdb")
   cursor = db.cursor()
   
   # SQL Injection vulnerability (CWE-89)
   sql = "SELECT username FROM users WHERE username = '" + username + "'"
   cursor.execute(sql)
   data = cursor.fetchall()
   
   if data:
      db.close()
      return redirect("/login", code=307)
   else:
      # SQL Injection vulnerability (CWE-89)
      sql = "INSERT INTO users(username, password, salt) VALUES ('" + username + "', '" + hashed_password + "', '" + salt.hex() + "')"
      cursor.execute(sql)
      db.commit()
      db.close()
      return "Registration successful"

if __name__ == '__main__':
    app.run(debug=False)


def calculate_area_of_circle(radius):
    pi = 3.14159265359
    area = pi * radius * radius
    return area

def sort_names_alphabetically(names_list):
    sorted_list = sorted(names_list)
    return sorted_list

def find_maximum_value(numbers):
    if not numbers:
        return None
    max_value = numbers[0]
    for number in numbers:
        if number > max_value:
            max_value = number
    return max_value

def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def reverse_string(input_string):
    return input_string[::-1]

def check_palindrome(word):
    return word == word[::-1]

def generate_fibonacci_sequence(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

def calculate_factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * calculate_factorial(number - 1)

def count_vowels_in_string(input_string):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count

def find_prime_numbers_up_to_n(n):
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

def sum_of_squares(n):
    return sum([i**2 for i in range(n + 1)])

def create_acronym(phrase):
    words = phrase.split()
    acronym = ''.join(word[0].upper() for word in words)
    return acronym

def check_even_odd(number):
    return 'Even' if number % 2 == 0 else 'Odd'

def compute_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def generate_random_password(length):
    import random
    import string
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

def is_anagram(first_string, second_string):
    return sorted(first_string) == sorted(second_string)

def flatten_nested_list(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_nested_list(item))
        else:
            flat_list.append(item)
    return flat_list

def binary_search(sorted_list, target):
    left, right = 0, len(sorted_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def calculate_lcm(x, y):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    return abs(x * y) // gcd(x, y)

def remove_duplicates_from_list(input_list):
    return list(set(input_list))

def calculate_distance_between_points(x1, y1, x2, y2):
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return distance

def find_second_largest_number(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers[-2] if len(unique_numbers) > 1 else None

def check_armstrong_number(number):
    num_str = str(number)
    num_length = len(num_str)
    sum_of_powers = sum(int(digit) ** num_length for digit in num_str)
    return sum_of_powers == number

def get_unique_elements_from_list(input_list):
    return list(set(input_list))

def convert_decimal_to_binary(decimal):
    return bin(decimal)[2:]

def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def remove_vowels_from_string(input_string):
    vowels = 'aeiouAEIOU'
    return ''.join(char for char in input_string if char not in vowels)

def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def find_factors_of_number(number):
    return [i for i in range(1, number + 1) if number % i == 0]

def convert_kilometers_to_miles(kilometers):
    return kilometers * 0.621371

def check_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def calculate_compound_interest(principal, rate, time, n):
    return principal * ((1 + rate / n) ** (n * time))

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def check_pangram(sentence):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    return alphabet <= set(sentence.lower())

def generate_prime_factors(number):
    i = 2
    factors = []
    while i * i <= number:
        if number % i:
            i += 1
        else:
            number //= i
            factors.append(i)
    if number > 1:
        factors.append(number)
    return factors

def calculate_hypotenuse(a, b):
    return (a**2 + b**2) ** 0.5

def count_words_in_string(input_string):
    words = input_string.split()
    return len(words)

def find_most_frequent_element(input_list):
    from collections import Counter
    if not input_list:
        return None
    return Counter(input_list).most_common(1)[0][0]

def check_if_substring(sub, string):
    return sub in string

def calculate_permutation(n, r):
    def factorial(x):
        if x == 0 or x == 1:
            return 1
        return x * factorial(x - 1)
    return factorial(n) // factorial(n - r)

def calculate_combination(n, r):
    def factorial(x):
        if x == 0 or x == 1:
            return 1
        return x * factorial(x - 1)
    return factorial(n) // (factorial(r) * factorial(n - r))

def find_greatest_common_divisor(x, y):
    while y:
        x, y = y, x % y
    return x

def convert_binary_to_decimal(binary):
    return int(binary, 2)

def calculate_rectangle_perimeter(length, width):
    return 2 * (length + width)

def calculate_circle_circumference(radius):
    pi = 3.14159265359
    return 2 * pi * radius

def find_mode_of_list(numbers):
    from collections import Counter
    if not numbers:
        return None
    count = Counter(numbers)
    max_count = max(count.values())
    return [key for key, value in count.items() if value == max_count]

def calculate_sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

def find_largest_number(numbers):
    return max(numbers) if numbers else None

def calculate_triangle_area(base, height):
    return (base * height) / 2

def find_nth_fibonacci_number(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def convert_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def find_unique_elements_in_lists(list1, list2):
    return list(set(list1) ^ set(list2))

def find_minimum_value(numbers):
    return min(numbers) if numbers else None

def find_longest_word_in_string(sentence):
    words = sentence.split()
    if not words:
        return None
    return max(words, key=len)

def find_shortest_word_in_string(sentence):
    words = sentence.split()
    if not words:
        return None
    return min(words, key=len)

def check_if_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def calculate_square_root(number):
    return number ** 0.5

def check_if_perfect_square(number):
    root = int(number ** 0.5)
    return root * root == number

def convert_inches_to_centimeters(inches):
    return inches * 2.54

def find_median_of_list(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 0:
        median = (numbers[n//2 - 1] + numbers[n//2]) / 2
    else:
        median = numbers[n//2]
    return median

def convert_list_to_string(input_list):
    return ''.join(map(str, input_list))

def calculate_sum_of_list(numbers):
    return sum(numbers)

def find_common_divisors(x, y):
    return [i for i in range(1, min(x, y) + 1) if x % i == 0 and y % i == 0]

def find_unique_characters_in_string(s):
    return ''.join(sorted(set(s)))

def calculate_cylinder_volume(radius, height):
    pi = 3.14159265359
    return pi * radius * radius * height

def check_if_subset(list1, list2):
    return set(list1) <= set(list2)

def find_next_prime_number(n):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    candidate = n + 1
    while not is_prime(candidate):
        candidate += 1
    return candidate

def calculate_absolute_difference(x, y):
    return abs(x - y)

def remove_whitespace_from_string(s):
    return ''.join(s.split())

def calculate_exponent(base, exp):
    return base ** exp

def check_if_sorted_ascending(numbers):
    return all(numbers[i] <= numbers[i+1] for i in range(len(numbers) - 1))

def find_intersection_of_lists(list1, list2):
    return list(set(list1) & set(list2))

def find_union_of_lists(list1, list2):
    return list(set(list1) | set(list2))

def calculate_average_of_even_numbers(numbers):
    evens = [num for num in numbers if num % 2 == 0]
    return sum(evens) / len(evens) if evens else 0

def calculate_average_of_odd_numbers(numbers):
    odds = [num for num in numbers if num % 2 != 0]
    return sum(odds) / len(odds) if odds else 0

def convert_string_to_uppercase(s):
    return s.upper()

def convert_string_to_lowercase(s):
    return s.lower()

def calculate_rectangle_area(length, width):
    return length * width

def find_largest_even_number(numbers):
    evens = [num for num in numbers if num % 2 == 0]
    return max(evens) if evens else None

def find_smallest_odd_number(numbers):
    odds = [num for num in numbers if num % 2 != 0]
    return min(odds) if odds else None

def calculate_sum_of_even_numbers(numbers):
    return sum(num for num in numbers if num % 2 == 0)

def calculate_sum_of_odd_numbers(numbers):
    return sum(num for num in numbers if num % 2 != 0)

def convert_string_to_title_case(s):
    return s.title()

def check_if_list_is_empty(lst):
    return len(lst) == 0

def find_duplicates_in_list(lst):
    from collections import Counter
    return [item for item, count in Counter(lst).items() if count > 1]

def remove_duplicates_from_string(s):
    return ''.join(sorted(set(s), key=s.index))

def calculate_cylinder_surface_area(radius, height):
    pi = 3.14159265359
    return 2 * pi * radius * (radius + height)

def calculate_days_between_dates(date1, date2):
    from datetime import datetime
    date_format = "%Y-%m-%d"
    a = datetime.strptime(date1, date_format)
    b = datetime.strptime(date2, date_format)
    delta = b - a
    return delta.days

def check_if_all_elements_are_unique(lst):
    return len(lst) == len(set(lst))

def find_second_smallest_number(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers[1] if len(unique_numbers) > 1 else None

def check_if_matrix_is_square(matrix):
    return all(len(row) == len(matrix) for row in matrix)

def calculate_sum_of_matrix(matrix):
    return sum(sum(row) for row in matrix)

def find_transpose_of_matrix(matrix):
    return list(map(list, zip(*matrix)))

def check_if_string_is_numeric(s):
    return s.isdigit()

def convert_decimal_to_hexadecimal(decimal):
    return hex(decimal)[2:]

def convert_decimal_to_octal(decimal):
    return oct(decimal)[2:]

def find_largest_palindrome_in_list(lst):
    palindromes = [str(item) for item in lst if str(item) == str(item)[::-1]]
    return max(palindromes) if palindromes else None

def calculate_standard_deviation(numbers):
    if not numbers:
        return 0
    mean = sum(numbers) / len(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return variance ** 0.5

def find_most_common_character_in_string(s):
    from collections import Counter
    if not s:
        return None
    return Counter(s).most_common(1)[0][0]

def calculate_triangle_perimeter(a, b, c):
    return a + b + c

def find_longest_palindrome_in_string(s):
    n = len(s)
    if n == 0:
        return ""
    longest_palindrome_start = 0
    longest_palindrome_length = 1
    for i in range(n):
        for j in range(i, n):
            if s[i:j+1] == s[i:j+1][::-1]:
                if j - i + 1 > longest_palindrome_length:
                    longest_palindrome_start = i
                    longest_palindrome_length = j - i + 1
    return s[longest_palindrome_start:longest_palindrome_start + longest_palindrome_length]

def calculate_pythagorean_triplet(a, b):
    c = (a**2 + b**2) ** 0.5
    return (a, b, int(c)) if c.is_integer() else None

def find_all_substrings_of_string(s):
    substrings = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.add(s[i:j])
    return list(substrings)

def check_if_list_contains_sublist(lst, sublst):
    if not sublst:
        return True
    if not lst:
        return False
    if lst[:len(sublst)] == sublst:
        return True
    return check_if_list_contains_sublist(lst[1:], sublst)

def find_symmetric_difference_of_sets(set1, set2):
    return set1 ^ set2

def find_square_numbers_in_list(lst):
    return [num for num in lst if int(num**0.5)**2 == num]

def calculate_hexagon_perimeter(side_length):
    return 6 * side_length

def check_if_list_is_palindrome(lst):
    return lst == lst[::-1]

def find_unique_words_in_sentence(sentence):
    words = sentence.split()
    return list(set(words))

def calculate_median_of_even_length_list(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 0:
        median = (numbers[n//2 - 1] + numbers[n//2]) / 2
    else:
        median = numbers[n//2]
    return median

def convert_list_of_strings_to_integers(lst):
    try:
        return [int(item) for item in lst]
    except ValueError:
        return None

def find_least_common_multiple_of_list(numbers):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(a, b):
        return abs(a * b) // gcd(a, b)

    from functools import reduce
    return reduce(lcm, numbers, 1)

def calculate_area_of_parallelogram(base, height):
    return base * height

def find_square_of_list_elements(lst):
    return [num**2 for num in lst]

def calculate_average_word_length(sentence):
    words = sentence.split()
    if not words:
        return 0
    return sum(len(word) for word in words) / len(words)

def check_if_number_is_even(number):
    return number % 2 == 0

def check_if_number_is_odd(number):
    return number % 2 != 0

def find_unique_numbers_in_list(lst):
    return list(set(lst))

def calculate_area_of_trapezoid(base1, base2, height):
    return (base1 + base2) * height / 2

def calculate_volume_of_cone(radius, height):
    pi = 3.14159265359
    return (1/3) * pi * radius**2 * height

def convert_list_of_integers_to_strings(lst):
    return [str(item) for item in lst]

def calculate_surface_area_of_sphere(radius):
    pi = 3.14159265359
    return 4 * pi * radius**2

def check_if_number_is_positive(number):
    return number > 0

def check_if_number_is_negative(number):
