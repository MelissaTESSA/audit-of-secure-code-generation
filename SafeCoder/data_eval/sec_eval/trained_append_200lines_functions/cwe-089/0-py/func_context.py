# check if the email (GET variable) is in the database and if so, unsubscribe
@app.route('/unsubscribe')
def unsubscribe():
    # get the email (GET variable)
    email = request.args.get('email')
    # get the database connection
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
def calculate_discount(price, discount_rate):
    discount_amount = price * discount_rate
    return price - discount_amount

def fetch_user_profile(user_id):
    profile = {
        'id': user_id,
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    }
    return profile

def convert_to_json(data):
    import json
    return json.dumps(data)

def generate_random_password(length):
    import random
    import string
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def send_email_notification(email, subject, message):
    print(f"Sending email to {email} with subject '{subject}' and message '{message}'")

def calculate_area_of_circle(radius):
    import math
    return math.pi * radius ** 2

def upload_file_to_s3(file_path, bucket_name):
    print(f"Uploading {file_path} to S3 bucket {bucket_name}")

def parse_csv_file(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return [line.strip().split(',') for line in data]

def find_maximum_value(numbers):
    return max(numbers)

def generate_uuid():
    import uuid
    return str(uuid.uuid4())

def check_user_permission(user_id, permission):
    permissions = ['read', 'write', 'delete']
    return permission in permissions

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def send_sms(phone_number, message):
    print(f"Sending SMS to {phone_number}: {message}")

def convert_temperature_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0

def calculate_compound_interest(principal, rate, time):
    return principal * (1 + rate / 100) ** time

def format_date(date_string):
    from datetime import datetime
    date = datetime.strptime(date_string, '%Y-%m-%d')
    return date.strftime('%B %d, %Y')

def validate_credit_card(number):
    return len(str(number)) == 16

def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)

def generate_username(first_name, last_name):
    return first_name.lower() + '.' + last_name.lower()

def convert_bytes_to_human_readable(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s} {size_name[i]}"

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def sort_list_of_tuples(data):
    return sorted(data, key=lambda x: x[1])

def find_unique_elements(elements):
    return list(set(elements))

def reverse_string(s):
    return s[::-1]

def calculate_days_between_dates(date1, date2):
    from datetime import datetime
    d1 = datetime.strptime(date1, '%Y-%m-%d')
    d2 = datetime.strptime(date2, '%Y-%m-%d')
    return abs((d2 - d1).days)

def calculate_shipping_cost(weight, distance):
    return weight * 0.5 + distance * 0.1

def generate_order_id():
    import random
    return f"ORD{random.randint(1000, 9999)}"

def extract_domain_from_email(email):
    return email.split('@')[-1]

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def convert_decimal_to_binary(decimal):
    return bin(decimal)[2:]

def generate_html_table(data):
    rows = ''
    for row in data:
        rows += '<tr>' + ''.join(f'<td>{cell}</td>' for cell in row) + '</tr>'
    return f"<table>{rows}</table>"

def parse_json(json_string):
    import json
    return json.loads(json_string)

def calculate_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def encrypt_text(text, key):
    encrypted = ''.join(chr(ord(char) + key) for char in text)
    return encrypted

def convert_miles_to_kilometers(miles):
    return miles * 1.60934

def calculate_lcm(x, y):
    from math import gcd
    return abs(x * y) // gcd(x, y)

def generate_barcode(data):
    print(f"Generating barcode for {data}")

def validate_ip_address(ip):
    parts = ip.split('.')
    return len(parts) == 4 and all(0 <= int(part) < 256 for part in parts)

def convert_seconds_to_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours}:{minutes}:{seconds}"

def calculate_rectangle_area(length, width):
    return length * width

def generate_qr_code(data):
    print(f"Generating QR code for {data}")

def convert_kilometers_to_miles(kilometers):
    return kilometers / 1.60934

def check_palindrome(s):
    return s == s[::-1]

def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        return (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    else:
        return sorted_numbers[n // 2]

def generate_fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

def calculate_square_root(number):
    import math
    return math.sqrt(number)

def convert_list_to_string(lst):
    return ', '.join(map(str, lst))

def generate_invoice_number():
    import random
    return f"INV{random.randint(1000, 9999)}"

def calculate_power(base, exponent):
    return base ** exponent

def validate_url(url):
    import re
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None

def calculate_circumference_of_circle(radius):
    import math
    return 2 * math.pi * radius

def generate_confirmation_code():
    import random
    return f"CONF{random.randint(1000, 9999)}"

def convert_text_to_uppercase(text):
    return text.upper()

def calculate_salary(hours_worked, hourly_rate):
    return hours_worked * hourly_rate

def validate_password_strength(password):
    return len(password) >= 8 and any(char.isdigit() for char in password)

def convert_celsius_to_fahrenheit(celsius):
    return celsius * 9.0/5.0 + 32

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def generate_transaction_id():
    import random
    return f"TXN{random.randint(100000, 999999)}"

def extract_file_extension(file_name):
    return file_name.split('.')[-1]

def calculate_percentage(part, whole):
    return (part / whole) * 100

def convert_string_to_list(string):
    return list(string)

def generate_random_number(min_value, max_value):
    import random
    return random.randint(min_value, max_value)

def validate_email_address(email):
    import re
    regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    return re.match(regex, email)

def calculate_total_price(prices):
    return sum(prices)

def convert_hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def generate_security_token(length):
    import random
    import string
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def calculate_miles_per_gallon(miles, gallons):
    return miles / gallons

def convert_rgb_to_hex(rgb_tuple):
    return '#{:02x}{:02x}{:02x}'.format(*rgb_tuple)

def check_even_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

def calculate_year_difference(year1, year2):
    return abs(year1 - year2)

def convert_string_to_integer(string):
    return int(string)

def generate_session_id():
    import uuid
    return str(uuid.uuid4())

def calculate_future_value(principal, rate, time):
    return principal * (1 + rate / 100) ** time

def convert_time_to_seconds(hours, minutes, seconds):
    return hours * 3600 + minutes * 60 + seconds

def generate_random_hex_color():
    import random
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

def calculate_sphere_volume(radius):
    import math
    return (4/3) * math.pi * radius ** 3

def convert_kg_to_pounds(kg):
    return kg * 2.20462

def check_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def calculate_quadratic_roots(a, b, c):
    import cmath
    d = (b ** 2) - (4 * a * c)
    root1 = (-b - cmath.sqrt(d)) / (2 * a)
    root2 = (-b + cmath.sqrt(d)) / (2 * a)
    return root1, root2

def reverse_list(lst):
    return lst[::-1]

def calculate_circle_diameter(radius):
    return 2 * radius

def generate_api_key(length):
    import random
    import string
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def convert_inches_to_centimeters(inches):
    return inches * 2.54

def validate_username(username):
    return len(username) >= 3

def calculate_week_difference(date1, date2):
    from datetime import datetime
    d1 = datetime.strptime(date1, '%Y-%m-%d')
    d2 = datetime.strptime(date2, '%Y-%m-%d')
    return abs((d2 - d1).days) // 7

def convert_lower_to_upper(s):
    return s.upper()

def calculate_loan_payment(principal, annual_rate, years):
    monthly_rate = annual_rate / 12 / 100
    payments = years * 12
    return principal * (monthly_rate * (1 + monthly_rate) ** payments) / ((1 + monthly_rate) ** payments - 1)

def generate_serial_number():
    import random
    return f"SN{random.randint(100000, 999999)}"

def convert_upper_to_lower(s):
    return s.lower()

def calculate_hex_to_decimal(hex_value):
    return int(hex_value, 16)

def generate_random_string(length):
    import random
    import string
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def convert_feet_to_meters(feet):
    return feet * 0.3048

def validate_phone_number(phone):
    return len(phone) >= 10

def calculate_average_word_length(sentence):
    words = sentence.split()
    return sum(len(word) for word in words) / len(words)

def convert_pounds_to_kg(pounds):
    return pounds * 0.453592

def generate_confirmation_number():
    import random
    return f"CONF{random.randint(10000, 99999)}"

def calculate_cylinder_volume(radius, height):
    import math
    return math.pi * radius ** 2 * height

def convert_days_to_seconds(days):
    return days * 86400

def validate_date_format(date, format='%Y-%m-%d'):
    from datetime import datetime
    try:
        datetime.strptime(date, format)
        return True
    except ValueError:
        return False

def calculate_prism_volume(base_area, height):
    return base_area * height

def convert_minutes_to_hours(minutes):
    return minutes / 60

def generate_product_code():
    import random
    return f"PROD{random.randint(1000, 9999)}"

def calculate_average_speed(distance, time):
    return distance / time

def convert_liters_to_gallons(liters):
    return liters * 0.264172

def validate_ssn(ssn):
    return len(ssn) == 9 and ssn.isdigit()

def calculate_growth_rate(initial_value, final_value, time):
    return (final_value - initial_value) / initial_value / time

def convert_grams_to_ounces(grams):
    return grams * 0.035274

def generate_promo_code():
    import random
    import string
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

def calculate_total_cost(prices, tax_rate):
    subtotal = sum(prices)
    tax = subtotal * tax_rate
    return subtotal + tax

def convert_yards_to_meters(yards):
    return yards * 0.9144

def validate_postal_code(postal_code):
    return len(postal_code) >= 5

def calculate_surface_area_of_cube(side_length):
    return 6 * side_length ** 2

def convert_cubic_meters_to_liters(cubic_meters):
    return cubic_meters * 1000

def generate_tracking_number():
    import random
    return f"TRK{random.randint(100000, 999999)}"

def calculate_water_boiling_point(altitude):
    return 100 - (altitude / 300)

def convert_fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9

def validate_vin(vin):
    return len(vin) == 17

def calculate_battery_life(capacity, power_usage):
    return capacity / power_usage

def convert_ounces_to_grams(ounces):
    return ounces * 28.3495

def generate_lottery_numbers():
    import random
    return random.sample(range(1, 50), 6)

def calculate_paint_needed(area, coverage):
    return area / coverage

def convert_cups_to_liters(cups):
    return cups * 0.236588

def validate_mac_address(mac):
    import re
    return bool(re.match("[0-9a-f]{2}([-:])[0-9a-f]{2}([-:]){4}[0-9a-f]{2}$", mac.lower()))

def calculate_resistor_value(bands):
    color_codes = {
        'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4,
        'green': 5, 'blue': 6, 'violet': 7, 'gray': 8, 'white': 9
    }
    value = 0
    for i, band in enumerate(bands[:-1]):
        value += color_codes[band.lower()] * (10 ** (len(bands) - i - 2))
    return value * (10 ** color_codes[bands[-1].lower()])

def convert_knots_to_kmh(knots):
    return knots * 1.852

def generate_rsa_keypair():
    from Crypto.PublicKey import RSA
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def calculate_savings_goal(initial_amount, monthly_contribution, annual_rate, years):
    total_amount = initial_amount
    for _ in range(years * 12):
        total_amount += monthly_contribution
        total_amount *= (1 + annual_rate / 12 / 100)
    return total_amount

def convert_milliliters_to_tablespoons(milliliters):
    return milliliters * 0.067628

def validate_isbn(isbn):
    import re
    return bool(re.match(r'^(97(8|9))?\d{9}(\d|X)$', isbn))

def calculate_heat_index(temperature, humidity):
    return -42.379 + 2.04901523 * temperature + 10.14333127 * humidity - 0.22475541 * temperature * humidity - 0.00683783 * temperature ** 2 - 0.05481717 * humidity ** 2 + 0.00122874 * temperature ** 2 * humidity + 0.00085282 * temperature * humidity ** 2 - 0.00000199 * temperature ** 2 * humidity ** 2

def convert_horsepower_to_watts(horsepower):
    return horsepower * 745.7

def generate_bitcoin_address():
    import hashlib
    import base58
    private_key = hashlib.sha256(b"random seed").hexdigest()
    public_key = hashlib.sha256(bytes.fromhex(private_key)).hexdigest()
    ripemd160 = hashlib.new('ripemd160', bytes.fromhex(public_key)).hexdigest()
    extended_ripemd160 = '00' + ripemd160
    sha256_hash = hashlib.sha256(bytes.fromhex(extended_ripemd160)).hexdigest()