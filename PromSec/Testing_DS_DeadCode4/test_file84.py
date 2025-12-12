#copilot mean_prob: 0.4783879372978678
#This file was assembled by gen.py, written by redactedAuthorFirstname redactedAuthorLastname.
from flask import Flask, request, redirect
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)

@app.route('/buy_order', methods=['POST'])
# def buy_stock():
#     stock_name = request.form['stock_name']
#     stock_quantity = request.form['stock_quantity']
#     username = session['username']

#     #insert the buy order in the database
#     db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
#-copilot next line-#copilot mean_prob: 0.4783879372978678

def buy_stock():
    stock_name = request.form['stock_name']
    stock_quantity = request.form['stock_quantity']
    username = session['username']

    #insert the buy order in the database
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
    cur = db.cursor()

    cur.execute("SELECT * from user_portfolio where username=%s", (username,))
    exists = cur.fetchone()
    if exists:
        cur.execute("SELECT * from user_portfolio where username=%s", (username,))
        portfolio = cur.fetchone()
        stock_quantity = int(portfolio[1]) + int(stock_quantity)
        cur.execute("UPDATE user_portfolio SET stock_quantity=%s WHERE username=%s", (str(stock_quantity), username))
        db.commit()
        db.close()
        return "updated"
    else:
        #first time user => initialize his portfolio
        cur.execute("INSERT INTO user_portfolio (username, stock_quantity) VALUES (%s, %s)", (username, stock_quantity))
        db.commit()
        db.close()
        return "initialized"




def calculate_interest(principal, rate, time):
    return principal * (1 + (rate * time))

def convert_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def generate_random_string(length):
    import random
    import string
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def is_palindrome(word):
    return word == word[::-1]

def find_maximum(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

def reverse_list(lst):
    return lst[::-1]

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def check_even(number):
    return number % 2 == 0

def square(number):
    return number * number

def cube(number):
    return number * number * number

def multiply(a, b):
    return a * b

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    if b == 0:
        return None
    return a / b

def concatenate_strings(str1, str2):
    return str1 + str2

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def capitalize_string(s):
    return s.capitalize()

def find_average(numbers):
    return sum(numbers) / len(numbers)

def sort_numbers(numbers):
    return sorted(numbers)

def count_vowels(s):
    return sum(1 for char in s if char.lower() in 'aeiou')

def generate_fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def check_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def calculate_area_of_circle(radius):
    import math
    return math.pi * radius * radius

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_lcm(a, b):
    return abs(a * b) // find_gcd(a, b)

def sum_of_squares(n):
    return sum(i * i for i in range(1, n+1))

def sum_of_cubes(n):
    return sum(i * i * i for i in range(1, n+1))

def remove_duplicates(lst):
    return list(set(lst))

def find_unique_elements(lst):
    return [item for item in lst if lst.count(item) == 1]

def flatten_list(lst):
    return [item for sublist in lst for item in sublist]

def get_even_numbers(lst):
    return [num for num in lst if num % 2 == 0]

def get_odd_numbers(lst):
    return [num for num in lst if num % 2 != 0]

def count_words(s):
    return len(s.split())

def reverse_string(s):
    return s[::-1]

def check_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def find_second_largest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers[-2]

def calculate_bmi(weight, height):
    return weight / (height * height)

def convert_to_uppercase(s):
    return s.upper()

def convert_to_lowercase(s):
    return s.lower()

def get_factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def count_occurrences(lst, element):
    return lst.count(element)

def is_substring(sub, string):
    return sub in string

def generate_square_numbers(n):
    return [i * i for i in range(n)]

def filter_positive_numbers(lst):
    return [num for num in lst if num > 0]

def filter_negative_numbers(lst):
    return [num for num in lst if num < 0]

def find_median(numbers):
    numbers.sort()
    mid = len(numbers) // 2
    if len(numbers) % 2 == 0:
        return (numbers[mid - 1] + numbers[mid]) / 2
    else:
        return numbers[mid]

def is_armstrong_number(n):
    num_str = str(n)
    num_len = len(num_str)
    return n == sum(int(digit) ** num_len for digit in num_str)

def calculate_power(base, exponent):
    return base ** exponent

def get_factors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

def is_perfect_number(n):
    return sum(get_factors(n)) - n == n

def binary_to_decimal(binary_str):
    return int(binary_str, 2)

def decimal_to_binary(n):
    return bin(n)[2:]

def hex_to_decimal(hex_str):
    return int(hex_str, 16)

def decimal_to_hex(n):
    return hex(n)[2:]

def octal_to_decimal(octal_str):
    return int(octal_str, 8)

def decimal_to_octal(n):
    return oct(n)[2:]

def sort_strings(strings):
    return sorted(strings)

def reverse_words_in_string(s):
    return ' '.join(reversed(s.split()))

def is_pangram(s):
    return set('abcdefghijklmnopqrstuvwxyz') <= set(s.lower())

def calculate_hypotenuse(a, b):
    return (a**2 + b**2)**0.5

def get_unique_elements(lst):
    return list(set(lst))

def remove_whitespace(s):
    return s.replace(" ", "")

def is_alphabetical(s):
    return all(c.isalpha() for c in s)

def find_common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))

def find_different_elements(lst1, lst2):
    return list(set(lst1) ^ set(lst2))

def generate_primes(n):
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def find_perfect_squares(n):
    return [i**2 for i in range(1, int(n**0.5) + 1)]

def rotate_left(lst, n):
    return lst[n:] + lst[:n]

def rotate_right(lst, n):
    return lst[-n:] + lst[:-n]

def calculate_perimeter_of_rectangle(length, width):
    return 2 * (length + width)

def calculate_area_of_rectangle(length, width):
    return length * width

def calculate_perimeter_of_square(side):
    return 4 * side

def calculate_area_of_square(side):
    return side * side

def calculate_perimeter_of_triangle(a, b, c):
    return a + b + c

def calculate_area_of_triangle(base, height):
    return 0.5 * base * height

def find_largest_in_list(lst):
    return max(lst)

def find_smallest_in_list(lst):
    return min(lst)

def sum_of_list(lst):
    return sum(lst)

def product_of_list(lst):
    product = 1
    for num in lst:
        product *= num
    return product

def calculate_average_of_list(lst):
    return sum(lst) / len(lst)

def find_mode(lst):
    from collections import Counter
    counter = Counter(lst)
    mode = counter.most_common(1)[0][0]
    return mode

def find_range_of_list(lst):
    return max(lst) - min(lst)

def find_variance(lst):
    mean = calculate_average_of_list(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst)

def find_standard_deviation(lst):
    variance = find_variance(lst)
    return variance ** 0.5

def is_perfect_square(n):
    return int(n**0.5) ** 2 == n

def calculate_nth_root(value, n):
    return value ** (1/n)

def count_characters(s):
    return len(s)

def count_specific_character(s, char):
    return s.count(char)

def is_uppercase(s):
    return s.isupper()

def is_lowercase(s):
    return s.islower()

def get_ascii_value(char):
    return ord(char)

def get_character_from_ascii(ascii_value):
    return chr(ascii_value)

def is_digit(s):
    return s.isdigit()

def is_alpha(s):
    return s.isalpha()

def is_alphanumeric(s):
    return s.isalnum()

def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]

def add_matrices(matrix1, matrix2):
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

def multiply_matrices(matrix1, matrix2):
    result = [[0] * len(matrix2[0]) for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

def is_symmetric_matrix(matrix):
    return matrix == transpose_matrix(matrix)

def is_skew_symmetric_matrix(matrix):
    return matrix == [[-matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix))]

def get_diagonal(matrix):
    return [matrix[i][i] for i in range(min(len(matrix), len(matrix[0])))]
