from flask import Flask, request, redirect
import MySQLdb

app = Flask(__name__)

@app.route('/add_event', methods=['POST'])
def add_event():
   title = request.form['title']
   date = request.form['date']
   
   db = MySQLdb.connect("localhost","testuser","test123","EVENTDB")
   cursor = db.cursor()
   
   cursor.execute("SELECT * FROM Events WHERE Title = '%s'" % title)
   if cursor.fetchone() is not None:
      cursor.close()
      db.close()
      return redirect('./add_event')
   else:
      cursor.execute("INSERT INTO Events (Title, Date) VALUES ('%s', '%s')" % (title, date))
      db.commit()
      cursor.close()
      db.close()
      return redirect('./view_events')

@app.route('/update_event_date', methods=['POST'])
def update_event_date():
   title = request.form['title']
   new_date = request.form['new_date']
   
   db = MySQLdb.connect("localhost","testuser","test123","EVENTDB")
   cursor = db.cursor()
   
   cursor.execute("UPDATE Events SET Date = '%s' WHERE Title = '%s'" % (new_date, title))
   db.commit()
   
   cursor.close()
   db.close()
   
   return "Event date updated successfully"

@app.route('/delete_event', methods=['POST'])
def delete_event():
   title = request.form['title']
   
   db = MySQLdb.connect("localhost","testuser","test123","EVENTDB")
   cursor = db.cursor()
   
   cursor.execute("DELETE FROM Events WHERE Title = '%s'" % title)
   db.commit()
   
   cursor.close()
   db.close()
   
   return "Event deleted successfully"

@app.route('/search_events', methods=['GET'])
def search_events():
   search_term = request.args.get('term', '')
   
   db = MySQLdb.connect("localhost","testuser","test123","EVENTDB")
   cursor = db.cursor()
   
   cursor.execute("SELECT * FROM Events WHERE Title LIKE '%%%s%%'" % search_term)
   events = cursor.fetchall()
   
   cursor.close()
   db.close()
   
   return str(events)

@app.route('/view_events', methods=['GET'])
def view_events():
   db = MySQLdb.connect("localhost","testuser","test123","EVENTDB")
   cursor = db.cursor()
   
   cursor.execute("SELECT * FROM Events")
   events = cursor.fetchall()
   
   cursor.close()
   db.close()
   
   return str(events)

if __name__ == '__main__':
   app.run(debug=False)



def calculate_discount(price, discount_rate):
    discount_amount = price * discount_rate / 100
    return price - discount_amount

def convert_temperature(celsius):
    return celsius * 9/5 + 32

def is_even(number):
    return number % 2 == 0

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def reverse_string(s):
    return s[::-1]

def find_maximum(lst):
    if not lst:
        return None
    max_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

def get_unique_elements(lst):
    return list(set(lst))

def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

def is_palindrome(s):
    return s == s[::-1]

def sum_of_squares(n):
    return sum(i*i for i in range(1, n+1))

def merge_dictionaries(dict1, dict2):
    result = dict1.copy()
    result.update(dict2)
    return result

def get_prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

def calculate_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def linear_search(lst, target):
    for i, value in enumerate(lst):
        if value == target:
            return i
    return -1

def binary_search(lst, target):
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst) // 2]
    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def check_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

def count_words(sentence):
    return len(sentence.split())

def calculate_area_of_circle(radius):
    from math import pi
    return pi * radius * radius

def calculate_perimeter_of_rectangle(length, width):
    return 2 * (length + width)

def convert_to_binary(n):
    return bin(n)[2:]

def find_factors(n):
    return [i for i in range(1, n+1) if n % i == 0]

def convert_to_hexadecimal(n):
    return hex(n)[2:]

def calculate_power(base, exponent):
    return base ** exponent

def count_occurrences(lst, value):
    return lst.count(value)

def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_intersection(list1, list2):
    return list(set(list1) & set(list2))

def get_union(list1, list2):
    return list(set(list1) | set(list2))

def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

def get_second_largest(lst):
    unique_lst = list(set(lst))
    unique_lst.sort()
    return unique_lst[-2] if len(unique_lst) >= 2 else None

def transpose_matrix(matrix):
    return list(map(list, zip(*matrix)))

def multiply_matrices(matrix1, matrix2):
    result = [[sum(a * b for a, b in zip(row, col)) for col in zip(*matrix2)] for row in matrix1]
    return result

def check_armstrong_number(n):
    total = sum(int(digit) ** len(str(n)) for digit in str(n))
    return n == total

def calculate_lcm(a, b):
    gcd = calculate_gcd(a, b)
    return abs(a*b) // gcd

def remove_vowels(s):
    vowels = 'aeiouAEIOU'
    return ''.join(char for char in s if char not in vowels)

def sort_dict_by_key(d):
    return dict(sorted(d.items()))

def sort_dict_by_value(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))

def calculate_median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]

def calculate_mode(lst):
    from collections import Counter
    count = Counter(lst)
    max_count = max(count.values())
    return [k for k, v in count.items() if v == max_count]

def calculate_standard_deviation(lst):
    from statistics import stdev
    return stdev(lst)

def calculate_variance(lst):
    from statistics import variance
    return variance(lst)

def calculate_correlation_coefficient(x, y):
    from statistics import mean
    n = len(x)
    mean_x, mean_y = mean(x), mean(y)
    covariance = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n)) / n
    std_x = (sum((x[i] - mean_x) ** 2 for i in range(n)) / n) ** 0.5
    std_y = (sum((y[i] - mean_y) ** 2 for i in range(n)) / n) ** 0.5
    return covariance / (std_x * std_y)

def calculate_present_value(future_value, rate, periods):
    return future_value / ((1 + rate) ** periods)

def calculate_future_value(present_value, rate, periods):
    return present_value * ((1 + rate) ** periods)

def calculate_compound_interest(principal, rate, times, periods):
    return principal * ((1 + rate / times) ** (times * periods))

def calculate_simple_interest(principal, rate, periods):
    return principal * rate * periods

def calculate_bmi(weight, height):
    return weight / (height * height)

def calculate_emi(principal, rate, periods):
    rate_monthly = rate / (12 * 100)
    return principal * rate_monthly * ((1 + rate_monthly) ** periods) / (((1 + rate_monthly) ** periods) - 1)

def calculate_body_fat_percentage(weight, waist, wrist, hip, forearm):
    return (weight * 0.732) + 8.987 + (wrist / 3.140) - (waist * 0.157) - (hip * 0.249) + (forearm * 0.434)

def convert_speed_kmh_to_mph(speed_kmh):
    return speed_kmh * 0.621371

def convert_speed_mph_to_kmh(speed_mph):
    return speed_mph / 0.621371

def calculate_wind_chill(temperature, wind_speed):
    return 35.74 + 0.6215 * temperature - 35.75 * (wind_speed ** 0.16) + 0.4275 * temperature * (wind_speed ** 0.16)

def calculate_heat_index(temperature, humidity):
    return -42.379 + 2.04901523 * temperature + 10.14333127 * humidity - 0.22475541 * temperature * humidity - 0.00683783 * temperature**2 - 0.05481717 * humidity**2 + 0.00122874 * temperature**2 * humidity + 0.00085282 * temperature * humidity**2 - 0.00000199 * temperature**2 * humidity**2

def calculate_dew_point(temperature, humidity):
    a, b = 17.27, 237.7
    alpha = ((a * temperature) / (b + temperature)) + (humidity / 100.0)
    return (b * alpha) / (a - alpha)

def convert_angle_degrees_to_radians(angle_degrees):
    from math import radians
    return radians(angle_degrees)

def convert_angle_radians_to_degrees(angle_radians):
    from math import degrees
    return degrees(angle_radians)

def calculate_sine(angle_radians):
    from math import sin
    return sin(angle_radians)

def calculate_cosine(angle_radians):
    from math import cos
    return cos(angle_radians)

def calculate_tangent(angle_radians):
    from math import tan
    return tan(angle_radians)

def convert_volume_liters_to_gallons(volume_liters):
    return volume_liters * 0.264172

def convert_volume_gallons_to_liters(volume_gallons):
    return volume_gallons / 0.264172

def calculate_hypotenuse(a, b):
    from math import sqrt
    return sqrt(a**2 + b**2)

def calculate_perimeter_of_triangle(a, b, c):
    return a + b + c

def calculate_area_of_triangle(base, height):
    return 0.5 * base * height

def calculate_circumference_of_circle(radius):
    from math import pi
    return 2 * pi * radius

def calculate_surface_area_of_sphere(radius):
    from math import pi
    return 4 * pi * radius**2

def calculate_volume_of_sphere(radius):
    from math import pi
    return (4/3) * pi * radius**3

def calculate_surface_area_of_cylinder(radius, height):
    from math import pi
    return 2 * pi * radius * (radius + height)

def calculate_volume_of_cylinder(radius, height):
    from math import pi
    return pi * radius**2 * height

def calculate_surface_area_of_cone(radius, height):
    from math import pi, sqrt
    return pi * radius * (radius + sqrt(height**2 + radius**2))

def calculate_volume_of_cone(radius, height):
    from math import pi
    return (1/3) * pi * radius**2 * height

def convert_length_inches_to_centimeters(length_inches):
    return length_inches * 2.54

def convert_length_centimeters_to_inches(length_centimeters):
    return length_centimeters / 2.54

def convert_weight_pounds_to_kilograms(weight_pounds):
    return weight_pounds * 0.453592

def convert_weight_kilograms_to_pounds(weight_kilograms):
    return weight_kilograms / 0.453592

def calculate_loan_repayment(principal, rate, periods):
    rate_monthly = rate / (12 * 100)
    return principal * rate_monthly / (1 - (1 + rate_monthly) ** -periods)

def calculate_amortization(principal, rate, periods):
    monthly_payment = calculate_loan_repayment(principal, rate, periods)
    balance = principal
    amortization_schedule = []
    for n in range(1, periods + 1):
        interest_payment = balance * rate / (12 * 100)
        principal_payment = monthly_payment - interest_payment
        balance -= principal_payment
        amortization_schedule.append((n, monthly_payment, principal_payment, interest_payment, balance))
    return amortization_schedule

def calculate_savings_future_value(monthly_savings, rate, periods):
    future_value = 0
    for _ in range(periods):
        future_value = (future_value + monthly_savings) * (1 + rate / 12)
    return future_value

def calculate_investment_return(principal, rate, periods):
    return principal * ((1 + rate) ** periods)

def calculate_break_even_point(fixed_costs, price_per_unit, cost_per_unit):
    return fixed_costs / (price_per_unit - cost_per_unit)

def calculate_markup_cost(cost, markup_percentage):
    return cost + (cost * markup_percentage / 100)

def calculate_margin_price(selling_price, cost_price):
    return (selling_price - cost_price) / selling_price * 100

def calculate_rsi(prices):
    gains = [prices[i] - prices[i-1] for i in range(1, len(prices)) if prices[i] > prices[i-1]]
    losses = [prices[i-1] - prices[i] for i in range(1, len(prices)) if prices[i] < prices[i-1]]
    average_gain = sum(gains) / 14
    average_loss = sum(losses) / 14
    rs = average_gain / average_loss
    return 100 - (100 / (1 + rs))

def calculate_macd(prices):
    short_ema = calculate_ema(prices, 12)
    long_ema = calculate_ema(prices, 26)
    macd = [short - long for short, long in zip(short_ema, long_ema)]
    signal = calculate_ema(macd, 9)
    return macd, signal

def calculate_ema(prices, period):
    ema = [sum(prices[:period]) / period]
    multiplier = 2 / (period + 1)
    for price in prices[period:]:
        ema.append((price - ema[-1]) * multiplier + ema[-1])
    return ema

def calculate_bollinger_bands(prices, period=20, num_std_dev=2):
    sma = [sum(prices[i-period:i]) / period for i in range(period, len(prices))]
    std_dev = [stdev(prices[i-period:i]) for i in range(period, len(prices))]
    upper_band = [sma[i] + num_std_dev * std_dev[i] for i in range(len(sma))]
    lower_band = [sma[i] - num_std_dev * std_dev[i] for i in range(len(sma))]
    return upper_band, lower_band

def calculate_beta(stock_returns, market_returns):
    covariance = sum((stock_return - mean(stock_returns)) * (market_return - mean(market_returns)) for stock_return, market_return in zip(stock_returns, market_returns)) / len(stock_returns)
    market_variance = sum((market_return - mean(market_returns)) ** 2 for market_return in market_returns) / len(market_returns)
    return covariance / market_variance

def calculate_sharpe_ratio(returns, risk_free_rate):
    excess_returns = [r - risk_free_rate for r in returns]
    return mean(excess_returns) / stdev(excess_returns)

def calculate_irr(cash_flows):
    from numpy import irr
    return irr(cash_flows)

def calculate_npv(rate, cash_flows):
    return sum(cf / (1 + rate) ** i for i, cf in enumerate(cash_flows))

def calculate_roi(gain, cost):
    return (gain - cost) / cost

def calculate_payback_period(initial_investment, cash_flows):
    cumulative_cash_flow = 0
    for i, cash_flow in enumerate(cash_flows):
        cumulative_cash_flow += cash_flow
        if cumulative_cash_flow >= initial_investment:
            return i + 1
    return None

def calculate_wacc(equity, debt, cost_of_equity, cost_of_debt, tax_rate):
    total_value = equity + debt
    wacc = (equity / total_value) * cost_of_equity + (debt / total_value) * cost_of_debt * (1 - tax_rate)
    return wacc
