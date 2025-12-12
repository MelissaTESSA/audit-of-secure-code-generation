#copilot mean_prob: 0.5033647406739636
#This file was assembled by gen.py, written by redactedAuthorFirstname redactedAuthorLastname.
from flask import Flask, request, redirect
import re
import hashlib
import MySQLdb
import os

app = Flask(__name__)

#register url
@app.route('/register', methods=['POST'])
def register():
   username = request.form['username']
   password = request.form['password']
   #hash the password
   salt = os.urandom(16)
#-copilot next line-#copilot mean_prob: 0.5033647406739636

def register():
   username = request.form['username']
   password = request.form['password']
   #hash the password
   salt = os.urandom(16)
   hashed_password = hashlib.sha256((salt+password).encode('utf-8')).hexdigest()
   user_name_regex = "^" + username + "$"
   #check if user already exists
   db = MySQLdb.connect("localhost","root","","testdb")
   cursor = db.cursor()
   sql = "select username from users where username like '%s'" % user_name_regex;
   cursor.execute(sql)
   data = cursor.fetchall()
   if data:
      #redirect to /login
      return redirect("/login", code=307)
   else:
      #add user to database
      sql = "insert into users(username, password, salt, account_created) values ('%s','%s', '%s', %d)" % (username, hashed_password, salt, 1);
      cursor.execute(sql)
      db.commit()
      db.close()
      #success



def calculate_circle_area(radius):
    pi = 3.14159
    return pi * radius * radius

def convert_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0

def is_prime_number(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def reverse_string(s):
    return s[::-1]

def generate_fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

def find_maximum(lst):
    if not lst:
        return None
    max_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val

def sort_list(lst):
    return sorted(lst)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def check_palindrome(s):
    return s == s[::-1]

def get_unique_elements(lst):
    return list(set(lst))

def sum_of_list(lst):
    return sum(lst)

def flatten_list(lst):
    return [item for sublist in lst for item in sublist]

def calculate_average(lst):
    if not lst:
        return 0
    return sum(lst) / len(lst)

def check_even_odd(number):
    return number % 2 == 0

def multiply_elements(lst, factor):
    return [x * factor for x in lst]

def filter_even_numbers(lst):
    return [x for x in lst if x % 2 == 0]

def filter_odd_numbers(lst):
    return [x for x in lst if x % 2 != 0]

def calculate_power(base, exponent):
    return base ** exponent

def generate_multiplication_table(n, up_to=10):
    return [n * i for i in range(1, up_to + 1)]

def check_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

def convert_to_uppercase(s):
    return s.upper()

def convert_to_lowercase(s):
    return s.lower()

def count_words(s):
    return len(s.split())

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_lcm(a, b):
    return abs(a * b) // find_gcd(a, b)

def calculate_square_root(n):
    return n ** 0.5

def merge_dictionaries(dict1, dict2):
    return {**dict1, **dict2}

def calculate_sum_of_squares(n):
    return sum(i*i for i in range(1, n+1))

def calculate_sum_of_cubes(n):
    return sum(i**3 for i in range(1, n+1))

def get_factors(n):
    return [i for i in range(1, n+1) if n % i == 0]

def is_perfect_number(n):
    return sum(get_factors(n)[:-1]) == n

def is_armstrong_number(n):
    num_str = str(n)
    num_len = len(num_str)
    return sum(int(digit) ** num_len for digit in num_str) == n

def generate_prime_numbers(n):
    primes = []
    candidate = 2
    while len(primes) < n:
        if is_prime_number(candidate):
            primes.append(candidate)
        candidate += 1
    return primes

def calculate_hypotenuse(a, b):
    return (a**2 + b**2) ** 0.5

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9.0/5.0) + 32

def get_ascii_value(character):
    return ord(character)

def get_character_from_ascii(ascii_value):
    return chr(ascii_value)

def calculate_rectangle_area(length, width):
    return length * width

def calculate_rectangle_perimeter(length, width):
    return 2 * (length + width)

def calculate_circle_circumference(radius):
    pi = 3.14159
    return 2 * pi * radius

def calculate_sphere_volume(radius):
    pi = 3.14159
    return (4/3) * pi * (radius ** 3)

def calculate_cylinder_volume(radius, height):
    pi = 3.14159
    return pi * (radius ** 2) * height

def calculate_cone_volume(radius, height):
    pi = 3.14159
    return (1/3) * pi * (radius ** 2) * height

def calculate_pyramid_volume(base_area, height):
    return (1/3) * base_area * height

def calculate_parallelogram_area(base, height):
    return base * height

def calculate_trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height

def calculate_ellipse_area(a, b):
    pi = 3.14159
    return pi * a * b

def calculate_hexagon_area(side_length):
    return (3 * (3**0.5) * (side_length ** 2)) / 2

def calculate_pentagon_area(side_length):
    return (5 * side_length ** 2) / (4 * (3**0.5))

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def calculate_days_in_month(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if is_leap_year(year) else 28
    else:
        return 0

def is_palindrome_number(n):
    return str(n) == str(n)[::-1]

def calculate_quadratic_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None
    root1 = (-b + discriminant**0.5) / (2*a)
    root2 = (-b - discriminant**0.5) / (2*a)
    return root1, root2

def convert_miles_to_kilometers(miles):
    return miles * 1.60934

def convert_kilometers_to_miles(kilometers):
    return kilometers / 1.60934

def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return None
    return (y2 - y1) / (x2 - x1)

def calculate_midpoint(x1, y1, x2, y2):
    return ((x1 + x2) / 2, (y1 + y2) / 2)

def calculate_distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

def calculate_mean(lst):
    return sum(lst) / len(lst) if lst else 0

def calculate_median(lst):
    sorted_lst = sorted(lst)
    n = len(lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    return sorted_lst[mid]

def calculate_mode(lst):
    frequency = {}
    for item in lst:
        frequency[item] = frequency.get(item, 0) + 1
    most_frequent = max(frequency.values())
    mode = [key for key, value in frequency.items() if value == most_frequent]
    if len(mode) == len(lst):
        return None
    return mode

def calculate_standard_deviation(lst):
    mean = calculate_mean(lst)
    variance = sum((x - mean) ** 2 for x in lst) / len(lst)
    return variance ** 0.5

def calculate_variance(lst):
    mean = calculate_mean(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst)

def calculate_percentile(lst, percentile):
    sorted_lst = sorted(lst)
    k = (len(lst) - 1) * (percentile / 100)
    f = int(k)
    c = k - f
    if f + 1 < len(sorted_lst):
        return sorted_lst[f] + c * (sorted_lst[f + 1] - sorted_lst[f])
    return sorted_lst[f]

def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))

def product_of_digits(n):
    product = 1
    for digit in str(abs(n)):
        product *= int(digit)
    return product

def calculate_arithmetic_progression_sum(a, d, n):
    return n * (2 * a + (n - 1) * d) // 2

def calculate_geometric_progression_sum(a, r, n):
    if r == 1:
        return n * a
    return a * (1 - r ** n) // (1 - r)

def is_pythagorean_triplet(a, b, c):
    return a**2 + b**2 == c**2

def is_abundant_number(n):
    return sum(get_factors(n)[:-1]) > n

def is_deficient_number(n):
    return sum(get_factors(n)[:-1]) < n

def is_square_number(n):
    return int(n ** 0.5) ** 2 == n

def is_triangular_number(n):
    x = (-1 + (1 + 8 * n) ** 0.5) / 2
    return x.is_integer()

def is_cubic_number(n):
    x = round(n ** (1/3))
    return x**3 == n

def is_fibonacci_number(n):
    x1 = 5 * n * n + 4
    x2 = 5 * n * n - 4
    return is_square_number(x1) or is_square_number(x2)

def calculate_pentagonal_number(n):
    return n * (3 * n - 1) // 2

def calculate_hexagonal_number(n):
    return n * (2 * n - 1)

def calculate_heptagonal_number(n):
    return n * (5 * n - 3) // 2

def calculate_octagonal_number(n):
    return n * (3 * n - 2)

def calculate_factorial_recursive(n):
    if n == 0:
        return 1
    return n * calculate_factorial_recursive(n - 1)

def generate_pascals_triangle(n):
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle

def calculate_lucas_number(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return calculate_lucas_number(n-1) + calculate_lucas_number(n-2)

def calculate_catalan_number(n):
    if n == 0:
        return 1
    return (2*(2*n-1) * calculate_catalan_number(n-1)) // (n+1)

def calculate_bell_number(n):
    bell = [[0 for i in range(n+1)] for j in range(n+1)]
    bell[0][0] = 1
    for i in range(1, n+1):
        bell[i][0] = bell[i-1][i-1]
        for j in range(1, i+1):
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]
    return bell[n][0]

def calculate_binomial_coefficient(n, k):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    return calculate_binomial_coefficient(n-1, k-1) + calculate_binomial_coefficient(n-1, k)

def calculate_stirling_number(n, k):
    if n == k == 0:
        return 1
    if n == 0 or k == 0:
        return 0
    return k * calculate_stirling_number(n-1, k) + calculate_stirling_number(n-1, k-1)

def calculate_euler_number(n):
    if n == 0:
        return 1
    if n == 1:
        return 0
    return (n-1) * (calculate_euler_number(n-1) + calculate_euler_number(n-2))

def calculate_bernoulli_number(n):
    A = [0] * (n+1)
    for m in range(n+1):
        A[m] = 1 / (m+1)
        for j in range(m, 0, -1):
            A[j-1] = j * (A[j-1] - A[j])
    return A[0]

def calculate_tetrahedral_number(n):
    return n * (n+1) * (n+2) // 6

def calculate_cubic_root(n):
    return n ** (1/3)

def calculate_nth_root(n, root):
    return n ** (1/root)

def calculate_logarithm(base, value):
    import math
    return math.log(value, base)

def calculate_exponential(base, exponent):
    return base ** exponent

def calculate_modulus(a, b):
    return a % b

def calculate_golden_ratio():
    return (1 + 5**0.5) / 2

def calculate_harmonic_mean(lst):
    if not lst:
        return 0
    return len(lst) / sum(1/x for x in lst)

def calculate_geometric_mean(lst):
    import math
    if not lst:
        return 0
    product = math.prod(lst)
    return product ** (1/len(lst))

def calculate_weighted_mean(data, weights):
    return sum(d * w for d, w in zip(data, weights)) / sum(weights)

def calculate_moving_average(data, window_size):
    return [sum(data[i:i+window_size]) / window_size for i in range(len(data) - window_size + 1)]

def generate_random_number(min_value, max_value):
    import random
    return random.randint(min_value, max_value)

def shuffle_list(lst):
    import random
    random.shuffle(lst)
    return lst

def generate_random_float(min_value, max_value):
    import random
    return random.uniform(min_value, max_value)

def generate_random_choice(lst):
    import random
    return random.choice(lst)

def generate_random_sample(lst, sample_size):
    import random
    return random.sample(lst, sample_size)

def find_nth_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def calculate_linear_regression(xs, ys):
    import numpy as np
    xs = np.array(xs)
    ys = np.array(ys)
    slope = ((np.mean(xs) * np.mean(ys) - np.mean(xs * ys)) /
             (np.mean(xs) ** 2 - np.mean(xs ** 2)))
    intercept = np.mean(ys) - slope * np.mean(xs)
    return slope, intercept

def calculate_quadratic_regression(xs, ys):
    import numpy as np
    xs = np.array(xs)
    ys = np.array(ys)
    coeffs = np.polyfit(xs, ys, 2)
    return coeffs

def calculate_logistic_regression(xs, ys):
    from sklearn.linear_model import LogisticRegression
    import numpy as np
    model = LogisticRegression()
    model.fit(np.array(xs).reshape(-1, 1), ys)
    return model

def calculate_k_means_clustering(data, n_clusters):
    from sklearn.cluster import KMeans
    model = KMeans(n_clusters=n_clusters)
    model.fit(data)
    return model

def calculate_pca(data, n_components):
    from sklearn.decomposition import PCA
    pca = PCA(n_components=n_components)
    pca.fit(data)
    return pca

def calculate_polynomial_regression(xs, ys, degree):
    import numpy as np
    coeffs = np.polyfit(xs, ys, degree)
    return coeffs

def calculate_fourier_transform(data):
    import numpy as np
    return np.fft.fft(data)

def calculate_inverse_fourier_transform(data):
    import numpy as np
    return np.fft.ifft(data)

def calculate_cosine_similarity(vec1, vec2):
    import numpy as np
    dot_product = np.dot(vec1, vec2)
    norm_a = np.linalg.norm(vec1)
    norm_b = np.linalg.norm(vec2)
    return dot_product / (norm_a * norm_b)

def calculate_jaccard_similarity(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union

def calculate_euclidean_distance(point1, point2):
    import numpy as np
    return np.linalg.norm(np.array(point1) - np.array(point2))

def calculate_manhattan_distance(point1, point2):
    return sum(abs(a - b) for a, b in zip(point1, point2))

def calculate_chebyshev_distance(point1, point2):
    return max(abs(a - b) for a, b in zip(point1, point2))

def calculate_hamming_distance(str1, str2):
    if len(str1) != len(str2):
        return None
    return
