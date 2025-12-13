@app.route('/buy_order', methods=['POST'])
def buy_stock():
    stock_name = request.form['stock_name']
    stock_quantity = request.form['stock_quantity']
    username = session['username']

    #insert the buy order in the database
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
def calculate_discount(price, discount_rate):
    discounted_price = price - (price * discount_rate)
    return discounted_price

def fetch_weather_data(city):
    api_url = f"http://api.weather.com/v3/{city}"
    response = requests.get(api_url)
    return response.json()

def convert_temperature(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

def generate_random_string(length):
    import random
    import string
    result = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return result

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def calculate_area_of_circle(radius):
    pi = 3.14159
    return pi * radius * radius

def reverse_string(s):
    return s[::-1]

def find_maximum(numbers):
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value

def sort_numbers(numbers):
    return sorted(numbers)

def fetch_user_profile(user_id):
    profile_url = f"http://api.user.com/profile/{user_id}"
    response = requests.get(profile_url)
    return response.json()

def calculate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    fib_series = [0, 1]
    for i in range(2, n):
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series

def capitalize_words(sentence):
    return ' '.join(word.capitalize() for word in sentence.split())

def calculate_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def check_palindrome(s):
    return s == s[::-1]

def convert_to_binary(n):
    return bin(n)[2:]

def filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def sort_strings(strings):
    return sorted(strings)

def fetch_exchange_rate(currency_code):
    api_url = f"http://api.exchangerate.com/{currency_code}"
    response = requests.get(api_url)
    return response.json()

def calculate_bmi(weight, height):
    return weight / (height * height)

def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

def generate_fibonacci_sequence(n):
    fib_sequence = []
    a, b = 0, 1
    while len(fib_sequence) < n:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

def count_words(sentence):
    return len(sentence.split())

def find_minimum(numbers):
    min_value = numbers[0]
    for num in numbers:
        if num < min_value:
            min_value = num
    return min_value

def convert_to_hexadecimal(n):
    return hex(n)[2:]

def filter_odd_numbers(numbers):
    return [num for num in numbers if num % 2 != 0]

def fetch_news_headlines():
    api_url = "http://api.news.com/headlines"
    response = requests.get(api_url)
    return response.json()

def calculate_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def calculate_lcm(a, b):
    return abs(a * b) // calculate_gcd(a, b)

def convert_to_octal(n):
    return oct(n)[2:]

def calculate_power(base, exponent):
    return base ** exponent

def calculate_modulus(a, b):
    return a % b

def get_unique_elements(lst):
    return list(set(lst))

def flatten_nested_list(nested_list):
    return [item for sublist in nested_list for item in sublist]

def calculate_distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def convert_to_uppercase(s):
    return s.upper()

def convert_to_lowercase(s):
    return s.lower()

def remove_whitespace(s):
    return s.strip()

def reverse_list(lst):
    return lst[::-1]

def find_duplicates(lst):
    return [item for item in set(lst) if lst.count(item) > 1]

def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]

def calculate_mode(numbers):
    from collections import Counter
    count = Counter(numbers)
    max_count = max(count.values())
    return [num for num, freq in count.items() if freq == max_count]

def calculate_variance(numbers):
    mean = sum(numbers) / len(numbers)
    return sum((x - mean) ** 2 for x in numbers) / len(numbers)

def calculate_standard_deviation(numbers):
    variance = calculate_variance(numbers)
    return variance ** 0.5

def find_intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

def find_union(lst1, lst2):
    return list(set(lst1) | set(lst2))

def find_difference(lst1, lst2):
    return list(set(lst1) - set(lst2))

def is_subset(lst1, lst2):
    return set(lst1).issubset(set(lst2))

def is_superset(lst1, lst2):
    return set(lst1).issuperset(set(lst2))

def convert_to_title_case(s):
    return s.title()

def compute_hypotenuse(a, b):
    return (a ** 2 + b ** 2) ** 0.5

def calculate_sum_of_squares(numbers):
    return sum(x ** 2 for x in numbers)

def calculate_product_of_list(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

def calculate_cumulative_sum(numbers):
    cumsum = [numbers[0]]
    for i in range(1, len(numbers)):
        cumsum.append(cumsum[-1] + numbers[i])
    return cumsum

def calculate_cumulative_product(numbers):
    cumprod = [numbers[0]]
    for i in range(1, len(numbers)):
        cumprod.append(cumprod[-1] * numbers[i])
    return cumprod

def calculate_harmonic_mean(numbers):
    return len(numbers) / sum(1/x for x in numbers)

def calculate_geometric_mean(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product ** (1/len(numbers))

def find_maximum_index(numbers):
    return numbers.index(max(numbers))

def find_minimum_index(numbers):
    return numbers.index(min(numbers))

def calculate_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def fetch_crypto_prices():
    api_url = "http://api.crypto.com/prices"
    response = requests.get(api_url)
    return response.json()

def calculate_simple_interest(principal, rate, time):
    return principal * rate * time / 100

def calculate_compound_interest(principal, rate, time, n):
    return principal * (1 + rate / n) ** (n * time)

def convert_speed_kmh_to_mph(speed_kmh):
    return speed_kmh * 0.621371

def convert_speed_mph_to_kmh(speed_mph):
    return speed_mph / 0.621371

def calculate_heat_index(temperature, humidity):
    return temperature + humidity / 100 * (temperature - 14.3) + 46.3

def fetch_gdp_data(country_code):
    api_url = f"http://api.economy.com/gdp/{country_code}"
    response = requests.get(api_url)
    return response.json()

def calculate_cagr(initial_value, final_value, years):
    return (final_value / initial_value) ** (1/years) - 1

def convert_volume_liters_to_gallons(volume_liters):
    return volume_liters * 0.264172

def convert_volume_gallons_to_liters(volume_gallons):
    return volume_gallons / 0.264172

def find_longest_word(words):
    max_len = max(len(word) for word in words)
    return [word for word in words if len(word) == max_len]

def find_shortest_word(words):
    min_len = min(len(word) for word in words)
    return [word for word in words if len(word) == min_len]

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

def count_consonants(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char.isalpha() and char not in vowels)

def find_common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))

def find_unique_elements(lst1, lst2):
    return list(set(lst1) ^ set(lst2))

def fetch_stock_prices(stock_symbol):
    api_url = f"http://api.stocks.com/{stock_symbol}/prices"
    response = requests.get(api_url)
    return response.json()

def calculate_profit(cost_price, selling_price):
    return selling_price - cost_price

def calculate_loss(cost_price, selling_price):
    return cost_price - selling_price

def calculate_percentage_change(old_value, new_value):
    return ((new_value - old_value) / old_value) * 100

def calculate_body_fat_percentage(weight, waist_circumference, wrist_circumference, hip_circumference, forearm_circumference):
    body_fat = (weight + waist_circumference + wrist_circumference + hip_circumference + forearm_circumference) / 5
    return body_fat

def convert_currency(amount, rate):
    return amount * rate

def calculate_daily_caloric_needs(weight, height, age, gender, activity_level):
    if gender == 'male':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    return bmr * activity_level

def convert_length_meters_to_feet(length_meters):
    return length_meters * 3.28084

def convert_length_feet_to_meters(length_feet):
    return length_feet / 3.28084

def calculate_age(dob):
    from datetime import date
    today = date.today()
    return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

def calculate_retirement_age(current_age, retirement_age):
    return retirement_age - current_age

def fetch_covid_statistics(country_code):
    api_url = f"http://api.covid.com/{country_code}/statistics"
    response = requests.get(api_url)
    return response.json()

def calculate_circle_circumference(radius):
    pi = 3.14159
    return 2 * pi * radius

def calculate_square_perimeter(side_length):
    return 4 * side_length

def calculate_rectangle_area(length, width):
    return length * width

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def calculate_trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height

def calculate_sphere_volume(radius):
    pi = 3.14159
    return 4/3 * pi * radius ** 3

def calculate_cylinder_volume(radius, height):
    pi = 3.14159
    return pi * radius ** 2 * height

def calculate_cone_volume(radius, height):
    pi = 3.14159
    return 1/3 * pi * radius ** 2 * height

def calculate_pyramid_volume(base_area, height):
    return base_area * height / 3

def calculate_prism_volume(base_area, height):
    return base_area * height

def calculate_parallelogram_area(base, height):
    return base * height

def calculate_rhombus_area(diagonal1, diagonal2):
    return 0.5 * diagonal1 * diagonal2

def calculate_hexagon_area(side_length):
    return (3 * 3**0.5 * side_length ** 2) / 2

def calculate_pentagon_area(side_length):
    from math import tan, pi
    return (5 * side_length ** 2) / (4 * tan(pi / 5))

def calculate_octagon_area(side_length):
    return 2 * (1 + 2**0.5) * side_length ** 2

def calculate_equilateral_triangle_area(side_length):
    return (3**0.5 / 4) * side_length ** 2

def calculate_tetrahedron_volume(edge_length):
    return (2**0.5 / 12) * edge_length ** 3

def calculate_cube_volume(side_length):
    return side_length ** 3

def calculate_cuboid_volume(length, width, height):
    return length * width * height

def fetch_population_data(country_code):
    api_url = f"http://api.population.com/{country_code}/data"
    response = requests.get(api_url)
    return response.json()

def calculate_work_done(force, distance):
    return force * distance

def calculate_kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity ** 2

def calculate_potential_energy(mass, height, gravity=9.8):
    return mass * gravity * height

def calculate_momentum(mass, velocity):
    return mass * velocity

def calculate_impulse(force, time):
    return force * time

def calculate_power_work(work, time):
    return work / time

def calculate_power_voltage_current(voltage, current):
    return voltage * current

def calculate_resistance(voltage, current):
    return voltage / current

def calculate_capacitance(charge, voltage):
    return charge / voltage

def calculate_inductance(voltage, current_change, time):
    return voltage * time / current_change

def calculate_frequency(wavelength, wave_speed):
    return wave_speed / wavelength

def calculate_wave_speed(frequency, wavelength):
    return frequency * wavelength

def calculate_refractive_index(speed_of_light, speed_in_medium):
    return speed_of_light / speed_in_medium

def fetch_historical_weather_data(city, date):
    api_url = f"http://api.weather.com/v3/{city}/historical/{date}"
    response = requests.get(api_url)
    return response.json()