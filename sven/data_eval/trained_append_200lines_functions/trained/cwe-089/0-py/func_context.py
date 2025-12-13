# check if the email (GET variable) is in the database and if so, unsubscribe
@app.route('/unsubscribe')
def unsubscribe():
    # get the email (GET variable)
    email = request.args.get('email')
    # get the database connection
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
def calculate_square_root(x):
    return x ** 0.5

def reverse_string(s):
    return s[::-1]

def convert_to_uppercase(text):
    return text.upper()

def find_maximum(nums):
    return max(nums)

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def calculate_area_of_circle(radius):
    return 3.14159 * radius * radius

def sort_list(lst):
    return sorted(lst)

def calculate_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_minimum(nums):
    return min(nums)

def is_palindrome(s):
    return s == s[::-1]

def calculate_power(base, exp):
    return base ** exp

def merge_dictionaries(dict1, dict2):
    res = dict1.copy()
    res.update(dict2)
    return res

def calculate_average(nums):
    return sum(nums) / len(nums)

def generate_fibonacci_series(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]

def calculate_perimeter_of_rectangle(length, width):
    return 2 * (length + width)

def convert_to_lowercase(text):
    return text.lower()

def calculate_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def calculate_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def calculate_factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def find_longest_word(words):
    return max(words, key=len)

def count_occurrences(word, char):
    return word.count(char)

def convert_list_to_set(lst):
    return set(lst)

def calculate_hypotenuse(a, b):
    return (a**2 + b**2) ** 0.5

def convert_kilometers_to_miles(km):
    return km * 0.621371

def convert_miles_to_kilometers(miles):
    return miles / 0.621371

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def check_even_odd(num):
    return "Even" if num % 2 == 0 else "Odd"

def calculate_circle_circumference(radius):
    return 2 * 3.14159 * radius

def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def find_second_largest(nums):
    first, second = float('-inf'), float('-inf')
    for n in nums:
        if n > first:
            first, second = n, first
        elif n > second:
            second = n
    return second

def calculate_lcm(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    return abs(a * b) // gcd(a, b)

def remove_duplicates_from_list(lst):
    return list(dict.fromkeys(lst))

def calculate_sum_of_squares(nums):
    return sum(x**2 for x in nums)

def reverse_list(lst):
    return lst[::-1]

def check_armstrong_number(num):
    digits = [int(d) for d in str(num)]
    return num == sum(d**len(digits) for d in digits)

def count_words_in_sentence(sentence):
    return len(sentence.split())

def check_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False

def calculate_modulus(a, b):
    return a % b

def filter_even_numbers(nums):
    return [num for num in nums if num % 2 == 0]

def sum_of_even_numbers(nums):
    return sum(num for num in nums if num % 2 == 0)

def calculate_mean(nums):
    return sum(nums) / len(nums)

def calculate_median(nums):
    nums.sort()
    mid = len(nums) // 2
    if len(nums) % 2 == 0:
        return (nums[mid - 1] + nums[mid]) / 2
    else:
        return nums[mid]

def calculate_mode(nums):
    from collections import Counter
    count = Counter(nums)
    max_count = max(count.values())
    return [k for k, v in count.items() if v == max_count]

def sort_dict_by_key(d):
    return dict(sorted(d.items()))

def calculate_interest(principal, rate, time):
    return principal * (1 + (rate / 100) * time)

def calculate_compound_interest(principal, rate, time, n):
    return principal * ((1 + (rate / (100 * n))) ** (n * time))

def calculate_standard_deviation(nums):
    mean = sum(nums) / len(nums)
    variance = sum((x - mean) ** 2 for x in nums) / len(nums)
    return variance ** 0.5

def calculate_variance(nums):
    mean = sum(nums) / len(nums)
    return sum((x - mean) ** 2 for x in nums) / len(nums)

def calculate_geometric_mean(nums):
    import math
    product = math.prod(nums)
    return product ** (1 / len(nums))

def calculate_harmonic_mean(nums):
    return len(nums) / sum(1 / x for x in nums)

def generate_primes_up_to_n(n):
    primes = []
    for num in range(2, n + 1):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            primes.append(num)
    return primes

def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

def remove_vowels_from_string(s):
    vowels = "aeiouAEIOU"
    return ''.join(char for char in s if char not in vowels)

def check_perfect_square(n):
    root = int(n ** 0.5)
    return root * root == n

def calculate_pythagorean_triplet(a, b):
    c = (a**2 + b**2) ** 0.5
    return c.is_integer()

def calculate_sum_of_list(lst):
    return sum(lst)

def encrypt_string(s, shift):
    encrypted = []
    for char in s:
        if char.isalpha():
            shift_base = ord('a') if char.islower() else ord('A')
            encrypted.append(chr(shift_base + (ord(char) - shift_base + shift) % 26))
        else:
            encrypted.append(char)
    return ''.join(encrypted)

def decrypt_string(s, shift):
    return encrypt_string(s, -shift)

def calculate_sum_of_digits(num):
    return sum(int(d) for d in str(num))

def find_unique_elements(lst):
    return list(set(lst))

def check_strong_number(num):
    def factorial(n):
        return 1 if n == 0 else n * factorial(n - 1)
    return num == sum(factorial(int(d)) for d in str(num))

def calculate_sum_of_cubes(nums):
    return sum(x**3 for x in nums)

def convert_list_to_string(lst):
    return ''.join(map(str, lst))

def calculate_distance_between_points(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

def check_harshad_number(num):
    return num % sum(int(d) for d in str(num)) == 0

def calculate_sum_of_odd_numbers(nums):
    return sum(num for num in nums if num % 2 != 0)

def generate_pascals_triangle(n):
    triangle = [[1] * (i + 1) for i in range(n)]
    for i in range(2, n):
        for j in range(1, i):
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    return triangle

def convert_decimal_to_binary(n):
    return bin(n)[2:]

def convert_binary_to_decimal(b):
    return int(b, 2)

def convert_decimal_to_hexadecimal(n):
    return hex(n)[2:]

def convert_hexadecimal_to_decimal(h):
    return int(h, 16)

def convert_decimal_to_octal(n):
    return oct(n)[2:]

def convert_octal_to_decimal(o):
    return int(o, 8)

def calculate_nth_root(value, n):
    return value ** (1/n)

def check_perfect_number(num):
    return num == sum(i for i in range(1, num) if num % i == 0)

def generate_random_number_between(a, b):
    import random
    return random.randint(a, b)

def convert_string_to_list(s):
    return list(s)

def find_largest_element(lst):
    return max(lst)

def find_smallest_element(lst):
    return min(lst)

def swap_values(a, b):
    return b, a

def calculate_volume_of_cylinder(radius, height):
    return 3.14159 * radius * radius * height

def calculate_surface_area_of_cylinder(radius, height):
    return 2 * 3.14159 * radius * (radius + height)

def calculate_volume_of_sphere(radius):
    return (4/3) * 3.14159 * radius ** 3

def calculate_surface_area_of_sphere(radius):
    return 4 * 3.14159 * radius ** 2

def calculate_volume_of_cone(radius, height):
    return (1/3) * 3.14159 * radius ** 2 * height

def calculate_surface_area_of_cone(radius, height):
    return 3.14159 * radius * (radius + (height ** 2 + radius ** 2) ** 0.5)

def calculate_volume_of_cube(side):
    return side ** 3

def calculate_surface_area_of_cube(side):
    return 6 * side ** 2

def calculate_volume_of_cuboid(length, width, height):
    return length * width * height

def calculate_surface_area_of_cuboid(length, width, height):
    return 2 * (length * width + width * height + height * length)

def count_occurrences_in_list(lst, item):
    return lst.count(item)

def remove_element_from_list(lst, item):
    return [x for x in lst if x != item]

def convert_string_to_integer(s):
    try:
        return int(s)
    except ValueError:
        return None

def convert_integer_to_string(n):
    return str(n)

def convert_list_to_tuple(lst):
    return tuple(lst)

def convert_tuple_to_list(tpl):
    return list(tpl)

def check_valid_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

def find_intersection_of_lists(list1, list2):
    return list(set(list1) & set(list2))

def find_union_of_lists(list1, list2):
    return list(set(list1) | set(list2))

def find_difference_of_lists(list1, list2):
    return list(set(list1) - set(list2))

def convert_cm_to_inches(cm):
    return cm / 2.54

def convert_inches_to_cm(inches):
    return inches * 2.54

def calculate_sum_of_natural_numbers(n):
    return n * (n + 1) // 2

def calculate_product_of_list(lst):
    result = 1
    for num in lst:
        result *= num
    return result

def calculate_difference_between_dates(date1, date2):
    from datetime import datetime
    d1 = datetime.strptime(date1, "%Y-%m-%d")
    d2 = datetime.strptime(date2, "%Y-%m-%d")
    return (d2 - d1).days

def get_day_of_week(date):
    from datetime import datetime
    return datetime.strptime(date, "%Y-%m-%d").strftime("%A")

def find_nth_fibonacci_number(n):
    if n <= 1:
        return n
    return find_nth_fibonacci_number(n - 1) + find_nth_fibonacci_number(n - 2)

def calculate_average_word_length(sentence):
    words = sentence.split()
    return sum(len(word) for word in words) / len(words)

def check_valid_email(email):
    import re
    pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    return re.match(pattern, email) is not None

def check_valid_ipv4_address(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit() or not 0 <= int(part) <= 255:
            return False
    return True

def calculate_days_in_month(year, month):
    import calendar
    return calendar.monthrange(year, month)[1]

def convert_string_to_float(s):
    try:
        return float(s)
    except ValueError:
        return None

def convert_float_to_string(f):
    return str(f)

def capitalize_first_letter_of_each_word(sentence):
    return ' '.join(word.capitalize() for word in sentence.split())

def check_valid_password(password):
    import re
    if len(password) < 8:
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[@$!%*?&#]", password):
        return False
    return True

def check_valid_url(url):
    import re
    pattern = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(pattern, url) is not None

def calculate_discounted_price(price, discount):
    return price - (price * (discount / 100))