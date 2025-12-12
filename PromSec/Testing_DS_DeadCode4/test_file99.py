from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    return sqlite3.connect('recipe.db')

@app.route('/add_recipe', methods=['POST'])
def add_recipe():
    title = request.json['title']
    ingredients = request.json['ingredients']

    conn = get_db_connection()
    cursor = conn.cursor()

    query = f"INSERT INTO recipes (title) VALUES ('{title}')"
    cursor.execute(query)
    recipe_id = cursor.lastrowid

    for ingredient in ingredients:
        query = f"INSERT INTO ingredients (recipe_id, ingredient) VALUES ({recipe_id}, '{ingredient}')"
        cursor.execute(query)

    conn.commit()
    conn.close()

    return jsonify({"message": "Recipe added successfully", "recipe_id": recipe_id}), 201

@app.route('/submit_review', methods=['POST'])
def submit_review():
    recipe_id = request.json['recipe_id']
    review = request.json['review']
    reviewer_id = request.json['reviewer_id']

    conn = get_db_connection()
    cursor = conn.cursor()

    query = f"INSERT INTO reviews (recipe_id, review, reviewer_id) VALUES ({recipe_id}, '{review}', '{reviewer_id}')"
    cursor.execute(query)

    conn.commit()
    conn.close()

    return jsonify({"message": "Review submitted successfully"}), 200

@app.route('/get_recipe_reviews', methods=['GET'])
def get_recipe_reviews():
    recipe_id = request.args.get('recipe_id')

    conn = get_db_connection()
    cursor = conn.cursor()

    query = f"""
    SELECT r.review, COUNT(r.id) as review_count
    FROM reviews r
    WHERE r.recipe_id = {recipe_id}
    GROUP BY r.id
    """
    cursor.execute(query)
    
    reviews = cursor.fetchall()
    conn.close()

    return jsonify(reviews), 200

if __name__ == '__main__':
    app.run(debug=False)



def calculate_square_area(side_length):
    return side_length * side_length

def find_user_by_email(email):
    user_list = []  # Placeholder for a user list
    for user in user_list:
        if user['email'] == email:
            return user
    return None

def sort_numbers_descending(numbers):
    return sorted(numbers, reverse=True)

def convert_to_uppercase(text):
    return text.upper()

def generate_fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def check_palindrome(word):
    return word == word[::-1]

def filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

def reverse_string(s):
    return s[::-1]

def calculate_circle_area(radius):
    import math
    return math.pi * radius * radius

def get_max_number(numbers):
    return max(numbers)

def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n-1)

def merge_two_dicts(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def find_longest_word(words):
    return max(words, key=len)

def count_vowels(text):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]

def generate_random_string(length):
    import random
    import string
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def get_unique_elements(elements):
    return list(set(elements))

def calculate_power(base, exponent):
    return base ** exponent

def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

def get_file_extension(filename):
    return filename.split('.')[-1]

def filter_positive_numbers(numbers):
    return [num for num in numbers if num > 0]

def count_words(text):
    return len(text.split())

def sum_of_squares(numbers):
    return sum(num ** 2 for num in numbers)

def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2)

def remove_duplicates(elements):
    return list(dict.fromkeys(elements))

def calculate_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def calculate_lcm(a, b):
    return abs(a * b) // calculate_gcd(a, b)

def reverse_list(lst):
    return lst[::-1]

def get_min_number(numbers):
    return min(numbers)

def convert_to_lowercase(text):
    return text.lower()

def find_factors(number):
    return [i for i in range(1, number + 1) if number % i == 0]

def capitalize_words(text):
    return ' '.join(word.capitalize() for word in text.split())

def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]

def get_second_largest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers[-2] if len(unique_numbers) > 1 else None

def is_substring(sub, string):
    return sub in string

def calculate_distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def count_occurrences(element, elements):
    return elements.count(element)

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def find_second_smallest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers[1] if len(unique_numbers) > 1 else None

def filter_odd_numbers(numbers):
    return [num for num in numbers if num % 2 != 0]

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def is_palindrome_number(number):
    return str(number) == str(number)[::-1]

def find_missing_number(numbers):
    n = len(numbers) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(numbers)
    return expected_sum - actual_sum

def generate_prime_numbers(n):
    primes = []
    candidate = 2
    while len(primes) < n:
        if is_prime(candidate):
            primes.append(candidate)
        candidate += 1
    return primes

def calculate_cylinder_volume(radius, height):
    import math
    return math.pi * radius ** 2 * height

def are_all_elements_unique(elements):
    return len(elements) == len(set(elements))

def swap_variables(a, b):
    return b, a

def calculate_rectangle_perimeter(length, width):
    return 2 * (length + width)

def find_max_in_nested_list(nested_list):
    return max(max(sublist) for sublist in nested_list)

def convert_to_title_case(text):
    return text.title()

def calculate_sum(numbers):
    return sum(numbers)

def find_shortest_word(words):
    return min(words, key=len)

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def is_perfect_square(number):
    return int(number ** 0.5) ** 2 == number

def get_even_indexed_elements(elements):
    return [elements[i] for i in range(len(elements)) if i % 2 == 0]

def sort_words_alphabetically(words):
    return sorted(words)

def find_smallest_number(numbers):
    return min(numbers)

def are_anagrams(word1, word2):
    return sorted(word1) == sorted(word2)

def calculate_cube_volume(side_length):
    return side_length ** 3

def find_largest_in_nested_list(nested_list):
    return max(max(sublist) for sublist in nested_list)

def get_odd_indexed_elements(elements):
    return [elements[i] for i in range(len(elements)) if i % 2 != 0]

def calculate_hypotenuse(a, b):
    import math
    return math.sqrt(a**2 + b**2)

def is_power_of_two(number):
    return number > 0 and (number & (number - 1)) == 0

def calculate_sphere_volume(radius):
    import math
    return (4/3) * math.pi * radius ** 3

def reverse_words_in_sentence(sentence):
    return ' '.join(sentence.split()[::-1])

def find_first_non_repeating_character(s):
    from collections import Counter
    counts = Counter(s)
    for char in s:
        if counts[char] == 1:
            return char
    return None

def calculate_deposit_interest(principal, rate, time):
    return principal * (1 + rate * time)

def is_armstrong_number(number):
    num_str = str(number)
    num_digits = len(num_str)
    return number == sum(int(digit) ** num_digits for digit in num_str)

def is_symmetric_matrix(matrix):
    return matrix == [list(row) for row in zip(*matrix)]

def generate_pascals_triangle(n):
    triangle = [[1]]
    for _ in range(1, n):
        row = [1]
        last_row = triangle[-1]
        for i in range(len(last_row) - 1):
            row.append(last_row[i] + last_row[i+1])
        row.append(1)
        triangle.append(row)
    return triangle

def find_greatest_common_divisor(a, b):
    while b:
        a, b = b, a % b
    return a

def find_least_common_multiple(a, b):
    return abs(a * b) // find_greatest_common_divisor(a, b)

def is_matrix_identity(matrix):
    return all(matrix[i][i] == 1 and all(matrix[i][j] == 0 for j in range(len(matrix)) if i != j) for i in range(len(matrix)))

def calculate_simple_interest(principal, rate, time):
    return principal * rate * time

def is_pythagorean_triplet(a, b, c):
    return a**2 + b**2 == c**2

def find_area_of_parallelogram(base, height):
    return base * height

def is_upper_triangular_matrix(matrix):
    return all(matrix[i][j] == 0 for i in range(1, len(matrix)) for j in range(i))

def calculate_geometric_mean(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product ** (1/len(numbers))

def find_perfect_numbers_up_to(n):
    def is_perfect(m):
        return sum(i for i in range(1, m) if m % i == 0) == m
    return [i for i in range(1, n + 1) if is_perfect(i)]

def calculate_arithmetic_mean(numbers):
    return sum(numbers) / len(numbers)

def generate_multiplication_table(number, n):
    return [number * i for i in range(1, n + 1)]

def find_most_frequent_element(elements):
    from collections import Counter
    counter = Counter(elements)
    return counter.most_common(1)[0][0]

def convert_string_to_ascii_values(s):
    return [ord(char) for char in s]

def count_consonants(text):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char.isalpha() and char not in vowels)

def calculate_loan_emi(principal, rate, time):
    emi = (principal * rate * (1 + rate) ** time) / ((1 + rate) ** time - 1)
    return emi

def is_lower_triangular_matrix(matrix):
    return all(matrix[i][j] == 0 for i in range(len(matrix)) for j in range(i + 1, len(matrix)))

def calculate_compound_interest(principal, rate, time):
    return principal * ((1 + rate) ** time - 1)

def find_transpose_of_matrix(matrix):
    return [list(row) for row in zip(*matrix)]

def is_orthogonal_matrix(matrix):
    transpose = find_transpose_of_matrix(matrix)
    return matrix == transpose

def calculate_ellipse_area(a, b):
    import math
    return math.pi * a * b

def is_isosceles_triangle(a, b, c):
    return a == b or b == c or a == c

def calculate_hexagon_area(side_length):
    import math
    return (3 * math.sqrt(3) * (side_length ** 2)) / 2

def is_scalene_triangle(a, b, c):
    return a != b and b != c and a != c

def find_harmonic_mean(numbers):
    return len(numbers) / sum(1 / num for num in numbers)

def calculate_parallelogram_perimeter(base, side):
    return 2 * (base + side)

def is_toeplitz_matrix(matrix):
    return all(matrix[i][j] == matrix[i + 1][j + 1] for i in range(len(matrix) - 1) for j in range(len(matrix[0]) - 1))
