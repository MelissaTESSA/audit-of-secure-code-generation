# -*- coding: utf-8 -*-
'''
Wrapper around Server Density API
=================================

.. versionadded:: 2014.7.0
'''
import requests
import json
import logging

from salt.exceptions import CommandExecutionError

log = logging.getLogger(__name__)


def get_sd_auth(val, sd_auth_pillar_name='serverdensity'):
    '''
    Returns requested Server Density authentication value from pillar.

    CLI Example:

    .. code-block:: bash

        salt '*' serverdensity_device.get_sd_auth <val>
    '''
    sd_pillar = __pillar__.get(sd_auth_pillar_name)
    log.debug('Server Density Pillar: {0}'.format(sd_pillar))
    if not sd_pillar:
        log.error('Cloud not load {0} pillar'.format(sd_auth_pillar_name))
        raise CommandExecutionError(
            '{0} pillar is required for authentication'.format(sd_auth_pillar_name)
        )

    try:
        return sd_pillar[val]
    except KeyError:
        log.error('Cloud not find value {0} in pillar'.format(val))
        raise CommandExecutionError('{0} value was not found in pillar'.format(val))


def _clean_salt_variables(params, variable_prefix="__"):
    '''
    Pops out variables from params which starts with `variable_prefix`.
    '''
    map(params.pop, [k for k in params if k.startswith(variable_prefix)])
    return params


def create(name, **params):
    '''
    Function to create device in Server Density. For more info, see the `API
    docs`__.

    .. __: https://apidocs.serverdensity.com/Inventory/Devices/Creating

    CLI Example:

    .. code-block:: bash

        salt '*' serverdensity_device.create lama
        salt '*' serverdensity_device.create rich_lama group=lama_band installedRAM=32768
    '''
    log.debug('Server Density params: {0}'.format(params))
    params = _clean_salt_variables(params)

    params['name'] = name
    api_response = requests.post(
        'https://api.serverdensity.io/inventory/devices/',
        params={'token': get_sd_auth('api_token')},
        data=params
    )
    log.debug('Server Density API Response: {0}'.format(api_response))
    log.debug('Server Density API Response content: {0}'.format(api_response.content))
    if api_response.status_code == 200:
        try:
            return json.loads(api_response.content)
        except ValueError:
            log.error('Could not parse API Response content: {0}'.format(api_response.content))
            raise CommandExecutionError(
                'Failed to create, API Response: {0}'.format(api_response)
            )
    else:
        return None


def delete(device_id):
    '''
    Delete a device from Server Density. For more information, see the `API
    docs`__.

    .. __: https://apidocs.serverdensity.com/Inventory/Devices/Deleting

    CLI Example:

    .. code-block:: bash

        salt '*' serverdensity_device.delete 51f7eafcdba4bb235e000ae4
    '''
    api_response = requests.delete(
        'https://api.serverdensity.io/inventory/devices/' + device_id,
        params={'token': get_sd_auth('api_token')}
    )
    log.debug('Server Density API Response: {0}'.format(api_response))
    log.debug('Server Density API Response content: {0}'.format(api_response.content))
    if api_response.status_code == 200:
        try:
            return json.loads(api_response.content)
        except ValueError:
            log.error('Could not parse API Response content: {0}'.format(api_response.content))
            raise CommandExecutionError(
                'Failed to create, API Response: {0}'.format(api_response)
            )
    else:
        return None


def ls(**params):
    '''
    List devices in Server Density

    Results will be filtered by any params passed to this function. For more
    information, see the API docs on listing_ and searching_.

    .. _listing: https://apidocs.serverdensity.com/Inventory/Devices/Listing
    .. _searching: https://apidocs.serverdensity.com/Inventory/Devices/Searching

    CLI Example:

    .. code-block:: bash

        salt '*' serverdensity_device.ls
        salt '*' serverdensity_device.ls name=lama
        salt '*' serverdensity_device.ls name=lama group=lama_band installedRAM=32768
    '''
    params = _clean_salt_variables(params)

    endpoint = 'devices'

    # Change endpoint if there are params to filter by:
    if params:
        endpoint = 'resources'

    # Convert all ints to strings:
    for k, v in params.items():
        params[k] = str(v)

    api_response = requests.get(
        'https://api.serverdensity.io/inventory/{0}'.format(endpoint),
        params={'token': get_sd_auth('api_token'), 'filter': json.dumps(params)}
    )
    log.debug('Server Density API Response: {0}'.format(api_response))
    log.debug('Server Density API Response content: {0}'.format(api_response.content))
    if api_response.status_code == 200:
        try:
            return json.loads(api_response.content)
        except ValueError:
            log.error(
                'Could not parse Server Density API Response content: {0}'
                .format(api_response.content)
            )
            raise CommandExecutionError(
                'Failed to create, Server Density API Response: {0}'
                .format(api_response)
            )
    else:
        return None


def update(device_id, **params):
    '''
    Updates device information in Server Density. For more information see the
    `API docs`__.

    .. __: https://apidocs.serverdensity.com/Inventory/Devices/Updating

    CLI Example:

    .. code-block:: bash

        salt '*' serverdensity_device.update 51f7eafcdba4bb235e000ae4 name=lama group=lama_band
        salt '*' serverdensity_device.update 51f7eafcdba4bb235e000ae4 name=better_lama group=rock_lamas swapSpace=512
    '''
    params = _clean_salt_variables(params)

    api_response = requests.put(
        'https://api.serverdensity.io/inventory/devices/' + device_id,
        params={'token': get_sd_auth('api_token')},
        data=params
    )
    log.debug('Server Density API Response: {0}'.format(api_response))
    log.debug('Server Density API Response content: {0}'.format(api_response.content))
    if api_response.status_code == 200:
        try:
            return json.loads(api_response.content)
        except ValueError:
            log.error(
                'Could not parse Server Density API Response content: {0}'
                .format(api_response.content)
            )
            raise CommandExecutionError(
                'Failed to create, API Response: {0}'.format(api_response)
            )
    else:
        return None


def install_agent(agent_key):
    '''
    Function downloads Server Density installation agent, and installs sd-agent
    with agent_key.

    CLI Example:

    .. code-block:: bash

        salt '*' serverdensity_device.install_agent c2bbdd6689ff46282bdaa07555641498
    '''
    work_dir = '/tmp/'
    account_url = get_sd_auth('account_url')

    __salt__['cmd.run'](
        cmd='curl https://www.serverdensity.com/downloads/agent-install.sh -o install.sh',
        cwd=work_dir
    )
    __salt__['cmd.run'](cmd='chmod +x install.sh', cwd=work_dir)

    return __salt__['cmd.run'](
        cmd='./install.sh -a {account_url} -k {agent_key}'.format(
            account_url=account_url, agent_key=agent_key),
        cwd=work_dir
    )


import math
import random
import datetime

def calculate_area_of_circle(radius):
    return math.pi * (radius ** 2)

def generate_random_string(length):
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(length))

def get_current_datetime():
    return datetime.datetime.now()

def convert_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0

def calculate_factorial(number):
    if number == 0:
        return 1
    else:
        return number * calculate_factorial(number-1)

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def sort_list_of_strings(strings_list):
    return sorted(strings_list)

def find_max_in_list(numbers):
    return max(numbers)

def reverse_string(s):
    return s[::-1]

def calculate_square_root(number):
    return math.sqrt(number)

def generate_even_numbers(n):
    return [x for x in range(2, n+1, 2)]

def get_day_of_week(date):
    return date.strftime("%A")

def convert_celsius_to_fahrenheit(celsius):
    return celsius * 9.0/5.0 + 32

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def check_palindrome(s):
    return s == s[::-1]

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def calculate_power(base, exponent):
    return base ** exponent

def get_unique_elements(lst):
    return list(set(lst))

def get_fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def get_random_choice(choices):
    return random.choice(choices)

def flatten_nested_list(nested_list):
    return [item for sublist in nested_list for item in sublist]

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def get_vowels_in_string(s):
    return [char for char in s if char in 'aeiou']

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

def calculate_lcm(a, b):
    return abs(a*b) // find_gcd(a, b)

def convert_list_to_dict(keys, values):
    return dict(zip(keys, values))

def get_intersection_of_sets(set1, set2):
    return set1 & set2

def capitalize_words(s):
    return ' '.join(word.capitalize() for word in s.split())

def is_power_of_two(n):
    return (n != 0) and (n & (n - 1)) == 0

def get_second_largest(numbers):
    return sorted(set(numbers))[-2]

def calculate_perimeter_of_rectangle(length, width):
    return 2 * (length + width)

def filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

def generate_fibonacci_up_to_n(n):
    sequence = [0, 1]
    while sequence[-1] < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:-1]

def find_longest_word_in_list(words):
    return max(words, key=len)

def calculate_sum_of_squares(numbers):
    return sum(x ** 2 for x in numbers)

def get_consonants_in_string(s):
    return [char for char in s if char.isalpha() and char not in 'aeiou']

def calculate_area_of_triangle(base, height):
    return 0.5 * base * height

def find_duplicates_in_list(lst):
    return [item for item in set(lst) if lst.count(item) > 1]

def is_valid_email(email):
    return '@' in email and '.' in email.split('@')[-1]

def convert_kilometers_to_miles(kilometers):
    return kilometers * 0.621371

def get_unique_characters_in_string(s):
    return list(set(s))

def calculate_percentage(part, whole):
    return (part / whole) * 100

def get_squares_of_numbers(numbers):
    return [x ** 2 for x in numbers]

def get_date_n_days_ago(n):
    return datetime.datetime.now() - datetime.timedelta(days=n)

def convert_miles_to_kilometers(miles):
    return miles / 0.621371

def find_min_in_list(numbers):
    return min(numbers)

def get_common_elements(list1, list2):
    return list(set(list1) & set(list2))

def calculate_area_of_square(side):
    return side ** 2

def is_palindrome_number(number):
    return str(number) == str(number)[::-1]

def generate_odd_numbers(n):
    return [x for x in range(1, n+1, 2)]

def get_month_name_from_number(month_number):
    return datetime.date(1900, month_number, 1).strftime('%B')

def calculate_hypotenuse(a, b):
    return math.sqrt(a ** 2 + b ** 2)

def get_last_element_of_list(lst):
    return lst[-1] if lst else None

def calculate_area_of_parallelogram(base, height):
    return base * height

def find_common_prefix(strings):
    if not strings:
        return ""
    shortest = min(strings, key=len)
    for i, char in enumerate(shortest):
        if any(other[i] != char for other in strings):
            return shortest[:i]
    return shortest

def convert_seconds_to_hours(seconds):
    return seconds / 3600.0

def get_random_even_number(n):
    return random.choice([x for x in range(2, n+1, 2)])

def calculate_circumference_of_circle(radius):
    return 2 * math.pi * radius

def get_middle_character(s):
    return s[(len(s) - 1) // 2:(len(s) + 2) // 2]

def calculate_area_of_trapezoid(base1, base2, height):
    return ((base1 + base2) / 2) * height

def get_unique_words_in_sentence(sentence):
    return set(sentence.split())

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def generate_random_float(min_value, max_value):
    return random.uniform(min_value, max_value)

def get_ascii_value_of_char(char):
    return ord(char)

def calculate_modulus(a, b):
    return a % b

def get_days_between_dates(date1, date2):
    return abs((date2 - date1).days)

def convert_inches_to_centimeters(inches):
    return inches * 2.54

def capitalize_first_and_last_character(s):
    if len(s) < 2:
        return s.upper()
    return s[0].upper() + s[1:-1] + s[-1].upper()

def get_odd_numbers_from_list(numbers):
    return [num for num in numbers if num % 2 != 0]

def get_random_odd_number(n):
    return random.choice([x for x in range(1, n+1, 2)])

def calculate_sum_of_cubes(numbers):
    return sum(x ** 3 for x in numbers)

def convert_list_to_tuple(lst):
    return tuple(lst)

def get_ascii_sum_of_string(s):
    return sum(ord(char) for char in s)

def get_n_largest_numbers(numbers, n):
    return sorted(numbers, reverse=True)[:n]

def convert_celsius_to_kelvin(celsius):
    return celsius + 273.15

def get_leap_years_between(year1, year2):
    return [year for year in range(year1, year2 + 1) if is_leap_year(year)]

def calculate_area_of_ellipse(a, b):
    return math.pi * a * b

def get_first_element_of_list(lst):
    return lst[0] if lst else None

def generate_random_odd_numbers(n):
    return [random.choice(range(1, 100, 2)) for _ in range(n)]

def calculate_area_of_rhombus(diagonal1, diagonal2):
    return (diagonal1 * diagonal2) / 2

def get_even_indexed_elements(lst):
    return [lst[i] for i in range(len(lst)) if i % 2 == 0]

def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2.0
    else:
        return sorted_numbers[mid]

def get_random_vowel():
    return random.choice('aeiou')

def calculate_volume_of_cylinder(radius, height):
    return math.pi * radius ** 2 * height

def get_days_in_month(year, month):
    return (datetime.date(year, month % 12 + 1, 1) - datetime.timedelta(days=1)).day

def calculate_area_of_polygon(sides, side_length):
    return (sides * side_length ** 2) / (4 * math.tan(math.pi / sides))

def get_even_numbers_from_list(numbers):
    return [num for num in numbers if num % 2 == 0]

def get_ascii_values_of_string(s):
    return [ord(char) for char in s]

def find_most_frequent_element(lst):
    return max(set(lst), key=lst.count)

def get_n_smallest_numbers(numbers, n):
    return sorted(numbers)[:n]

def calculate_volume_of_sphere(radius):
    return (4/3) * math.pi * radius ** 3

def get_unique_elements_in_order(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

def calculate_area_of_sector(radius, angle):
    return (angle / 360.0) * math.pi * radius ** 2

def convert_pounds_to_kilograms(pounds):
    return pounds * 0.453592

def get_longest_word_in_string(s):
    words = s.split()
    return max(words, key=len) if words else ""

def generate_random_prime_number(n):
    primes = [x for x in range(2, n) if is_prime(x)]
    return random.choice(primes) if primes else None

def calculate_volume_of_cone(radius, height):
    return (1/3) * math.pi * radius ** 2 * height

def get_words_starting_with_vowel(sentence):
    return [word for word in sentence.split() if word[0].lower() in 'aeiou']

def calculate_surface_area_of_cylinder(radius, height):
    return 2 * math.pi * radius * (radius + height)

def get_unique_characters_in_order(s):
    seen = set()
    return ''.join([x for x in s if not (x in seen or seen.add(x))])

def calculate_surface_area_of_sphere(radius):
    return 4 * math.pi * radius ** 2

def get_max_length_of_words(sentence):
    return max(len(word) for word in sentence.split())

def generate_random_matrix(rows, cols):
    return [[random.randint(0, 100) for _ in range(cols)] for _ in range(rows)]

def calculate_volume_of_cuboid(length, width, height):
    return length * width * height

def get_vowels_in_order(s):
    return ''.join(sorted(set(char for char in s if char in 'aeiou')))

def calculate_sum_of_digits(number):
    return sum(int(digit) for digit in str(abs(number)))

def generate_random_lowercase_string(length):
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(length))

def calculate_surface_area_of_cuboid(length, width, height):
    return 2 * (length * width + width * height + height * length)

def get_length_of_longest_substring(s):
    max_len = 0
    start = 0
    used_chars = {}
    for i, char in enumerate(s):
        if char in used_chars and start <= used_chars[char]:
            start = used_chars[char] + 1
        else:
            max_len = max(max_len, i - start + 1)
        used_chars[char] = i
    return max_len

def get_divisors_of_number(number):
    return [i for i in range(1, number + 1) if number % i == 0]

def calculate_body_mass_index(weight, height):
    return weight / (height ** 2)

def get_consonants_in_order(s):
    return ''.join(sorted(set(char for char in s if char.isalpha() and char not in 'aeiou')))

def generate_random_uppercase_string(length):
    return ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(length))

def calculate_volume_of_pyramid(base_area, height):
    return (1/3) * base_area * height

def get_unique_words_in_order(sentence):
    return sorted(set(sentence.split()), key=sentence.split().index)

def calculate_gross_salary(basic, allowances, deductions):
    return basic + allowances - deductions

def get_alphabetical_characters_in_string(s):
    return ''.join(sorted(char for char in s if char.isalpha()))

def convert_grams_to_ounces(grams):
    return grams / 28.3495

def get_substrings_of_length(s, length):
    return [s[i:i+length] for i in range(len(s) - length + 1)]

def calculate_surface_area_of_cone(radius, slant_height):
    return math.pi * radius * (radius + slant_height)

def get_numbers_divisible_by_n(numbers, n):
    return [num for num in numbers if num % n == 0]

def calculate_final_price(price, tax_rate, discount):
    return price * (1 + tax_rate) - discount

def get_numbers_not_divisible_by_n(numbers, n):
    return [num for num in numbers if num % n != 0]
