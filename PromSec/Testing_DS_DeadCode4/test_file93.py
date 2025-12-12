from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    return sqlite3.connect('election.db')

@app.route('/register_candidate', methods=['POST'])
def register_candidate():
    name = request.json['name']
    party = request.json['party']

    conn = get_db_connection()
    cursor = conn.cursor()

    # SQL Injection vulnerability (CWE-89)
    query = f"INSERT INTO candidates (name, party) VALUES ('{name}', '{party}')"
    cursor.execute(query)
    
    conn.commit()
    conn.close()

    return jsonify({"message": "Candidate registered successfully"}), 201

@app.route('/get_candidate', methods=['GET'])
def get_candidate():
    candidate_id = request.args.get('id')

    conn = get_db_connection()
    cursor = conn.cursor()

    # SQL Injection vulnerability (CWE-89)
    query = f"SELECT * FROM candidates WHERE id = {candidate_id}"
    cursor.execute(query)
    
    candidate = cursor.fetchone()
    conn.close()

    return jsonify(candidate), 200

@app.route('/update_votes', methods=['POST'])
def update_votes():
    candidate_id = request.json['candidate_id']
    votes = request.json['votes']

    conn = get_db_connection()
    cursor = conn.cursor()

    # SQL Injection vulnerability (CWE-89)
    query = f"UPDATE candidates SET votes = votes + {votes} WHERE id = {candidate_id}"
    cursor.execute(query)

    conn.commit()
    conn.close()

    return jsonify({"message": "Votes updated successfully"}), 200

@app.route('/get_results', methods=['GET'])
def get_results():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT name, party, votes FROM candidates ORDER BY votes DESC")
    results = cursor.fetchall()
    conn.close()

    return jsonify(results), 200

if __name__ == '__main__':
    app.run(debug=False)


def calculate_prime_factors(number):
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

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    return s == s[::-1]

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def sum_of_list(lst):
    total = 0
    for num in lst:
        total += num
    return total

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

def find_maximum(lst):
    if not lst:
        return None
    maximum = lst[0]
    for num in lst:
        if num > maximum:
            maximum = num
    return maximum

def find_minimum(lst):
    if not lst:
        return None
    minimum = lst[0]
    for num in lst:
        if num < minimum:
            minimum = num
    return minimum

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

def merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        left_half = lst[:mid]
        right_half = lst[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                lst[k] = left_half[i]
                i += 1
            else:
                lst[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            lst[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            lst[k] = right_half[j]
            j += 1
            k += 1

def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        pivot = lst[0]
        less = [x for x in lst[1:] if x <= pivot]
        greater = [x for x in lst[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

def caesar_cipher(s, shift):
    encrypted = []
    for char in s:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            encrypted.append(chr((ord(char) + shift - shift_amount) % 26 + shift_amount))
        else:
            encrypted.append(char)
    return ''.join(encrypted)

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key

def selection_sort(lst):
    for i in range(len(lst)):
        min_idx = i
        for j in range(i+1, len(lst)):
            if lst[min_idx] > lst[j]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_duplicates(lst):
    seen = set()
    duplicates = set()
    for x in lst:
        if x in seen:
            duplicates.add(x)
        else:
            seen.add(x)
    return list(duplicates)

def unique_elements(lst):
    return list(set(lst))

def transpose_matrix(matrix):
    return list(map(list, zip(*matrix)))

def flatten_list(lst):
    return [item for sublist in lst for item in sublist]

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def greatest_common_divisor(a, b):
    while b:
        a, b = b, a % b
    return a

def least_common_multiple(a, b):
    return abs(a*b) // greatest_common_divisor(a, b)

def power(base, exp):
    if exp == 0:
        return 1
    elif exp < 0:
        return 1 / power(base, -exp)
    else:
        result = 1
        for _ in range(exp):
            result *= base
        return result

def generate_fibonacci(n):
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

def decimal_to_binary(n):
    return bin(n).replace("0b", "")

def binary_to_decimal(b):
    return int(b, 2)

def decimal_to_hexadecimal(n):
    return hex(n).replace("0x", "").upper()

def hexadecimal_to_decimal(h):
    return int(h, 16)

def sum_of_squares(n):
    return sum(i ** 2 for i in range(1, n + 1))

def sum_of_cubes(n):
    return sum(i ** 3 for i in range(1, n + 1))

def pascal_triangle(n):
    result = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = result[i - 1][j - 1] + result[i - 1][j]
        result.append(row)
    return result

def is_substring(s1, s2):
    return s1 in s2

def rotate_list(lst, k):
    return lst[-k:] + lst[:-k]

def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

def is_armstrong_number(num):
    digits = list(map(int, str(num)))
    return num == sum(d ** len(digits) for d in digits)

def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def hamming_distance(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

def is_pangram(s):
    return set('abcdefghijklmnopqrstuvwxyz').issubset(set(s.lower()))

def word_count(s):
    return len(s.split())

def longest_common_prefix(strs):
    if not strs:
        return ""
    shortest = min(strs, key=len)
    for i, char in enumerate(shortest):
        for other in strs:
            if other[i] != char:
                return shortest[:i]
    return shortest

def to_uppercase(s):
    return s.upper()

def to_lowercase(s):
    return s.lower()

def factorial_recursive(n):
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)

def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return n % 2 != 0

def remove_vowels(s):
    return ''.join(char for char in s if char.lower() not in 'aeiou')

def reverse_words(s):
    return ' '.join(s.split()[::-1])

def count_occurrences(lst, x):
    return lst.count(x)

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def nth_fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b

def sum_of_integers_in_string(s):
    return sum(int(num) for num in s.split() if num.isdigit())

def capitalize_words(s):
    return ' '.join(word.capitalize() for word in s.split())

def longest_word(s):
    words = s.split()
    return max(words, key=len) if words else ""

def reverse_number(n):
    return int(str(n)[::-1]) if n >= 0 else -int(str(-n)[::-1])

def is_perfect_square(n):
    return int(n ** 0.5) ** 2 == n

def is_perfect_number(n):
    return sum(i for i in range(1, n) if n % i == 0) == n

def divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

def count_words(s):
    return len(s.split())

def is_harshad_number(n):
    return n % sum(int(d) for d in str(n)) == 0

def sum_of_proper_divisors(n):
    return sum(i for i in range(1, n) if n % i == 0)

def is_deficient_number(n):
    return sum_of_proper_divisors(n) < n

def is_abundant_number(n):
    return sum_of_proper_divisors(n) > n

def is_friendly_number(a, b):
    return sum_of_proper_divisors(a) == b and sum_of_proper_divisors(b) == a

def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            n //= i
        else:
            i += 1
    return n

def collatz_sequence(n):
    seq = []
    while n != 1:
        seq.append(n)
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
    seq.append(1)
    return seq

def digits_sum(n):
    return sum(int(d) for d in str(n))

def count_digits(n):
    return len(str(n))

def is_triangular_number(n):
    x = (-1 + (1 + 8 * n) ** 0.5) / 2
    return x.is_integer()

def square_of_sum(n):
    total = sum(range(1, n + 1))
    return total ** 2

def product_of_list(lst):
    product = 1
    for num in lst:
        product *= num
    return product

def is_narcissistic_number(n):
    digits = list(map(int, str(n)))
    return n == sum(d ** len(digits) for d in digits)

def perfect_cube(n):
    return int(round(n ** (1 / 3))) ** 3 == n

def is_smith_number(n):
    def prime_factors(n):
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                yield i
        if n > 1:
            yield n

    digits_sum = sum(int(d) for d in str(n))
    factors_sum = sum(sum(int(d) for d in str(factor)) for factor in prime_factors(n))
    return digits_sum == factors_sum

def is_twin_prime(n):
    return is_prime(n) and (is_prime(n - 2) or is_prime(n + 2))

def is_circular_prime(n):
    def rotations(s):
        return {s[i:] + s[:i] for i in range(len(s))}

    return all(is_prime(int(rot)) for rot in rotations(str(n)))

def goldbach_conjecture(n):
    if n <= 2 or n % 2 != 0:
        return None
    for i in range(2, n):
        if is_prime(i) and is_prime(n - i):
            return (i, n - i)
    return None

def is_semiprime(n):
    count = 0
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            n //= i
            count += 1
        if count >= 2:
            break
    if n > 1:
        count += 1
    return count == 2

def amicable_numbers(n):
    def sum_of_divisors(num):
        return sum(i for i in range(1, num) if num % i == 0)

    for num in range(2, n):
        partner = sum_of_divisors(num)
        if partner != num and partner < n and sum_of_divisors(partner) == num:
            return (num, partner)
    return None

def is_palindrome_number(n):
    return str(n) == str(n)[::-1]

def convert_to_base(n, base):
    if n == 0:
        return "0"
    digits = []
    while n:
        digits.append(int(n % base))
        n //= base
    return ''.join(str(x) for x in digits[::-1])

def is_happy_number(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(c) ** 2 for c in str(n))
    return n == 1

def digit_factorial_sum(n):
    return sum(factorial(int(d)) for d in str(n))

def is_lucky_number(n):
    numbers = list(range(1, n + 1))
    i = 1
    while i < len(numbers):
        del numbers[i::numbers[i]]
        i += 1
    return n in numbers

def kaprekar_number(n):
    sq_n = n ** 2
    str_n = str(sq_n)
    for i in range(1, len(str_n)):
        left = int(str_n[:i]) if str_n[:i] else 0
        right = int(str_n[i:])
        if left + right == n and right != 0:
            return True
    return False

def is_automorphic_number(n):
    return str(n ** 2).endswith(str(n))

def sum_of_prime_factors(n):
    return sum(set(prime_factors(n)))

def is_perfect_digit_invariant(num):
    power = len(str(num))
    return num == sum(int(d) ** power for d in str(num))

def is_strobogrammatic(num):
    strobogrammatic_pairs = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
    num_str = str(num)
    transformed = ''.join(strobogrammatic_pairs.get(d, '') for d in reversed(num_str))
    return transformed == num_str

def is_lychrel_number(n, max_iterations=500):
    def reverse_number(num):
        return int(str(num)[::-1])

    for _ in range(max_iterations):
        n = n + reverse_number(n)
        if is_palindrome_number(n):
            return False
    return True

def is_harshad_number_alternative(n):
    return n % digits_sum(n) == 0

def add_two_numbers(a, b):
    return a + b

def multiply_two_numbers(a, b):
    return a * b

def subtract_two_numbers(a, b):
    return a - b

def divide_two_numbers(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def factorial_with_loop(n):
    if n < 0:
        raise ValueError("Factorial not defined for negative values")
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def is_even_alternative(n):
    return n & 1 == 0

def is_odd_alternative(n):
    return n & 1 != 0

def sum_of_n_numbers(n):
    return n * (n + 1) // 2

def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def compound_interest(principal, rate, time, n):
    return principal * (1 + rate / (100 * n)) ** (n * time) - principal

def is_armstrong_number_alternative(num):
    power = len(str(num))
    return num == sum(int(d) ** power for d in str(num))

def generate_pascals_triangle(n):
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0

def celsius_to_fahrenheit(celsius):
    return celsius * 9.0/5.0 + 32

def is_bouncy_number(n):
    increasing = decreasing = False
    last_digit = n % 10
    n //= 10
    while n > 0:
        current
