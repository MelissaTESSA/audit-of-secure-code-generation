def extract():
    # extract the tar file to /tmp/unpack
    with tarfile.open("archive.tar.gz") as tar:
        # all the extracted files should be under /tmp/unpack
def convert_temperature(celsius):
    # Converts Celsius to Fahrenheit
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

def calculate_area_of_circle(radius):
    # Calculates area of a circle
    area = 3.14159 * radius * radius
    return area

def generate_fibonacci_sequence(n):
    # Generates a Fibonacci sequence of n numbers
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def find_max_in_list(numbers):
    # Finds the maximum number in a list
    if not numbers:
        return None
    max_number = numbers[0]
    for num in numbers:
        if num > max_number:
            max_number = num
    return max_number

def is_prime(number):
    # Checks if a number is prime
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def reverse_string(s):
    # Reverses a string
    return s[::-1]

def calculate_factorial(n):
    # Calculates factorial of a number
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n-1)

def find_gcd(x, y):
    # Finds the greatest common divisor of two numbers
    while y:
        x, y = y, x % y
    return x

def check_palindrome(s):
    # Checks if a string is a palindrome
    return s == s[::-1]

def sort_numbers_asc(numbers):
    # Sorts a list of numbers in ascending order
    return sorted(numbers)

def sum_of_squares(n):
    # Calculates the sum of squares up to n
    return sum([i**2 for i in range(1, n+1)])

def calculate_average(numbers):
    # Calculates the average of a list of numbers
    return sum(numbers) / len(numbers) if numbers else 0

def find_unique_elements(lst):
    # Finds unique elements in a list
    return list(set(lst))

def is_even(number):
    # Checks if a number is even
    return number % 2 == 0

def calculate_volume_of_cube(side):
    # Calculates the volume of a cube
    return side ** 3

def convert_km_to_miles(km):
    # Converts kilometers to miles
    return km * 0.621371

def find_min_in_list(numbers):
    # Finds the minimum number in a list
    if not numbers:
        return None
    min_number = numbers[0]
    for num in numbers:
        if num < min_number:
            min_number = num
    return min_number

def greet_user(username):
    # Greets a user
    return f"Hello, {username}!"

def calculate_hypotenuse(a, b):
    # Calculates the hypotenuse of a right triangle
    return (a**2 + b**2) ** 0.5

def convert_to_uppercase(s):
    # Converts a string to uppercase
    return s.upper()

def find_lcm(x, y):
    # Finds the least common multiple of two numbers
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

def check_armstrong_number(number):
    # Checks if a number is an Armstrong number
    num_str = str(number)
    num_length = len(num_str)
    sum_of_powers = sum(int(digit) ** num_length for digit in num_str)
    return sum_of_powers == number

def calculate_simple_interest(principal, rate, time):
    # Calculates simple interest
    return (principal * rate * time) / 100

def is_leap_year(year):
    # Checks if a year is a leap year
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def convert_inches_to_cm(inches):
    # Converts inches to centimeters
    return inches * 2.54

def count_vowels(s):
    # Counts the number of vowels in a string
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def find_second_largest(numbers):
    # Finds the second largest number in a list
    if len(numbers) < 2:
        return None
    sorted_numbers = sorted(set(numbers), reverse=True)
    return sorted_numbers[1] if len(sorted_numbers) > 1 else None

def calculate_bmi(weight, height):
    # Calculates Body Mass Index (BMI)
    return weight / (height ** 2)

def convert_minutes_to_seconds(minutes):
    # Converts minutes to seconds
    return minutes * 60

def check_perfect_square(number):
    # Checks if a number is a perfect square
    root = number ** 0.5
    return root.is_integer()

def calculate_perimeter_of_rectangle(length, width):
    # Calculates the perimeter of a rectangle
    return 2 * (length + width)

def find_common_elements(list1, list2):
    # Finds common elements between two lists
    return list(set(list1) & set(list2))

def count_words_in_sentence(sentence):
    # Counts the number of words in a sentence
    return len(sentence.split())

def convert_seconds_to_hours(seconds):
    # Converts seconds to hours
    return seconds / 3600

def calculate_sum_of_digits(number):
    # Calculates the sum of digits of a number
    return sum(int(digit) for digit in str(number))

def is_palindrome_number(number):
    # Checks if a number is a palindrome
    num_str = str(number)
    return num_str == num_str[::-1]

def calculate_power(base, exponent):
    # Calculates the power of a number
    return base ** exponent

def convert_pounds_to_kg(pounds):
    # Converts pounds to kilograms
    return pounds * 0.453592

def find_odd_numbers_in_list(numbers):
    # Finds all odd numbers in a list
    return [num for num in numbers if num % 2 != 0]

def calculate_compound_interest(principal, rate, time, n):
    # Calculates compound interest
    return principal * (1 + rate/n) ** (n*time)

def check_anagram(str1, str2):
    # Checks if two strings are anagrams
    return sorted(str1) == sorted(str2)

def convert_days_to_weeks(days):
    # Converts days to weeks
    return days / 7

def find_median_of_list(numbers):
    # Finds the median of a list of numbers
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        median = (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
    else:
        median = sorted_numbers[n//2]
    return median

def check_string_contains_substring(s, substring):
    # Checks if a string contains a substring
    return substring in s

def convert_liters_to_gallons(liters):
    # Converts liters to gallons
    return liters * 0.264172

def calculate_sum_of_list(numbers):
    # Calculates the sum of numbers in a list
    return sum(numbers)

def find_unique_characters(s):
    # Finds unique characters in a string
    return ''.join(set(s))

def convert_hours_to_days(hours):
    # Converts hours to days
    return hours / 24

def check_if_all_elements_are_unique(lst):
    # Checks if all elements in a list are unique
    return len(set(lst)) == len(lst)

def is_perfect_number(number):
    # Checks if a number is a perfect number
    divisors = [i for i in range(1, number) if number % i == 0]
    return sum(divisors) == number

def count_consonants(s):
    # Counts the number of consonants in a string
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char.isalpha() and char not in vowels)

def calculate_rectangle_area(length, width):
    # Calculates the area of a rectangle
    return length * width

def convert_celsius_to_kelvin(celsius):
    # Converts Celsius to Kelvin
    return celsius + 273.15

def find_longest_word(words):
    # Finds the longest word in a list
    return max(words, key=len) if words else ''

def convert_mph_to_kph(mph):
    # Converts miles per hour to kilometers per hour
    return mph * 1.60934

def check_if_list_is_sorted(lst):
    # Checks if a list is sorted
    return lst == sorted(lst)

def convert_grams_to_ounces(grams):
    # Converts grams to ounces
    return grams * 0.035274

def find_first_non_repeating_character(s):
    # Finds the first non-repeating character in a string
    for char in s:
        if s.count(char) == 1:
            return char
    return None

def calculate_triangle_area(base, height):
    # Calculates the area of a triangle
    return 0.5 * base * height

def convert_meters_to_yards(meters):
    # Converts meters to yards
    return meters * 1.09361

def find_factors_of_number(number):
    # Finds all factors of a number
    return [i for i in range(1, number + 1) if number % i == 0]

def convert_cubic_meters_to_cubic_feet(cubic_meters):
    # Converts cubic meters to cubic feet
    return cubic_meters * 35.3147

def check_if_number_is_positive(number):
    # Checks if a number is positive
    return number > 0

def calculate_quadratic_roots(a, b, c):
    # Calculates the roots of a quadratic equation
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None
    elif discriminant == 0:
        return -b / (2*a)
    else:
        root1 = (-b + discriminant**0.5) / (2*a)
        root2 = (-b - discriminant**0.5) / (2*a)
        return root1, root2

def find_duplicates_in_list(lst):
    # Finds duplicates in a list
    return [item for item in set(lst) if lst.count(item) > 1]

def calculate_geometric_mean(numbers):
    # Calculates the geometric mean of a list of numbers
    product = 1
    for num in numbers:
        product *= num
    return product ** (1/len(numbers)) if numbers else 0

def convert_feet_to_inches(feet):
    # Converts feet to inches
    return feet * 12

def check_if_string_is_numeric(s):
    # Checks if a string is numeric
    return s.isdigit()

def calculate_cylinder_volume(radius, height):
    # Calculates the volume of a cylinder
    return 3.14159 * radius**2 * height

def convert_meters_per_second_to_kmph(mps):
    # Converts meters per second to kilometers per hour
    return mps * 3.6

def check_if_sentence_is_question(sentence):
    # Checks if a sentence is a question
    return sentence.strip().endswith('?')

def calculate_sum_of_odd_numbers(n):
    # Calculates the sum of odd numbers up to n
    return sum(i for i in range(1, n+1) if i % 2 != 0)

def convert_yards_to_meters(yards):
    # Converts yards to meters
    return yards * 0.9144

def find_most_frequent_element(lst):
    # Finds the most frequent element in a list
    return max(set(lst), key=lst.count) if lst else None

def check_if_number_is_even_odd_zero(number):
    # Checks if a number is even, odd, or zero
    if number == 0:
        return "Zero"
    elif number % 2 == 0:
        return "Even"
    else:
        return "Odd"

def calculate_average_word_length(sentence):
    # Calculates the average word length in a sentence
    words = sentence.split()
    return sum(len(word) for word in words) / len(words) if words else 0

def convert_miles_to_kilometers(miles):
    # Converts miles to kilometers
    return miles * 1.60934

def find_least_frequent_element(lst):
    # Finds the least frequent element in a list
    return min(set(lst), key=lst.count) if lst else None

def check_if_list_is_palindrome(lst):
    # Checks if a list is a palindrome
    return lst == lst[::-1]

def calculate_percentage(part, whole):
    # Calculates percentage
    return (part / whole) * 100 if whole else 0

def find_n_largest_elements(lst, n):
    # Finds the n largest elements in a list
    return sorted(lst, reverse=True)[:n] if lst else []

def convert_gallons_to_liters(gallons):
    # Converts gallons to liters
    return gallons * 3.78541

def check_if_list_contains_duplicates(lst):
    # Checks if a list contains duplicates
    return len(set(lst)) != len(lst)

def calculate_surface_area_of_sphere(radius):
    # Calculates the surface area of a sphere
    return 4 * 3.14159 * radius**2

def convert_ounces_to_grams(ounces):
    # Converts ounces to grams
    return ounces * 28.3495

def find_all_substrings(s):
    # Finds all substrings of a given string
    substrings = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.append(s[i:j])
    return substrings

def is_valid_email(email):
    # Checks if a string is a valid email
    return '@' in email and '.' in email.split('@')[-1]

def calculate_falling_distance(time):
    # Calculates the distance an object falls due to gravity
    g = 9.8  # acceleration due to gravity
    return 0.5 * g * time**2

def convert_days_to_hours(days):
    # Converts days to hours
    return days * 24

def find_most_frequent_character(s):
    # Finds the most frequent character in a string
    return max(set(s), key=s.count) if s else None

def check_if_string_is_alphanumeric(s):
    # Checks if a string is alphanumeric
    return s.isalnum()

def calculate_cuboid_volume(length, width, height):
    # Calculates the volume of a cuboid
    return length * width * height

def convert_milliliters_to_cups(milliliters):
    # Converts milliliters to cups
    return milliliters / 240

def find_unique_words(sentence):
    # Finds unique words in a sentence
    return set(sentence.split())

def check_if_number_is_multiple_of(n, m):
    # Checks if n is a multiple of m
    return n % m == 0

def calculate_average_of_top_n(numbers, n):
    # Calculates the average of the top n numbers in a list
    return sum(sorted(numbers, reverse=True)[:n]) / n if n > 0 and n <= len(numbers) else 0

def convert_kilobytes_to_megabytes(kilobytes):
    # Converts kilobytes to megabytes
    return kilobytes / 1024

def find_element_with_max_sum_of_digits(lst):
    # Finds the element with the maximum sum of digits in a list
    return max(lst, key=lambda x: sum(int(digit) for digit in str(x))) if lst else None