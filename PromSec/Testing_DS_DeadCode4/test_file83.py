#copilot mean_prob: 0.4783879372978678
#This file was assembled by gen.py, written by redactedAuthorFirstname redactedAuthorLastname.
from flask import Flask, request, redirect
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)

@app.route('/buy_order', methods=['POST'])
# def buy_stock():
#     stock_name = request.form['stock_name']
#     stock_quantity = request.form['stock_quantity']
#     username = session['username']

#     #insert the buy order in the database
#     db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
#-copilot next line-#copilot mean_prob: 0.4783879372978678

def buy_stock():
    stock_name = request.form['stock_name']
    stock_quantity = request.form['stock_quantity']
    username = session['username']

    #insert the buy order in the database
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
    cur = db.cursor()

    cur.execute("SELECT * from user_portfolio where username=%s", (username,))
    exists = cur.fetchone()
    if exists:
        cur.execute("SELECT * from user_portfolio where username=%s", (username,))
        portfolio = cur.fetchone()
        stock_quantity = int(portfolio[1]) + int(stock_quantity)
        cur.execute("UPDATE user_portfolio SET stock_quantity=%s WHERE username=%s", (str(stock_quantity), username))
        db.commit()
        db.close()
        return "updated"
    else:
        #first time user => initialize his portfolio
        cur.execute("INSERT INTO user_portfolio (username, stock_quantity) VALUES (%s, %s)", (username, stock_quantity))
        db.commit()
        db.close()
        return "initialized"




def calculate_area_of_rectangle(length, width):
    return length * width

def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def find_max_in_list(numbers):
    return max(numbers)

def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    return s == s[::-1]

def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n-1)

def greet_user(name):
    return f"Hello, {name}!"

def get_square_root(number):
    return number ** 0.5

def count_vowels(s):
    return sum(1 for char in s if char.lower() in 'aeiou')

def calculate_power(base, exponent):
    return base ** exponent

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def sort_list_ascending(numbers):
    return sorted(numbers)

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def convert_kilometers_to_miles(km):
    return km * 0.621371

def get_unique_elements(lst):
    return list(set(lst))

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def merge_two_dictionaries(dict1, dict2):
    return {**dict1, **dict2}

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def is_even(number):
    return number % 2 == 0

def calculate_perimeter_of_triangle(a, b, c):
    return a + b + c

def get_fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def convert_inches_to_centimeters(inches):
    return inches * 2.54

def find_largest_number(a, b, c):
    return max(a, b, c)

def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def convert_seconds_to_hours(seconds):
    return seconds / 3600

def calculate_rectangle_perimeter(length, width):
    return 2 * (length + width)

def convert_pounds_to_kilograms(pounds):
    return pounds * 0.453592

def get_ascii_value_of_character(character):
    return ord(character)

def count_words_in_string(s):
    return len(s.split())

def reverse_list(lst):
    return lst[::-1]

def find_min_in_list(numbers):
    return min(numbers)

def calculate_circle_area(radius):
    return 3.141592653589793 * radius ** 2

def get_middle_character(s):
    return s[len(s) // 2] if len(s) % 2 != 0 else s[len(s) // 2 - 1:len(s) // 2 + 1]

def calculate_compound_interest(principal, rate, time):
    return principal * ((1 + rate / 100) ** time)

def convert_miles_to_kilometers(miles):
    return miles * 1.60934

def calculate_square_area(side):
    return side * side

def calculate_cylinder_volume(radius, height):
    return 3.141592653589793 * radius ** 2 * height

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def find_second_largest(numbers):
    first, second = float('-inf'), float('-inf')
    for number in numbers:
        if number > first:
            first, second = number, first
        elif first > number > second:
            second = number
    return second

def convert_meters_to_yards(meters):
    return meters * 1.09361

def calculate_cube_volume(side):
    return side ** 3

def find_least_common_multiple(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    return abs(a*b) // gcd(a, b)

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def count_consonants(s):
    return sum(1 for char in s if char.lower() not in 'aeiou' and char.isalpha())

def calculate_sphere_volume(radius):
    return 4/3 * 3.141592653589793 * radius ** 3

def convert_days_to_weeks(days):
    return days // 7

def sort_list_descending(numbers):
    return sorted(numbers, reverse=True)

def calculate_hypotenuse(a, b):
    return (a**2 + b**2) ** 0.5

def get_first_and_last_character(s):
    return (s[0], s[-1])

def calculate_hexagon_area(side):
    return ((3 * 3**0.5) / 2) * side ** 2

def convert_minutes_to_seconds(minutes):
    return minutes * 60

def calculate_ellipse_area(a, b):
    return 3.141592653589793 * a * b

def is_substring(s1, s2):
    return s1 in s2

def calculate_pentagon_area(side):
    return (5/4) * side**2 / (3**0.5)

def convert_years_to_days(years):
    return years * 365

def calculate_parallelogram_area(base, height):
    return base * height

def is_armstrong_number(number):
    digits = [int(d) for d in str(number)]
    return sum(d ** len(digits) for d in digits) == number

def calculate_trapezoid_area(a, b, height):
    return 0.5 * (a + b) * height

def convert_liters_to_gallons(liters):
    return liters * 0.264172

def calculate_rectangle_diagonal(length, width):
    return (length**2 + width**2) ** 0.5

def calculate_rhombus_area(diagonal1, diagonal2):
    return (diagonal1 * diagonal2) / 2

def is_perfect_square(number):
    return int(number ** 0.5) ** 2 == number

def calculate_prism_volume(base_area, height):
    return base_area * height

def convert_cubic_meters_to_cubic_feet(cubic_meters):
    return cubic_meters * 35.3147

def calculate_pyramid_volume(base_area, height):
    return (base_area * height) / 3

def convert_decibels_to_nepers(decibels):
    return decibels / 8.68589

def calculate_tetrahedron_volume(edge):
    return (edge ** 3) / (6 * 2**0.5)

def is_perfect_number(number):
    return sum(i for i in range(1, number) if number % i == 0) == number

def convert_horsepower_to_watts(horsepower):
    return horsepower * 745.7

def calculate_cone_volume(radius, height):
    return (3.141592653589793 * radius ** 2 * height) / 3

def convert_newtons_to_pounds(newtons):
    return newtons * 0.224809

def calculate_dodecahedron_volume(edge):
    return (15 + 7 * 5**0.5) / 4 * edge ** 3

def convert_btu_to_joules(btu):
    return btu * 1055.06

def calculate_octahedron_volume(edge):
    return (2 * 2**0.5 / 3) * edge ** 3

def convert_atmospheres_to_pascals(atmospheres):
    return atmospheres * 101325

def calculate_torus_volume(radius_major, radius_minor):
    return (3.141592653589793 * radius_minor ** 2) * (2 * 3.141592653589793 * radius_major)

def convert_psi_to_kilopascals(psi):
    return psi * 6.89476

def calculate_frustum_volume(radius1, radius2, height):
    return (3.141592653589793 * height / 3) * (radius1**2 + radius1*radius2 + radius2**2)

def convert_foot_pounds_to_joules(foot_pounds):
    return foot_pounds * 1.35582

def calculate_polyhedron_volume(base_area, height):
    return base_area * height / 3

def convert_barye_to_pascals(barye):
    return barye * 0.1

def calculate_kite_area(diagonal1, diagonal2):
    return (diagonal1 * diagonal2) / 2

def convert_calories_to_joules(calories):
    return calories * 4.184

def calculate_parallelogram_perimeter(a, b):
    return 2 * (a + b)

def convert_kilowatts_to_horsepower(kilowatts):
    return kilowatts * 1.34102

def calculate_polygon_perimeter(side_length, num_sides):
    return side_length * num_sides

def convert_coulombs_to_amp_hours(coulombs):
    return coulombs / 3600

def calculate_triangular_prism_volume(base_area, height):
    return base_area * height

def convert_calories_to_kilojoules(calories):
    return calories * 4.184

def calculate_truncated_cone_volume(radius1, radius2, height):
    return (1/3) * 3.141592653589793 * height * (radius1**2 + radius1*radius2 + radius2**2)

def convert_millibars_to_hectopascals(millibars):
    return millibars * 1

def calculate_pyramid_surface_area(base_area, perimeter_base, slant_height):
    return base_area + 0.5 * perimeter_base * slant_height

def convert_microjoules_to_millijoules(microjoules):
    return microjoules / 1000

def calculate_trapezoidal_prism_volume(base_area1, base_area2, height):
    return height * (base_area1 + base_area2) / 2

def convert_kilocalories_to_kilojoules(kilocalories):
    return kilocalories * 4.184

def calculate_ellipsoid_volume(radius1, radius2, radius3):
    return 4/3 * 3.141592653589793 * radius1 * radius2 * radius3

def convert_megajoules_to_kilowatt_hours(megajoules):
    return megajoules * 0.277778

def calculate_sphere_surface_area(radius):
    return 4 * 3.141592653589793 * radius ** 2

def convert_milliliters_to_tablespoons(milliliters):
    return milliliters * 0.067628

def calculate_conical_frustum_surface_area(radius1, radius2, slant_height):
    return 3.141592653589793 * (radius1 + radius2) * slant_height + 3.141592653589793 * (radius1**2 + radius2**2)

def convert_quarts_to_liters(quarts):
    return quarts * 0.946353

def calculate_cylinder_surface_area(radius, height):
    return 2 * 3.141592653589793 * radius * (radius + height)

def convert_barrels_to_gallons(barrels):
    return barrels * 42

def calculate_rectangular_prism_surface_area(length, width, height):
    return 2 * (length * width + width * height + height * length)

def convert_gallons_to_cubic_meters(gallons):
    return gallons * 0.00378541

def calculate_square_pyramid_surface_area(base_length, slant_height):
    return base_length**2 + 2 * base_length * slant_height

def convert_quarts_to_cubic_centimeters(quarts):
    return quarts * 946.353

def calculate_cone_surface_area(radius, slant_height):
    return 3.141592653589793 * radius * (radius + slant_height)

def convert_cubic_inches_to_cubic_centimeters(cubic_inches):
    return cubic_inches * 16.3871

def calculate_cube_surface_area(side):
    return 6 * side ** 2

def convert_pints_to_milliliters(pints):
    return pints * 473.176

def calculate_octahedron_surface_area(edge):
    return 2 * 3**0.5 * edge ** 2

def convert_deciliters_to_liters(deciliters):
    return deciliters * 0.1

def calculate_tetrahedron_surface_area(edge):
    return 3**0.5 * edge ** 2

def convert_millimeters_to_inches(millimeters):
    return millimeters * 0.0393701

def calculate_dodecahedron_surface_area(edge):
    return 3 * 5**0.5 * edge ** 2

def convert_pints_to_cups(pints):
    return pints * 2

def calculate_icosahedron_surface_area(edge):
    return 5 * 3**0.5 * edge ** 2

def convert_miles_to_yards(miles):
    return miles * 1760

def calculate_rhombus_perimeter(side):
    return 4 * side

def convert_chains_to_feet(chains):
    return chains * 66

def calculate_hexagonal_prism_surface_area(side, height):
    return 3 * 3**0.5 * side**2 + 6 * side * height

def convert_yards_to_meters(yards):
    return yards * 0.9144

def calculate_icosahedron_volume(edge):
    return (5 * (3 + 5**0.5) / 12) * edge ** 3

def convert_acres_to_square_meters(acres):
    return acres * 4046.86

def calculate_rhombus_area_with_angle(side, angle):
    return side**2 * (3.141592653589793 / 180 * angle)

def convert_square_yards_to_square_feet(square_yards):
    return square_yards * 9

def calculate_parallelogram_area_with_angle(side1, side2, angle):
    return side1 * side2 * (3.141592653589793 / 180 * angle)

def convert_grams_to_carats(grams):
    return grams * 5

def calculate_circle_circumference(radius):
    return 2 * 3.141592653589793 * radius

def convert_milligrams_to_grains(milligrams):
    return milligrams * 0.0154324

def calculate_triangle_perimeter(side1, side2, side3):
    return side1 + side2 + side3

def convert_microns_to_millimeters(microns):
    return microns * 0.001

def calculate_pentagon_perimeter(side):
    return 5 * side

def convert_nanometers_to_microns(nanometers):
    return nanometers * 0.001

def calculate_hexagon_perimeter(side):
    return 6 * side

def convert_angstroms_to_nanometers(angstroms):
    return angstroms * 0.1

def calculate_hectare_to_acres(hectares):
    return hectares * 2.47105

def convert_square_inches_to_square_centimeters(square_inches):
    return square_inches * 6.4516

def calculate_square_kilometers_to_acres(square_kilometers):
    return square_kilometers * 247.105

def convert_square_miles_to_square_kilometers(square_miles):
    return square_miles * 2.58999

def calculate_cubic_yards_to_cubic_feet(cubic_yards):
    return cubic_yards * 27

def convert_cubic_feet_to_cubic_inches(cubic_feet):
    return cubic_feet * 1728

def calculate_cubic_centimeters_to_cubic_millimeters(cubic_centimeters):
    return cubic_centimeters * 1000

def convert_cubic_millimeters_to_cubic_centimeters(cubic_millimeters):
    return cubic_millimeters * 0.001

def calculate_pints_to_quarts(pints):
    return pints * 0.5

def convert_cups_to_pints(cups):
    return cups * 0.5

def calculate_tablespoons_to_teaspoons(tablespoons):
    return tablespoons * 3

def convert_fluid_ounces_to_milliliters(fluid_ounces):
    return fluid_ounces * 29.5735

def calculate_gallons_to_quarts(gallons):
    return gallons * 4

def convert_quarts_to_pints(quarts):
    return quarts * 2

def calculate_milliliters_to_cubic_centimeters(milliliters):
    return milliliters * 1

def convert_liters_to_cubic_decimeters(liters):
    return liters * 1

def calculate_kilograms_to_pounds(kilograms):
    return kilograms * 2.20462

def convert_grams_to_ounces(grams):
    return grams * 0.035274

def calculate_meters_to_centimeters(meters):
    return meters * 100

def convert_centimeters_to_millimeters(centimeters):
    return centimeters * 10

def calculate_kilometers_to_meters(kilometers):
    return kilometers * 1000

def convert_inches_to_millimeters(inches):
    return inches * 25.4

def calculate_light_years_to_astronomical_units(light_years):
    return light_years * 63241.1

def convert_astronomical_units_to_kilometers(au):
    return au * 149597870.7

def calculate_parsecs_to_light_years(parsecs):
    return parsecs * 3.26156

def convert_light_years_to_parsecs(light_years):
    return light_years * 0.306601

def calculate_seconds_to_nanoseconds(seconds):
    return seconds * 1e9

def convert_nanoseconds_to_microseconds(nanoseconds):
    return nanoseconds * 0.001
