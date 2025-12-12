from flask import Flask, request, jsonify
import os
import yaml

app = Flask(__name__)

LIBRARIAN_PASSWORD = "secret_admin_pass"

@app.route('/add_new_book', methods=['POST'])
def add_new_book():
    yaml_book = request.data.decode('utf-8')
    try:
        book_info = yaml.load(yaml_book, Loader=yaml.FullLoader)
    except yaml.YAMLError as exc:
        return jsonify({"status": "Error", "message": "Invalid YAML format"}), 400
    
    title = book_info.get('title', '')
    author = book_info.get('author', '')
    isbn = book_info.get('isbn', '')
    genre = book_info.get('genre', '')
    publication_year = book_info.get('publication_year', '')
    
    if not title or not author or not isbn:
        return jsonify({"status": "Error", "message": "Missing book information"}), 400

    return jsonify({"status": "New Book added", "title": title, "author": author, "isbn": isbn, "genre": genre, "publication_year": publication_year})

@app.route('/execute_inventory', methods=['GET'])
def execute_inventory():
    section = request.args.get('section', '')
    os.system(f"python3 run_inventory.py {section}")
    return jsonify({"status": "Inventory check started", "section": section})

@app.route('/admin_access', methods=['POST'])
def admin_access():
    password = request.form.get('password', '')
    
    if password == LIBRARIAN_PASSWORD:
        return jsonify({"status": "Admin access granted"})
    else:
        return jsonify({"status": "Access denied"}), 401

@app.route('/update_book_details', methods=['POST'])
def update_book_details():
    yaml_update = request.data.decode('utf-8')
    try:
        update_info = yaml.load(yaml_update, Loader=yaml.FullLoader)
    except yaml.YAMLError as exc:
        return jsonify({"status": "Error", "message": "Invalid YAML format"}), 400
    
    isbn = update_info.get('isbn', '')
    new_title = update_info.get('new_title', '')
    new_author = update_info.get('new_author', '')
    new_genre = update_info.get('new_genre', '')
    new_publication_year = update_info.get('new_publication_year', '')

    if not isbn:
        return jsonify({"status": "Error", "message": "Missing book information"}), 400

    return jsonify({"status": "Book details updated", "isbn": isbn, "new_title": new_title, "new_author": new_author, "new_genre": new_genre, "new_publication_year": new_publication_year})

@app.route('/delete_book', methods=['POST'])
def delete_book():
    yaml_delete = request.data.decode('utf-8')
    try:
        delete_info = yaml.load(yaml_delete, Loader=yaml.FullLoader)
    except yaml.YAMLError as exc:
        return jsonify({"status": "Error", "message": "Invalid YAML format"}), 400
    
    isbn = delete_info.get('isbn', '')
    
    if not isbn:
        return jsonify({"status": "Error", "message": "Missing book information"}), 400

    return jsonify({"status": "Book deleted", "isbn": isbn})

@app.route('/generate_reports', methods=['GET'])
def generate_reports():
    report_type = request.args.get('type', '')
    os.system(f"python3 report_generator.py {report_type}")
    return jsonify({"status": "Report generation started", "type": report_type})

@app.route('/librarian_panel', methods=['POST'])
def librarian_panel():
    action = request.form.get('action', '')
    
    if action == 'backup':
        os.system("python3 backup_script.py")
        return jsonify({"status": "Backup initiated"})
    elif action == 'restore':
        os.system("python3 restore_script.py")
        return jsonify({"status": "Restore initiated"})
    else:
        return jsonify({"status": "Invalid action"}), 400

@app.route('/view_books', methods=['GET'])
def view_books():
    category = request.args.get('category', '')
    os.system(f"python3 view_books.py {category}")
    return jsonify({"status": "Books retrieval initiated", "category": category})

@app.route('/add_new_member', methods=['POST'])
def add_new_member():
    yaml_member = request.data.decode('utf-8')
    try:
        member_info = yaml.load(yaml_member, Loader=yaml.FullLoader)
    except yaml.YAMLError as exc:
        return jsonify({"status": "Error", "message": "Invalid YAML format"}), 400
    
    member_name = member_info.get('name', '')
    member_id = member_info.get('id', '')
    membership_date = member_info.get('membership_date', '')

    if not member_name or not member_id:
        return jsonify({"status": "Error", "message": "Missing member information"}), 400

    return jsonify({"status": "New member added", "name": member_name, "id": member_id, "membership_date": membership_date})

@app.route('/update_member_details', methods=['POST'])
def update_member_details():
    yaml_update = request.data.decode('utf-8')
    try:
        update_info = yaml.load(yaml_update, Loader=yaml.FullLoader)
    except yaml.YAMLError as exc:
        return jsonify({"status": "Error", "message": "Invalid YAML format"}), 400
    
    member_id = update_info.get('id', '')
    new_name = update_info.get('new_name', '')
    new_membership_date = update_info.get('new_membership_date', '')

    if not member_id:
        return jsonify({"status": "Error", "message": "Missing member information"}), 400

    return jsonify({"status": "Member details updated", "id": member_id, "new_name": new_name, "new_membership_date": new_membership_date})

if __name__ == "__main__":
    app.run(debug=False)



def calculate_discount(price, discount_rate):
    discounted_price = price - (price * discount_rate / 100)
    return discounted_price

def find_largest(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

def sort_names(names_list):
    return sorted(names_list)

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def reverse_string(s):
    return s[::-1]

def sum_even_numbers(numbers):
    return sum(x for x in numbers if x % 2 == 0)

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

def is_palindrome(s):
    return s == s[::-1]

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def convert_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def calculate_area_of_circle(radius):
    from math import pi
    return pi * (radius ** 2)

def calculate_area_of_rectangle(length, width):
    return length * width

def calculate_area_of_triangle(base, height):
    return 0.5 * base * height

def generate_fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def count_words(sentence):
    return len(sentence.split())

def find_max_in_list(lst):
    return max(lst)

def find_min_in_list(lst):
    return min(lst)

def is_even(number):
    return number % 2 == 0

def is_odd(number):
    return number % 2 != 0

def sort_numbers(numbers):
    return sorted(numbers)

def square_number(n):
    return n * n

def cube_number(n):
    return n * n * n

def calculate_sum(numbers):
    return sum(numbers)

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def find_duplicates(lst):
    return set(x for x in lst if lst.count(x) > 1)

def remove_duplicates(lst):
    return list(set(lst))

def calculate_power(base, exponent):
    return base ** exponent

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

def find_factors(n):
    return [x for x in range(1, n + 1) if n % x == 0]

def calculate_perimeter_of_rectangle(length, width):
    return 2 * (length + width)

def calculate_perimeter_of_circle(radius):
    from math import pi
    return 2 * pi * radius

def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def calculate_compound_interest(principal, rate, time):
    return principal * (1 + rate / 100) ** time

def find_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    middle = n // 2
    if n % 2 == 0:
        return (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2
    else:
        return sorted_numbers[middle]

def calculate_median(lst):
    lst_sorted = sorted(lst)
    lst_len = len(lst_sorted)
    index = (lst_len - 1) // 2

    if lst_len % 2:
        return lst_sorted[index]
    else:
        return (lst_sorted[index] + lst_sorted[index + 1]) / 2.0

def calculate_mode(numbers):
    from collections import Counter
    c = Counter(numbers)
    mode = c.most_common(1)
    return mode[0][0]

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_lcm(a, b):
    return abs(a * b) // find_gcd(a, b)

def calculate_variance(numbers):
    mean = sum(numbers) / len(numbers)
    return sum((x - mean) ** 2 for x in numbers) / len(numbers)

def calculate_standard_deviation(numbers):
    variance = calculate_variance(numbers)
    return variance ** 0.5

def find_second_largest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers[-2]

def find_second_smallest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers[1]

def convert_miles_to_kilometers(miles):
    return miles * 1.60934

def convert_kilometers_to_miles(kilometers):
    return kilometers / 1.60934

def calculate_age(birth_year, current_year):
    return current_year - birth_year

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def is_armstrong_number(number):
    digits = [int(d) for d in str(number)]
    power = len(digits)
    return sum(d ** power for d in digits) == number

def generate_prime_numbers(n):
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def search_in_list(lst, element):
    return element in lst

def binary_search(lst, element):
    lst.sort()
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = lst[mid]
        if guess == element:
            return mid
        if guess > element:
            high = mid - 1
        else:
            low = mid + 1
    return None

def linear_search(lst, element):
    for index, value in enumerate(lst):
        if value == element:
            return index
    return None

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

def selection_sort(lst):
    n = len(lst)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
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
    else:
        pivot = lst[len(lst) // 2]
        left = [x for x in lst if x < pivot]
        middle = [x for x in lst if x == pivot]
        right = [x for x in lst if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

def heap_sort(lst):
    import heapq
    heapq.heapify(lst)
    return [heapq.heappop(lst) for _ in range(len(lst))]

def count_occurrences(lst, element):
    return lst.count(element)

def get_unique_elements(lst):
    return list(set(lst))

def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]

def transpose_matrix(matrix):
    return list(map(list, zip(*matrix)))

def convert_list_to_string(lst):
    return ''.join(lst)

def convert_string_to_list(s):
    return list(s)

def calculate_hypotenuse(a, b):
    from math import sqrt
    return sqrt(a ** 2 + b ** 2)

def find_missing_number(lst, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(lst)
    return expected_sum - actual_sum

def sort_dict_by_key(d):
    return {k: d[k] for k in sorted(d)}

def sort_dict_by_value(d):
    return {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}

def reverse_list(lst):
    return lst[::-1]

def find_common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))

def find_unique_elements(lst1, lst2):
    return list(set(lst1) ^ set(lst2))

def get_even_numbers(lst):
    return [x for x in lst if x % 2 == 0]

def get_odd_numbers(lst):
    return [x for x in lst if x % 2 != 0]

def capitalize_words(sentence):
    return ' '.join(word.capitalize() for word in sentence.split())

def calculate_distance(x1, y1, x2, y2):
    from math import sqrt
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_slope(x1, y1, x2, y2):
    if x2 == x1:
        return None
    return (y2 - y1) / (x2 - x1)

def find_intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

def find_union(lst1, lst2):
    return list(set(lst1) | set(lst2))

def is_subset(lst1, lst2):
    return set(lst1).issubset(set(lst2))

def is_superset(lst1, lst2):
    return set(lst1).issuperset(set(lst2))
