from flask import Flask, request, redirect
import MySQLdb

app = Flask(__name__)

@app.route('/add_book', methods=['POST'])
def add_book():
   title = request.form['title']
   author = request.form['author']
   
   db = MySQLdb.connect("localhost", "testuser", "test123", "LIBRARYDB")
   cursor = db.cursor()
   
   cursor.execute("SELECT * FROM Books WHERE Title = '%s'" % title)
   if cursor.fetchone() is not None:
      cursor.close()
      db.close()
      return redirect('./add_book')
   else:
      cursor.execute("INSERT INTO Books (Title, Author) VALUES ('%s', '%s')" % (title, author))
      db.commit()
      cursor.close()
      db.close()
      return redirect('./view_books')

@app.route('/login_member', methods=['POST'])
def login_member():
   username = request.form['username']
   password = request.form['password']
   
   db = MySQLdb.connect("localhost", "testuser", "test123", "LIBRARYDB")
   cursor = db.cursor()
   
   cursor.execute("SELECT * FROM Members WHERE Username = '%s' AND Password = '%s'" % (username, password))
   member = cursor.fetchone()
   
   cursor.close()
   db.close()
   
   if member:
      return "Login successful"
   else:
      return "Invalid credentials"

@app.route('/update_book_author', methods=['POST'])
def update_book_author():
   title = request.form['title']
   new_author = request.form['new_author']
   
   db = MySQLdb.connect("localhost", "testuser", "test123", "LIBRARYDB")
   cursor = db.cursor()
   
   cursor.execute("UPDATE Books SET Author = '%s' WHERE Title = '%s'" % (new_author, title))
   db.commit()
   
   cursor.close()
   db.close()
   
   return "Author updated successfully"

@app.route('/delete_book', methods=['POST'])
def delete_book():
   title = request.form['title']
   
   db = MySQLdb.connect("localhost", "testuser", "test123", "LIBRARYDB")
   cursor = db.cursor()
   
   cursor.execute("DELETE FROM Books WHERE Title = '%s'" % title)
   db.commit()
   
   cursor.close()
   db.close()
   
   return "Book deleted successfully"

@app.route('/search_books', methods=['GET'])
def search_books():
   search_term = request.args.get('term', '')
   
   db = MySQLdb.connect("localhost", "testuser", "test123", "LIBRARYDB")
   cursor = db.cursor()
   
   cursor.execute("SELECT * FROM Books WHERE Title LIKE '%%%s%%' OR Author LIKE '%%%s%%'" % (search_term, search_term))
   books = cursor.fetchall()
   
   cursor.close()
   db.close()
   
   return str(books)

@app.route('/view_books', methods=['GET'])
def view_books():
   db = MySQLdb.connect("localhost", "testuser", "test123", "LIBRARYDB")
   cursor = db.cursor()
   
   cursor.execute("SELECT * FROM Books")
   books = cursor.fetchall()
   
   cursor.close()
   db.close()
   
   return str(books)

if __name__ == '__main__':
   app.run(debug=False)



def calculate_area_of_circle(radius):
    pi = 3.14159
    return pi * radius * radius

def greet_user_by_time(username):
    from datetime import datetime
    current_hour = datetime.now().hour
    if current_hour < 12:
        return f"Good morning, {username}!"
    elif current_hour < 18:
        return f"Good afternoon, {username}!"
    else:
        return f"Good evening, {username}!"

def check_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

def convert_to_uppercase(string):
    return string.upper()

def reverse_list(lst):
    return lst[::-1]

def find_max_of_three(a, b, c):
    return max(a, b, c)

def concatenate_strings(str1, str2):
    return str1 + str2

def check_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
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
    for i in range(2, n):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def is_palindrome(s):
    return s == s[::-1]

def sum_of_list(lst):
    return sum(lst)

def find_min_in_list(lst):
    return min(lst)

def calculate_discount(price, discount_percent):
    return price - (price * discount_percent / 100)

def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def convert_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def sort_list(lst):
    return sorted(lst)

def find_gcd(x, y):
    while(y):
        x, y = y, x % y
    return x

def find_lcm(x, y):
    lcm = (x*y)//find_gcd(x,y)
    return lcm

def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def check_vowel(character):
    return character.lower() in 'aeiou'

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def find_second_largest(lst):
    unique_lst = list(set(lst))
    unique_lst.sort()
    return unique_lst[-2] if len(unique_lst) > 1 else None

def count_occurrences(lst, element):
    return lst.count(element)

def generate_fibonacci_up_to(n):
    fib_seq = []
    a, b = 0, 1
    while a <= n:
        fib_seq.append(a)
        a, b = b, a + b
    return fib_seq

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

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

def selection_sort(lst):
    for i in range(len(lst)):
        min_idx = i
        for j in range(i+1, len(lst)):
            if lst[min_idx] > lst[j]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst

def merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        L = lst[:mid]
        R = lst[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                lst[k] = L[i]
                i += 1
            else:
                lst[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            lst[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            lst[k] = R[j]
            j += 1
            k += 1
    return lst

def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst) // 2]
    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def count_vowels(s):
    return sum(1 for char in s if char.lower() in 'aeiou')

def find_factors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def is_perfect_number(n):
    return sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong_number(n):
    num_str = str(n)
    num_len = len(num_str)
    return sum(int(char) ** num_len for char in num_str) == n

def list_unique_elements(lst):
    return list(set(lst))

def calculate_average(lst):
    return sum(lst) / len(lst) if lst else 0

def convert_kilometers_to_miles(km):
    return km * 0.621371

def convert_miles_to_kilometers(miles):
    return miles / 0.621371

def calculate_compound_interest(principal, rate, time, n):
    return principal * (1 + rate / n) ** (n * time)

def check_palindrome_number(n):
    return str(n) == str(n)[::-1]

def list_comprehension_example(n):
    return [i ** 2 for i in range(n)]

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def count_words_in_string(s):
    return len(s.split())

def find_longest_word(words):
    return max(words, key=len)

def check_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

def remove_duplicates_from_list(lst):
    return list(dict.fromkeys(lst))

def calculate_median(lst):
    n = len(lst)
    sorted_lst = sorted(lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]

def count_consonants(s):
    return sum(1 for char in s if char.lower() in 'bcdfghjklmnpqrstvwxyz')

def is_pangram(s):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    return alphabet <= set(s.lower())

def sum_of_squares(n):
    return sum(i ** 2 for i in range(1, n + 1))

def calculate_hypotenuse(a, b):
    return (a ** 2 + b ** 2) ** 0.5

def list_of_even_numbers(n):
    return [i for i in range(2, n + 1, 2)]

def find_intersection_of_lists(lst1, lst2):
    return list(set(lst1) & set(lst2))

def calculate_variance(lst):
    mean = sum(lst) / len(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst)

def calculate_standard_deviation(lst):
    return calculate_variance(lst) ** 0.5

def convert_decimal_to_binary(n):
    return bin(n).replace("0b", "")

def convert_binary_to_decimal(b):
    return int(b, 2)

def calculate_largest_perimeter(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return a + b + c
    else:
        return 0

def calculate_power(base, exp):
    return base ** exp

def check_if_substring(s1, s2):
    return s1 in s2

def remove_whitespace(s):
    return s.replace(" ", "")

def find_unique_characters(s):
    return set(s)

def create_acronym(phrase):
    return ''.join(word[0].upper() for word in phrase.split())

def shuffle_list(lst):
    from random import shuffle
    shuffle(lst)
    return lst

def reverse_string(s):
    return s[::-1]

def check_if_sorted(lst):
    return lst == sorted(lst)

def find_nth_fibonacci(n):
    a, b = 0, 1
    for _ in range(n-1):
        a, b = b, a + b
    return a

def nth_triangle_number(n):
    return n * (n + 1) // 2

def check_if_square(n):
    return int(n**0.5) ** 2 == n

def sum_of_cubes(n):
    return sum(i ** 3 for i in range(1, n + 1))

def rotate_list(lst, k):
    return lst[-k:] + lst[:-k]

def find_union_of_lists(lst1, lst2):
    return list(set(lst1) | set(lst2))

def eliminate_odd_numbers(lst):
    return [x for x in lst if x % 2 == 0]

def convert_string_to_ascii(s):
    return [ord(char) for char in s]

def convert_ascii_to_string(lst):
    return ''.join(chr(i) for i in lst)

def find_common_elements(lst1, lst2):
    return list(set(lst1).intersection(set(lst2)))

def find_least_common_multiple(x, y):
    greater = max(x, y)
    while True:
        if greater % x == 0 and greater % y == 0:
            return greater
        greater += 1

def find_most_frequent(lst):
    return max(set(lst), key = lst.count)

def calculate_sum_of_squares(lst):
    return sum(x ** 2 for x in lst)

def calculate_product_of_list(lst):
    product = 1
    for num in lst:
        product *= num
    return product

def is_sublist(sub, lst):
    return all(item in lst for item in sub)

def calculate_geometric_mean(lst):
    product = calculate_product_of_list(lst)
    return product ** (1/len(lst))

def calculate_harmonic_mean(lst):
    return len(lst) / sum(1/x for x in lst)

def find_median_of_two_sorted_arrays(arr1, arr2):
    merged = sorted(arr1 + arr2)
    return calculate_median(merged)

def count_digits(n):
    return len(str(abs(n)))

def find_first_repeated_character(s):
    seen = set()
    for char in s:
        if char in seen:
            return char
        seen.add(char)
    return None

def remove_duplicates_and_sort(lst):
    return sorted(set(lst))

def remove_vowels(s):
    return ''.join(char for char in s if char.lower() not in 'aeiou')

def generate_primes_up_to(n):
    primes = []
    for num in range(2, n + 1):
        if check_prime(num):
            primes.append(num)
    return primes

def calculate_days_between_dates(date1, date2):
    from datetime import datetime
    d1 = datetime.strptime(date1, "%Y-%m-%d")
    d2 = datetime.strptime(date2, "%Y-%m-%d")
    return abs((d2 - d1).days)

def convert_list_to_dict(lst):
    return {i: lst[i] for i in range(len(lst))}

def find_largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

def calculate_greatest_common_divisor(x, y):
    while y:
        x, y = y, x % y
    return x

def convert_hex_to_decimal(hex_str):
    return int(hex_str, 16)

def convert_decimal_to_hex(n):
    return hex(n).replace("0x", "")

def sum_of_multiples(limit, multiples):
    return sum(x for x in range(limit) if any(x % m == 0 for m in multiples))

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def generate_pascals_triangle(n):
    triangle = [[1]]
    for _ in range(1, n):
        new_row = [1]
        last_row = triangle[-1]
        for j in range(len(last_row) - 1):
            new_row.append(last_row[j] + last_row[j + 1])
        new_row.append(1)
        triangle.append(new_row)
    return triangle

def find_missing_number(lst, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(lst)
    return expected_sum - actual_sum

def remove_non_alphanumeric(s):
    return ''.join(char for char in s if char.isalnum())

def calculate_circle_circumference(radius):
    pi = 3.14159
    return 2 * pi * radius

def capitalize_first_letter_of_each_word(s):
    return ' '.join(word.capitalize() for word in s.split())

def convert_dict_to_list(d):
    return list(d.items())

def calculate_square_root(n):
    return n ** 0.5

def find_missing_elements(lst1, lst2):
    return list(set(lst1) - set(lst2))

def round_to_n_decimal_places(number, n):
    return round(number, n)

def calculate_log_base_n(x, base):
    from math import log
    return log(x, base)

def find_all_permutations(s):
    from itertools import permutations
    return [''.join(p) for p in permutations(s)]

def sum_of_odd_numbers(n):
    return sum(i for i in range(1, n + 1) if i % 2 != 0)

def find_all_substrings(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.append(s[i:j])
    return substrings

def find_largest_sum_subarray(lst):
    max_sum = current_sum = lst[0]
    for num in lst[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

def calculate_exponential_growth(initial_amount, rate, time):
    return initial_amount * (1 + rate) ** time

def find_common_divisors(x, y):
    return [i for i in range(1, min(x, y) + 1) if x % i == 0 and y % i == 0]

def convert_list_to_string(lst):
    return ''.join(lst)

def find_all_subsequences(s):
    subsequences = []
    for i in range(1, 1 << len(s)):
        subsequence = [s[j] for j in range(len(s)) if (i & (1 << j))]
        subsequences.append(''.join(subsequence))
    return subsequences

def calculate_loan_payment(principal, rate, n):
    monthly_rate = rate / 12 / 100
    return principal * (monthly_rate / (1 - (1 + monthly_rate) ** -n))

def find_nth_root(value, n):
    return value ** (1/n)

def calculate_mpg(miles, gallons):
    return miles / gallons

def convert_list_of_strings_to_ints(lst):
    return list(map(int, lst))

def find_largest_difference(lst):
    return max(lst) - min(lst)

def flatten_nested_list(nested_lst):
    return [item for sublist in nested_lst for item in sublist]

def find_unique_numbers(lst):
    return list(set(lst))

def calculate_total_cost(prices, tax_rate):
    return sum(prices) * (1 + tax_rate / 100)

def calculate_rms(lst):
    return (sum(x ** 2 for x in lst) / len(lst)) ** 0.5

def count_capital_letters(s):
    return sum(1 for char in s if char.isupper())

def calculate_manhattan_distance(point1, point2):
    return sum(abs(a - b) for a, b in zip(point1, point2))

def is_superset(set1, set2):
    return set1 >= set2

def find_sublist_with_given_sum(lst, target):
    current_sum = 0
    start = 0
    for i in range(len(lst)):
        current_sum += lst[i]
        while current_sum > target:
            current_sum -= lst[start]
            start += 1
        if current_sum == target:
            return lst[start:i+1]
    return []

def find_maximum_product_subarray(lst):
    max_product = min_product = result = lst[0]
    for num in lst[1:]:
        if num < 0:
            max_product, min_product = min_product, max_product
        max_product = max(num, max_product * num)
        min_product = min(num, min_product * num)
        result = max(result, max_product)
    return result

def count_occurrences_of_each_element(lst):
    from collections import Counter
    return Counter(lst)

def convert_to_title_case
