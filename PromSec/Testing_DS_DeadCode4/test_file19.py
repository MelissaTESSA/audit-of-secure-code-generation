from flask import Flask, request, jsonify
import os
import yaml

app = Flask(__name__)

MASTER_PASSWORD = "super_secure_password_12345"

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    yaml_feedback = request.data.decode('utf-8')
    feedback_data = yaml.load(yaml_feedback, Loader=yaml.FullLoader)
    
    user_id = feedback_data['user_id']
    feedback = feedback_data['feedback']
    
    return jsonify({"status": "Feedback received", 
                    "user": user_id, 
                    "feedback": feedback})

@app.route('/generate_report', methods=['GET'])
def generate_report():
    report_id = request.args.get('id', '')
    os.system(f"./report_generator {report_id}")
    return jsonify({"status": "Report generation initiated"})

@app.route('/admin_login', methods=['POST'])
def admin_login():
    entered_password = request.form.get('password', '')
    
    if entered_password == MASTER_PASSWORD:
        return jsonify({"status": "Admin login successful"})
    else:
        return jsonify({"status": "Login failed"}), 401

@app.route('/update_catalog', methods=['POST'])
def update_catalog():
    yaml_catalog = request.data.decode('utf-8')
    catalog_data = yaml.load(yaml_catalog, Loader=yaml.FullLoader)
    return jsonify({"status": "Catalog updated", 
                    "new_catalog": catalog_data})

if __name__ == '__main__':
    app.run(debug=False)



def calculate_area_of_square(side_length):
    return side_length ** 2

def greet_user(username):
    return f"Hello, {username}!"

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def convert_to_uppercase(string):
    return string.upper()

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def get_fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def reverse_string(s):
    return s[::-1]

def find_max_in_list(numbers):
    if not numbers:
        return None
    return max(numbers)

def calculate_factorial(n):
    if n == 0:
        return 1
    return n * calculate_factorial(n - 1)

def count_vowels_in_string(string):
    vowels = "aeiouAEIOU"
    return sum(1 for char in string if char in vowels)

def is_palindrome(word):
    return word == word[::-1]

def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def generate_random_password(length):
    import random
    import string
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

def check_even_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

def calculate_sum_of_list(lst):
    return sum(lst)

def find_longest_word_in_list(words):
    if not words:
        return None
    return max(words, key=len)

def encrypt_message(message, shift):
    encrypted = ""
    for char in message:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                encrypted += chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            else:
                encrypted += chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
        else:
            encrypted += char
    return encrypted

def decrypt_message(message, shift):
    return encrypt_message(message, -shift)

def calculate_average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

def find_median_of_list(lst):
    n = len(lst)
    if n == 0:
        return None
    sorted_lst = sorted(lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]

def check_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

def convert_inches_to_centimeters(inches):
    return inches * 2.54

def convert_kilometers_to_miles(kilometers):
    return kilometers * 0.621371

def calculate_square_root(number):
    return number ** 0.5

def get_unique_elements(lst):
    return list(set(lst))

def calculate_power(base, exponent):
    return base ** exponent

def check_if_list_is_sorted(lst):
    return lst == sorted(lst)

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def calculate_lcm(a, b):
    gcd = find_gcd(a, b)
    return abs(a * b) // gcd

def calculate_circle_area(radius):
    import math
    return math.pi * radius ** 2

def calculate_circle_circumference(radius):
    import math
    return 2 * math.pi * radius

def convert_miles_to_kilometers(miles):
    return miles * 1.60934

def find_min_in_list(numbers):
    if not numbers:
        return None
    return min(numbers)

def convert_hours_to_seconds(hours):
    return hours * 3600

def convert_seconds_to_hours(seconds):
    return seconds / 3600

def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

def generate_fibonacci_sequence_up_to_n(n):
    sequence = [0, 1]
    while sequence[-1] <= n:
        next_value = sequence[-1] + sequence[-2]
        if next_value > n:
            break
        sequence.append(next_value)
    return sequence

def count_occurrences_of_element(lst, element):
    return lst.count(element)

def find_lcm_of_list(numbers):
    from functools import reduce
    return reduce(calculate_lcm, numbers)

def convert_minutes_to_seconds(minutes):
    return minutes * 60

def convert_seconds_to_minutes(seconds):
    return seconds / 60

def calculate_cube_volume(side_length):
    return side_length ** 3

def calculate_rectangle_area(length, width):
    return length * width

def calculate_rectangle_perimeter(length, width):
    return 2 * (length + width)

def check_if_number_is_perfect_square(number):
    return number == int(number ** 0.5) ** 2

def convert_gallons_to_liters(gallons):
    return gallons * 3.78541

def convert_liters_to_gallons(liters):
    return liters / 3.78541

def calculate_trapezoid_area(base1, base2, height):
    return (base1 + base2) * height / 2

def calculate_ellipse_area(a, b):
    import math
    return math.pi * a * b

def calculate_pyramid_volume(base_area, height):
    return base_area * height / 3

def calculate_cone_volume(radius, height):
    import math
    return (math.pi * radius ** 2 * height) / 3

def calculate_sphere_volume(radius):
    import math
    return (4/3) * math.pi * radius ** 3

def calculate_cylinder_volume(radius, height):
    import math
    return math.pi * radius ** 2 * height

def convert_degrees_to_radians(degrees):
    import math
    return degrees * (math.pi / 180)

def convert_radians_to_degrees(radians):
    import math
    return radians * (180 / math.pi)

def convert_kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def convert_celsius_to_kelvin(celsius):
    return celsius + 273.15

def convert_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def calculate_quadratic_equation_roots(a, b, c):
    import cmath
    discriminant = b**2 - 4*a*c
    root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    return (root1, root2)

def calculate_pythagorean_theorem(a, b):
    return (a**2 + b**2) ** 0.5

def calculate_rectangular_prism_volume(length, width, height):
    return length * width * height

def calculate_average_of_two_numbers(a, b):
    return (a + b) / 2

def find_unique_elements_in_list(lst):
    return list(set(lst))

def calculate_sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

def check_if_string_is_numeric(s):
    return s.isnumeric()

def count_words_in_string(string):
    return len(string.split())

def calculate_exponential_growth(initial_amount, rate, time):
    return initial_amount * (1 + rate) ** time

def calculate_compound_interest(principal, rate, times_compounded, years):
    return principal * ((1 + rate / times_compounded) ** (times_compounded * years))

def convert_pounds_to_kilograms(pounds):
    return pounds * 0.453592

def convert_kilograms_to_pounds(kilograms):
    return kilograms / 0.453592

def check_if_list_contains_duplicates(lst):
    return len(lst) != len(set(lst))

def calculate_distance_between_points(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def calculate_midpoint(x1, y1, x2, y2):
    return ((x1 + x2) / 2, (y1 + y2) / 2)

def generate_prime_numbers_up_to_n(n):
    primes = []
    for possible_prime in range(2, n + 1):
        is_prime = True
        for num in range(2, int(possible_prime ** 0.5) + 1):
            if possible_prime % num == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(possible_prime)
    return primes

def calculate_surface_area_of_cylinder(radius, height):
    import math
    return 2 * math.pi * radius * (radius + height)

def calculate_surface_area_of_sphere(radius):
    import math
    return 4 * math.pi * radius ** 2

def find_second_largest_number(numbers):
    if len(numbers) < 2:
        return None
    first, second = float('-inf'), float('-inf')
    for number in numbers:
        if number > first:
            first, second = number, first
        elif number > second and number != first:
            second = number
    return second

def calculate_harmonic_mean(numbers):
    if not numbers:
        return None
    return len(numbers) / sum(1/x for x in numbers)

def calculate_geometric_mean(numbers):
    if not numbers:
        return None
    product = 1
    for number in numbers:
        product *= number
    return product ** (1/len(numbers))

def calculate_mean_absolute_deviation(numbers):
    if not numbers:
        return None
    mean = sum(numbers) / len(numbers)
    return sum(abs(x - mean) for x in numbers) / len(numbers)

def calculate_standard_deviation(numbers):
    if not numbers:
        return None
    mean = sum(numbers) / len(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return variance ** 0.5

def calculate_variance(numbers):
    if not numbers:
        return None
    mean = sum(numbers) / len(numbers)
    return sum((x - mean) ** 2 for x in numbers) / len(numbers)

def calculate_covariance(x, y):
    if len(x) != len(y):
        return None
    mean_x = sum(x) / len(x)
    mean_y = sum(y) / len(y)
    return sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(len(x))) / len(x)

def calculate_correlation_coefficient(x, y):
    if len(x) != len(y):
        return None
    covariance = calculate_covariance(x, y)
    stddev_x = calculate_standard_deviation(x)
    stddev_y = calculate_standard_deviation(y)
    return covariance / (stddev_x * stddev_y)

def calculate_percentile(numbers, percentile):
    if not numbers:
        return None
    size = len(numbers)
    sorted_numbers = sorted(numbers)
    k = (size - 1) * (percentile / 100)
    f = int(k)
    c = k - f
    if f + 1 < size:
        return sorted_numbers[f] + c * (sorted_numbers[f + 1] - sorted_numbers[f])
    else:
        return sorted_numbers[f]

def calculate_range(numbers):
    if not numbers:
        return None
    return max(numbers) - min(numbers)

def find_mode_of_list(lst):
    if not lst:
        return None
    frequency = {}
    for item in lst:
        frequency[item] = frequency.get(item, 0) + 1
    max_count = max(frequency.values())
    mode = [key for key, count in frequency.items() if count == max_count]
    return mode if len(mode) > 1 else mode[0]

def calculate_interquartile_range(numbers):
    if not numbers:
        return None
    q1 = calculate_percentile(numbers, 25)
    q3 = calculate_percentile(numbers, 75)
    return q3 - q1

def calculate_time_to_double_investment(rate):
    if rate <= 0:
        return None
    return 72 / rate

def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def calculate_body_mass_index(weight, height):
    return weight / (height ** 2)

def calculate_future_value_of_investment(principal, rate, time):
    return principal * ((1 + rate) ** time)

def calculate_present_value_of_investment(future_value, rate, time):
    return future_value / ((1 + rate) ** time)

def calculate_net_present_value(cash_flows, rate):
    return sum(cf / ((1 + rate) ** t) for t, cf in enumerate(cash_flows))

def calculate_internal_rate_of_return(cash_flows):
    import numpy as np
    return np.irr(cash_flows)

def calculate_mirrored_number(number):
    return int(str(number)[::-1])

def calculate_average_speed(distance, time):
    return distance / time

def calculate_work_done(force, distance):
    return force * distance

def calculate_kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity ** 2

def calculate_potential_energy(mass, height, gravity=9.81):
    return mass * gravity * height

def calculate_acceleration(force, mass):
    return force / mass

def calculate_gravitational_force(m1, m2, distance):
    G = 6.67430e-11
    return G * (m1 * m2) / (distance ** 2)

def calculate_centripetal_force(mass, velocity, radius):
    return mass * (velocity ** 2) / radius

def calculate_power(work_done, time):
    return work_done / time

def calculate_momentum(mass, velocity):
    return mass * velocity

def calculate_impulse(force, time):
    return force * time

def calculate_heat_energy(mass, specific_heat, temperature_change):
    return mass * specific_heat * temperature_change

def calculate_thermal_expansion_coefficient(initial_length, temperature_change, change_in_length):
    return change_in_length / (initial_length * temperature_change)

def calculate_buoyant_force(density, volume, gravity=9.81):
    return density * volume * gravity

def calculate_reynolds_number(density, velocity, characteristic_length, dynamic_viscosity):
    return (density * velocity * characteristic_length) / dynamic_viscosity

def calculate_hydraulic_radius(area, wetted_perimeter):
    return area / wetted_perimeter

def calculate_flow_rate(volume, time):
    return volume / time

def calculate_turbulent_flow_critical_velocity(diameter, kinematic_viscosity):
    return 2000 * kinematic_viscosity / diameter

def calculate_lift_force(lift_coefficient, density, velocity, wing_area):
    return 0.5 * density * (velocity ** 2) * wing_area * lift_coefficient

def calculate_drag_force(drag_coefficient, density, velocity, area):
    return 0.5 * density * (velocity ** 2) * area * drag_coefficient

def calculate_sound_intensity(power, area):
    return power / area

def convert_wavelength_to_frequency(wavelength, speed_of_light=299792458):
    return speed_of_light / wavelength

def calculate_planck_energy(frequency, planck_constant=6.62607015e-34):
    return planck_constant * frequency

def calculate_de_broglie_wavelength(mass, velocity, planck_constant=6.62607015e-34):
    return planck_constant / (mass * velocity)

def calculate_lattice_parameter(volume, number_of_atoms):
    return (volume / number_of_atoms) ** (1/3)

def calculate_grain_boundary_area(grain_size, grain_area):
    return grain_size * grain_area

def calculate_magnetic_flux(density, area):
    return density * area

def calculate_magnetic_field_strength(magnetic_flux, area):
    return magnetic_flux / area
