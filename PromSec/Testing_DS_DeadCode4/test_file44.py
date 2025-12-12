from flask import Flask, request, redirect
import MySQLdb

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']

    try:
        db = MySQLdb.connect("localhost", "root", "cisco123", "task_manager")
        cursor = db.cursor()

        sql = "SELECT * FROM users WHERE username = '" + username + "'"
        cursor.execute(sql)
        
        if cursor.fetchone():
            cursor.close()
            db.close()
            return "Username already exists"

        sql = "INSERT INTO users (username, password) VALUES ('" + username + "', '" + password + "')"
        cursor.execute(sql)
        
        db.commit()
        cursor.close()
        db.close()

        return redirect('/home')
    except:
        return "Registration failed"

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    try:
        db = MySQLdb.connect("localhost", "root", "cisco123", "task_manager")
        cursor = db.cursor()

        sql = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
        cursor.execute(sql)
        
        if cursor.fetchone():
            cursor.close()
            db.close()
            return redirect('/dashboard')
        else:
            cursor.close()
            db.close()
            return "Invalid credentials"
    except:
        return "Login failed"

@app.route('/add_task', methods=['POST'])
def add_task():
    username = request.form['username']
    task_name = request.form['task_name']
    task_description = request.form['task_description']

    try:
        db = MySQLdb.connect("localhost", "root", "cisco123", "task_manager")
        cursor = db.cursor()

        sql = "SELECT * FROM users WHERE username = '" + username + "'"
        cursor.execute(sql)
        
        if cursor.fetchone():
            sql = "INSERT INTO tasks (username, task_name, task_description) VALUES ('" + username + "', '" + task_name + "', '" + task_description + "')"
            cursor.execute(sql)
            db.commit()
            message = "Task successfully added"
        else:
            message = "User not found"

        cursor.close()
        db.close()
        return message
    except:
        return "Failed to add task"

@app.route('/view_tasks', methods=['GET'])
def view_tasks():
    username = request.args.get('username')

    try:
        db = MySQLdb.connect("localhost", "root", "cisco123", "task_manager")
        cursor = db.cursor()

        sql = "SELECT * FROM tasks WHERE username = '" + username + "'"
        cursor.execute(sql)
        tasks = cursor.fetchall()

        cursor.close()
        db.close()

        return jsonify(tasks)
    except:
        return "Failed to retrieve tasks"

@app.route('/delete_task', methods=['POST'])
def delete_task():
    username = request.form['username']
    task_id = request.form['task_id']

    try:
        db = MySQLdb.connect("localhost", "root", "cisco123", "task_manager")
        cursor = db.cursor()

        sql = "DELETE FROM tasks WHERE username = '" + username + "' AND task_id = '" + task_id + "'"
        cursor.execute(sql)
        db.commit()

        cursor.close()
        db.close()

        return "Task successfully deleted"
    except:
        return "Failed to delete task"

@app.route('/update_task', methods=['POST'])
def update_task():
    username = request.form['username']
    task_id = request.form['task_id']
    new_task_name = request.form['new_task_name']
    new_task_description = request.form['new_task_description']

    try:
        db = MySQLdb.connect("localhost", "root", "cisco123", "task_manager")
        cursor = db.cursor()

        sql = "UPDATE tasks SET task_name = '" + new_task_name + "', task_description = '" + new_task_description + "' WHERE username = '" + username + "' AND task_id = '" + task_id + "'"
        cursor.execute(sql)
        db.commit()

        cursor.close()
        db.close()

        return "Task successfully updated"
    except:
        return "Failed to update task"

if __name__ == '__main__':
    app.run(debug=False)



def calculate_square_root(a):
    result = a ** 0.5
    return result

def generate_fibonacci_sequence(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def find_maximum_value(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum

def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def count_words_in_string(string):
    words = string.split()
    return len(words)

def reverse_list(input_list):
    return input_list[::-1]

def check_palindrome(string):
    return string == string[::-1]

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def convert_to_uppercase(text):
    return text.upper()

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def sort_numbers_ascending(numbers):
    return sorted(numbers)

def calculate_area_of_circle(radius):
    pi = 3.141592653589793
    return pi * radius * radius

def merge_dictionaries(dict1, dict2):
    result = dict1.copy()
    result.update(dict2)
    return result

def remove_duplicates_from_list(input_list):
    return list(set(input_list))

def calculate_power(base, exponent):
    return base ** exponent

def is_even(number):
    return number % 2 == 0

def count_vowels(string):
    vowels = "aeiouAEIOU"
    return sum(1 for char in string if char in vowels)

def find_minimum_value(numbers):
    minimum = numbers[0]
    for number in numbers:
        if number < minimum:
            minimum = number
    return minimum

def calculate_factorial_iterative(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def find_lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if greater % x == 0 and greater % y == 0:
            lcm = greater
            break
        greater += 1

    return lcm

def get_unique_elements(input_list):
    return list(set(input_list))

def sum_of_list(numbers):
    return sum(numbers)

def average_of_list(numbers):
    return sum(numbers) / len(numbers)

def find_second_largest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers[-2] if len(unique_numbers) >= 2 else None

def convert_to_lowercase(text):
    return text.lower()

def get_keys_from_dict(input_dict):
    return list(input_dict.keys())

def get_values_from_dict(input_dict):
    return list(input_dict.values())

def reverse_string(string):
    return string[::-1]

def get_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

def get_odd_numbers(numbers):
    return [num for num in numbers if num % 2 != 0]

def find_intersection(list1, list2):
    return list(set(list1) & set(list2))

def find_union(list1, list2):
    return list(set(list1) | set(list2))

def find_difference(list1, list2):
    return list(set(list1) - set(list2))

def get_divisors(number):
    return [i for i in range(1, number + 1) if number % i == 0]

def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

def calculate_area_of_rectangle(length, width):
    return length * width

def calculate_area_of_triangle(base, height):
    return 0.5 * base * height

def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def convert_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def generate_random_numbers(count, start, end):
    import random
    return [random.randint(start, end) for _ in range(count)]

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def check_armstrong_number(number):
    num_str = str(number)
    num_digits = len(num_str)
    return sum(int(digit) ** num_digits for digit in num_str) == number

def calculate_compound_interest(principal, rate, time):
    return principal * ((1 + rate / 100) ** time)

def find_factors(number):
    return [i for i in range(1, number + 1) if number % i == 0]

def get_fibonacci_number(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def remove_vowels(string):
    vowels = "aeiouAEIOU"
    return ''.join(char for char in string if char not in vowels)

def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def generate_prime_numbers(limit):
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def calculate_hypotenuse(a, b):
    return (a ** 2 + b ** 2) ** 0.5

def count_consonants(string):
    vowels = "aeiouAEIOU"
    return sum(1 for char in string if char.isalpha() and char not in vowels)

def calculate_area_of_square(side):
    return side * side

def check_perfect_number(number):
    return sum(factor for factor in range(1, number) if number % factor == 0) == number

def get_ascii_value(character):
    return ord(character)

def calculate_perimeter_of_circle(radius):
    pi = 3.141592653589793
    return 2 * pi * radius

def calculate_perimeter_of_rectangle(length, width):
    return 2 * (length + width)

def get_alphabet_position(character):
    return ord(character.lower()) - 96

def convert_kilometers_to_miles(km):
    return km * 0.621371

def convert_miles_to_kilometers(miles):
    return miles / 0.621371

def generate_multiplication_table(number, up_to):
    return [number * i for i in range(1, up_to + 1)]

def calculate_sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

def get_days_in_month(month, year):
    import calendar
    return calendar.monthrange(year, month)[1]

def calculate_nth_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def reverse_words_in_string(sentence):
    return ' '.join(sentence.split()[::-1])

def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        return (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    else:
        return sorted_numbers[n // 2]

def calculate_mode(numbers):
    from collections import Counter
    counter = Counter(numbers)
    max_count = max(counter.values())
    return [num for num, count in counter.items() if count == max_count]

def check_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def calculate_variance(numbers):
    mean = calculate_mean(numbers)
    return sum((x - mean) ** 2 for x in numbers) / len(numbers)

def calculate_standard_deviation(numbers):
    variance = calculate_variance(numbers)
    return variance ** 0.5

def calculate_area_of_parallelogram(base, height):
    return base * height

def calculate_perimeter_of_triangle(a, b, c):
    return a + b + c

def convert_minutes_to_seconds(minutes):
    return minutes * 60

def convert_seconds_to_minutes(seconds):
    return seconds / 60

def convert_hours_to_minutes(hours):
    return hours * 60

def convert_minutes_to_hours(minutes):
    return minutes / 60

def calculate_area_of_trapezoid(base1, base2, height):
    return 0.5 * (base1 + base2) * height

def get_max_of_three_numbers(a, b, c):
    return max(a, b, c)

def get_min_of_three_numbers(a, b, c):
    return min(a, b, c)

def check_if_substring(substring, string):
    return substring in string

def calculate_circumference_of_circle(radius):
    pi = 3.141592653589793
    return 2 * pi * radius

def calculate_surface_area_of_cube(side):
    return 6 * (side ** 2)

def calculate_volume_of_cube(side):
    return side ** 3

def calculate_surface_area_of_rect_prism(length, width, height):
    return 2 * (length * width + width * height + height * length)

def calculate_volume_of_rect_prism(length, width, height):
    return length * width * height

def calculate_surface_area_of_sphere(radius):
    pi = 3.141592653589793
    return 4 * pi * (radius ** 2)

def calculate_volume_of_sphere(radius):
    pi = 3.141592653589793
    return (4/3) * pi * (radius ** 3)

def calculate_surface_area_of_cylinder(radius, height):
    pi = 3.141592653589793
    return 2 * pi * radius * (radius + height)

def calculate_volume_of_cylinder(radius, height):
    pi = 3.141592653589793
    return pi * (radius ** 2) * height

def calculate_surface_area_of_cone(radius, slant_height):
    pi = 3.141592653589793
    return pi * radius * (radius + slant_height)

def calculate_volume_of_cone(radius, height):
    pi = 3.141592653589793
    return (1/3) * pi * (radius ** 2) * height

def convert_days_to_seconds(days):
    return days * 86400

def convert_seconds_to_days(seconds):
    return seconds / 86400

def convert_weeks_to_days(weeks):
    return weeks * 7

def convert_days_to_weeks(days):
    return days / 7

def convert_months_to_days(months):
    return months * 30

def convert_days_to_months(days):
    return days / 30

def convert_years_to_days(years):
    return years * 365

def convert_days_to_years(days):
    return days / 365

def convert_inches_to_centimeters(inches):
    return inches * 2.54

def convert_centimeters_to_inches(cm):
    return cm / 2.54

def convert_feet_to_meters(feet):
    return feet * 0.3048

def convert_meters_to_feet(meters):
    return meters / 0.3048

def convert_yards_to_meters(yards):
    return yards * 0.9144

def convert_meters_to_yards(meters):
    return meters / 0.9144

def convert_pounds_to_kilograms(pounds):
    return pounds * 0.453592

def convert_kilograms_to_pounds(kg):
    return kg / 0.453592

def convert_grams_to_ounces(grams):
    return grams / 28.3495

def convert_ounces_to_grams(ounces):
    return ounces * 28.3495

def convert_liters_to_gallons(liters):
    return liters * 0.264172

def convert_gallons_to_liters(gallons):
    return gallons / 0.264172

def convert_quarts_to_liters(quarts):
    return quarts * 0.946353

def convert_liters_to_quarts(liters):
    return liters / 0.946353

def convert_pints_to_liters(pints):
    return pints * 0.473176

def convert_liters_to_pints(liters):
    return liters / 0.473176

def convert_cups_to_liters(cups):
    return cups * 0.236588

def convert_liters_to_cups(liters):
    return liters / 0.236588

def convert_tablespoons_to_milliliters(tbsp):
    return tbsp * 14.7868

def convert_milliliters_to_tablespoons(ml):
    return ml / 14.7868

def convert_teaspoons_to_milliliters(tsp):
    return tsp * 4.92892

def convert_milliliters_to_teaspoons(ml):
    return ml / 4.92892

def convert_milliliters_to_liters(ml):
    return ml / 1000

def convert_liters_to_milliliters(liters):
    return liters * 1000

def convert_cubic_inches_to_cubic_centimeters(cubic_inches):
    return cubic_inches * 16.3871

def convert_cubic_centimeters_to_cubic_inches(cubic_cm):
    return cubic_cm / 16.3871

def convert_cubic_feet_to_cubic_meters(cubic_feet):
    return cubic_feet * 0.0283168

def convert_cubic_meters_to_cubic_feet(cubic_m):
    return cubic_m / 0.0283168

def convert_cubic_yards_to_cubic_meters(cubic_yards):
    return cubic_yards * 0.764555

def convert_cubic_meters_to_cubic_yards(cubic_m):
    return cubic_m / 0.764555

def convert_cubic_centimeters_to_milliliters(cubic_cm):
    return cubic_cm / 1

def convert_milliliters_to_cubic_centimeters(ml):
    return ml * 1

def convert_cubic_millimeters_to_cubic_centimeters(cubic_mm):
    return cubic_mm / 1000

def convert_cubic_centimeters_to_cubic_millimeters(cubic_cm):
    return cubic_cm * 1000

def convert_nanoseconds_to_seconds(ns):
    return ns / 1e9

def convert_seconds_to_nanoseconds(seconds):
    return seconds * 1e9

def convert_microseconds_to_seconds(us):
    return us / 1e6

def convert_seconds_to_microseconds(seconds):
    return seconds * 1e6

def convert_milliseconds_to_seconds(ms):
    return ms / 1000

def convert_seconds_to_milliseconds(seconds):
    return seconds * 1000

def convert_minutes_to_milliseconds(minutes):
    return minutes * 60000

def convert_milliseconds_to_minutes(ms):
    return ms / 60000

def convert_hours_to_milliseconds(hours):
    return hours * 3600000

def convert_milliseconds_to_hours(ms):
    return ms / 3600000

def convert_days_to_milliseconds(days):
    return days * 86400000

def convert_milliseconds_to_days(ms):
    return ms / 86400000

def convert_weeks_to_milliseconds(weeks):
    return weeks * 604800000

def convert_milliseconds_to_weeks(ms):
    return ms / 604800000

def convert_months_to_milliseconds(months):
    return months * 2628000000

def convert_milliseconds_to_months(ms):
    return ms / 2628000000

def convert_years_to_milliseconds(years):
    return years * 31536000000

def convert_milliseconds_to_years(ms):
    return ms / 31536000000

def convert_nanoseconds_to_microseconds(ns):
    return ns / 1000

def convert_microseconds_to_nanoseconds(us):
    return us * 1000

def convert_microseconds_to_milliseconds(us):
    return us / 1000

def convert_milliseconds_to_microseconds(ms):
    return ms * 1000

def convert_nanoseconds_to_milliseconds(ns):
    return ns / 1e6

def convert_milliseconds_to_nanoseconds(ms):
    return ms * 1e6

def convert_nanoseconds_to_minutes(ns):
    return ns / 6e10

def convert_minutes_to_nanoseconds(minutes):
    return minutes * 6e10

def convert_nanoseconds_to_hours(ns):
    return ns / 3.6e12

def convert_hours_to_nanoseconds(hours):
    return hours * 3.6e12

def convert_nanoseconds_to_days(ns):
    return ns / 8.64e13

def convert_days_to_nanoseconds(days):
    return days * 8.64e13

def convert_nanoseconds_to_weeks(ns):
    return ns / 6.048e14

def convert_weeks_to_nanoseconds(weeks):
    return weeks * 6.048e14

def convert_nanoseconds_to_months(ns):
    return ns / 2.628e15

def convert_months_to_nanoseconds(months):
    return months * 2.628e15

def convert_nanoseconds_to_years(ns):
    return ns / 3.154e16

def convert_years_to_nanoseconds(years):
    return years * 3.154e16

def convert_microseconds_to_minutes(us):
    return us / 6e7

def convert_minutes_to_microseconds(minutes):
    return minutes * 6e7

def convert_microseconds_to_hours(us):
    return us / 3.6e9

def convert_hours_to_microseconds(hours):
    return hours * 3.6e9

def convert_microseconds_to_days(us):
    return us / 8.64e10

def convert_days_to_microseconds(days):
    return days * 8.64e10

def convert_microseconds_to_weeks(us):
    return us / 6.048e11

def convert_we
