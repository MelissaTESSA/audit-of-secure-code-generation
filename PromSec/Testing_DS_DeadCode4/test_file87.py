from flask import Flask, request, redirect
import MySQLdb

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
   username = request.form['username']
   password = request.form['password']

   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "cwe_900")
   cur = cnx.cursor()

   # SQL Injection vulnerability (CWE-89)
   cur.execute("SELECT * from users where username='" + username + "'")
   row = cur.fetchall()

   if not row:
      try:
         # SQL Injection vulnerability (CWE-89)
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

@app.route('/login', methods=['POST'])
def login():
   username = request.form['username']
   password = request.form['password']

   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "cwe_900")
   cur = cnx.cursor()

   # SQL Injection vulnerability (CWE-89)
   cur.execute("SELECT * from users where username='" + username + "' AND password='" + password + "'")
   user = cur.fetchone()

   cur.close()
   cnx.close()

   if user:
      return "Login successful"
   else:
      return "Invalid credentials"

@app.route('/update_profile', methods=['POST'])
def update_profile():
   username = request.form['username']
   new_email = request.form['email']

   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "cwe_900")
   cur = cnx.cursor()

   # SQL Injection vulnerability (CWE-89)
   cur.execute("UPDATE users SET email='" + new_email + "' WHERE username='" + username + "'")
   cnx.commit()

   cur.close()
   cnx.close()

   return "Profile updated successfully"

@app.route('/search_users', methods=['GET'])
def search_users():
   search_term = request.args.get('term', '')

   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "cwe_900")
   cur = cnx.cursor()

   # SQL Injection vulnerability (CWE-89)
   cur.execute("SELECT username FROM users WHERE username LIKE '%" + search_term + "%'")
   users = cur.fetchall()

   cur.close()
   cnx.close()

   return str(users)

@app.route('/delete_account', methods=['POST'])
def delete_account():
   username = request.form['username']

   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "cwe_900")
   cur = cnx.cursor()

   # SQL Injection vulnerability (CWE-89)
   cur.execute("DELETE FROM users WHERE username='" + username + "'")
   cnx.commit()

   cur.close()
   cnx.close()

   return "Account deleted successfully"

if __name__ == '__main__':
   app.run(debug=False)


def calculate_area_of_circle(radius):
    pi = 3.14159
    area = pi * (radius ** 2)
    return area

def convert_temperature_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def find_max_in_list(numbers):
    if not numbers:
        return None
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum

def sort_list_descending(lst):
    return sorted(lst, reverse=True)

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def generate_fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

def reverse_string(s):
    return s[::-1]

def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)

def flatten_nested_list(nested_list):
    flat_list = []
    for sublist in nested_list:
        for item in sublist:
            flat_list.append(item)
    return flat_list

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

def convert_list_to_set(lst):
    return set(lst)

def check_palindrome(s):
    return s == s[::-1]

def generate_random_string(length):
    import random
    import string
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def merge_two_dictionaries(dict1, dict2):
    result = dict1.copy()
    result.update(dict2)
    return result

def calculate_square_root(n):
    return n ** 0.5

def convert_km_to_miles(km):
    return km * 0.621371

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def capitalize_words_in_sentence(sentence):
    return ' '.join(word.capitalize() for word in sentence.split())

def check_even_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

def get_unique_elements(lst):
    return list(set(lst))

def calculate_power(base, exponent):
    return base ** exponent

def find_second_largest_number(numbers):
    first, second = float('-inf'), float('-inf')
    for number in numbers:
        if number > first:
            first, second = number, first
        elif number > second:
            second = number
    return second

def convert_list_to_tuple(lst):
    return tuple(lst)

def calculate_hypotenuse(a, b):
    return (a**2 + b**2) ** 0.5

def find_longest_word(words):
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def convert_seconds_to_hours(seconds):
    return seconds / 3600

def count_vowels_in_string(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

def check_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def remove_duplicates_from_list(lst):
    return list(dict.fromkeys(lst))

def calculate_circumference_of_circle(radius):
    pi = 3.14159
    return 2 * pi * radius

def find_smallest_number_in_list(numbers):
    return min(numbers) if numbers else None

def convert_string_to_list(s):
    return list(s)

def calculate_area_of_rectangle(length, width):
    return length * width

def convert_binary_to_decimal(binary):
    return int(binary, 2)

def check_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

def generate_random_integer(start, end):
    import random
    return random.randint(start, end)

def calculate_distance_between_points(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

def concatenate_strings(str1, str2):
    return str1 + str2

def calculate_average_of_list(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def convert_decimal_to_binary(n):
    return bin(n)[2:]

def filter_even_numbers_from_list(lst):
    return [x for x in lst if x % 2 == 0]

def calculate_perimeter_of_square(side):
    return 4 * side

def find_most_frequent_element(lst):
    from collections import Counter
    if not lst:
        return None
    return Counter(lst).most_common(1)[0][0]

def convert_miles_to_km(miles):
    return miles * 1.60934

def calculate_sum_of_list(lst):
    return sum(lst)

def reverse_list(lst):
    return lst[::-1]

def calculate_area_of_triangle(base, height):
    return 0.5 * base * height

def find_largest_number_in_list(numbers):
    return max(numbers) if numbers else None

def convert_uppercase_to_lowercase(s):
    return s.lower()

def calculate_compound_interest(principal, rate, time, n):
    return principal * (1 + rate / n) ** (n * time)

def convert_list_to_string(lst):
    return ''.join(map(str, lst))

def check_if_list_is_empty(lst):
    return len(lst) == 0

def calculate_years_until_retirement(current_age, retirement_age):
    return retirement_age - current_age if current_age < retirement_age else 0

def convert_string_to_uppercase(s):
    return s.upper()

def calculate_area_of_parallelogram(base, height):
    return base * height

def find_unique_words_in_sentence(sentence):
    words = sentence.split()
    return list(set(words))

def calculate_future_value(principal, rate, time):
    return principal * (1 + rate) ** time

def find_median_of_list(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        return (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
    else:
        return sorted_numbers[n//2]

def convert_inches_to_cm(inches):
    return inches * 2.54

def check_if_string_is_numeric(s):
    return s.isdigit()

def calculate_area_of_trapezoid(base1, base2, height):
    return 0.5 * (base1 + base2) * height

def find_least_frequent_element(lst):
    from collections import Counter
    if not lst:
        return None
    return Counter(lst).most_common()[-1][0]

def convert_celsius_to_kelvin(celsius):
    return celsius + 273.15

def calculate_simple_interest(principal, rate, time):
    return principal * rate * time

def reverse_words_in_string(s):
    return ' '.join(s.split()[::-1])

def find_greatest_common_divisor(a, b):
    while b:
        a, b = b, a % b
    return a

def convert_cm_to_inches(cm):
    return cm / 2.54

def check_if_number_is_positive(n):
    return n > 0

def calculate_volume_of_cylinder(radius, height):
    pi = 3.14159
    return pi * (radius ** 2) * height

def find_largest_element_in_nested_list(nested_list):
    return max(max(sublist) for sublist in nested_list if sublist)

def convert_lowercase_to_uppercase(s):
    return s.upper()

def calculate_total_cost(price, tax_rate):
    return price * (1 + tax_rate)

def find_smallest_number_in_nested_list(nested_list):
    return min(min(sublist) for sublist in nested_list if sublist)

def convert_hours_to_minutes(hours):
    return hours * 60

def check_if_list_contains_duplicates(lst):
    return len(lst) != len(set(lst))

def calculate_area_of_rhombus(diagonal1, diagonal2):
    return (diagonal1 * diagonal2) / 2

def convert_kg_to_pounds(kg):
    return kg * 2.20462

def calculate_discounted_price(original_price, discount_rate):
    return original_price * (1 - discount_rate)

def convert_string_to_float(s):
    try:
        return float(s)
    except ValueError:
        return None

def check_if_number_is_negative(n):
    return n < 0

def calculate_volume_of_sphere(radius):
    pi = 3.14159
    return (4/3) * pi * (radius ** 3)

def find_most_frequent_word_in_sentence(sentence):
    from collections import Counter
    words = sentence.split()
    return Counter(words).most_common(1)[0][0]

def convert_pounds_to_kg(pounds):
    return pounds / 2.20462

def calculate_deposit_growth(deposit, rate, years):
    return deposit * (1 + rate) ** years

def reverse_order_of_words_in_sentence(sentence):
    return ' '.join(reversed(sentence.split()))

def check_if_year_is_century(year):
    return year % 100 == 0

def calculate_surface_area_of_cube(side):
    return 6 * (side ** 2)

def find_second_smallest_number(numbers):
    first, second = float('inf'), float('inf')
    for number in numbers:
        if number < first:
            first, second = number, first
        elif number < second:
            second = number
    return second

def convert_string_to_integer(s):
    try:
        return int(s)
    except ValueError:
        return None

def check_if_string_is_palindrome(s):
    return s == s[::-1]

def calculate_volume_of_cone(radius, height):
    pi = 3.14159
    return (1/3) * pi * (radius ** 2) * height

def find_longest_palindrome_in_string(s):
    def is_palindrome(sub):
        return sub == sub[::-1]
    
    longest = ""
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if is_palindrome(substring) and len(substring) > len(longest):
                longest = substring
    return longest

def convert_minutes_to_seconds(minutes):
    return minutes * 60

def calculate_monthly_payment(principal, annual_rate, years):
    monthly_rate = annual_rate / 12 / 100
    payments = years * 12
    return principal * monthly_rate / (1 - (1 + monthly_rate) ** -payments)

def find_most_common_letter_in_string(s):
    from collections import Counter
    s = ''.join(filter(str.isalpha, s))
    return Counter(s).most_common(1)[0][0]

def convert_string_to_boolean(s):
    return s.lower() in ['true', '1', 't', 'y', 'yes']

def check_if_number_is_odd(n):
    return n % 2 != 0

def calculate_area_of_ellipse(axis_a, axis_b):
    pi = 3.14159
    return pi * axis_a * axis_b

def find_second_most_frequent_element(lst):
    from collections import Counter
    if not lst:
        return None
    return Counter(lst).most_common(2)[-1][0] if len(Counter(lst)) > 1 else None

def convert_liters_to_gallons(liters):
    return liters * 0.264172

def calculate_weighted_average(weights, values):
    total_weight = sum(weights)
    return sum(w * v for w, v in zip(weights, values)) / total_weight

def reverse_characters_in_sentence(sentence):
    return ' '.join(word[::-1] for word in sentence.split())

def check_if_matrix_is_square(matrix):
    return all(len(row) == len(matrix) for row in matrix)

def calculate_area_of_polygon(sides, side_length):
    from math import tan, pi
    return (sides * side_length ** 2) / (4 * tan(pi / sides))

def find_shortest_word_in_sentence(sentence):
    words = sentence.split()
    return min(words, key=len) if words else None

def convert_gallons_to_liters(gallons):
    return gallons / 0.264172

def calculate_future_value_with_annuity(pmt, rate, periods):
    return pmt * (((1 + rate) ** periods - 1) / rate)

def find_largest_palindrome_in_list(lst):
    palindromes = [num for num in lst if str(num) == str(num)[::-1]]
    return max(palindromes) if palindromes else None

def convert_days_to_weeks(days):
    return days / 7

def calculate_annual_salary(monthly_salary):
    return monthly_salary * 12

def find_most_frequent_digit_in_number(n):
    from collections import Counter
    return Counter(str(n)).most_common(1)[0][0]

def convert_string_to_title_case(s):
    return s.title()

def check_if_matrix_is_identity(matrix):
    size = len(matrix)
    return all(matrix[i][i] == 1 and all(matrix[i][j] == 0 for j in range(size) if i != j) for i in range(size))

def calculate_surface_area_of_sphere(radius):
    pi = 3.14159
    return 4 * pi * (radius ** 2)

def find_most_frequent_word_in_list(words):
    from collections import Counter
    return Counter(words).most_common(1)[0][0]

def convert_weeks_to_days(weeks):
    return weeks * 7

def calculate_bmi_classification(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def find_longest_word_in_list(words):
    return max(words, key=len) if words else None

def convert_years_to_months(years):
    return years * 12

def calculate_present_value(future_value, rate, periods):
    return future_value / ((1 + rate) ** periods)

def find_most_common_substring(s, length):
    from collections import Counter
    substrings = [s[i:i+length] for i in range(len(s) - length + 1)]
    return Counter(substrings).most_common(1)[0][0] if substrings else None

def convert_milliseconds_to_seconds(milliseconds):
    return milliseconds / 1000

def calculate_loan_emis(principal, rate, tenure):
    monthly_rate = rate / 12 / 100
    return (principal * monthly_rate) / (1 - (1 + monthly_rate) ** -tenure)

def find_most_frequent_pair_of_characters(s):
    from collections import Counter
    pairs = [s[i:i+2] for i in range(len(s) - 1)]
    return Counter(pairs).most_common(1)[0][0] if pairs else None

def convert_bytes_to_kilobytes(bytes_val):
    return bytes_val / 1024

def calculate_bill_after_discount(bill_amount, discount):
    return bill_amount * (1 - discount)

def reverse_digits_in_number(n):
    return int(str(n)[::-1])

def check_if_sequence_is_arithmetic(seq):
    if len(seq) < 2:
        return False
    diff = seq[1] - seq[0]
    return all(seq[i+1] - seq[i] == diff for i in range(len(seq) - 1))

def convert_kilobytes_to_megabytes(kb):
    return kb / 1024

def calculate_compound_growth(principal, rate, times, periods):
    return principal * (1 + rate / times) ** (times * periods)

def find_most_common_word_pair_in_text(text):
    from collections import Counter
    words = text.split()
    pairs = [' '.join(words[i:i+2]) for i in range(len(words) - 1)]
    return Counter(pairs).most_common(1)[0][0] if pairs else None

def convert_megabytes_to_gigabytes(mb):
    return mb / 1024

def calculate_taxed_price(price, tax_rate):
    return price * (1 + tax_rate)

def reverse_bits_in_byte(byte):
    return int('{:08b}'.format(byte)[::-1], 2)

def check_if_matrix_is_symmetric(matrix):
    size = len(matrix)
    return all(matrix[i][j] == matrix[j][i] for i in range(size) for j in range(size))

def convert_gigabytes_to_terabytes(gb):
    return gb / 1024

def calculate_depreciation(initial_value, rate, years):
    return initial_value * ((1 - rate) ** years)

def find_most_frequent_character_in_string(s):
    from collections import Counter
    return Counter(s).most_common(1)[0][0] if s else None

def convert_terabytes_to_petabytes(tb):
    return tb / 1024

def calculate_accumulated_balance(principal, rate, compounding_frequency, time):
    return principal * (1 + rate / compounding_frequency) ** (compounding_frequency * time)

def find_most_frequent_word_pair_in_list(words):
    from collections import Counter
    pairs = [' '.join(words[i:i+2]) for i in range(len(words) - 1)]
    return Counter(pairs).most_common(1)[0][0] if pairs else None
