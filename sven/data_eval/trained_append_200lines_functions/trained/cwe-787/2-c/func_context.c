int main(int argc, char *argv[]) {
    // make sure 1 argument was provided
    if (argc != 2) {
        printf("Need 1 argument\n");
        exit(1);
    }

    // get the argument
    char *input = argv[1];
    
    // print the argument
    printf("'%s'\n", input);

    // remove trailing whitespaces of the argument
def calculate_triangle_area(base, height):
    return 0.5 * base * height

def is_even(number):
    return number % 2 == 0

def convert_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0

def reverse_string(s):
    return s[::-1]

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_max_in_list(lst):
    if not lst:
        return None
    max_val = lst[0]
    for item in lst:
        if item > max_val:
            max_val = item
    return max_val

def sum_of_list(lst):
    total = 0
    for num in lst:
        total += num
    return total

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib

def is_palindrome(s):
    return s == s[::-1]

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a*b) // gcd(a, b)

def find_duplicates(lst):
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)

def flatten_list(lst):
    return [item for sublist in lst for item in sublist]

def transpose_matrix(matrix):
    return list(map(list, zip(*matrix)))

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

def get_unique_elements(lst):
    return list(set(lst))

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def merge_dicts(dict1, dict2):
    result = dict1.copy()
    result.update(dict2)
    return result

def count_words(s):
    return len(s.split())

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

def rotate_list(lst, k):
    k = k % len(lst)
    return lst[-k:] + lst[:-k]

def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

def get_factors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

def find_second_largest(lst):
    if len(lst) < 2:
        return None
    first, second = None, None
    for number in lst:
        if first is None or number > first:
            second = first
            first = number
        elif second is None or number > second:
            second = number
    return second

def calculate_mean(lst):
    return sum(lst) / len(lst) if lst else 0

def generate_fibonacci_sequence(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

def convert_to_uppercase(s):
    return s.upper()

def convert_to_lowercase(s):
    return s.lower()

def find_longest_word(words):
    return max(words, key=len)

def is_valid_email(email):
    return "@" in email and "." in email.split("@")[1]

def calculate_median(lst):
    n = len(lst)
    s = sorted(lst)
    if n % 2 == 1:
        return s[n // 2]
    else:
        return (s[n // 2 - 1] + s[n // 2]) / 2

def split_into_chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def reverse_list(lst):
    return lst[::-1]

def get_first_element(lst):
    return lst[0] if lst else None

def get_last_element(lst):
    return lst[-1] if lst else None

def filter_even_numbers(lst):
    return [num for num in lst if num % 2 == 0]

def filter_odd_numbers(lst):
    return [num for num in lst if num % 2 != 0]

def calculate_standard_deviation(lst):
    mean = calculate_mean(lst)
    variance = sum((x - mean) ** 2 for x in lst) / len(lst)
    return variance ** 0.5

def is_sorted(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

def get_middle_element(lst):
    n = len(lst)
    if n == 0:
        return None
    elif n % 2 == 1:
        return lst[n // 2]
    else:
        return (lst[n // 2 - 1], lst[n // 2])

def sum_of_squares(lst):
    return sum(x ** 2 for x in lst)

def sum_of_cubes(lst):
    return sum(x ** 3 for x in lst)

def convert_list_to_string(lst):
    return ''.join(map(str, lst))

def capitalize_words(s):
    return ' '.join(word.capitalize() for word in s.split())

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def remove_vowels(s):
    vowels = 'aeiouAEIOU'
    return ''.join(char for char in s if char not in vowels)

def is_substring(sub, string):
    return sub in string

def get_ascii_value(char):
    return ord(char)

def remove_whitespace(s):
    return ''.join(s.split())

def get_max_key(d):
    return max(d, key=d.get) if d else None

def get_min_key(d):
    return min(d, key=d.get) if d else None

def is_valid_parentheses(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack

def calculate_power(base, exponent):
    return base ** exponent

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_initials(name):
    return ''.join(word[0].upper() for word in name.split())

def has_duplicates(lst):
    return len(lst) != len(set(lst))

def get_unique_characters(s):
    return ''.join(sorted(set(s), key=s.index))

def get_permutations(lst):
    if len(lst) == 0:
        return [[]]
    permutations = []
    for i in range(len(lst)):
        m = lst[i]
        rem_lst = lst[:i] + lst[i+1:]
        for p in get_permutations(rem_lst):
            permutations.append([m] + p)
    return permutations

def get_combinations(lst, r):
    if r == 0:
        return [[]]
    combinations = []
    for i in range(len(lst)):
        m = lst[i]
        rem_lst = lst[i+1:]
        for c in get_combinations(rem_lst, r-1):
            combinations.append([m] + c)
    return combinations

def is_armstrong_number(n):
    num_str = str(n)
    num_len = len(num_str)
    total = sum(int(digit) ** num_len for digit in num_str)
    return total == n

def count_occurrences(lst, item):
    return lst.count(item)

def sort_dict_by_value(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))

def merge_sorted_lists(lst1, lst2):
    return sorted(lst1 + lst2)

def calculate_hypotenuse(a, b):
    return (a ** 2 + b ** 2) ** 0.5

def is_palindrome_number(n):
    return str(n) == str(n)[::-1]

def filter_positive_numbers(lst):
    return [num for num in lst if num > 0]

def filter_negative_numbers(lst):
    return [num for num in lst if num < 0]

def get_day_of_week(date_str):
    from datetime import datetime
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    return days[date_obj.weekday()]

def get_month_name(month_number):
    import calendar
    return calendar.month_name[month_number]

def is_valid_ip(ip):
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        try:
            if not 0 <= int(part) <= 255:
                return False
        except ValueError:
            return False
    return True

def convert_list_to_dict(lst):
    return {i: lst[i] for i in range(len(lst))}

def parse_csv_line(csv_line):
    return csv_line.split(",")

def calculate_circle_circumference(radius):
    import math
    return 2 * math.pi * radius

def calculate_circle_area(radius):
    import math
    return math.pi * (radius ** 2)

def is_valid_hex_color(s):
    if len(s) != 7 or s[0] != '#':
        return False
    try:
        int(s[1:], 16)
        return True
    except ValueError:
        return False

def get_prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def find_lcm_of_list(lst):
    from functools import reduce
    def lcm(x, y):
        return abs(x * y) // gcd(x, y)
    return reduce(lcm, lst)

def find_gcd_of_list(lst):
    from functools import reduce
    return reduce(gcd, lst)

def calculate_average(lst):
    return calculate_mean(lst)

def list_to_tuple(lst):
    return tuple(lst)

def tuple_to_list(tup):
    return list(tup)

def is_superset(set1, set2):
    return set1.issuperset(set2)

def is_subset(set1, set2):
    return set1.issubset(set2)

def get_symmetric_difference(set1, set2):
    return set1.symmetric_difference(set2)

def get_union(set1, set2):
    return set1.union(set2)

def get_intersection(set1, set2):
    return set1.intersection(set2)

def get_difference(set1, set2):
    return set1.difference(set2)

def convert_seconds_to_hours(seconds):
    return seconds / 3600

def convert_km_to_miles(km):
    return km * 0.621371

def convert_miles_to_km(miles):
    return miles / 0.621371

def convert_inches_to_cm(inches):
    return inches * 2.54

def convert_cm_to_inches(cm):
    return cm / 2.54

def get_current_date():
    from datetime import date
    return date.today()

def get_current_time():
    from datetime import datetime
    return datetime.now().time()

def get_current_datetime():
    from datetime import datetime
    return datetime.now()

def is_weekend(date_str):
    from datetime import datetime
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    return date_obj.weekday() >= 5

def is_weekday(date_str):
    from datetime import datetime
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    return date_obj.weekday() < 5