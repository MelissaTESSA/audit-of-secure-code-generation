#copilot mean_prob: 0.7065046051139934
#This file was assembled by gen.py, written by redactedAuthorFirstname redactedAuthorLastname.
from flask import Flask, request, redirect
import re
import hashlib
import MySQLdb
import os
import bcrypt

app = Flask(__name__)

#register url
@app.route('/register', methods=['POST'])
# def register():
#    username = request.form['username']
#    password = request.form['password']
#    #hash the password
#-copilot next line-
#copilot mean_prob: 0.7065046051139934

def register():
   username = request.form['username']
   password = request.form['password']
   #hash the password
   hashed_password = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
   name = request.form['name']
   cweid = request.form['cweid']
   email = request.form['email']
   #initialize MySQL
   db = MySQLdb.connect(host=os.environ["DATABASE_URL"],user=os.environ["DATABASE_USER"], passwd=os.environ["DATABASE_PASSWORD"], db=os.environ["DATABASE_NAME"])
   cursor = db.cursor()
   cursor.execute("SELECT username FROM users WHERE username='" + username + "'")
   user = cursor.fetchone()
   if not user:
      cursor.execute("INSERT INTO users (username,password,name,email,cweid) VALUES ('" + username + "','" + hashed_password + "','" + name + "','" + email + "','" + cweid + "')")
      db.commit()
      #set cookie
      user_id = cursor.lastrowid
      session_id = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(16))
      cursor.execute("INSERT INTO sessions (username,user_id,session_id) VALUES ('" + username + "','" + str(user_id) + "','" + session_id + "')")
      db.commit()
      cursor.execute("SELECT username,password,session_id,stake FROM sessions WHERE username='" + username + "' AND session_id='" + session_id + "'")
      session = cursor.fetchone()
      session_id = session[2]
      stake = session[3]
      return redirect('/login?username=' + username + '&session_id=' + session_id + '&stake=' + str(stake))
   else:
      return 'Username is already taken'



def calculate_area_of_triangle(base, height):
    return 0.5 * base * height

def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def find_maximum_of_three(a, b, c):
    return max(a, b, c)

def reverse_string(s):
    return s[::-1]

def check_even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

def is_prime_number(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def calculate_factorial(number):
    if number == 0:
        return 1
    else:
        return number * calculate_factorial(number - 1)

def fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def calculate_sum_of_list(lst):
    return sum(lst)

def find_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def check_palindrome(s):
    return s == s[::-1]

def calculate_power(base, exponent):
    return base ** exponent

def convert_kilometers_to_miles(km):
    return km * 0.621371

def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def convert_inches_to_centimeters(inches):
    return inches * 2.54

def find_lcm(x, y):
    greater = max(x, y)
    while True:
        if greater % x == 0 and greater % y == 0:
            return greater
        greater += 1

def find_factors_of_number(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

def calculate_average_of_list(lst):
    return sum(lst) / len(lst) if lst else 0

def convert_miles_to_kilometers(miles):
    return miles * 1.60934

def calculate_permutation(n, r):
    return calculate_factorial(n) / calculate_factorial(n - r)

def calculate_combination(n, r):
    return calculate_factorial(n) / (calculate_factorial(r) * calculate_factorial(n - r))

def find_minimum_of_list(lst):
    return min(lst) if lst else None

def calculate_square_root(number):
    return number ** 0.5

def convert_minutes_to_seconds(minutes):
    return minutes * 60

def check_vowel_or_consonant(char):
    vowels = "aeiouAEIOU"
    return "Vowel" if char in vowels else "Consonant"

def calculate_sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

def convert_feet_to_meters(feet):
    return feet * 0.3048

def check_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def calculate_circumference_of_circle(radius):
    return 2 * 3.14159 * radius

def convert_hours_to_seconds(hours):
    return hours * 3600

def check_armstrong_number(number):
    num_str = str(number)
    num_digits = len(num_str)
    return number == sum(int(digit) ** num_digits for digit in num_str)

def find_second_largest_in_list(lst):
    unique_lst = list(set(lst))
    unique_lst.sort(reverse=True)
    return unique_lst[1] if len(unique_lst) > 1 else None

def convert_pounds_to_kilograms(pounds):
    return pounds * 0.453592

def calculate_volume_of_cylinder(radius, height):
    return 3.14159 * (radius ** 2) * height

def convert_seconds_to_hours(seconds):
    return seconds / 3600

def calculate_cube_of_number(number):
    return number ** 3

def find_unique_elements_in_list(lst):
    return list(set(lst))

def convert_liters_to_gallons(liters):
    return liters * 0.264172

def calculate_grade_percentage(marks_obtained, total_marks):
    return (marks_obtained / total_marks) * 100

def reverse_list(lst):
    return lst[::-1]

def convert_cubic_meters_to_cubic_feet(cubic_meters):
    return cubic_meters * 35.3147

def calculate_hypotenuse(a, b):
    return (a ** 2 + b ** 2) ** 0.5

def convert_grams_to_ounces(grams):
    return grams * 0.035274

def find_index_of_element(lst, element):
    return lst.index(element) if element in lst else -1

def calculate_sum_of_even_numbers_in_list(lst):
    return sum(x for x in lst if x % 2 == 0)

def convert_cubic_inches_to_cubic_centimeters(cubic_inches):
    return cubic_inches * 16.3871

def calculate_sum_of_odd_numbers_in_list(lst):
    return sum(x for x in lst if x % 2 != 0)

def convert_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def find_first_repeated_element(lst):
    seen = set()
    for x in lst:
        if x in seen:
            return x
        seen.add(x)
    return None

def calculate_surface_area_of_sphere(radius):
    return 4 * 3.14159 * (radius ** 2)

def convert_days_to_hours(days):
    return days * 24

def find_intersection_of_two_lists(lst1, lst2):
    return list(set(lst1) & set(lst2))

def convert_centimeters_to_inches(cm):
    return cm * 0.393701

def calculate_square_of_number(number):
    return number ** 2

def find_union_of_two_lists(lst1, lst2):
    return list(set(lst1) | set(lst2))

def convert_yards_to_meters(yards):
    return yards * 0.9144

def calculate_sum_of_squares_of_list(lst):
    return sum(x ** 2 for x in lst)

def convert_kilograms_to_pounds(kg):
    return kg * 2.20462

def find_difference_of_two_numbers(a, b):
    return a - b

def calculate_area_of_rectangle(length, width):
    return length * width

def convert_gallons_to_liters(gallons):
    return gallons * 3.78541

def find_product_of_list(lst):
    product = 1
    for num in lst:
        product *= num
    return product

def convert_milliliters_to_ounces(ml):
    return ml * 0.033814

def calculate_area_of_square(side):
    return side ** 2

def convert_knots_to_kilometers_per_hour(knots):
    return knots * 1.852

def find_longest_string_in_list(lst):
    return max(lst, key=len) if lst else None

def convert_acres_to_square_meters(acres):
    return acres * 4046.86

def calculate_cubic_of_number(number):
    return number ** 3

def convert_pascals_to_bars(pascals):
    return pascals * 1e-5

def find_most_frequent_element_in_list(lst):
    return max(set(lst), key=lst.count) if lst else None

def convert_watts_to_horsepower(watts):
    return watts / 745.7

def calculate_area_of_parallelogram(base, height):
    return base * height

def convert_newtons_to_pounds_force(newtons):
    return newtons * 0.224809

def find_shortest_string_in_list(lst):
    return min(lst, key=len) if lst else None

def convert_cubic_feet_to_cubic_meters(cubic_feet):
    return cubic_feet * 0.0283168

def calculate_area_of_trapezoid(base1, base2, height):
    return 0.5 * (base1 + base2) * height

def convert_nanometers_to_micrometers(nanometers):
    return nanometers * 0.001

def find_median_of_list(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]

def convert_kilopascals_to_atmospheres(kPa):
    return kPa / 101.325

def calculate_area_of_rhombus(diagonal1, diagonal2):
    return (diagonal1 * diagonal2) / 2

def convert_inches_to_millimeters(inches):
    return inches * 25.4

def find_greatest_common_divisor_of_list(lst):
    from math import gcd
    from functools import reduce
    return reduce(gcd, lst)

def convert_quarts_to_liters(quarts):
    return quarts * 0.946353

def calculate_sum_of_cubes_of_list(lst):
    return sum(x ** 3 for x in lst)

def convert_tonnes_to_kilograms(tonnes):
    return tonnes * 1000

def find_least_common_multiple_of_list(lst):
    from math import gcd
    from functools import reduce
    def lcm(x, y):
        return x * y // gcd(x, y)
    return reduce(lcm, lst, 1)

def convert_meters_per_second_to_kilometers_per_hour(mps):
    return mps * 3.6

def calculate_sum_of_absolute_differences(lst1, lst2):
    return sum(abs(a - b) for a, b in zip(lst1, lst2))

def convert_hectares_to_acres(hectares):
    return hectares * 2.47105

def find_sum_of_multiples_of_three(lst):
    return sum(x for x in lst if x % 3 == 0)

def convert_millimeters_to_inches(mm):
    return mm * 0.0393701

def calculate_sum_of_prime_numbers_in_list(lst):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return sum(x for x in lst if is_prime(x))

def convert_gigabytes_to_megabytes(gb):
    return gb * 1024

def calculate_area_of_ellipse(a, b):
    return 3.14159 * a * b

def convert_joules_to_calories(joules):
    return joules * 0.239006

def find_unique_pairs_with_sum(lst, target_sum):
    seen = set()
    pairs = set()
    for num in lst:
        complement = target_sum - num
        if complement in seen:
            pairs.add((min(num, complement), max(num, complement)))
        seen.add(num)
    return list(pairs)

def convert_cubic_centimeters_to_liters(cc):
    return cc / 1000

def calculate_geometric_mean_of_list(lst):
    product = 1
    for num in lst:
        product *= num
    return product ** (1 / len(lst))

def convert_kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def find_missing_number_in_sequence(seq):
    n = len(seq) + 1
    total = n * (n + 1) // 2
    return total - sum(seq)

def convert_yards_to_feet(yards):
    return yards * 3

def calculate_arithmetic_mean_of_list(lst):
    return sum(lst) / len(lst) if lst else 0

def convert_milliliters_to_liters(ml):
    return ml / 1000

def find_maximum_subarray_sum(lst):
    max_ending_here = max_so_far = lst[0]
    for x in lst[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

def convert_miles_per_hour_to_meters_per_second(mph):
    return mph * 0.44704

def calculate_harmonic_mean_of_list(lst):
    return len(lst) / sum(1 / x for x in lst) if lst else 0

def convert_ounces_to_grams(ounces):
    return ounces * 28.3495

def find_longest_increasing_subsequence(lst):
    if not lst:
        return []
    lis = [1] * len(lst)
    for i in range(1, len(lst)):
        for j in range(i):
            if lst[i] > lst[j]:
                lis[i] = max(lis[i], lis[j] + 1)
    max_index = lis.index(max(lis))
    sequence = []
    current_length = lis[max_index]
    for i in range(max_index, -1, -1):
        if lis[i] == current_length:
            sequence.append(lst[i])
            current_length -= 1
    return sequence[::-1]

def convert_hectopascals_to_millibars(hPa):
    return hPa

def calculate_manhattan_distance(point1, point2):
    return sum(abs(a - b) for a, b in zip(point1, point2))

def convert_micrograms_to_milligrams(micrograms):
    return micrograms * 0.001

def find_smallest_missing_positive_integer(lst):
    lst = [x for x in lst if x > 0]
    lst.sort()
    smallest_missing = 1
    for num in lst:
        if num == smallest_missing:
            smallest_missing += 1
    return smallest_missing

def convert_pints_to_liters(pints):
    return pints * 0.473176

def calculate_chebyshev_distance(point1, point2):
    return max(abs(a - b) for a, b in zip(point1, point2))

def convert_megabytes_to_kilobytes(mb):
    return mb * 1024

def find_number_of_zeros_in_factorial(n):
    count = 0
    i = 5
    while n // i > 0:
        count += n // i
        i *= 5
    return count

def convert_millimeters_to_centimeters(mm):
    return mm / 10

def calculate_sum_of_perfect_squares_up_to_n(n):
    return sum(i ** 2 for i in range(1, int(n ** 0.5) + 1))

def convert_kilowatts_to_horsepower(kw):
    return kw * 1.34102

def find_longest_palindromic_substring(s):
    n = len(s)
    if n == 0:
        return ""
    longest = s[0]
    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = s[i:j]
            if substring == substring[::-1] and len(substring) > len(longest):
                longest = substring
    return longest

def convert_pounds_to_grams(pounds):
    return pounds * 453.592

def calculate_sum_of_fibonacci_numbers_up_to_n(n):
    a, b = 0, 1
    sum_fib = 0
    while a <= n:
        sum_fib += a
        a, b = b, a + b
    return sum_fib

def convert_miles_to_yards(miles):
    return miles * 1760

def find_most_frequent_word_in_list(lst):
    return max(set(lst), key=lst.count) if lst else None

def convert_picometers_to_nanometers(pm):
    return pm * 0.001

def calculate_average_word_length_in_sentence(sentence):
    words = sentence.split()
    return sum(len(word) for word in words) / len(words) if words else 0

def convert_horsepower_to_kilowatts(hp):
    return hp * 0.7457

def find_all_subsets_of_set(s):
    from itertools import chain, combinations
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s) + 1)))

def convert_barrels_to_gallons(barrels):
    return barrels * 42

def calculate_distance_between_two_points(point1, point2):
    return sum((a - b) ** 2 for a, b in zip(point1, point2)) ** 0.5

def convert_square_miles_to_square_kilometers(sq_miles):
    return sq_miles * 2.58999

def find_all_permutations_of_string(s):
    from itertools import permutations
    return [''.join(p) for p in permutations(s)]

def convert_terabytes_to_gigabytes(tb):
    return tb * 1024

def calculate_sum_of_cubes_up_to_n(n):
    return sum(i ** 3 for i in range(1, n + 1))

def convert_cubic_yards_to_cubic_meters(cu_yd):
    return cu_yd * 0.764555

def find_longest_common_prefix_in_list(lst):
    if not lst:
        return ""
    shortest = min(lst, key=len)
    for i, char in enumerate(shortest):
        for other in lst:
            if other[i] != char:
                return shortest[:i]
    return shortest

def convert_parsecs_to_light_years(parsecs):
    return parsecs * 3.262

def calculate_sum_of_reciprocals_up_to_n(n):
    return sum(1 / i for i in range(1, n + 1))

def convert_square_inches_to_square_centimeters(sq_in):
    return sq_in * 6.4516

def find_longest_consecutive_sequence_in_list(lst):
    num_set = set(lst)
    longest_streak = 0
    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1
            while current_num + 1
