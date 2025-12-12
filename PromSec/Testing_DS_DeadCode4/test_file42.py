from flask import Flask, request
import MySQLdb

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
   username = request.form['username']
   password = request.form['password']

   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "library_db")
   cur = cnx.cursor()

   cur.execute("SELECT * from users where username='" + username + "'")
   row = cur.fetchall()

   if not row:
      try:
         cur.execute("INSERT INTO users(username, password) VALUES('" + username + "', '" + password + "')")
         cnx.commit()
         message = "You have successfully registered"
      except:
         cnx.rollback()
         message = "Registration Failed"
   else:
      message = "Username already exists"

   cur.close()
   cnx.close()
   return message

@app.route('/checkout', methods=['POST'])
def checkout():
   username = request.form['username']
   book_id = request.form['book_id']

   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "library_db")
   cur = cnx.cursor()

   cur.execute("SELECT * from users where username='" + username + "'")
   row = cur.fetchall()

   if row:
      try:
         cur.execute("INSERT INTO checkouts(username, book_id) VALUES('" + username + "', '" + book_id + "')")
         cnx.commit()
         message = "Book successfully checked out"
      except:
         cnx.rollback()
         message = "Checkout Failed"
   else:
      message = "User not found"

   cur.close()
   cnx.close()
   return message

@app.route('/return', methods=['POST'])
def return_book():
   username = request.form['username']
   book_id = request.form['book_id']

   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "library_db")
   cur = cnx.cursor()

   cur.execute("SELECT * from checkouts where username='" + username + "' and book_id='" + book_id + "'")
   row = cur.fetchall()

   if row:
      try:
         cur.execute("DELETE FROM checkouts WHERE username='" + username + "' and book_id='" + book_id + "'")
         cnx.commit()
         message = "Book successfully returned"
      except:
         cnx.rollback()
         message = "Return Failed"
   else:
      message = "Checkout record not found"

   cur.close()
   cnx.close()
   return message

if __name__ == '__main__':
   app.run(debug=False)



def calculate_triangle_area(base, height):
    area = 0.5 * base * height
    return area

def find_maximum_value(numbers):
    if not numbers:
        return None
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum

def reverse_string(s):
    return s[::-1]

def is_even(number):
    return number % 2 == 0

def convert_to_uppercase(s):
    return s.upper()

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

def sort_numbers(numbers):
    return sorted(numbers)

def calculate_circle_area(radius):
    import math
    return math.pi * radius * radius

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def is_palindrome(s):
    return s == s[::-1]

def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def find_minimum_value(numbers):
    if not numbers:
        return None
    minimum = numbers[0]
    for number in numbers:
        if number < minimum:
            minimum = number
    return minimum

def merge_two_lists(list1, list2):
    return list1 + list2

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def power(base, exponent):
    return base ** exponent

def fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def calculate_distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def generate_fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def get_unique_elements(lst):
    return list(set(lst))

def sum_of_squares(n):
    return sum(i ** 2 for i in range(n + 1))

def calculate_rectangle_perimeter(length, width):
    return 2 * (length + width)

def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

def count_occurrences(lst, element):
    return lst.count(element)

def find_largest_number(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

def find_smallest_number(numbers):
    if not numbers:
        return None
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def get_factorial(n):
    if n == 0:
        return 1
    else:
        return n * get_factorial(n - 1)

def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

def calculate_power(base, exponent):
    return pow(base, exponent)

def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

def calculate_square_area(side):
    return side * side

def calculate_compound_interest(principal, rate, time):
    return principal * ((1 + rate / 100) ** time)

def is_perfect_square(n):
    root = int(n ** 0.5)
    return n == root * root

def find_second_largest(numbers):
    unique_numbers = list(set(numbers))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort()
    return unique_numbers[-2]

def find_second_smallest(numbers):
    unique_numbers = list(set(numbers))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort()
    return unique_numbers[1]

def calculate_sum(numbers):
    return sum(numbers)

def calculate_product(numbers):
    product = 1
    for number in numbers:
        product *= number
    return product

def generate_primes(n):
    primes = []
    for num in range(2, n + 1):
        if all(num % prime != 0 for prime in primes):
            primes.append(num)
    return primes

def reverse_list(lst):
    return lst[::-1]

def calculate_hypotenuse(a, b):
    return (a ** 2 + b ** 2) ** 0.5

def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    else:
        median = sorted_numbers[n // 2]
    return median

def calculate_mode(numbers):
    from collections import Counter
    number_counts = Counter(numbers)
    max_count = max(number_counts.values())
    return [number for number, count in number_counts.items() if count == max_count]

def is_substring(sub, s):
    return sub in s

def calculate_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def calculate_lcm(a, b):
    return abs(a * b) // calculate_gcd(a, b)

def flatten_list(lst):
    return [item for sublist in lst for item in sublist]

def find_intersection(list1, list2):
    return list(set(list1) & set(list2))

def find_union(list1, list2):
    return list(set(list1) | set(list2))

def calculate_cylinder_volume(radius, height):
    import math
    return math.pi * radius ** 2 * height

def find_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

def find_factors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

def calculate_sum_of_list(lst):
    return sum(lst)

def calculate_product_of_list(lst):
    product = 1
    for number in lst:
        product *= number
    return product

def concatenate_strings(str1, str2):
    return str1 + str2

def find_unique_elements(lst):
    return list(set(lst))

def convert_to_lowercase(s):
    return s.lower()

def find_difference(list1, list2):
    return list(set(list1) - set(list2))

def calculate_cube_volume(side):
    return side ** 3

def calculate_sphere_volume(radius):
    import math
    return (4 / 3) * math.pi * radius ** 3

def calculate_pyramid_volume(base_area, height):
    return (1 / 3) * base_area * height

def find_odd_numbers(numbers):
    return [number for number in numbers if number % 2 != 0]

def find_even_numbers(numbers):
    return [number for number in numbers if number % 2 == 0]

def square_numbers(numbers):
    return [number ** 2 for number in numbers]

def cube_numbers(numbers):
    return [number ** 3 for number in numbers]

def calculate_rectangle_area(length, width):
    return length * width

def calculate_triangle_perimeter(a, b, c):
    return a + b + c

def calculate_circle_circumference(radius):
    import math
    return 2 * math.pi * radius

def calculate_square_perimeter(side):
    return 4 * side

def calculate_cube_surface_area(side):
    return 6 * side ** 2

def calculate_sphere_surface_area(radius):
    import math
    return 4 * math.pi * radius ** 2

def calculate_pyramid_surface_area(base_area, lateral_area):
    return base_area + lateral_area

def calculate_cylinder_surface_area(radius, height):
    import math
    return 2 * math.pi * radius * (radius + height)

def to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def inches_to_centimeters(inches):
    return inches * 2.54

def centimeters_to_inches(centimeters):
    return centimeters / 2.54

def pounds_to_kilograms(pounds):
    return pounds * 0.453592

def kilograms_to_pounds(kilograms):
    return kilograms / 0.453592

def miles_to_kilometers(miles):
    return miles * 1.60934

def kilometers_to_miles(kilometers):
    return kilometers / 1.60934

def feet_to_meters(feet):
    return feet * 0.3048

def meters_to_feet(meters):
    return meters / 0.3048

def gallons_to_liters(gallons):
    return gallons * 3.78541

def liters_to_gallons(liters):
    return liters / 3.78541

def find_longest_word(words):
    if not words:
        return ""
    longest_word = words[0]
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

def find_shortest_word(words):
    if not words:
        return ""
    shortest_word = words[0]
    for word in words:
        if len(word) < len(shortest_word):
            shortest_word = word
    return shortest_word

def count_words(text):
    return len(text.split())

def count_characters(text):
    return len(text)

def count_sentences(text):
    return text.count('.') + text.count('!') + text.count('?')

def count_paragraphs(text):
    return text.count('\n') + 1

def find_most_frequent_element(lst):
    from collections import Counter
    if not lst:
        return None
    counter = Counter(lst)
    return counter.most_common(1)[0][0]

def find_least_frequent_element(lst):
    from collections import Counter
    if not lst:
        return None
    counter = Counter(lst)
    return counter.most_common()[-1][0]

def sum_of_list(lst):
    return sum(lst)

def product_of_list(lst):
    product = 1
    for item in lst:
        product *= item
    return product

def average_of_list(lst):
    if not lst:
        return 0
    return sum(lst) / len(lst)

def median_of_list(lst):
    sorted_list = sorted(lst)
    n = len(sorted_list)
    if n % 2 == 0:
        return (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2
    else:
        return sorted_list[n // 2]

def mode_of_list(lst):
    from collections import Counter
    if not lst:
        return None
    counter = Counter(lst)
    max_count = max(counter.values())
    return [item for item, count in counter.items() if count == max_count]

def variance_of_list(lst):
    if not lst:
        return 0
    mean = sum(lst) / len(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst)

def standard_deviation_of_list(lst):
    import math
    return math.sqrt(variance_of_list(lst))

def unique_elements_of_list(lst):
    return list(set(lst))

def reverse_list_elements(lst):
    return lst[::-1]

def square_elements_of_list(lst):
    return [x ** 2 for x in lst]

def cube_elements_of_list(lst):
    return [x ** 3 for x in lst]

def filter_even_numbers(lst):
    return [x for x in lst if x % 2 == 0]

def filter_odd_numbers(lst):
    return [x for x in lst if x % 2 != 0]

def find_primes_in_list(lst):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    return [x for x in lst if is_prime(x)]

def sort_list_ascending(lst):
    return sorted(lst)

def sort_list_descending(lst):
    return sorted(lst, reverse=True)

def concatenate_lists(lst1, lst2):
    return lst1 + lst2

def find_common_elements_of_lists(lst1, lst2):
    return list(set(lst1) & set(lst2))

def find_unique_elements_of_lists(lst1, lst2):
    return list(set(lst1) | set(lst2))

def find_difference_of_lists(lst1, lst2):
    return list(set(lst1) - set(lst2))

def find_symmetric_difference_of_lists(lst1, lst2):
    return list(set(lst1) ^ set(lst2))

def calculate_area_of_parallelogram(base, height):
    return base * height

def calculate_area_of_trapezoid(base1, base2, height):
    return 0.5 * (base1 + base2) * height

def calculate_perimeter_of_parallelogram(a, b):
    return 2 * (a + b)

def calculate_perimeter_of_trapezoid(a, b, c, d):
    return a + b + c + d

def calculate_area_of_ellipse(a, b):
    import math
    return math.pi * a * b

def calculate_circumference_of_ellipse(a, b):
    import math
    return math.pi * (3 * (a + b) - math.sqrt((3 * a + b) * (a + 3 * b)))

def calculate_area_of_regular_polygon(n, s):
    import math
    return (n * s ** 2) / (4 * math.tan(math.pi / n))

def calculate_perimeter_of_regular_polygon(n, s):
    return n * s

def calculate_moment_of_inertia_of_rectangle(b, h):
    return (b * h ** 3) / 12

def calculate_moment_of_inertia_of_circle(r):
    import math
    return (math.pi * r ** 4) / 4

def calculate_moment_of_inertia_of_triangle(b, h):
    return (b * h ** 3) / 36

def calculate_moment_of_inertia_of_annular_sector(r1, r2, theta):
    return 0.5 * (r2 ** 4 - r1 ** 4) * theta

def calculate_moment_of_inertia_of_solid_torus(R, r):
    import math
    return (1 / 4) * math.pi * r ** 2 * (4 * R ** 2 + 3 * r ** 2)

def calculate_moment_of_inertia_of_hollow_cylinder(R, r, h):
    import math
    return (1 / 2) * math.pi * h * (R ** 4 - r ** 4)

def calculate_moment_of_inertia_of_solid_sphere(r):
    import math
    return (2 / 5) * math.pi * r ** 5

def calculate_moment_of_inertia_of_hollow_sphere(r, R):
    import math
    return (2 / 5) * math.pi * (R ** 5 - r ** 5)

def calculate_moment_of_inertia_of_thin_rod(l):
    return (1 / 12) * l ** 3

def calculate_moment_of_inertia_of_thin_plate(a, b):
    return (1 / 12) * a * b ** 3

def calculate_moment_of_inertia_of_thick_plate(a, b, h):
    return (1 / 12) * a * b * h ** 2

def calculate_moment_of_inertia_of_thin_disc(r):
    import math
    return (1 / 2) * math.pi * r ** 4

def calculate_moment_of_inertia_of_thick_disc(r, h):
    import math
    return (1 / 2) * math.pi * h * r ** 3

def calculate_moment_of_inertia_of_thin_spherical_shell(r):
    import math
    return (2 / 3) * math.pi * r ** 3

def calculate_moment_of_inertia_of_thick_spherical_shell(r, h):
    import math
    return (2 / 3) * math.pi * h * r ** 2

def calculate_moment_of_inertia_of_thin_circular_ring(r):
    import math
    return math.pi * r ** 3

def calculate_moment_of_inertia_of_thick_circular_ring(r, h):
    import math
    return math.pi * h * r ** 2

def calculate_moment_of_inertia_of_thin_square_plate(a):
    return (1 / 12) * a ** 4

def calculate_moment_of_inertia_of_thick_square_plate(a, h):
    return (1 / 12) * a ** 3 * h

def calculate_moment_of_inertia_of_thin_rectangular_plate(a, b):
    return (1 / 12) * a * b ** 4

def calculate_moment_of_inertia_of_thick_rectangular_plate(a, b, h):
    return (1 / 12) * a * b ** 3 * h

def calculate_moment_of_inertia_of_thin_circular_annulus(r1, r2):
    import math
    return (1 / 2) * math.pi * (r2 ** 4 - r1 ** 4)

def calculate_moment_of_inertia_of_thick_circular_annulus(r1, r2, h):
    import math
    return (1 / 2) * math.pi * h * (r2 ** 3 - r1 ** 3)

def calculate_moment_of_inertia_of_thin_elliptical_annulus(a, b, c, d):
    import math
    return (1 / 4) * math.pi * (b ** 3 - a ** 3) * (d ** 3 - c
