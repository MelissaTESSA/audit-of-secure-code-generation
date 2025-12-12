from flask import Flask, request, redirect
import MySQLdb

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
   username = request.form['username']
   password = request.form['password']
   
   db = MySQLdb.connect("localhost","testuser","test123","TESTDB")
   cursor = db.cursor()
   
   # SQL Injection vulnerability (CWE-89)
   cursor.execute("SELECT * FROM User WHERE Username = '%s'" % username)
   if cursor.fetchone() is not None:
      cursor.close()
      db.close()
      return redirect('./register')
   else:
      # SQL Injection vulnerability (CWE-89)
      cursor.execute("INSERT INTO User VALUES ('%s', '%s')" % (username, password))
      db.commit()
      cursor.close()
      db.close()
      return redirect('./login')

@app.route('/login', methods=['POST'])
def login():
   username = request.form['username']
   password = request.form['password']
   
   db = MySQLdb.connect("localhost","testuser","test123","TESTDB")
   cursor = db.cursor()
   
   # SQL Injection vulnerability (CWE-89)
   cursor.execute("SELECT * FROM User WHERE Username = '%s' AND Password = '%s'" % (username, password))
   user = cursor.fetchone()
   
   cursor.close()
   db.close()
   
   if user:
      return "Login successful"
   else:
      return "Invalid credentials"

@app.route('/update_profile', methods=['POST'])
def update_profile():
   username = request.form['username']
   new_email = request.form['email']
   
   db = MySQLdb.connect("localhost","testuser","test123","TESTDB")
   cursor = db.cursor()
   
   # SQL Injection vulnerability (CWE-89)
   cursor.execute("UPDATE User SET Email = '%s' WHERE Username = '%s'" % (new_email, username))
   db.commit()
   
   cursor.close()
   db.close()
   
   return "Profile updated successfully"

@app.route('/delete_user', methods=['POST'])
def delete_user():
   username = request.form['username']
   
   db = MySQLdb.connect("localhost","testuser","test123","TESTDB")
   cursor = db.cursor()
   
   # SQL Injection vulnerability (CWE-89)
   cursor.execute("DELETE FROM User WHERE Username = '%s'" % username)
   db.commit()
   
   cursor.close()
   db.close()
   
   return "User deleted successfully"

@app.route('/search_users', methods=['GET'])
def search_users():
   search_term = request.args.get('term', '')
   
   db = MySQLdb.connect("localhost","testuser","test123","TESTDB")
   cursor = db.cursor()
   
   # SQL Injection vulnerability (CWE-89)
   cursor.execute("SELECT * FROM User WHERE Username LIKE '%%%s%%'" % search_term)
   users = cursor.fetchall()
   
   cursor.close()
   db.close()
   
   return str(users)

if __name__ == '__main__':
   app.run(debug=False)


def calculate_discount(price, discount):
    discounted_price = price - (price * discount / 100)
    return discounted_price

def find_max_in_list(numbers):
    if not numbers:
        return None
    return max(numbers)

def sort_names_by_length(names):
    return sorted(names, key=len)

def convert_to_uppercase(text):
    return text.upper()

def sum_of_squares(n):
    return sum(i**2 for i in range(n))

def reverse_string(s):
    return s[::-1]

def check_palindrome(s):
    return s == s[::-1]

def generate_fibonacci(n):
    fib_sequence = [0, 1]
    for _ in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def count_vowels(s):
    return sum(1 for char in s if char.lower() in 'aeiou')

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def calculate_area_of_circle(radius):
    return 3.14159 * radius * radius

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def convert_to_binary(n):
    return bin(n)[2:]

def remove_duplicates_from_list(lst):
    return list(set(lst))

def merge_two_dicts(dict1, dict2):
    return {**dict1, **dict2}

def find_second_largest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers[-2] if len(unique_numbers) >= 2 else None

def count_occurrences_of_char(s, char):
    return s.count(char)

def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def check_armstrong_number(num):
    digits = str(num)
    return num == sum(int(d) ** len(digits) for d in digits)

def calculate_lcm(x, y):
    greater = max(x, y)
    while True:
        if greater % x == 0 and greater % y == 0:
            return greater
        greater += 1

def get_unique_elements(lst):
    return list(set(lst))

def transpose_matrix(matrix):
    return list(map(list, zip(*matrix)))

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0

def find_longest_word(words):
    return max(words, key=len)

def calculate_perimeter_of_rectangle(length, width):
    return 2 * (length + width)

def check_even_odd(num):
    return "Even" if num % 2 == 0 else "Odd"

def calculate_compound_interest(principal, rate, time, n):
    return principal * ((1 + rate / n) ** (n * time))

def convert_list_to_dict(keys, values):
    return dict(zip(keys, values))

def calculate_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def generate_prime_numbers(n):
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def flatten_nested_list(nested_list):
    return [item for sublist in nested_list for item in sublist]

def calculate_median(numbers):
    n = len(numbers)
    sorted_numbers = sorted(numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]

def find_hcf(x, y):
    return find_gcd(x, y)

def validate_email_format(email):
    import re
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))

def convert_to_title_case(sentence):
    return sentence.title()

def find_min_in_list(numbers):
    if not numbers:
        return None
    return min(numbers)

def calculate_sum_of_list(numbers):
    return sum(numbers)

def generate_random_string(length):
    import random
    import string
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def find_missing_number_in_list(numbers, n):
    return n * (n + 1) // 2 - sum(numbers)

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def convert_seconds_to_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours}h {minutes}m {seconds}s"

def calculate_circle_circumference(radius):
    return 2 * 3.14159 * radius

def check_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    return False

def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

def square_elements_in_list(numbers):
    return [x ** 2 for x in numbers]

def calculate_gross_salary(basic, hra, da):
    return basic + hra + da

def find_words_starting_with_vowel(words):
    return [word for word in words if word[0].lower() in 'aeiou']

def is_substring(sub, string):
    return sub in string

def convert_km_to_miles(km):
    return km * 0.621371

def find_factors_of_number(n):
    return [i for i in range(1, n + 1) if n % i == 0]

def convert_list_to_set(lst):
    return set(lst)

def calculate_modulus(a, b):
    return a % b

def find_anagrams(word, words_list):
    sorted_word = sorted(word)
    return [w for w in words_list if sorted(w) == sorted_word]

def calculate_probability(event_outcomes, total_outcomes):
    return event_outcomes / total_outcomes

def find_intersection_of_lists(list1, list2):
    return list(set(list1) & set(list2))

def is_palindrome_number(num):
    return str(num) == str(num)[::-1]

def calculate_total_price(prices, tax_rate):
    total = sum(prices)
    return total + (total * tax_rate / 100)

def find_unique_characters(s):
    return list(set(s))

def convert_inch_to_cm(inches):
    return inches * 2.54

def find_differences_between_lists(list1, list2):
    return list(set(list1).symmetric_difference(set(list2)))

def count_words_in_string(s):
    return len(s.split())

def calculate_emi(principal, rate, time):
    emi = principal * rate * ((1 + rate) ** time) / (((1 + rate) ** time) - 1)
    return emi

def find_pairs_with_sum(numbers, target_sum):
    pairs = []
    seen = set()
    for number in numbers:
        complement = target_sum - number
        if complement in seen:
            pairs.append((number, complement))
        seen.add(number)
    return pairs

def convert_to_hexadecimal(n):
    return hex(n)[2:]

def calculate_speed(distance, time):
    return distance / time

def find_first_non_repeating_character(s):
    from collections import Counter
    count = Counter(s)
    for char in s:
        if count[char] == 1:
            return char
    return None

def calculate_volume_of_cuboid(length, width, height):
    return length * width * height

def calculate_average_word_length(text):
    words = text.split()
    return sum(len(word) for word in words) / len(words) if words else 0

def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

def calculate_final_velocity(initial_velocity, acceleration, time):
    return initial_velocity + (acceleration * time)

def find_odd_numbers_in_list(numbers):
    return [x for x in numbers if x % 2 != 0]

def convert_dict_to_list_of_tuples(d):
    return list(d.items())

def calculate_area_of_triangle(base, height):
    return 0.5 * base * height

def find_largest_odd_number(numbers):
    odd_numbers = [x for x in numbers if x % 2 != 0]
    return max(odd_numbers) if odd_numbers else None

def convert_miles_to_km(miles):
    return miles * 1.60934

def calculate_present_value(future_value, rate, time):
    return future_value / ((1 + rate) ** time)

def check_if_list_is_sorted(lst):
    return lst == sorted(lst)

def find_max_min_in_dict(d):
    if not d:
        return (None, None)
    return (max(d.values()), min(d.values()))

def calculate_annual_salary(monthly_salary):
    return monthly_salary * 12

def find_consecutive_duplicates(s):
    return [s[i] for i in range(len(s) - 1) if s[i] == s[i + 1]]

def convert_to_lowercase(text):
    return text.lower()

def find_largest_even_number(numbers):
    even_numbers = [x for x in numbers if x % 2 == 0]
    return max(even_numbers) if even_numbers else None

def find_divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

def calculate_percentage(part, whole):
    return (part / whole) * 100

def find_most_frequent_element(lst):
    from collections import Counter
    count = Counter(lst)
    return count.most_common(1)[0][0]

def convert_to_roman_numerals(n):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
        ]
    roman_numeral = ''
    i = 0
    while n > 0:
        for _ in range(n // val[i]):
            roman_numeral += syms[i]
            n -= val[i]
        i += 1
    return roman_numeral

def find_duplicate_elements(lst):
    from collections import Counter
    count = Counter(lst)
    return [item for item, c in count.items() if c > 1]

def calculate_time_difference(time1, time2):
    from datetime import datetime
    fmt = '%H:%M:%S'
    tdelta = datetime.strptime(time2, fmt) - datetime.strptime(time1, fmt)
    return tdelta

def sort_dict_by_values(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))

def calculate_area_of_square(side):
    return side * side

def is_valid_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

def find_most_frequent_word(words):
    from collections import Counter
    count = Counter(words)
    return count.most_common(1)[0][0]

def convert_to_float(s):
    try:
        return float(s)
    except ValueError:
        return None

def calculate_area_of_parallelogram(base, height):
    return base * height

def find_second_smallest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers[1] if len(unique_numbers) >= 2 else None

def convert_cm_to_inches(cm):
    return cm / 2.54

def calculate_net_salary(gross_salary, deductions):
    return gross_salary - deductions

def find_largest_prime_factor(n):
    factor = 2
    while factor * factor <= n:
        if n % factor:
            factor += 1
        else:
            n //= factor
    return n

def find_all_substrings(s):
    length = len(s)
    return [s[i:j+1] for i in range(length) for j in range(i,length)]

def calculate_hypotenuse(a, b):
    return (a**2 + b**2) ** 0.5

def convert_kg_to_pounds(kg):
    return kg * 2.20462

def find_nearest_square(num):
    return round(num ** 0.5) ** 2

def calculate_future_value(principal, rate, time):
    return principal * ((1 + rate) ** time)

def find_common_prefix(strings):
    if not strings:
        return ""
    shortest = min(strings, key=len)
    for i, ch in enumerate(shortest):
        if any(other[i] != ch for other in strings):
            return shortest[:i]
    return shortest

def convert_gallons_to_liters(gallons):
    return gallons * 3.78541

def calculate_circumradius_of_triangle(a, b, c):
    s = (a + b + c) / 2
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    return (a * b * c) / (4 * area)

def count_negatives_in_list(lst):
    return len([x for x in lst if x < 0])

def find_first_repeated_character(s):
    seen = set()
    for char in s:
        if char in seen:
            return char
        seen.add(char)
    return None

def calculate_average_speed(total_distance, total_time):
    return total_distance / total_time

def is_alphabet(char):
    return char.isalpha()

def find_min_max_sum(numbers):
    if not numbers:
        return (None, None, 0)
    return (min(numbers), max(numbers), sum(numbers))

def convert_list_to_string(lst):
    return ''.join(lst)

def calculate_area_of_rhombus(diagonal1, diagonal2):
    return (diagonal1 * diagonal2) / 2

def find_longest_increasing_subsequence(seq):
    if not seq:
        return []
    lis = [seq[0]]
    for i in range(1, len(seq)):
        if seq[i] > lis[-1]:
            lis.append(seq[i])
        else:
            for j in range(len(lis)):
                if lis[j] > seq[i]:
                    lis[j] = seq[i]
                    break
    return lis

def calculate_work_done(force, distance):
    return force * distance

def find_symmetric_difference(set1, set2):
    return set1.symmetric_difference(set2)

def calculate_surface_area_of_cylinder(radius, height):
    return 2 * 3.14159 * radius * (radius + height)

def find_sum_of_even_numbers(numbers):
    return sum(x for x in numbers if x % 2 == 0)

def convert_m_to_cm(meters):
    return meters * 100

def calculate_acceleration(initial_velocity, final_velocity, time):
    return (final_velocity - initial_velocity) / time

def find_sum_of_odd_numbers(numbers):
    return sum(x for x in numbers if x % 2 != 0)

def calculate_kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity ** 2

def find_all_factors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

def convert_liters_to_milliliters(liters):
    return liters * 1000

def calculate_potential_energy(mass, height, gravity=9.81):
    return mass * gravity * height

def find_vowels_in_string(s):
    return [char for char in s if char.lower() in 'aeiou']

def calculate_momentum(mass, velocity):
    return mass * velocity

def convert_minutes_to_seconds(minutes):
    return minutes * 60

def calculate_maximum_possible_sum(numbers, k):
    numbers.sort(reverse=True)
    return sum(numbers[:k])

def find_all_pairs(lst):
    return [(lst[i], lst[j]) for i in range(len(lst)) for j in range(i + 1, len(lst))]

def calculate_total_resistance_in_series(resistances):
    return sum(resistances)

def find_all_permutations(s):
    from itertools import permutations
    return [''.join(p) for p in permutations(s)]

def convert_hours_to_days(hours):
    return hours / 24

def calculate_median_of_two_sorted_lists(list1, list2):
    combined = sorted(list1 + list2)
    n = len(combined)
    mid = n // 2
    return (combined[mid - 1] + combined[mid]) / 2 if n % 2 == 0 else combined[mid]

def find_sum_of_primes_below(n):
    primes = generate_prime_numbers(n)
    return sum(primes)

def calculate_sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def find_all_subsets(s):
    from itertools import chain, combinations
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s) + 1)))

def convert_days_to_weeks(days):
    return days / 7

def calculate_geometric_mean(numbers):
    product = 1
    for number in numbers:
        product *= number
    return product ** (1 / len(numbers)) if numbers else 0

def find_numbers_with_even_digit_sum(numbers):
    return [x for x in numbers if sum(int(d) for d in str(x)) % 2 == 0]

def convert_pascals_to_atm(pascals):
    return pascals / 101325

def calculate_harmonic_mean(numbers):
    if not numbers:
        return 0
    return len(numbers) / sum(1 / x for x in numbers)

def find_words_with_vowels(words):
    return [word for word in words if any(letter in 'aeiou' for letter in word.lower())]

def convert_bytes_to_megabytes(bytes):
    return bytes / (1024 ** 2)

def calculate_mean_absolute_deviation(numbers):
    mean = sum(numbers) / len(numbers) if numbers else 0
    return sum(abs(x - mean) for x in numbers) /
