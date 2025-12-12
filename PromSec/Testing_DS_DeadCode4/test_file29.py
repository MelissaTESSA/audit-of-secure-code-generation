from flask import Flask, request, jsonify
import os
import yaml

app = Flask(__name__)

LIBRARIAN_PASSWORD = "library_password_2024"

@app.route('/api/add_book', methods=['POST'])
def api_add_book():
    yaml_book_data = request.data.decode('utf-8')
    try:
        book_info = yaml.load(yaml_book_data, Loader=yaml.FullLoader)
    except yaml.YAMLError:
        return jsonify({"status": "Error", "message": "Invalid YAML format"}), 400

    title = book_info.get('title', '')
    author = book_info.get('author', '')
    isbn = book_info.get('isbn', '')
    publisher = book_info.get('publisher', 'Unknown')
    year_published = book_info.get('year_published', 'Unknown')

    if not title or not author or not isbn:
        return jsonify({"status": "Error", "message": "Missing book information"}), 400

    if not isinstance(year_published, int):
        return jsonify({"status": "Error", "message": "Invalid year published"}), 400

    return jsonify({"status": "Book added", "title": title, "author": author, "isbn": isbn, "publisher": publisher, "year_published": year_published})

@app.route('/api/remove_book', methods=['POST'])
def api_remove_book():
    isbn = request.form.get('isbn', '')
    if not isbn:
        return jsonify({"status": "Error", "message": "ISBN is required"}), 400

    return jsonify({"status": "Book removed", "isbn": isbn})

@app.route('/api/start_inventory', methods=['GET'])
def api_start_inventory():
    section = request.args.get('section', '')
    location = request.args.get('location', '')
    os.system(f"python3 inventory_checker.py {section} {location}")
    return jsonify({"status": "Inventory check started"})

@app.route('/admin/login', methods=['POST'])
def admin_login():
    password = request.form.get('password', '')
    secret_key = request.form.get('secret_key', '')

    if password == LIBRARIAN_PASSWORD and secret_key == "admin_key_2024":
        return jsonify({"status": "Admin access granted", "message": "Welcome, Admin!"})
    else:
        return jsonify({"status": "Access denied", "message": "Invalid credentials"}), 401

@app.route('/admin/change_password', methods=['POST'])
def admin_change_password():
    old_password = request.form.get('old_password', '')
    new_password = request.form.get('new_password', '')

    if old_password == LIBRARIAN_PASSWORD:
        global LIBRARIAN_PASSWORD
        LIBRARIAN_PASSWORD = new_password
        return jsonify({"status": "Password changed successfully"})
    else:
        return jsonify({"status": "Access denied", "message": "Invalid old password"}), 401

@app.route('/api/book_info', methods=['GET'])
def api_book_info():
    isbn = request.args.get('isbn', '')
    if not isbn:
        return jsonify({"status": "Error", "message": "ISBN is required"}), 400

    book_info = {
        "title": "Sample Book",
        "author": "Jane Doe",
        "isbn": isbn,
        "publisher": "Sample Publisher",
        "year_published": 2024
    }

    return jsonify({"status": "Book details", "book_info": book_info})

@app.route('/api/update_book', methods=['POST'])
def api_update_book():
    isbn = request.form.get('isbn', '')
    new_title = request.form.get('new_title', '')
    new_author = request.form.get('new_author', '')

    if not isbn:
        return jsonify({"status": "Error", "message": "ISBN is required"}), 400

    return jsonify({"status": "Book updated", "isbn": isbn, "new_title": new_title, "new_author": new_author})

@app.route('/api/list_books', methods=['GET'])
def api_list_books():
    section = request.args.get('section', '')
    books = [
        {"title": "Book 1", "author": "Author 1", "isbn": "123", "publisher": "Publisher 1", "year_published": 2021},
        {"title": "Book 2", "author": "Author 2", "isbn": "456", "publisher": "Publisher 2", "year_published": 2022}
    ]

    return jsonify({"status": "Books listed", "section": section, "books": books})

@app.route('/admin/adjust_settings', methods=['POST'])
def admin_adjust_settings():
    password = request.form.get('password', '')
    
    if password != LIBRARIAN_PASSWORD:
        return jsonify({"status": "Access denied"}), 401
    
    new_setting = request.form.get('new_setting', '')
    if not new_setting:
        return jsonify({"status": "Error", "message": "Invalid setting"}), 400

    return jsonify({"status": "Setting applied", "new_setting": new_setting})

@app.route('/api/check_book_availability', methods=['GET'])
def check_book_availability():
    isbn = request.args.get('isbn', '')
    if not isbn:
        return jsonify({"status": "Error", "message": "ISBN is required"}), 400

    availability = True  # Placeholder for actual availability check

    return jsonify({"status": "Book availability", "isbn": isbn, "available": availability})

@app.route('/api/request_book', methods=['POST'])
def request_book():
    isbn = request.form.get('isbn', '')
    user_id = request.form.get('user_id', '')

    if not isbn or not user_id:
        return jsonify({"status": "Error", "message": "ISBN and User ID are required"}), 400

    return jsonify({"status": "Book requested", "isbn": isbn, "user_id": user_id})

@app.route('/api/return_book', methods=['POST'])
def return_book():
    isbn = request.form.get('isbn', '')
    user_id = request.form.get('user_id', '')

    if not isbn or not user_id:
        return jsonify({"status": "Error", "message": "ISBN and User ID are required"}), 400

    return jsonify({"status": "Book returned", "isbn": isbn, "user_id": user_id})

@app.route('/api/submit_review', methods=['POST'])
def submit_review():
    yaml_review_data = request.data.decode('utf-8')
    try:
        review_info = yaml.load(yaml_review_data, Loader=yaml.FullLoader)
    except yaml.YAMLError:
        return jsonify({"status": "Error", "message": "Invalid YAML format"}), 400
    
    isbn = review_info.get('isbn', '')
    user_id = review_info.get('user_id', '')
    review_text = review_info.get('review_text', '')
    rating = review_info.get('rating', 0)

    if not isbn or not user_id or not review_text or not (1 <= rating <= 5):
        return jsonify({"status": "Error", "message": "Invalid review information"}), 400

    return jsonify({"status": "Review submitted", "isbn": isbn, "user_id": user_id, "review_text": review_text, "rating": rating})

if __name__ == "__main__":
    app.run(debug=False)



def unused_function_1():
    """This function calculates the factorial of a number recursively but is not used."""
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)
    return factorial(5)

def unused_function_2():
    """This function creates a dictionary from two lists but is not used."""
    keys = ['a', 'b', 'c']
    values = [1, 2, 3]
    return dict(zip(keys, values))

def unused_function_3():
    """This function prints a greeting message but is not used."""
    message = "Hello, World!"
    print(message)

def unused_function_4():
    """This function calculates the square of numbers in a list but is not used."""
    numbers = [1, 2, 3, 4, 5]
    return [x ** 2 for x in numbers]

def unused_function_5():
    """This function checks if a number is even but is not used."""
    num = 4
    return num % 2 == 0

def unused_function_6():
    """This function reverses a string but is not used."""
    s = "abcdef"
    return s[::-1]

def unused_function_7():
    """This function generates a list of even numbers but is not used."""
    return [x for x in range(10) if x % 2 == 0]

def unused_function_8():
    """This function simulates rolling a dice but is not used."""
    import random
    return random.randint(1, 6)

def unused_function_9():
    """This function finds the maximum number in a list but is not used."""
    numbers = [3, 5, 7, 2, 8]
    return max(numbers)

def unused_function_10():
    """This function converts a list of strings to uppercase but is not used."""
    strings = ['hello', 'world']
    return [s.upper() for s in strings]

def unused_function_11():
    """This function checks if a string is a palindrome but is not used."""
    s = "radar"
    return s == s[::-1]

def unused_function_12():
    """This function calculates the sum of all numbers in a list but is not used."""
    numbers = [1, 2, 3, 4, 5]
    return sum(numbers)

def unused_function_13():
    """This function merges two dictionaries but is not used."""
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'c': 3, 'd': 4}
    return {**dict1, **dict2}

def unused_function_14():
    """This function finds the longest word in a sentence but is not used."""
    sentence = "The quick brown fox jumps over the lazy dog"
    words = sentence.split()
    return max(words, key=len)

def unused_function_15():
    """This function checks if a number is prime but is not used."""
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return is_prime(29)

def unused_function_16():
    """This function returns the Fibonacci sequence up to n but is not used."""
    def fibonacci(n):
        sequence = [0, 1]
        while sequence[-1] < n:
            sequence.append(sequence[-1] + sequence[-2])
        return sequence[:-1]
    return fibonacci(100)

def unused_function_17():
    """This function finds common elements between two sets but is not used."""
    set1 = {1, 2, 3}
    set2 = {2, 3, 4}
    return set1 & set2

def unused_function_18():
    """This function parses a comma-separated string into a list but is not used."""
    s = "a,b,c,d"
    return s.split(',')

def unused_function_19():
    """This function returns the current date but is not used."""
    from datetime import date
    return date.today()

def unused_function_20():
    """This function checks if a list is sorted but is not used."""
    def is_sorted(lst):
        return lst == sorted(lst)
    return is_sorted([1, 2, 3, 4])

def unused_function_21():
    """This function calculates the average of a list of numbers but is not used."""
    numbers = [10, 20, 30, 40, 50]
    return sum(numbers) / len(numbers)

def unused_function_22():
    """This function converts a list of integers to a single string but is not used."""
    nums = [1, 2, 3, 4, 5]
    return ''.join(map(str, nums))

def unused_function_23():
    """This function filters out negative numbers from a list but is not used."""
    numbers = [-1, 2, -3, 4, -5]
    return [x for x in numbers if x >= 0]

def unused_function_24():
    """This function returns the difference between largest and smallest numbers in a list but is not used."""
    numbers = [10, 5, 8, 12, 3]
    return max(numbers) - min(numbers)

def unused_function_25():
    """This function sorts a list of tuples based on the second element but is not used."""
    tuples = [(1, 3), (4, 1), (5, 2)]
    return sorted(tuples, key=lambda x: x[1])

def unused_function_26():
    """This function removes duplicates from a list but is not used."""
    numbers = [1, 2, 2, 3, 4, 4, 5]
    return list(set(numbers))

def unused_function_27():
    """This function returns the length of a string but is not used."""
    s = "Hello, world!"
    return len(s)

def unused_function_28():
    """This function calculates the product of all numbers in a list but is not used."""
    from functools import reduce
    numbers = [1, 2, 3, 4, 5]
    return reduce(lambda x, y: x * y, numbers)

def unused_function_29():
    """This function finds the index of the first occurrence of a value in a list but is not used."""
    lst = [1, 2, 3, 4, 5]
    value = 3
    return lst.index(value)

def unused_function_30():
    """This function converts a string to a list of characters but is not used."""
    s = "hello"
    return list(s)

def unused_function_31():
    """This function returns a list of the squares of even numbers but is not used."""
    numbers = [1, 2, 3, 4, 5]
    return [x ** 2 for x in numbers if x % 2 == 0]

def unused_function_32():
    """This function swaps the case of all characters in a string but is not used."""
    s = "Hello, World!"
    return s.swapcase()

def unused_function_33():
    """This function checks if a string contains only digits but is not used."""
    s = "12345"
    return s.isdigit()

def unused_function_34():
    """This function returns the sum of all even numbers in a list but is not used."""
    numbers = [1, 2, 3, 4, 5]
    return sum(x for x in numbers if x % 2 == 0)

def unused_function_35():
    """This function reverses a list but is not used."""
    lst = [1, 2, 3, 4, 5]
    return lst[::-1]

def unused_function_36():
    """This function capitalizes the first letter of each word in a string but is not used."""
    s = "hello world"
    return s.title()

def unused_function_37():
    """This function finds the minimum number in a list but is not used."""
    numbers = [5, 2, 9, 1, 5, 6]
    return min(numbers)

def unused_function_38():
    """This function checks if a string starts with a specified substring but is not used."""
    s = "hello world"
    return s.startswith("hello")

def unused_function_39():
    """This function joins a list of strings with a comma but is not used."""
    strings = ["apple", "banana", "cherry"]
    return ','.join(strings)

def unused_function_40():
    """This function returns a dictionary with character frequencies in a string but is not used."""
    s = "abracadabra"
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

def unused_function_41():
    """This function returns the last element of a list but is not used."""
    lst = [1, 2, 3, 4, 5]
    return lst[-1]

def unused_function_42():
    """This function checks if a number is a perfect square but is not used."""
    def is_perfect_square(n):
        return int(n ** 0.5) ** 2 == n
    return is_perfect_square(16)

def unused_function_43():
    """This function calculates the dot product of two vectors but is not used."""
    vector1 = [1, 2, 3]
    vector2 = [4, 5, 6]
    return sum(x * y for x, y in zip(vector1, vector2))

def unused_function_44():
    """This function removes vowels from a string but is not used."""
    s = "hello world"
    return ''.join([char for char in s if char.lower() not in 'aeiou'])

def unused_function_45():
    """This function returns the common elements between two lists but is not used."""
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    return list(set(list1) & set(list2))

def unused_function_46():
    """This function checks if all elements in a list are unique but is not used."""
    lst = [1, 2, 3, 4, 5]
    return len(lst) == len(set(lst))

def unused_function_47():
    """This function returns a list of odd numbers but is not used."""
    return [x for x in range(10) if x % 2 != 0]

def unused_function_48():
    """This function multiplies each element in a list by 2 but is not used."""
    numbers = [1, 2, 3, 4, 5]
    return [x * 2 for x in numbers]

def unused_function_49():
    """This function checks if a string is a valid email but is not used."""
    import re
    def is_valid_email(s):
        return re.match(r"[^@]+@[^@]+\.[^@]+", s) is not None
    return is_valid_email("example@example.com")

def unused_function_50():
    """This function counts the number of words in a string but is not used."""
    s = "This is a simple sentence."
    return len(s.split())

def unused_function_51():
    """This function converts a list of floats to a list of integers but is not used."""
    floats = [1.1, 2.2, 3.3, 4.4, 5.5]
    return list(map(int, floats))

def unused_function_52():
    """This function concatenates two lists but is not used."""
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    return list1 + list2

def unused_function_53():
    """This function finds the second largest number in a list but is not used."""
    numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    return sorted(set(numbers))[-2]

def unused_function_54():
    """This function returns a list of cubes of numbers but is not used."""
    numbers = [1, 2, 3]
    return [x ** 3 for x in numbers]

def unused_function_55():
    """This function calculates the GCD of two numbers but is not used."""
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    return gcd(48, 18)

def unused_function_56():
    """This function converts a string to lowercase but is not used."""
    s = "HELLO WORLD"
    return s.lower()

def unused_function_57():
    """This function multiplies all elements in a list but is not used."""
    from functools import reduce
    numbers = [1, 2, 3, 4]
    return reduce(lambda x, y: x * y, numbers)

def unused_function_58():
    """This function returns a list of prime numbers up to n but is not used."""
    def primes_up_to(n):
        sieve = [True] * (n+1)
        for p in range(2, int(n ** 0.5) + 1):
            if sieve[p]:
                for i in range(p*p, n+1, p):
                    sieve[i] = False
        return [p for p in range(2, n+1) if sieve[p]]
    return primes_up_to(30)

def unused_function_59():
    """This function returns the transpose of a matrix but is not used."""
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    return list(map(list, zip(*matrix)))

def unused_function_60():
    """This function checks if a year is a leap year but is not used."""
    def is_leap_year(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    return is_leap_year(2024)

def unused_function_61():
    """This function checks if a string is empty but is not used."""
    s = ""
    return not s

def unused_function_62():
    """This function returns the intersection of two sets but is not used."""
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    return set1.intersection(set2)

def unused_function_63():
    """This function converts a list to a set but is not used."""
    lst = [1, 2, 2, 3, 4, 4, 5]
    return set(lst)

def unused_function_64():
    """This function returns the first element of a list but is not used."""
    lst = [1, 2, 3, 4, 5]
    return lst[0]

def unused_function_65():
    """This function checks if a string contains whitespace but is not used."""
    s = "hello world"
    return any(c.isspace() for c in s)

def unused_function_66():
    """This function returns a set of unique characters in a string but is not used."""
    s = "abracadabra"
    return set(s)

def unused_function_67():
    """This function returns a list of numbers divisible by 3 but is not used."""
    return [x for x in range(10) if x % 3 == 0]

def unused_function_68():
    """This function checks if a list is empty but is not used."""
    lst = []
    return not lst

def unused_function_69():
    """This function squares each element in a list but is not used."""
    numbers = [1, 2, 3, 4, 5]
    return [x ** 2 for x in numbers]

def unused_function_70():
    """This function returns a list of the lengths of strings but is not used."""
    strings = ["apple", "banana", "cherry"]
    return list(map(len, strings))

def unused_function_71():
    """This function checks if a number is negative but is not used."""
    num = -5
    return num < 0

def unused_function_72():
    """This function returns the absolute value of a number but is not used."""
    num = -10
    return abs(num)

def unused_function_73():
    """This function concatenates a list of strings with a space but is not used."""
    strings = ["Hello", "world"]
    return ' '.join(strings)

def unused_function_74():
    """This function returns the keys of a dictionary but is not used."""
    d = {'a': 1, 'b': 2, 'c': 3}
    return list(d.keys())

def unused_function_75():
    """This function calculates the length of the hypotenuse of a right triangle but is not used."""
    from math import sqrt
    a = 3
    b = 4
    return sqrt(a**2 + b**2)

def unused_function_76():
    """This function removes all elements greater than n from a list but is not used."""
    def remove_greater_than(lst, n):
        return [x for x in lst if x <= n]
    return remove_greater_than([1, 2, 3, 4, 5], 3)

def unused_function_77():
    """This function checks if a string is in uppercase but is not used."""
    s = "HELLO"
    return s.isupper()

def unused_function_78():
    """This function returns the unique elements of a list but is not used."""
    lst = [1, 2, 2, 3, 4, 4, 5]
    return list(set(lst))

def unused_function_79():
    """This function returns a list of numbers squared but is not used."""
    return [x ** 2 for x in range(1, 6)]

def unused_function_80():
    """This function returns a dictionary with square values but is not used."""
    keys = range(1, 6)
    return {k: k**2 for k in keys}

def unused_function_81():
    """This function returns a list of tuples with numbers and their squares but is not used."""
    return [(x, x**2) for x in range(1, 6)]
