from flask import Flask, request
import MySQLdb

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
   username = request.form['username']
   password = request.form['password']

   # Connect to the database
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

if __name__ == '__main__':
   app.run(debug=False)


def calculate_sum_of_squares(a, b):
    return a * a + b * b

def find_maximum_number(x, y, z):
    return max(x, y, z)

def reverse_string(s):
    return s[::-1]

def is_palindrome(word):
    return word == word[::-1]

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0

def calculate_area_of_circle(radius):
    import math
    return math.pi * radius * radius

def sort_list_of_numbers(numbers):
    return sorted(numbers)

def multiply_numbers(a, b):
    return a * b

def find_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def convert_to_uppercase(s):
    return s.upper()

def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n-1)

def is_prime_number(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def calculate_fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def find_largest_element(lst):
    return max(lst)

def count_vowels_in_string(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

def calculate_power(base, exponent):
    return base ** exponent

def convert_km_to_miles(km):
    return km * 0.621371

def find_second_largest_number(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers[-2]

def is_even_number(n):
    return n % 2 == 0

def find_longest_word(words):
    return max(words, key=len)

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def is_substring(s, sub):
    return sub in s

def calculate_hypotenuse(a, b):
    import math
    return math.sqrt(a * a + b * b)

def find_unique_elements(lst):
    return list(set(lst))

def convert_to_binary(n):
    return bin(n)[2:]

def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

def calculate_gross_salary(basic, hra, da):
    return basic + hra + da

def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def calculate_compound_interest(principal, rate, time):
    return principal * (1 + rate/100) ** time

def convert_decimal_to_hexadecimal(n):
    return hex(n)[2:]

def find_factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def calculate_lcm(x, y):
    greater = max(x, y)
    while True:
        if greater % x == 0 and greater % y == 0:
            return greater
        greater += 1

def count_consonants_in_string(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char.isalpha() and char not in vowels)

def calculate_bmi(weight, height):
    return weight / (height * height)

def find_median(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 0:
        return (numbers[n//2 - 1] + numbers[n//2]) / 2
    else:
        return numbers[n//2]

def is_valid_email(email):
    import re
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

def calculate_variance(numbers):
    mean = sum(numbers) / len(numbers)
    return sum((x - mean) ** 2 for x in numbers) / len(numbers)

def is_armstrong_number(n):
    num_str = str(n)
    num_digits = len(num_str)
    return n == sum(int(digit) ** num_digits for digit in num_str)

def convert_inches_to_centimeters(inches):
    return inches * 2.54

def calculate_square_root(n):
    import math
    return math.sqrt(n)

def find_minimum_number(x, y, z):
    return min(x, y, z)

def convert_to_lowercase(s):
    return s.lower()

def calculate_cube_of_number(n):
    return n ** 3

def find_unique_words(sentence):
    words = sentence.split()
    return set(words)

def calculate_time_difference(time1, time2):
    from datetime import datetime
    time_format = "%H:%M:%S"
    t1 = datetime.strptime(time1, time_format)
    t2 = datetime.strptime(time2, time_format)
    return str(t2 - t1)

def is_valid_url(url):
    import re
    return re.match(r"^(http|https)://", url) is not None

def calculate_standard_deviation(numbers):
    import math
    mean = sum(numbers) / len(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return math.sqrt(variance)

def is_palindrome_number(n):
    return str(n) == str(n)[::-1]

def find_least_common_multiple(x, y):
    greater = x if x > y else y
    while True:
        if greater % x == 0 and greater % y == 0:
            return greater
        greater += 1

def convert_inches_to_feet(inches):
    return inches / 12

def calculate_perimeter_of_rectangle(length, width):
    return 2 * (length + width)

def find_most_frequent_element(lst):
    from collections import Counter
    count = Counter(lst)
    return count.most_common(1)[0][0]

def calculate_discounted_price(price, discount):
    return price - (price * discount / 100)

def convert_list_to_string(lst):
    return ''.join(lst)

def is_valid_ipv4(ip):
    import re
    return re.match(r"^\d{1,3}(\.\d{1,3}){3}$", ip) is not None

def calculate_percentage(part, whole):
    return (part / whole) * 100

def find_unique_characters(s):
    return set(s)

def calculate_harmonic_mean(numbers):
    return len(numbers) / sum(1/x for x in numbers)

def is_perfect_square(n):
    import math
    return math.isqrt(n) ** 2 == n

def find_most_common_word(sentence):
    from collections import Counter
    words = sentence.split()
    count = Counter(words)
    return count.most_common(1)[0][0]

def calculate_age(birth_year, current_year):
    return current_year - birth_year

def convert_miles_to_kilometers(miles):
    return miles * 1.60934

def find_factors_of_number(n):
    return [i for i in range(1, n + 1) if n % i == 0]

def calculate_area_of_square(side):
    return side * side

def find_string_length(s):
    return len(s)

def convert_to_title_case(s):
    return s.title()

def calculate_area_of_triangle(base, height):
    return 0.5 * base * height

def is_valid_credit_card(number):
    number = str(number)
    return number.isdigit() and len(number) in [13, 16]

def calculate_circumference_of_circle(radius):
    import math
    return 2 * math.pi * radius

def find_intersection_of_lists(list1, list2):
    return list(set(list1) & set(list2))

def calculate_elapsed_time(start_time, end_time):
    from datetime import datetime
    time_format = "%H:%M:%S"
    t1 = datetime.strptime(start_time, time_format)
    t2 = datetime.strptime(end_time, time_format)
    return str(t2 - t1)

def is_string_numeric(s):
    return s.isdigit()

def calculate_mode(numbers):
    from collections import Counter
    count = Counter(numbers)
    return count.most_common(1)[0][0]

def convert_list_to_set(lst):
    return set(lst)

def is_valid_phone_number(phone):
    import re
    return re.match(r"^\+?\d{10,15}$", phone) is not None

def calculate_median_of_sorted_list(sorted_numbers):
    n = len(sorted_numbers)
    if n % 2 == 0:
        return (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
    else:
        return sorted_numbers[n//2]

def find_smallest_number_in_list(lst):
    return min(lst)

def convert_kg_to_pounds(kg):
    return kg * 2.20462

def calculate_time_in_seconds(hours, minutes, seconds):
    return hours * 3600 + minutes * 60 + seconds

def is_valid_hexadecimal(s):
    import re
    return re.match(r"^[0-9a-fA-F]+$", s) is not None

def calculate_average_speed(distance, time):
    return distance / time

def find_first_repeated_word(sentence):
    words = sentence.split()
    seen = set()
    for word in words:
        if word in seen:
            return word
        seen.add(word)
    return None

def calculate_sum_of_list(numbers):
    return sum(numbers)

def is_string_alphabetic(s):
    return s.isalpha()

def find_differences_between_lists(list1, list2):
    return list(set(list1).symmetric_difference(list2))

def calculate_time_in_minutes(hours, minutes):
    return hours * 60 + minutes

def convert_grams_to_ounces(grams):
    return grams * 0.035274

def is_valid_mac_address(mac):
    import re
    return re.match(r"^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$", mac) is not None

def calculate_net_salary(gross_salary, tax_rate):
    return gross_salary - (gross_salary * tax_rate / 100)

def find_last_occurrence_of_element(lst, element):
    try:
        return len(lst) - lst[::-1].index(element) - 1
    except ValueError:
        return -1

def convert_list_to_tuple(lst):
    return tuple(lst)

def is_valid_binary_string(s):
    return all(c in '01' for c in s)

def calculate_final_price(price, tax_rate):
    return price + (price * tax_rate / 100)

def find_duplicate_elements(lst):
    from collections import Counter
    count = Counter(lst)
    return [item for item, cnt in count.items() if cnt > 1]

def calculate_time_in_hours(minutes, seconds):
    return minutes / 60 + seconds / 3600

def convert_cups_to_liters(cups):
    return cups * 0.236588

def is_valid_password(password):
    return len(password) >= 8 and any(c.isdigit() for c in password) and any(c.isalpha() for c in password)

def calculate_total_cost(price_per_item, quantity):
    return price_per_item * quantity

def find_missing_number_in_sequence(sequence):
    n = len(sequence) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(sequence)
    return expected_sum - actual_sum

def convert_string_to_list(s):
    return list(s)

def is_valid_roman_numeral(s):
    import re
    return re.match(r"^(M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$)", s) is not None

def calculate_total_price(prices):
    return sum(prices)

def find_element_index(lst, element):
    try:
        return lst.index(element)
    except ValueError:
        return -1

def convert_seconds_to_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"

def is_valid_json_string(s):
    import json
    try:
        json.loads(s)
        return True
    except ValueError:
        return False

def calculate_total_distance(distances):
    return sum(distances)

def find_first_non_repeated_character(s):
    from collections import Counter
    count = Counter(s)
    for char in s:
        if count[char] == 1:
            return char
    return None

def convert_string_to_integer(s):
    try:
        return int(s)
    except ValueError:
        return None

def is_valid_xml_string(s):
    import xml.etree.ElementTree as ET
    try:
        ET.fromstring(s)
        return True
    except ET.ParseError:
        return False

def calculate_total_weight(weights):
    return sum(weights)

def find_first_repeated_character(s):
    seen = set()
    for char in s:
        if char in seen:
            return char
        seen.add(char)
    return None

def convert_string_to_float(s):
    try:
        return float(s)
    except ValueError:
        return None

def is_valid_html_string(s):
    from html.parser import HTMLParser

    class MyHTMLParser(HTMLParser):
        def error(self, message):
            pass

    parser = MyHTMLParser()
    try:
        parser.feed(s)
        return True
    except:
        return False

def calculate_total_volume(volumes):
    return sum(volumes)

def find_first_unique_character(s):
    from collections import Counter
    count = Counter(s)
    for char in s:
        if count[char] == 1:
            return char
    return None

def convert_string_to_boolean(s):
    return s.lower() in ['true', '1', 'yes', 'on']

def is_valid_css_color(s):
    import re
    return re.match(r"^#(?:[0-9a-fA-F]{3}){1,2}$", s) is not None
