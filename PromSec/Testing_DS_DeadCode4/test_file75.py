from flask import Flask, request, redirect
import re
import hashlib
import MySQLdb
import os
import bcrypt

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    pw_hash = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
    confirm_password = request.form['confirm_password']

    cnx = MySQLdb.connect("127.0.0.1", "root", "password", "project_manager")
    cur = cnx.cursor()
    cur.execute("SELECT * from users where username='" + username + "'")
    row = cur.fetchall()
    if not row:
        try:
            cur.execute("INSERT INTO users(username, pw_hash) VALUES('%s', '%s')" % (username, pw_hash.decode('utf-8')))
            cnx.commit()
            message = "You have successfully registered"
            cur.close()
            cnx.close()
            return message
        except:
            cnx.rollback()
            message = "Registration Failed"
            cur.close()
            cnx.close()
            return message
    else:
        message = "Username already exists"
        cur.close()
        cnx.close()
        return message

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    cnx = MySQLdb.connect("127.0.0.1", "root", "password", "project_manager")
    cur = cnx.cursor()
    cur.execute("SELECT pw_hash from users where username='" + username + "'")
    row = cur.fetchone()
    cur.close()
    cnx.close()
    if row and bcrypt.checkpw(password.encode('utf8'), row[0].encode('utf8')):
        return redirect('/dashboard')
    else:
        return "Invalid credentials"

@app.route('/create_project', methods=['POST'])
def create_project():
    project_name = request.form['project_name']
    description = request.form['description']
    username = request.form['username']

    cnx = MySQLdb.connect("127.0.0.1", "root", "password", "project_manager")
    cur = cnx.cursor()
    cur.execute("SELECT * from users where username='" + username + "'")
    row = cur.fetchall()
    if row:
        try:
            cur.execute("INSERT INTO projects(project_name, description, username) VALUES('%s', '%s', '%s')" % (project_name, description, username))
            cnx.commit()
            message = "Project created successfully"
            cur.close()
            cnx.close()
            return message
        except:
            cnx.rollback()
            message = "Project creation failed"
            cur.close()
            cnx.close()
            return message
    else:
        message = "User not found"
        cur.close()
        cnx.close()
        return message

@app.route('/add_task', methods=['POST'])
def add_task():
    project_name = request.form['project_name']
    task_name = request.form['task_name']
    task_description = request.form['task_description']

    cnx = MySQLdb.connect("127.0.0.1", "root", "password", "project_manager")
    cur = cnx.cursor()
    cur.execute("SELECT * from projects where project_name='" + project_name + "'")
    row = cur.fetchall()
    if row:
        try:
            cur.execute("INSERT INTO tasks(project_name, task_name, task_description) VALUES('%s', '%s', '%s')" % (project_name, task_name, task_description))
            cnx.commit()
            message = "Task added successfully"
            cur.close()
            cnx.close()
            return message
        except:
            cnx.rollback()
            message = "Task addition failed"
            cur.close()
            cnx.close()
            return message
    else:
        message = "Project not found"
        cur.close()
        cnx.close()
        return message

@app.route('/view_tasks', methods=['GET'])
def view_tasks():
    project_name = request.args.get('project_name')

    cnx = MySQLdb.connect("127.0.0.1", "root", "password", "project_manager")
    cur = cnx.cursor()
    cur.execute("SELECT * from tasks where project_name='%s'" % project_name)
    tasks = cur.fetchall()
    cur.close()
    cnx.close()
    return jsonify(tasks)

if __name__ == '__main__':
    app.run(debug=False)



def calculate_area_of_circle(radius):
    pi = 3.14159
    return pi * radius * radius

def reverse_string(s):
    return s[::-1]

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def check_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def sum_of_list(lst):
    return sum(lst)

def find_max(lst):
    return max(lst)

def find_min(lst):
    return min(lst)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def calculate_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def calculate_lcm(x, y):
    return abs(x * y) // calculate_gcd(x, y)

def binary_search(arr, x):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

def is_palindrome(s):
    return s == s[::-1]

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def find_duplicates(lst):
    return list(set([x for x in lst if lst.count(x) > 1]))

def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

def convert_to_binary(n):
    return bin(n).replace("0b", "")

def convert_to_hexadecimal(n):
    return hex(n).replace("0x", "")

def convert_to_octal(n):
    return oct(n).replace("0o", "")

def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

def generate_fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def count_vowels(s):
    return sum(s.count(v) for v in "aeiouAEIOU")

def count_consonants(s):
    return sum(s.count(c) for c in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")

def find_factors(n):
    return [x for x in range(1, n + 1) if n % x == 0]

def check_armstrong_number(n):
    num = str(n)
    length = len(num)
    return sum(int(digit) ** length for digit in num) == n

def check_perfect_number(n):
    return sum(x for x in range(1, n) if n % x == 0) == n

def check_harshad_number(n):
    return n % sum(int(digit) for digit in str(n)) == 0

def find_greatest_common_divisor(x, y):
    while y:
        x, y = y, x % y
    return x

def find_least_common_multiple(x, y):
    return abs(x * y) // find_greatest_common_divisor(x, y)

def encrypt_caesar_cipher(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)
    return result

def decrypt_caesar_cipher(text, shift):
    return encrypt_caesar_cipher(text, -shift)

def validate_email(email):
    import re
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))

def convert_celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def convert_fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def calculate_bmi(weight, height):
    return weight / (height * height)

def calculate_compound_interest(principal, rate, time):
    return principal * (1 + rate / 100) ** time

def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def find_nth_prime(n):
    count, num = 0, 1
    while count < n:
        num += 1
        if check_prime(num):
            count += 1
    return num

def generate_random_string(length):
    import random
    import string
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def calculate_distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

def find_median(lst):
    lst.sort()
    n = len(lst)
    if n % 2 == 0:
        return (lst[n//2 - 1] + lst[n//2]) / 2
    else:
        return lst[n//2]

def find_mode(lst):
    frequency = {}
    for item in lst:
        frequency[item] = frequency.get(item, 0) + 1
    mode = max(frequency, key=frequency.get)
    return mode

def convert_seconds_to_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"

def calculate_factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def find_largest_product_in_series(series, n):
    max_product = 0
    for i in range(len(series) - n + 1):
        product = 1
        for j in range(n):
            product *= int(series[i + j])
        if product > max_product:
            max_product = product
    return max_product

def convert_list_to_string(lst):
    return ''.join(map(str, lst))

def convert_string_to_list(s):
    return list(s)

def calculate_mean(lst):
    return sum(lst) / len(lst)

def calculate_variance(lst):
    mean = calculate_mean(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst)

def calculate_standard_deviation(lst):
    return calculate_variance(lst) ** 0.5

def find_second_largest(lst):
    first, second = float('-inf'), float('-inf')
    for number in lst:
        if number > first:
            first, second = number, first
        elif number > second and number != first:
            second = number
    return second

def find_second_smallest(lst):
    first, second = float('inf'), float('inf')
    for number in lst:
        if number < first:
            first, second = number, first
        elif number < second and number != first:
            second = number
    return second

def is_valid_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def check_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def count_words_in_string(s):
    return len(s.split())

def capitalize_words_in_string(s):
    return ' '.join(word.capitalize() for word in s.split())

def count_occurrences_of_substring(s, substring):
    return s.count(substring)

def find_unique_elements(lst):
    return list(set(lst))

def calculate_average(lst):
    return sum(lst) / len(lst)

def convert_kilometers_to_miles(km):
    return km * 0.621371

def convert_miles_to_kilometers(miles):
    return miles / 0.621371

def swap_elements(a, b):
    return b, a

def find_maximum_subarray_sum(arr):
    max_so_far = arr[0]
    max_ending_here = arr[0]
    for i in range(1, len(arr)):
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

def find_minimum_subarray_sum(arr):
    min_so_far = arr[0]
    min_ending_here = arr[0]
    for i in range(1, len(arr)):
        min_ending_here = min(arr[i], min_ending_here + arr[i])
        min_so_far = min(min_so_far, min_ending_here)
    return min_so_far

def is_substring(sub, string):
    return sub in string

def is_superstring(super, string):
    return all(char in super for char in string)

def is_perfect_square(n):
    return int(n**0.5)**2 == n

def convert_decimal_to_binary(n):
    return bin(n)[2:]

def convert_decimal_to_hexadecimal(n):
    return hex(n)[2:]

def convert_decimal_to_octal(n):
    return oct(n)[2:]

def convert_binary_to_decimal(b):
    return int(b, 2)

def convert_hexadecimal_to_decimal(h):
    return int(h, 16)

def convert_octal_to_decimal(o):
    return int(o, 8)

def find_all_divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

def find_common_elements(lst1, lst2):
    return list(set(lst1).intersection(lst2))

def find_unique_common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))

def find_missing_number(arr, n):
    total = n * (n + 1) // 2
    return total - sum(arr)

def find_missing_numbers(lst, n):
    return list(set(range(1, n + 1)) - set(lst))

def check_if_sorted(lst):
    return lst == sorted(lst) or lst == sorted(lst, reverse=True)

def find_longest_word(lst):
    return max(lst, key=len)

def find_shortest_word(lst):
    return min(lst, key=len)

def calculate_hypotenuse(a, b):
    return (a**2 + b**2)**0.5

def is_pythagorean_triplet(a, b, c):
    return a**2 + b**2 == c**2

def find_pythagorean_triplets(n):
    return [(a, b, c) for a in range(1, n) for b in range(a, n) for c in range(b, n) if a**2 + b**2 == c**2]

def calculate_square_root(n):
    return n**0.5

def calculate_cube_root(n):
    return n**(1/3)

def calculate_nth_root(n, m):
    return n**(1/m)

def find_longest_palindrome(s):
    longest = ""
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j + 1]
            if is_palindrome(substring) and len(substring) > len(longest):
                longest = substring
    return longest

def find_shortest_palindrome(s):
    shortest = s if is_palindrome(s) else ""
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j + 1]
            if is_palindrome(substring):
                if len(shortest) == 0 or len(substring) < len(shortest):
                    shortest = substring
    return shortest

def calculate_sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def calculate_product_of_digits(n):
    product = 1
    for digit in str(n):
        product *= int(digit)
    return product

def find_armstrong_numbers(n):
    return [x for x in range(n) if check_armstrong_number(x)]

def find_perfect_numbers(n):
    return [x for x in range(n) if check_perfect_number(x)]

def find_harshad_numbers(n):
    return [x for x in range(n) if check_harshad_number(x)]

def calculate_sum_of_squares(n):
    return sum(x**2 for x in range(1, n + 1))

def calculate_sum_of_cubes(n):
    return sum(x**3 for x in range(1, n + 1))

def convert_to_uppercase(s):
    return s.upper()

def convert_to_lowercase(s):
    return s.lower()

def swap_case(s):
    return s.swapcase()

def reverse_words_in_string(s):
    return ' '.join(s.split()[::-1])

def sort_words_in_string(s):
    return ' '.join(sorted(s.split()))

def find_longest_sentence(text):
    sentences = text.split('.')
    return max(sentences, key=len)

def find_shortest_sentence(text):
    sentences = text.split('.')
    return min(sentences, key=len)

def count_sentences_in_text(text):
    return text.count('.') + text.count('!') + text.count('?')

def count_paragraphs_in_text(text):
    return text.count('\n') + 1

def find_unique_words(text):
    words = text.split()
    return list(set(words))

def calculate_total_characters(text):
    return len(text)

def calculate_total_words(text):
    return len(text.split())

def calculate_total_sentences(text):
    return text.count('.') + text.count('!') + text.count('?')

def calculate_total_paragraphs(text):
    return text.count('\n') + 1

def find_palindromic_words(text):
    words = text.split()
    return [word for word in words if is_palindrome(word)]

def find_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

def is_pangram(text):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    return alphabet <= set(text.lower())

def find_pangram_sentences(text):
    sentences = text.split('.')
    return [sentence for sentence in sentences if is_pangram(sentence)]

def count_pangram_sentences(text):
    return len(find_pangram_sentences(text))

def find_unique_characters(text):
    return list(set(text))

def find_most_frequent_character(text):
    frequency = {}
    for char in text:
        frequency[char] = frequency.get(char, 0) + 1
    return max(frequency, key=frequency.get)

def find_least_frequent_character(text):
    frequency = {}
    for char in text:
        frequency[char] = frequency.get(char, 0) + 1
    return min(frequency, key=frequency.get)
