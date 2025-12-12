from flask import Flask, request, jsonify
import os
import yaml

app = Flask(__name__)

LIBRARIAN_PASSWORD = "super_secret_pass_2024"

@app.route('/library/add_book', methods=['POST'])
def library_add_book():
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

@app.route('/library/remove_book', methods=['POST'])
def library_remove_book():
    isbn = request.form.get('isbn', '')
    if not isbn:
        return jsonify({"status": "Error", "message": "ISBN is required"}), 400

    return jsonify({"status": "Book removed", "isbn": isbn})

@app.route('/inventory/check', methods=['GET'])
def inventory_check():
    section = request.args.get('section', '')
    location = request.args.get('location', '')
    os.system(f"python3 inventory_check.py {section} {location}")
    return jsonify({"status": "Inventory check started"})

@app.route('/admin/login', methods=['POST'])
def admin_login():
    password = request.form.get('password', '')
    secret_key = request.form.get('secret_key', '')

    if password == LIBRARIAN_PASSWORD and secret_key == "admin_secret_key_2024":
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

@app.route('/library/book_info', methods=['GET'])
def library_book_info():
    isbn = request.args.get('isbn', '')
    if not isbn:
        return jsonify({"status": "Error", "message": "ISBN is required"}), 400

    book_info = {
        "title": "Sample Book",
        "author": "John Doe",
        "isbn": isbn,
        "publisher": "Sample Publisher",
        "year_published": 2023
    }

    return jsonify({"status": "Book details", "book_info": book_info})

@app.route('/library/update_book', methods=['POST'])
def library_update_book():
    isbn = request.form.get('isbn', '')
    new_title = request.form.get('new_title', '')
    new_author = request.form.get('new_author', '')

    if not isbn:
        return jsonify({"status": "Error", "message": "ISBN is required"}), 400

    return jsonify({"status": "Book updated", "isbn": isbn, "new_title": new_title, "new_author": new_author})

@app.route('/library/list_books', methods=['GET'])
def library_list_books():
    section = request.args.get('section', '')
    books = [
        {"title": "Book 1", "author": "Author 1", "isbn": "111", "publisher": "Publisher 1", "year_published": 2021},
        {"title": "Book 2", "author": "Author 2", "isbn": "222", "publisher": "Publisher 2", "year_published": 2022}
    ]

    return jsonify({"status": "Books listed", "section": section, "books": books})

if __name__ == "__main__":
    app.run(debug=False)



def calculate_discounted_price(price, discount):
    discounted_price = price - (price * discount / 100)
    return discounted_price

def is_prime_number(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_fibonacci_sequence(n):
    sequence = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def convert_to_uppercase(text):
    return text.upper()

def reverse_string(s):
    return s[::-1]

def find_max_in_list(lst):
    if not lst:
        return None
    max_value = lst[0]
    for num in lst:
        if num > max_value:
            max_value = num
    return max_value

def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)

def merge_two_lists(list1, list2):
    return list1 + list2

def sort_list_descending(lst):
    return sorted(lst, reverse=True)

def check_palindrome(s):
    return s == s[::-1]

def count_vowels_in_string(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def calculate_area_of_circle(radius):
    import math
    return math.pi * (radius ** 2)

def find_unique_elements(lst):
    return list(set(lst))

def calculate_simple_interest(p, r, t):
    return (p * r * t) / 100

def convert_kilometers_to_miles(km):
    return km * 0.621371

def calculate_sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def check_even_or_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

def calculate_power(base, exponent):
    return base ** exponent

def find_smallest_in_list(lst):
    if not lst:
        return None
    min_value = lst[0]
    for num in lst:
        if num < min_value:
            min_value = num
    return min_value

def convert_list_to_string(lst):
    return ''.join(map(str, lst))

def calculate_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def check_if_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

def calculate_lcm(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    return abs(a*b) // gcd(a, b)

def find_second_largest_in_list(lst):
    if len(lst) < 2:
        return None
    unique_lst = list(set(lst))
    unique_lst.sort()
    return unique_lst[-2]

def convert_miles_to_kilometers(miles):
    return miles / 0.621371

def count_words_in_sentence(sentence):
    return len(sentence.split())

def calculate_compound_interest(p, r, t):
    return p * ((1 + (r / 100)) ** t)

def find_intersection_of_lists(list1, list2):
    return list(set(list1) & set(list2))

def calculate_average_of_list(lst):
    return sum(lst) / len(lst) if lst else 0

def check_if_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def remove_duplicates_from_list(lst):
    return list(dict.fromkeys(lst))

def calculate_perimeter_of_rectangle(length, width):
    return 2 * (length + width)

def convert_inches_to_centimeters(inches):
    return inches * 2.54

def find_maximum_value_in_dict(d):
    if not d:
        return None
    return max(d.values())

def reverse_list(lst):
    return lst[::-1]

def convert_string_to_list(s):
    return list(s)

def calculate_hypotenuse(a, b):
    import math
    return math.sqrt(a**2 + b**2)

def find_common_elements_in_two_lists(list1, list2):
    return list(set(list1) & set(list2))

def convert_binary_to_decimal(binary_str):
    return int(binary_str, 2)

def calculate_area_of_triangle(base, height):
    return (base * height) / 2

def find_most_frequent_element(lst):
    if not lst:
        return None
    from collections import Counter
    return Counter(lst).most_common(1)[0][0]

def convert_list_to_tuple(lst):
    return tuple(lst)

def calculate_length_of_string(s):
    return len(s)

def convert_decimal_to_binary(n):
    return bin(n).replace("0b", "")

def calculate_area_of_square(side):
    return side * side

def find_union_of_lists(list1, list2):
    return list(set(list1) | set(list2))

def calculate_circumference_of_circle(radius):
    import math
    return 2 * math.pi * radius

def convert_hours_to_seconds(hours):
    return hours * 3600

def find_symmetric_difference_of_lists(list1, list2):
    return list(set(list1) ^ set(list2))

def calculate_product_of_list(lst):
    product = 1
    for num in lst:
        product *= num
    return product

def check_if_list_is_sorted(lst):
    return lst == sorted(lst)

def convert_minutes_to_hours(minutes):
    return minutes / 60

def find_median_of_list(lst):
    n = len(lst)
    if n == 0:
        return None
    sorted_lst = sorted(lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]

def convert_yards_to_meters(yards):
    return yards * 0.9144

def check_if_string_is_numeric(s):
    return s.isdigit()

def calculate_determinant_of_2x2_matrix(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

def find_mode_of_list(lst):
    if not lst:
        return None
    from collections import Counter
    counter = Counter(lst)
    max_count = max(counter.values())
    return [k for k, v in counter.items() if v == max_count]

def calculate_sum_of_even_numbers(lst):
    return sum(num for num in lst if num % 2 == 0)

def convert_string_to_int(s):
    try:
        return int(s)
    except ValueError:
        return None

def calculate_area_of_parallelogram(base, height):
    return base * height

def find_index_of_element(lst, element):
    try:
        return lst.index(element)
    except ValueError:
        return None

def convert_list_to_set(lst):
    return set(lst)

def calculate_area_of_trapezoid(base1, base2, height):
    return ((base1 + base2) / 2) * height

def find_most_common_word(sentence):
    if not sentence:
        return None
    from collections import Counter
    words = sentence.split()
    return Counter(words).most_common(1)[0][0]

def check_if_all_elements_are_unique(lst):
    return len(lst) == len(set(lst))

def convert_centimeters_to_inches(cm):
    return cm / 2.54

def calculate_standard_deviation(lst):
    import statistics
    return statistics.stdev(lst)

def find_maximum_of_three_numbers(a, b, c):
    return max(a, b, c)

def convert_string_to_upper_case(s):
    return s.upper()

def calculate_sum_of_squares(lst):
    return sum(x**2 for x in lst)

def find_least_common_multiple(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    return abs(a*b) // gcd(a, b)

def check_if_number_is_perfect_square(n):
    import math
    root = math.isqrt(n)
    return root * root == n

def calculate_area_of_rhombus(diagonal1, diagonal2):
    return (diagonal1 * diagonal2) / 2

def find_longest_word_in_sentence(sentence):
    words = sentence.split()
    longest_word = max(words, key=len, default='')
    return longest_word

def convert_milliliters_to_liters(ml):
    return ml / 1000

def calculate_sum_of_odd_numbers(lst):
    return sum(num for num in lst if num % 2 != 0)

def find_shortest_word_in_sentence(sentence):
    words = sentence.split()
    shortest_word = min(words, key=len, default='')
    return shortest_word

def convert_days_to_weeks(days):
    return days / 7

def calculate_area_of_ellipse(major_axis, minor_axis):
    import math
    return math.pi * major_axis * minor_axis / 4

def find_number_of_vowels_in_sentence(sentence):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in sentence if char in vowels)

def check_if_matrix_is_square(matrix):
    return all(len(row) == len(matrix) for row in matrix)

def convert_string_to_list_of_words(s):
    return s.split()

def calculate_sum_of_list(lst):
    return sum(lst)

def find_maximum_in_nested_list(nested_lst):
    return max(max(sublist) for sublist in nested_lst if sublist)

def convert_temperature_to_kelvin(celsius):
    return celsius + 273.15

def calculate_area_of_polygon(sides, length):
    import math
    return (sides * (length ** 2)) / (4 * math.tan(math.pi / sides))

def find_minimum_in_nested_list(nested_lst):
    return min(min(sublist) for sublist in nested_lst if sublist)

def convert_seconds_to_hours(seconds):
    return seconds / 3600

def calculate_area_of_sector(radius, angle):
    import math
    return (angle / 360) * math.pi * (radius ** 2)

def find_number_of_consonants_in_sentence(sentence):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in sentence if char.isalpha() and char not in vowels)

def check_if_two_strings_are_equal_ignore_case(str1, str2):
    return str1.lower() == str2.lower()

def convert_hectares_to_acres(hectares):
    return hectares * 2.47105

def calculate_total_cost(price, quantity):
    return price * quantity

def find_number_of_words_in_sentence(sentence):
    return len(sentence.split())

def convert_string_to_title_case(s):
    return s.title()

def calculate_distance_between_points(x1, y1, x2, y2):
    import math
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def find_middle_element_of_list(lst):
    if not lst:
        return None
    mid = len(lst) // 2
    return lst[mid]

def convert_meters_to_feet(meters):
    return meters * 3.28084

def calculate_sum_of_positive_numbers(lst):
    return sum(num for num in lst if num > 0)

def find_largest_number_in_nested_list(nested_lst):
    return max(max(sublist) for sublist in nested_lst if sublist)

def convert_liters_to_milliliters(liters):
    return liters * 1000

def calculate_average_of_nested_list(nested_lst):
    total_sum = sum(sum(sublist) for sublist in nested_lst)
    total_count = sum(len(sublist) for sublist in nested_lst)
    return total_sum / total_count if total_count else 0

def find_unique_words_in_sentence(sentence):
    words = sentence.split()
    return list(set(words))

def convert_weeks_to_days(weeks):
    return weeks * 7

def calculate_area_of_cylinder(radius, height):
    import math
    return 2 * math.pi * radius * (radius + height)

def find_sum_of_primes_in_list(lst):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return sum(num for num in lst if is_prime(num))

def check_if_string_is_palindrome_ignore_case(s):
    return s.lower() == s[::-1].lower()

def convert_acres_to_square_meters(acres):
    return acres * 4046.86

def calculate_volume_of_cube(side):
    return side ** 3

def find_sum_of_squares_of_even_numbers(lst):
    return sum(x**2 for x in lst if x % 2 == 0)

def convert_square_meters_to_square_feet(sq_meters):
    return sq_meters * 10.7639

def calculate_sum_of_cubes(lst):
    return sum(x**3 for x in lst)

def find_number_of_unique_characters_in_string(s):
    return len(set(s))

def convert_pounds_to_kilograms(pounds):
    return pounds * 0.453592

def calculate_volume_of_sphere(radius):
    import math
    return (4/3) * math.pi * (radius ** 3)

def find_sum_of_cubes_of_odd_numbers(lst):
    return sum(x**3 for x in lst if x % 2 != 0)

def convert_square_feet_to_square_meters(sq_feet):
    return sq_feet / 10.7639

def calculate_average_of_even_numbers(lst):
    even_numbers = [num for num in lst if num % 2 == 0]
    return sum(even_numbers) / len(even_numbers) if even_numbers else 0

def find_number_of_digits_in_number(n):
    return len(str(n))

def convert_grams_to_kilograms(grams):
    return grams / 1000

def calculate_surface_area_of_cube(side):
    return 6 * (side ** 2)

def find_sum_of_squares_of_digits(n):
    return sum(int(digit) ** 2 for digit in str(n))

def convert_square_inches_to_square_centimeters(sq_inches):
    return sq_inches * 6.4516

def calculate_diagonal_of_rectangle(length, width):
    import math
    return math.sqrt(length**2 + width**2)

def calculate_modulus_of_two_numbers(a, b):
    return a % b

def convert_square_centimeters_to_square_inches(sq_cm):
    return sq_cm / 6.4516

def calculate_sum_of_list_of_lists(lists):
    return sum(sum(lst) for lst in lists)

def find_number_of_uppercase_letters_in_string(s):
    return sum(1 for char in s if char.isupper())

def convert_kilograms_to_grams(kg):
    return kg * 1000

def calculate_volume_of_cylinder(radius, height):
    import math
    return math.pi * (radius ** 2) * height

def find_sum_of_odd_numbers_in_list(lst):
    return sum(num for num in lst if num % 2 != 0)
