from flask import Flask, request, redirect
import MySQLdb

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
   username = request.form['username']
   password = request.form['password']

   try:
      db = MySQLdb.connect("localhost","root","cisco123","mysite")
      cursor = db.cursor()

      # SQL Injection vulnerability (CWE-89)
      sql = "SELECT * FROM user WHERE username = '" + username + "'"
      cursor.execute(sql)
      
      if cursor.fetchone():
         return "Username already exists"

      # SQL Injection vulnerability (CWE-89)
      sql = "INSERT INTO user (username, password) VALUES ('" + username + "', '" + password + "')"
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
      db = MySQLdb.connect("localhost","root","cisco123","mysite")
      cursor = db.cursor()

      # SQL Injection vulnerability (CWE-89)
      sql = "SELECT * FROM user WHERE username = '" + username + "' AND password = '" + password + "'"
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

if __name__ == '__main__':
   app.run(debug=False)


def calculate_area_of_circle(radius):
    pi = 3.14159
    return pi * (radius ** 2)

def convert_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0

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

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    return s == s[::-1]

def sort_list_of_numbers(numbers):
    return sorted(numbers)

def find_max_in_list(numbers):
    return max(numbers)

def find_min_in_list(numbers):
    return min(numbers)

def sum_of_list(numbers):
    return sum(numbers)

def average_of_list(numbers):
    return sum(numbers) / len(numbers)

def count_occurrences_of_element(lst, element):
    return lst.count(element)

def remove_duplicates_from_list(lst):
    return list(set(lst))

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_lcm(a, b):
    return abs(a*b) // find_gcd(a, b)

def convert_inches_to_centimeters(inches):
    return inches * 2.54

def convert_centimeters_to_inches(cm):
    return cm / 2.54

def is_even(number):
    return number % 2 == 0

def is_odd(number):
    return number % 2 != 0

def calculate_square_of_number(number):
    return number ** 2

def calculate_cube_of_number(number):
    return number ** 3

def get_ascii_value(character):
    return ord(character)

def get_character_from_ascii(ascii_value):
    return chr(ascii_value)

def convert_minutes_to_seconds(minutes):
    return minutes * 60

def convert_hours_to_minutes(hours):
    return hours * 60

def convert_days_to_hours(days):
    return days * 24

def convert_weeks_to_days(weeks):
    return weeks * 7

def convert_months_to_days(months):
    return months * 30.44

def convert_years_to_days(years):
    return years * 365.25

def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def calculate_compound_interest(principal, rate, time, n):
    return principal * (1 + rate / (100*n))**(n*time)

def find_nth_fibonacci_number(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def check_if_string_contains_substring(string, substring):
    return substring in string

def count_vowels_in_string(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

def count_consonants_in_string(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char.isalpha() and char not in vowels)

def find_largest_number_in_list(numbers):
    return max(numbers)

def find_smallest_number_in_list(numbers):
    return min(numbers)

def calculate_distance_between_points(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

def convert_kilometers_to_miles(km):
    return km * 0.621371

def convert_miles_to_kilometers(miles):
    return miles / 0.621371

def calculate_bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)

def convert_seconds_to_hours(seconds):
    return seconds / 3600

def convert_seconds_to_minutes(seconds):
    return seconds / 60

def calculate_percentage(part, whole):
    return (part / whole) * 100

def calculate_area_of_rectangle(length, width):
    return length * width

def calculate_perimeter_of_rectangle(length, width):
    return 2 * (length + width)

def calculate_area_of_triangle(base, height):
    return 0.5 * base * height

def calculate_perimeter_of_triangle(a, b, c):
    return a + b + c

def calculate_area_of_square(side):
    return side ** 2

def calculate_perimeter_of_square(side):
    return 4 * side

def convert_celsius_to_kelvin(celsius):
    return celsius + 273.15

def convert_kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def convert_fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9

def convert_kelvin_to_fahrenheit(kelvin):
    return kelvin * 9/5 - 459.67

def calculate_speed(distance, time):
    return distance / time

def convert_speed_mph_to_kph(mph):
    return mph * 1.60934

def convert_speed_kph_to_mph(kph):
    return kph / 1.60934

def calculate_force(mass, acceleration):
    return mass * acceleration

def calculate_pressure(force, area):
    return force / area

def calculate_work(force, distance):
    return force * distance

def calculate_kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity ** 2

def calculate_potential_energy(mass, height, gravity=9.81):
    return mass * height * gravity

def calculate_momentum(mass, velocity):
    return mass * velocity

def calculate_density(mass, volume):
    return mass / volume

def calculate_volume_of_cylinder(radius, height):
    pi = 3.14159
    return pi * (radius ** 2) * height

def calculate_surface_area_of_cylinder(radius, height):
    pi = 3.14159
    return 2 * pi * radius * (height + radius)

def calculate_area_of_parallelogram(base, height):
    return base * height

def calculate_circumference_of_circle(radius):
    pi = 3.14159
    return 2 * pi * radius

def calculate_hypotenuse_of_right_triangle(a, b):
    return (a**2 + b**2)**0.5

def calculate_area_of_ellipse(a, b):
    pi = 3.14159
    return pi * a * b

def calculate_surface_area_of_sphere(radius):
    pi = 3.14159
    return 4 * pi * (radius ** 2)

def calculate_volume_of_sphere(radius):
    pi = 3.14159
    return (4/3) * pi * (radius ** 3)

def calculate_surface_area_of_cone(radius, slant_height):
    pi = 3.14159
    return pi * radius * (radius + slant_height)

def calculate_volume_of_cone(radius, height):
    pi = 3.14159
    return (1/3) * pi * (radius ** 2) * height

def calculate_surface_area_of_rectangular_prism(length, width, height):
    return 2 * (length * width + width * height + height * length)

def calculate_volume_of_rectangular_prism(length, width, height):
    return length * width * height

def calculate_surface_area_of_pyramid(base_area, perimeter, slant_height):
    return base_area + 0.5 * perimeter * slant_height

def calculate_volume_of_pyramid(base_area, height):
    return (1/3) * base_area * height

def calculate_surface_area_of_tetrahedron(edge_length):
    return (3**0.5) * (edge_length ** 2)

def calculate_volume_of_tetrahedron(edge_length):
    return (2**0.5 / 12) * (edge_length ** 3)

def convert_hex_to_decimal(hex_str):
    return int(hex_str, 16)

def convert_decimal_to_hex(decimal):
    return hex(decimal)

def convert_binary_to_decimal(binary_str):
    return int(binary_str, 2)

def convert_decimal_to_binary(decimal):
    return bin(decimal)

def convert_octal_to_decimal(octal_str):
    return int(octal_str, 8)

def convert_decimal_to_octal(decimal):
    return oct(decimal)

def calculate_logarithm_base_10(value):
    import math
    return math.log10(value)

def calculate_natural_logarithm(value):
    import math
    return math.log(value)

def calculate_exponential(value):
    import math
    return math.exp(value)

def calculate_sine(angle_radians):
    import math
    return math.sin(angle_radians)

def calculate_cosine(angle_radians):
    import math
    return math.cos(angle_radians)

def calculate_tangent(angle_radians):
    import math
    return math.tan(angle_radians)

def calculate_arcsine(value):
    import math
    return math.asin(value)

def calculate_arccosine(value):
    import math
    return math.acos(value)

def calculate_arctangent(value):
    import math
    return math.atan(value)

def calculate_factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def calculate_power(base, exponent):
    return base ** exponent

def calculate_sum_of_squares(numbers):
    return sum(x**2 for x in numbers)

def calculate_sum_of_cubes(numbers):
    return sum(x**3 for x in numbers)

def find_median_of_list(numbers):
    numbers.sort()
    n = len(numbers)
    mid = n // 2
    if n % 2 == 0:
        return (numbers[mid - 1] + numbers[mid]) / 2
    else:
        return numbers[mid]

def find_mode_of_list(numbers):
    from collections import Counter
    count = Counter(numbers)
    max_count = max(count.values())
    return [k for k, v in count.items() if v == max_count]

def find_standard_deviation(numbers):
    import statistics
    return statistics.stdev(numbers)

def find_variance(numbers):
    import statistics
    return statistics.variance(numbers)

def calculate_quadratic_roots(a, b, c):
    import cmath
    d = (b**2) - (4*a*c)
    root1 = (-b + cmath.sqrt(d)) / (2*a)
    root2 = (-b - cmath.sqrt(d)) / (2*a)
    return root1, root2

def calculate_interest_rate(principal, final_amount, time):
    return ((final_amount / principal) ** (1/time) - 1) * 100

def calculate_heat_energy(mass, specific_heat_capacity, temperature_change):
    return mass * specific_heat_capacity * temperature_change

def calculate_wavelength(frequency, speed_of_light=3e8):
    return speed_of_light / frequency

def check_if_number_is_armstrong(number):
    num_str = str(number)
    num_length = len(num_str)
    return number == sum(int(digit) ** num_length for digit in num_str)

def convert_decimal_to_base(decimal, base):
    if decimal == 0:
        return "0"
    digits = []
    while decimal:
        digits.append(int(decimal % base))
        decimal //= base
    return ''.join(str(x) for x in digits[::-1])

def convert_base_to_decimal(number_str, base):
    return int(number_str, base)

def calculate_gravitational_force(m1, m2, distance):
    G = 6.674 * 10**-11
    return G * (m1 * m2) / (distance ** 2)

def calculate_ohms_law(voltage, resistance):
    return voltage / resistance

def calculate_resistance(voltage, current):
    return voltage / current

def calculate_voltage(current, resistance):
    return current * resistance

def calculate_current(voltage, resistance):
    return voltage / resistance

def calculate_series_resistance(resistances):
    return sum(resistances)

def calculate_parallel_resistance(resistances):
    return 1 / sum(1/r for r in resistances)

def calculate_refraction_index(speed_in_vacuum, speed_in_medium):
    return speed_in_vacuum / speed_in_medium

def calculate_acoustic_impedance(density, speed_of_sound):
    return density * speed_of_sound

def calculate_reynolds_number(density, velocity, characteristic_length, dynamic_viscosity):
    return (density * velocity * characteristic_length) / dynamic_viscosity

def calculate_coefficient_of_linear_expansion(original_length, temperature_change, length_change):
    return length_change / (original_length * temperature_change)

def calculate_wave_speed(frequency, wavelength):
    return frequency * wavelength

def calculate_mach_number(speed, speed_of_sound):
    return speed / speed_of_sound

def calculate_thermal_conductivity(heat_transfer_rate, area, temperature_difference, thickness):
    return (heat_transfer_rate * thickness) / (area * temperature_difference)

def calculate_thermal_expansion_coefficient(initial_volume, temperature_change, volume_change):
    return volume_change / (initial_volume * temperature_change)

def calculate_centripetal_force(mass, velocity, radius):
    return (mass * velocity ** 2) / radius

def calculate_centripetal_acceleration(velocity, radius):
    return velocity ** 2 / radius

def calculate_electric_field(force, charge):
    return force / charge

def calculate_magnetic_flux(magnetic_field, area, angle):
    import math
    return magnetic_field * area * math.cos(angle)

def calculate_coulombs_law(charge1, charge2, distance):
    k = 8.9875 * 10**9
    return k * (charge1 * charge2) / (distance ** 2)

def calculate_electric_potential_energy(charge, electric_potential):
    return charge * electric_potential

def calculate_magnetic_field_strength(current, distance):
    mu_0 = 4 * math.pi * 10**-7
    return (mu_0 * current) / (2 * math.pi * distance)

def calculate_power_in_electrical_circuit(voltage, current):
    return voltage * current

def calculate_efficiency(output_energy, input_energy):
    return (output_energy / input_energy) * 100

def calculate_entropy_change(heat_transfer, temperature):
    return heat_transfer / temperature

def calculate_ph(value):
    import math
    return -math.log10(value)

def calculate_dew_point(temperature, humidity):
    import math
    a = 17.27
    b = 237.7
    alpha = ((a * temperature) / (b + temperature)) + math.log(humidity/100.0)
    return (b * alpha) / (a - alpha)

def calculate_heat_index(temperature, humidity):
    return -42.379 + 2.04901523*temperature + 10.14333127*humidity - 0.22475541*temperature*humidity - 0.00683783*temperature**2 - 0.05481717*humidity**2 + 0.00122874*temperature**2*humidity + 0.00085282*temperature*humidity**2 - 0.00000199*temperature**2*humidity**2

def calculate_wind_chill(temperature, wind_speed):
    return 35.74 + 0.6215*temperature - 35.75*wind_speed**0.16 + 0.4275*temperature*wind_speed**0.16

def calculate_depreciation(initial_value, rate, time):
    return initial_value * ((1 - rate) ** time)

def calculate_amortization(principal, rate, time):
    rate_per_period = rate / 12
    return (principal * rate_per_period) / (1 - (1 + rate_per_period) ** -time)

def calculate_future_value(principal, rate, time):
    return principal * ((1 + rate) ** time)

def calculate_present_value(future_value, rate, time):
    return future_value / ((1 + rate) ** time)

def calculate_annuity_payment(principal, rate, time):
    rate_per_period = rate / 12
    return principal * (rate_per_period / (1 - (1 + rate_per_period) ** -time))

def calculate_perpetuity_payment(principal, rate):
    return principal * rate

def calculate_adjusted_gross_income(income, deductions):
    return income - deductions

def calculate_taxable_income(adjusted_gross_income, exemptions):
    return adjusted_gross_income - exemptions

def calculate_net_income(gross_income, taxes):
    return gross_income - taxes

def calculate_break_even_point(fixed_costs, price_per_unit, variable_costs_per_unit):
    return fixed_costs / (price_per_unit - variable_costs_per_unit)

def calculate_return_on_investment(gain_from_investment, cost_of_investment):
    return (gain_from_investment - cost_of_investment) / cost_of_investment

def calculate_payback_period(initial_investment, annual_cash_flow):
    return initial_investment / annual_cash_flow

def calculate_net_present_value(cash_flows, discount_rate):
    return sum(cf / ((1 + discount_rate) ** i) for i, cf in enumerate(cash_flows))

def calculate_internal_rate_of_return(initial_investment, cash_flows):
    from numpy import irr
    return irr([-initial_investment] + cash_flows)

def calculate_contribution_margin(sales, variable_costs):
    return sales - variable_costs

def calculate_gross_margin(revenue, cost_of_goods_sold):
    return (revenue - cost_of_goods_sold) / revenue

def calculate_operating_margin(operating_income, revenue):
    return operating_income / revenue

def calculate_net_profit_margin(net_income, revenue):
    return net_income / revenue

def calculate_quick_ratio(current_assets, inventories, current_liabilities):
    return (current_assets - inventories) / current_liabilities

def calculate_current_ratio(current_assets, current_liabilities):
    return current_assets / current_liabilities
