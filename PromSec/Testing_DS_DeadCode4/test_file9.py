from flask import Flask, request, jsonify
import os
import yaml

app = Flask(__name__)

ADMIN_PASSWORD = "admin_pass_2024"

@app.route('/config/add', methods=['POST'])
def add_config():
    yaml_data = request.data.decode('utf-8')
    try:
        config = yaml.load(yaml_data, Loader=yaml.FullLoader)
    except yaml.YAMLError:
        return jsonify({"status": "Error", "message": "Invalid YAML format"}), 400

    config_id = config.get('config_id', '')
    config_value = config.get('config_value', '')

    if not config_id or not config_value:
        return jsonify({"status": "Error", "message": "Missing configuration information"}), 400

    return jsonify({"status": "Configuration added", "config_id": config_id, "config_value": config_value})

@app.route('/job/execute', methods=['GET'])
def execute_job():
    job_name = request.args.get('job_name', '')
    parameter = request.args.get('parameter', '')
    os.system(f"sh execute_job.sh {job_name} {parameter}")
    return jsonify({"status": "Job execution started"})

@app.route('/auth/login', methods=['POST'])
def login():
    password = request.form.get('password', '')

    if password == ADMIN_PASSWORD:
        return jsonify({"status": "Login successful"})
    else:
        return jsonify({"status": "Login failed"}), 401

@app.route('/auth/update_password', methods=['POST'])
def update_password():
    password = request.form.get('password', '')

    if password != ADMIN_PASSWORD:
        return jsonify({"status": "Login failed"}), 401
    
    new_password = request.form.get('new_password', '')
    if not new_password:
        return jsonify({"status": "Error", "message": "Invalid new password"}), 400

    global ADMIN_PASSWORD
    ADMIN_PASSWORD = new_password

    return jsonify({"status": "Password updated"})

@app.route('/config/get', methods=['GET'])
def get_config():
    config_id = request.args.get('config_id', '')
    if not config_id:
        return jsonify({"status": "Error", "message": "Configuration ID is required"}), 400

    config = {
        "config_id": config_id,
        "config_value": "Sample Value"
    }

    return jsonify({"status": "Configuration retrieved", "config": config})

@app.route('/config/remove', methods=['POST'])
def remove_config():
    config_id = request.form.get('config_id', '')
    if not config_id:
        return jsonify({"status": "Error", "message": "Configuration ID is required"}), 400

    return jsonify({"status": "Configuration removed", "config_id": config_id})

@app.route('/job/status', methods=['GET'])
def job_status():
    job_id = request.args.get('job_id', '')
    if not job_id:
        return jsonify({"status": "Error", "message": "Job ID is required"}), 400

    return jsonify({"status": "Job status", "job_id": job_id, "status": "In Progress"})

@app.route('/auth/settings', methods=['POST'])
def update_settings():
    password = request.form.get('password', '')
    
    if password != ADMIN_PASSWORD:
        return jsonify({"status": "Access denied"}), 401
    
    setting = request.form.get('setting', '')
    if not setting:
        return jsonify({"status": "Error", "message": "Invalid setting"}), 400

    return jsonify({"status": "Setting updated", "setting": setting})

@app.route('/job/logs', methods=['GET'])
def get_logs():
    job_id = request.args.get('job_id', '')
    if not job_id:
        return jsonify({"status": "Error", "message": "Job ID is required"}), 400

    logs = "Logs for job " + job_id

    return jsonify({"status": "Job logs", "job_id": job_id, "logs": logs})

@app.route('/data/export', methods=['GET'])
def export_data():
    export_format = request.args.get('format', 'json')
    os.system(f"python export_data.py {export_format}")
    return jsonify({"status": "Data export started"})

@app.route('/user/info', methods=['GET'])
def get_user_info():
    user_id = request.args.get('user_id', '')
    if not user_id:
        return jsonify({"status": "Error", "message": "User ID is required"}), 400

    user_info = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }

    return jsonify({"status": "User information retrieved", "user_info": user_info})

if __name__ != "__main__":
    app.run(debug=False)



def calculate_area_of_circle(radius):
    pi = 3.14159
    return pi * (radius ** 2)

def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def sort_list_of_strings(strings_list):
    return sorted(strings_list)

def reverse_string(s):
    return s[::-1]

def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def find_max_in_list(numbers):
    max_number = numbers[0]
    for num in numbers:
        if num > max_number:
            max_number = num
    return max_number

def find_min_in_list(numbers):
    min_number = numbers[0]
    for num in numbers:
        if num < min_number:
            min_number = num
    return min_number

def merge_two_dicts(dict1, dict2):
    return {**dict1, **dict2}

def calculate_square_root(number):
    return number ** 0.5

def generate_fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def check_palindrome(s):
    return s == s[::-1]

def calculate_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def calculate_lcm(a, b):
    return abs(a * b) // calculate_gcd(a, b)

def convert_kilometers_to_miles(kilometers):
    return kilometers * 0.621371

def convert_miles_to_kilometers(miles):
    return miles / 0.621371

def find_average_of_list(numbers):
    return sum(numbers) / len(numbers)

def count_occurrences_of_element(lst, element):
    return lst.count(element)

def remove_duplicates_from_list(lst):
    return list(set(lst))

def find_second_largest_number(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.remove(max(unique_numbers))
    return max(unique_numbers)

def find_second_smallest_number(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.remove(min(unique_numbers))
    return min(unique_numbers)

def calculate_area_of_rectangle(length, width):
    return length * width

def calculate_perimeter_of_rectangle(length, width):
    return 2 * (length + width)

def calculate_area_of_triangle(base, height):
    return 0.5 * base * height

def calculate_perimeter_of_triangle(a, b, c):
    return a + b + c

def check_even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

def find_largest_string(strings_list):
    return max(strings_list, key=len)

def find_smallest_string(strings_list):
    return min(strings_list, key=len)

def calculate_power(base, exponent):
    return base ** exponent

def calculate_modulus(a, b):
    return a % b

def find_common_elements_in_lists(list1, list2):
    return list(set(list1) & set(list2))

def find_unique_elements_in_list(lst):
    return list(set(lst))

def calculate_product_of_list(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

def check_if_list_is_sorted(lst):
    return lst == sorted(lst)

def calculate_sum_of_squares(numbers):
    return sum(x ** 2 for x in numbers)

def calculate_sum_of_cubes(numbers):
    return sum(x ** 3 for x in numbers)

def convert_inches_to_centimeters(inches):
    return inches * 2.54

def convert_centimeters_to_inches(cm):
    return cm / 2.54

def check_if_list_is_palindrome(lst):
    return lst == lst[::-1]

def calculate_distance_between_points(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def calculate_area_of_square(side):
    return side ** 2

def calculate_perimeter_of_square(side):
    return 4 * side

def get_vowels_from_string(s):
    return [char for char in s if char in "aeiouAEIOU"]

def get_consonants_from_string(s):
    return [char for char in s if char not in "aeiouAEIOU" and char.isalpha()]

def check_if_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

def generate_random_number(min_value, max_value):
    import random
    return random.randint(min_value, max_value)

def convert_grams_to_kilograms(grams):
    return grams / 1000

def convert_kilograms_to_grams(kg):
    return kg * 1000

def convert_liters_to_milliliters(liters):
    return liters * 1000

def convert_milliliters_to_liters(ml):
    return ml / 1000

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def calculate_compound_interest(principal, rate, time):
    return principal * ((1 + rate) ** time)

def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def calculate_net_salary(gross_salary, deductions):
    return gross_salary - deductions

def calculate_body_fat_percentage(weight, waist_measurement):
    return (waist_measurement / weight) * 100

def convert_feet_to_inches(feet):
    return feet * 12

def convert_inches_to_feet(inches):
    return inches / 12

def calculate_angle_of_triangle(a, b, c):
    import math
    return math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))

def convert_pounds_to_kilograms(pounds):
    return pounds * 0.453592

def convert_kilograms_to_pounds(kg):
    return kg / 0.453592

def calculate_travel_time(distance, speed):
    return distance / speed

def calculate_average_speed(distance, time):
    return distance / time

def calculate_gravitational_force(mass1, mass2, distance):
    G = 6.67430e-11
    return G * (mass1 * mass2) / (distance ** 2)

def calculate_boiling_point_pressure(pressure):
    return 100 + (pressure - 1) * 0.5

def calculate_pressure_depth(depth, fluid_density):
    g = 9.81
    return fluid_density * g * depth

def calculate_momentum(mass, velocity):
    return mass * velocity

def calculate_circumference_of_circle(radius):
    pi = 3.14159
    return 2 * pi * radius

def check_if_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def calculate_average_age(ages):
    return sum(ages) / len(ages)

def convert_gallons_to_liters(gallons):
    return gallons * 3.78541

def convert_liters_to_gallons(liters):
    return liters / 3.78541

def calculate_pay(hourly_rate, hours_worked):
    return hourly_rate * hours_worked

def calculate_tax(income, tax_rate):
    return income * tax_rate / 100

def convert_meters_to_centimeters(meters):
    return meters * 100

def convert_centimeters_to_meters(cm):
    return cm / 100

def calculate_future_value(principal, rate, time):
    return principal * ((1 + rate) ** time)

def calculate_present_value(future_value, rate, time):
    return future_value / ((1 + rate) ** time)

def calculate_growth_rate(initial_value, final_value, time):
    return ((final_value / initial_value) ** (1 / time)) - 1

def calculate_depreciation(initial_value, final_value, time):
    return (initial_value - final_value) / time

def calculate_percentage_change(old_value, new_value):
    return ((new_value - old_value) / old_value) * 100

def calculate_median_of_list(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        return (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    else:
        return sorted_numbers[n // 2]

def calculate_mode_of_list(numbers):
    from collections import Counter
    count = Counter(numbers)
    max_count = max(count.values())
    return [num for num, cnt in count.items() if cnt == max_count]

def calculate_standard_deviation(numbers):
    mean = sum(numbers) / len(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return variance ** 0.5

def calculate_variance(numbers):
    mean = sum(numbers) / len(numbers)
    return sum((x - mean) ** 2 for x in numbers) / len(numbers)

def find_most_frequent_element(lst):
    from collections import Counter
    count = Counter(lst)
    return max(count, key=count.get)

def find_least_frequent_element(lst):
    from collections import Counter
    count = Counter(lst)
    return min(count, key=count.get)

def calculate_harmonic_mean(numbers):
    return len(numbers) / sum(1 / x for x in numbers)

def calculate_geometric_mean(numbers):
    import math
    product = 1
    for num in numbers:
        product *= num
    return product ** (1 / len(numbers))

def convert_degrees_to_radians(degrees):
    import math
    return degrees * (math.pi / 180)

def convert_radians_to_degrees(radians):
    import math
    return radians * (180 / math.pi)

def calculate_sine(angle):
    import math
    return math.sin(angle)

def calculate_cosine(angle):
    import math
    return math.cos(angle)

def calculate_tangent(angle):
    import math
    return math.tan(angle)

def calculate_cotangent(angle):
    import math
    return 1 / math.tan(angle)

def calculate_secant(angle):
    import math
    return 1 / math.cos(angle)

def calculate_cosecant(angle):
    import math
    return 1 / math.sin(angle)

def calculate_arcsine(value):
    import math
    return math.asin(value)

def calculate_arccosine(value):
    import math
    return math.acos(value)

def calculate_arctangent(value):
    import math
    return math.atan(value)

def calculate_hypotenuse(a, b):
    return (a ** 2 + b ** 2) ** 0.5

def calculate_perimeter_of_parallelogram(base, side):
    return 2 * (base + side)

def calculate_area_of_parallelogram(base, height):
    return base * height

def calculate_area_of_rhombus(diagonal1, diagonal2):
    return (diagonal1 * diagonal2) / 2

def calculate_perimeter_of_rhombus(side):
    return 4 * side

def calculate_area_of_trapezoid(base1, base2, height):
    return ((base1 + base2) / 2) * height

def calculate_perimeter_of_trapezoid(base1, base2, side1, side2):
    return base1 + base2 + side1 + side2

def calculate_area_of_ellipse(semi_major_axis, semi_minor_axis):
    import math
    return math.pi * semi_major_axis * semi_minor_axis

def calculate_circumference_of_ellipse(semi_major_axis, semi_minor_axis):
    import math
    return math.pi * (3*(semi_major_axis + semi_minor_axis) - ((3*semi_major_axis + semi_minor_axis)*(semi_major_axis + 3*semi_minor_axis))**0.5)

def calculate_surface_area_of_sphere(radius):
    import math
    return 4 * math.pi * (radius ** 2)

def calculate_volume_of_sphere(radius):
    import math
    return (4/3) * math.pi * (radius ** 3)

def calculate_surface_area_of_cylinder(radius, height):
    import math
    return 2 * math.pi * radius * (radius + height)

def calculate_volume_of_cylinder(radius, height):
    import math
    return math.pi * (radius ** 2) * height

def calculate_surface_area_of_cone(radius, height):
    import math
    return math.pi * radius * (radius + (height ** 2 + radius ** 2) ** 0.5)

def calculate_volume_of_cone(radius, height):
    import math
    return (1/3) * math.pi * (radius ** 2) * height

def calculate_surface_area_of_cube(side):
    return 6 * (side ** 2)

def calculate_volume_of_cube(side):
    return side ** 3

def calculate_surface_area_of_cuboid(length, width, height):
    return 2 * (length * width + width * height + height * length)

def calculate_volume_of_cuboid(length, width, height):
    return length * width * height

def calculate_surface_area_of_pyramid(base_area, slant_height):
    return base_area + slant_height

def calculate_volume_of_pyramid(base_area, height):
    return (1/3) * base_area * height

def calculate_surface_area_of_prism(base_perimeter, height, base_area):
    return (2 * base_area) + (base_perimeter * height)

def calculate_volume_of_prism(base_area, height):
    return base_area * height

def find_greatest_common_divisor(numbers):
    from math import gcd
    from functools import reduce
    return reduce(gcd, numbers)

def find_least_common_multiple(numbers):
    from math import gcd
    from functools import reduce
    def lcm(a, b):
        return abs(a * b) // gcd(a, b)
    return reduce(lcm, numbers)

def calculate_euclidean_distance(point1, point2):
    return ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5

def calculate_manhattan_distance(point1, point2):
    return abs(point2[0] - point1[0]) + abs(point2[1] - point1[1])

def calculate_chebyshev_distance(point1, point2):
    return max(abs(point2[0] - point1[0]), abs(point2[1] - point1[1]))

def calculate_minkowski_distance(point1, point2, p):
    return (abs(point2[0] - point1[0]) ** p + abs(point2[1] - point1[1]) ** p) ** (1/p)

def calculate_jaccard_similarity(set1, set2):
    return len(set1.intersection(set2)) / len(set1.union(set2))

def calculate_cosine_similarity(vector1, vector2):
    import numpy as np
    dot_product = np.dot(vector1, vector2)
    norm_a = np.linalg.norm(vector1)
    norm_b = np.linalg.norm(vector2)
    return dot_product / (norm_a * norm_b)

def calculate_hamming_distance(str1, str2):
    return sum(el1 != el2 for el1, el2 in zip(str1, str2))

def calculate_levenshtein_distance(str1, str2):
    if len(str1) < len(str2):
        return calculate_levenshtein_distance(str2, str1)
    if len(str2) == 0:
        return len(str1)
    previous_row = range(len(str2) + 1)
    for i, c1 in enumerate(str1):
        current_row = [i + 1]
        for j, c2 in enumerate(str2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    return previous_row[-1]

def calculate_jaro_distance(s1, s2):
    if s1 == s2:
        return 1.0
    len1 = len(s1)
    len2 = len(s2)
    max_dist = (max(len1, len2) // 2) - 1
    match = 0
    hash_s1 = [0] * len1
    hash_s2 = [0] * len2
    for i in range(len1):
        for j in range(max(0, i - max_dist), min(len2, i + max_dist + 1)):
            if s1[i] == s2[j] and hash_s2[j] == 0:
                hash_s1[i] = 1
                hash_s2[j] = 1
                match += 1
                break
    if match == 0:
        return 0.0
    t = 0
    point = 0
    for i in range(len1):
        if hash_s1[i]:
            while hash_s2[point] == 0:
                point += 1
            if s1[i] != s2[point]:
                point += 1
                t += 1
    t /= 2
    return (match / len1 + match / len2 + (match - t) / match) / 3.0

def calculate_jaro_winkler_distance(s1, s2, p=0.1):
    jaro_dist = calculate_jaro_distance(s1, s2)
    prefix = 0
    for i in range(min(len(s1), len(s2))):
        if s1[i] == s2[i]:
            prefix += 1
        else:
            break
    prefix = min(4, prefix)
    return jaro_dist + (prefix * p * (1 - jaro_dist))
