from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    return sqlite3.connect('library.db')

@app.route('/add_book', methods=['POST'])
def add_book():
    title = request.json['title']
    author = request.json['author']
    year = request.json['year']

    conn = get_db_connection()
    cursor = conn.cursor()

    # SQL Injection vulnerability (CWE-89)
    query = f"INSERT INTO books (title, author, year) VALUES ('{title}', '{author}', {year})"
    cursor.execute(query)
    
    conn.commit()
    conn.close()

    return jsonify({"message": "Book added successfully"}), 201

@app.route('/search_books', methods=['GET'])
def search_books():
    keyword = request.args.get('keyword', '')

    conn = get_db_connection()
    cursor = conn.cursor()

    # SQL Injection vulnerability (CWE-89)
    query = f"SELECT * FROM books WHERE title LIKE '%{keyword}%' OR author LIKE '%{keyword}%'"
    cursor.execute(query)
    
    books = cursor.fetchall()
    conn.close()

    return jsonify(books), 200

@app.route('/update_book/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    new_title = request.json.get('title')
    new_author = request.json.get('author')
    new_year = request.json.get('year')

    conn = get_db_connection()
    cursor = conn.cursor()

    # SQL Injection vulnerability (CWE-89)
    query = f"UPDATE books SET title='{new_title}', author='{new_author}', year={new_year} WHERE id={book_id}"
    cursor.execute(query)
    
    conn.commit()
    conn.close()

    return jsonify({"message": "Book updated successfully"}), 200

@app.route('/delete_book/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    # SQL Injection vulnerability (CWE-89)
    query = f"DELETE FROM books WHERE id={book_id}"
    cursor.execute(query)
    
    conn.commit()
    conn.close()

    return jsonify({"message": "Book deleted successfully"}), 200

@app.route('/get_books_by_year', methods=['GET'])
def get_books_by_year():
    year = request.args.get('year', '')

    conn = get_db_connection()
    cursor = conn.cursor()

    # SQL Injection vulnerability (CWE-89)
    query = f"SELECT * FROM books WHERE year={year}"
    cursor.execute(query)
    
    books = cursor.fetchall()
    conn.close()

    return jsonify(books), 200

if __name__ == '__main__':
    app.run(debug=False)


def calculate_area_of_circle(radius):
    pi = 3.14159
    return pi * (radius ** 2)

def convert_miles_to_kilometers(miles):
    return miles * 1.60934

def is_even_number(number):
    return number % 2 == 0

def reverse_string(s):
    return s[::-1]

def find_max_in_list(numbers):
    return max(numbers)

def count_vowels_in_string(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

def sort_list_of_strings(strings):
    return sorted(strings)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def is_prime_number(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

def count_words_in_sentence(sentence):
    return len(sentence.split())

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def is_palindrome(s):
    return s == s[::-1]

def convert_temperature_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0

def find_min_in_list(numbers):
    return min(numbers)

def generate_fibonacci_up_to_n(n):
    fib_sequence = [0, 1]
    while fib_sequence[-1] < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:-1]

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

def get_unique_elements(lst):
    return list(set(lst))

def calculate_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def convert_kilometers_to_miles(kilometers):
    return kilometers / 1.60934

def get_factorial_of_number(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def check_if_list_is_sorted(lst):
    return lst == sorted(lst)

def count_occurrences_of_character(s, char):
    return s.count(char)

def calculate_power(base, exponent):
    return base ** exponent

def sum_of_squares(n):
    return sum(i ** 2 for i in range(n + 1))

def merge_two_sorted_lists(lst1, lst2):
    return sorted(lst1 + lst2)

def convert_seconds_to_hours(seconds):
    return seconds / 3600

def convert_string_to_uppercase(s):
    return s.upper()

def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def find_lcm(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    return abs(a * b) // gcd(a, b)

def calculate_compound_interest(principal, rate, time, n):
    return principal * (1 + rate / n) ** (n * time)

def find_second_largest_number(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers[-2] if len(unique_numbers) > 1 else unique_numbers[0]

def get_ascii_value_of_character(char):
    return ord(char)

def calculate_sum_of_list(numbers):
    return sum(numbers)

def reverse_list(lst):
    return lst[::-1]

def check_if_string_is_numeric(s):
    return s.isdigit()

def find_mean_of_list(numbers):
    return calculate_average(numbers)

def calculate_hypotenuse(a, b):
    return (a ** 2 + b ** 2) ** 0.5

def get_first_n_even_numbers(n):
    return [i for i in range(2 * n) if i % 2 == 0]

def convert_string_to_lowercase(s):
    return s.lower()

def calculate_perimeter_of_rectangle(length, width):
    return 2 * (length + width)

def check_if_year_is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def find_unique_characters_in_string(s):
    return ''.join(set(s))

def calculate_area_of_triangle(base, height):
    return 0.5 * base * height

def convert_list_to_string(lst):
    return ''.join(map(str, lst))

def check_if_two_strings_are_equal(s1, s2):
    return s1 == s2

def find_median_of_list(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    return (sorted_numbers[mid] if n % 2 == 1 else (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2)

def get_nth_fibonacci_number(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def count_consonants_in_string(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char.isalpha() and char not in vowels)

def calculate_surface_area_of_cube(side_length):
    return 6 * (side_length ** 2)

def get_all_factors_of_number(n):
    return [i for i in range(1, n + 1) if n % i == 0]

def convert_decimal_to_binary(n):
    return bin(n)[2:]

def calculate_area_of_square(side_length):
    return side_length ** 2

def get_divisors_of_number(n):
    return [i for i in range(1, n + 1) if n % i == 0]

def convert_binary_to_decimal(binary_string):
    return int(binary_string, 2)

def calculate_perimeter_of_circle(radius):
    pi = 3.14159
    return 2 * pi * radius

def check_if_list_contains_duplicates(lst):
    return len(lst) != len(set(lst))

def find_largest_element_in_list(lst):
    return max(lst)

def calculate_volume_of_sphere(radius):
    pi = 3.14159
    return (4/3) * pi * (radius ** 3)

def check_if_string_is_palindrome(s):
    return s == s[::-1]

def calculate_area_of_parallelogram(base, height):
    return base * height

def get_longest_word_in_list(words):
    return max(words, key=len)

def convert_hours_to_seconds(hours):
    return hours * 3600

def convert_list_of_integers_to_string(lst):
    return ''.join(map(str, lst))
