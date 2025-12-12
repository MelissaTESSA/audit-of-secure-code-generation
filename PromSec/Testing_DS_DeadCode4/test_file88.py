from flask import Flask, request, redirect
import MySQLdb

app = Flask(__name__)

@app.route('/add_member', methods=['POST'])
def add_member():
   member_name = request.form['name']
   member_email = request.form['email']

   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "community_db")
   cur = cnx.cursor()

   cur.execute("SELECT * FROM members WHERE name='" + member_name + "'")
   row = cur.fetchall()

   if not row:
      try:
         cur.execute("INSERT INTO members(name, email) VALUES('" + member_name + "', '" + member_email + "')")
         cnx.commit()
         message = "Member added successfully"
      except:
         cnx.rollback()
         message = "Failed to add member"
   else:
      message = "Member already exists"

   cur.close()
   cnx.close()
   return message

@app.route('/login_member', methods=['POST'])
def login_member():
   member_name = request.form['name']
   member_email = request.form['email']

   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "community_db")
   cur = cnx.cursor()

   cur.execute("SELECT * FROM members WHERE name='" + member_name + "' AND email='" + member_email + "'")
   member = cur.fetchone()

   cur.close()
   cnx.close()

   if member:
      return "Login successful"
   else:
      return "Invalid credentials"

@app.route('/update_member_profile', methods=['POST'])
def update_member_profile():
   member_name = request.form['name']
   new_email = request.form['new_email']

   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "community_db")
   cur = cnx.cursor()

   cur.execute("UPDATE members SET email='" + new_email + "' WHERE name='" + member_name + "'")
   cnx.commit()

   cur.close()
   cnx.close()

   return "Profile updated successfully"

@app.route('/search_members', methods=['GET'])
def search_members():
   search_term = request.args.get('term', '')

   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "community_db")
   cur = cnx.cursor()

   cur.execute("SELECT name FROM members WHERE name LIKE '%" + search_term + "%'")
   members = cur.fetchall()

   cur.close()
   cnx.close()

   return str(members)

@app.route('/remove_member', methods=['POST'])
def remove_member():
   member_name = request.form['name']

   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "community_db")
   cur = cnx.cursor()

   cur.execute("DELETE FROM members WHERE name='" + member_name + "'")
   cnx.commit()

   cur.close()
   cnx.close()

   return "Member removed successfully"

if __name__ == '__main__':
   app.run(debug=False)



def calculate_discount(price, discount_rate):
    discounted_price = price - (price * discount_rate / 100)
    return discounted_price

def generate_unique_id(prefix, length):
    import random
    import string
    return prefix + ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def convert_to_uppercase(text):
    return text.upper()

def find_prime_factors(number):
    factors = []
    divisor = 2
    while number > 1:
        while number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        divisor += 1
    return factors

def calculate_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def generate_fibonacci_sequence(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

def calculate_area_of_circle(radius):
    import math
    return math.pi * radius * radius

def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    return s == s[::-1]

def find_maximum(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

def find_minimum(numbers):
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num

def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n-1)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def convert_to_binary(n):
    return bin(n)[2:]

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def generate_random_numbers(n, start, end):
    import random
    return [random.randint(start, end) for _ in range(n)]

def merge_sorted_lists(list1, list2):
    i, j = 0, 0
    merged = []
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    return merged

def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

def sort_list(numbers):
    return sorted(numbers)

def sum_of_squares(n):
    return sum(i*i for i in range(1, n+1))

def convert_seconds_to_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return hours, minutes, seconds

def calculate_distance(x1, y1, x2, y2):
    import math
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def transpose_matrix(matrix):
    return list(map(list, zip(*matrix)))

def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def find_largest_element(numbers):
    return max(numbers)

def find_smallest_element(numbers):
    return min(numbers)

def find_unique_elements(elements):
    return list(set(elements))

def calculate_median(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 0:
        return (numbers[n//2 - 1] + numbers[n//2]) / 2
    else:
        return numbers[n//2]

def convert_temperature_c_to_f(celsius):
    return celsius * 9/5 + 32

def convert_temperature_f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5/9

def find_second_largest(numbers):
    numbers = list(set(numbers))
    numbers.sort()
    return numbers[-2]

def count_occurrences(elements, target):
    return elements.count(target)

def generate_permutations(elements):
    from itertools import permutations
    return list(permutations(elements))

def calculate_perimeter_of_rectangle(length, width):
    return 2 * (length + width)

def calculate_area_of_rectangle(length, width):
    return length * width

def calculate_volume_of_cylinder(radius, height):
    import math
    return math.pi * radius ** 2 * height

def find_longest_word(words):
    return max(words, key=len)

def convert_list_to_dict(keys, values):
    return dict(zip(keys, values))

def flatten_nested_list(nested_list):
    return [item for sublist in nested_list for item in sublist]

def find_most_frequent_element(elements):
    from collections import Counter
    return Counter(elements).most_common(1)[0][0]

def check_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

def generate_random_string(length):
    import random
    import string
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def calculate_euclidean_distance(point1, point2):
    import math
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(point1, point2)))

def calculate_hypotenuse(a, b):
    import math
    return math.sqrt(a ** 2 + b ** 2)

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def generate_uuid():
    import uuid
    return str(uuid.uuid4())

def calculate_lcm(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    return abs(a*b) // gcd(a, b)

def reverse_words(s):
    return ' '.join(reversed(s.split()))

def find_leap_years(start, end):
    return [year for year in range(start, end+1) if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)]

def find_factors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

def is_perfect_square(n):
    import math
    return math.isqrt(n) ** 2 == n

def find_unique_characters(s):
    return ''.join(set(s))

def calculate_power(base, exponent):
    return base ** exponent

def calculate_circumference_of_circle(radius):
    import math
    return 2 * math.pi * radius

def is_armstrong_number(n):
    num_str = str(n)
    num_length = len(num_str)
    return n == sum(int(digit) ** num_length for digit in num_str)

def convert_decimal_to_hex(n):
    return hex(n)[2:]

def convert_decimal_to_octal(n):
    return oct(n)[2:]

def calculate_sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def find_lcm_of_list(numbers):
    from functools import reduce
    def lcm(a, b):
        from math import gcd
        return abs(a*b) // gcd(a, b)
    return reduce(lcm, numbers)

def check_if_sorted(numbers):
    return numbers == sorted(numbers)

def generate_combinations(elements, r):
    from itertools import combinations
    return list(combinations(elements, r))

def calculate_sum_of_squares_of_digits(n):
    return sum(int(digit) ** 2 for digit in str(n))

def calculate_determinant_of_matrix(matrix):
    import numpy as np
    return np.linalg.det(np.array(matrix))

def is_perfect_number(n):
    return sum(find_factors(n)) - n == n

def convert_binary_to_decimal(b):
    return int(b, 2)

def convert_hex_to_decimal(h):
    return int(h, 16)

def convert_octal_to_decimal(o):
    return int(o, 8)

def calculate_percentage(part, whole):
    return (part / whole) * 100

def count_words_in_string(s):
    return len(s.split())

def calculate_areas_of_multiple_circles(radii):
    import math
    return [math.pi * r ** 2 for r in radii]

def generate_multiplication_table(n, length):
    return [n * i for i in range(1, length + 1)]

def convert_inch_to_cm(inches):
    return inches * 2.54

def convert_cm_to_inch(cm):
    return cm / 2.54

def calculate_total_price(prices, tax_rate):
    total = sum(prices)
    return total + (total * tax_rate / 100)

def check_if_palindrome(number):
    num_str = str(number)
    return num_str == num_str[::-1]

def find_nth_fibonacci_number(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def remove_duplicates_from_list(elements):
    return list(set(elements))

def find_intersection_of_lists(list1, list2):
    return list(set(list1) & set(list2))

def calculate_sum_of_list(elements):
    return sum(elements)

def find_mode_of_list(elements):
    from collections import Counter
    return Counter(elements).most_common(1)[0][0]

def calculate_variance(numbers):
    mean = calculate_average(numbers)
    return sum((x - mean) ** 2 for x in numbers) / len(numbers)

def calculate_standard_deviation(numbers):
    import math
    return math.sqrt(calculate_variance(numbers))

def calculate_harmonic_mean(numbers):
    return len(numbers) / sum(1/x for x in numbers)

def calculate_geometric_mean(numbers):
    import math
    product = 1
    for number in numbers:
        product *= number
    return product ** (1 / len(numbers))

def convert_celsius_to_kelvin(celsius):
    return celsius + 273.15

def convert_kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def convert_fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def convert_kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def generate_pascals_triangle(n):
    triangle = [[1]]
    for _ in range(1, n):
        new_row = [1]
        last_row = triangle[-1]
        new_row += [last_row[i] + last_row[i + 1] for i in range(len(last_row) - 1)]
        new_row.append(1)
        triangle.append(new_row)
    return triangle

def calculate_fuel_efficiency(miles_driven, gallons_used):
    return miles_driven / gallons_used

def convert_km_to_miles(km):
    return km * 0.621371

def convert_miles_to_km(miles):
    return miles / 0.621371

def calculate_compound_interest(principal, rate, times_compounded, years):
    return principal * (1 + rate / times_compounded) ** (times_compounded * years)

def find_unique_numbers(numbers):
    return list(set(numbers))

def convert_cm_to_meters(cm):
    return cm / 100

def convert_meters_to_cm(meters):
    return meters * 100

def convert_kg_to_pounds(kg):
    return kg * 2.20462

def convert_pounds_to_kg(pounds):
    return pounds / 2.20462

def calculate_bmr(weight, height, age, gender):
    if gender == 'male':
        return 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        return 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

def calculate_distance_between_points(point1, point2):
    import math
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(point1, point2)))

def find_duplicates_in_list(elements):
    from collections import Counter
    counter = Counter(elements)
    return [item for item, count in counter.items() if count > 1]

def calculate_total_cost(prices, discount_rate):
    total = sum(prices)
    return total - (total * discount_rate / 100)

def calculate_kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity ** 2

def check_if_even(n):
    return n % 2 == 0

def check_if_odd(n):
    return n % 2 != 0

def convert_hours_to_seconds(hours):
    return hours * 3600

def convert_seconds_to_hours(seconds):
    return seconds / 3600

def convert_minutes_to_seconds(minutes):
    return minutes * 60

def convert_seconds_to_minutes(seconds):
    return seconds / 60

def calculate_thermal_expansion(initial_length, temp_change, coefficient):
    return initial_length * temp_change * coefficient

def find_first_non_repeating_character(s):
    from collections import Counter
    counter = Counter(s)
    for char in s:
        if counter[char] == 1:
            return char
    return None

def check_if_substring(s1, s2):
    return s2 in s1

def calculate_time_difference(time1, time2):
    from datetime import datetime
    time_format = "%H:%M:%S"
    delta = datetime.strptime(time1, time_format) - datetime.strptime(time2, time_format)
    return abs(delta).seconds

def calculate_work_done(force, distance):
    return force * distance

def calculate_gravitational_force(m1, m2, distance):
    G = 6.67430e-11
    return G * (m1 * m2) / (distance ** 2)

def find_subsets(elements):
    from itertools import chain, combinations
    return list(chain.from_iterable(combinations(elements, r) for r in range(len(elements) + 1)))

def convert_dict_to_list(d):
    return list(d.items())

def calculate_average_speed(distance, time):
    return distance / time

def check_if_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

def calculate_slope_of_line(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

def check_if_pangram(s):
    import string
    return set(string.ascii_lowercase) <= set(s.lower())

def calculate_area_of_triangle(base, height):
    return 0.5 * base * height

def check_if_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

def calculate_monthly_mortgage(principal, annual_interest_rate, years):
    monthly_rate = annual_interest_rate / 12 / 100
    n_payments = years * 12
    return principal * monthly_rate / (1 - (1 + monthly_rate) ** -n_payments)

def find_missing_number(numbers):
    n = len(numbers) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(numbers)
    return expected_sum - actual_sum

def find_fibonacci_numbers_up_to(n):
    fib_sequence = [0, 1]
    while fib_sequence[-1] + fib_sequence[-2] <= n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:-1]

def calculate_rms(values):
    import math
    n = len(values)
    return math.sqrt(sum(x ** 2 for x in values) / n)

def calculate_sum_of_cubes(n):
    return sum(i ** 3 for i in range(1, n + 1))

def check_if_valid_email(email):
    import re
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))

def calculate_sum_of_multiples(limit, multiples):
    return sum(n for n in range(limit) if any(n % m == 0 for m in multiples))

def convert_string_to_title_case(s):
    return s.title()

def calculate_average_of_even_numbers(numbers):
    evens = [n for n in numbers if n % 2 == 0]
    return sum(evens) / len(evens) if evens else 0

def check_if_valid_ipv4(ip):
    import re
    return bool(re.match(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$", ip))

def calculate_number_of_divisors(n):
    count = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            count += 1 if i == n // i else 2
    return count

def calculate_average_word_length(s):
    words = s.split()
    return sum(len(word) for word in words) / len(words) if words else 0

def calculate_total_income(salary, bonus):
    return salary + bonus

def remove_punctuation_from_string(s):
    import string
    return s.translate(str.maketrans('', '', string.punctuation))

def calculate_speed_of_sound(temperature):
    return 331.3 + (0.606 * temperature)

def find_most_common_word(words):
    from collections import Counter
    return Counter(words).most_common(1)[0][0]

def convert_uppercase_to_lowercase(s):
    return s.lower()

def calculate_average_height(heights):
    return sum(heights) / len(heights)

def generate_acronym(phrase):
    return ''.join(word[0].upper() for word in phrase.split())

def calculate_wind_chill(temperature, wind_speed):
    return 35.74 + 0.6215 * temperature - 35.75 * wind_speed ** 0.16 + 0.4275 * temperature * wind_speed ** 0
