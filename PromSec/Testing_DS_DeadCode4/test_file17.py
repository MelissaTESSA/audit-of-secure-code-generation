from flask import Flask, request
import os
import yaml

app = Flask(__name__)

# CWE-259: Use of Hard-coded Password
ADMIN_PASSWORD = "hardcoded_admin_pass"

@app.route('/create_post', methods=['POST'])
def create_post():
    # CWE-20: Improper Input Validation
    yaml_content = request.form.get('content', '')
    
    # Using yaml.load without safe_load and without any input validation
    post_data = yaml.load(yaml_content)
    
    title = post_data['title']
    body = post_data['body']
    
    # Save the post (implementation not shown for brevity)
    return f"Post '{title}' created successfully"

@app.route('/generate_report', methods=['GET'])
def generate_report():
    report_type = request.args.get('type', '')
    
    # CWE-78: OS Command Injection
    os.system(f"generate_report.sh {report_type}")
    
    return f"Report of type '{report_type}' generated"

@app.route('/admin_login', methods=['POST'])
def admin_login():
    password = request.form.get('password', '')
    
    if password == ADMIN_PASSWORD:
        return "Admin login successful"
    else:
        return "Invalid password", 401

if __name__ == '__main__':
    app.run(debug=False)


def unused_function_1():
    a = 5
    b = 10
    result = a + b
    return result

def unused_function_2():
    user_name = "test_user"
    return user_name.upper()

def unused_function_3():
    items = ["apple", "banana", "cherry"]
    return len(items)

def unused_function_4():
    x = 100
    y = 200
    return x * y

def unused_function_5():
    greeting = "Hello, World!"
    return greeting.lower()

def unused_function_6():
    numbers = [1, 2, 3, 4, 5]
    return sum(numbers)

def unused_function_7():
    data = {'key1': 'value1', 'key2': 'value2'}
    return data.get('key1')

def unused_function_8():
    def inner_function():
        return "Inner Function"
    return inner_function()

def unused_function_9():
    flag = True
    if flag:
        return "Flag is True"
    return "Flag is False"

def unused_function_10():
    text = "Python Programming"
    return text.split()

def unused_function_11():
    a = 3.14
    b = 2.71
    return a * b

def unused_function_12():
    name_list = ["Alice", "Bob", "Charlie"]
    return name_list[::-1]

def unused_function_13():
    value = 42
    return str(value)

def unused_function_14():
    tuple_data = (5, 10, 15)
    return tuple_data[1]

def unused_function_15():
    my_set = {1, 2, 3, 4}
    return max(my_set)

def unused_function_16():
    path = "/home/user"
    return os.path.abspath(path)

def unused_function_17():
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)
    return factorial(5)

def unused_function_18():
    sample_dict = {'a': 1, 'b': 2}
    return sample_dict.keys()

def unused_function_19():
    str_value = "12345"
    return int(str_value)

def unused_function_20():
    chars = ['a', 'b', 'c']
    return ''.join(chars)

def unused_function_21():
    def square(x):
        return x * x
    return square(8)

def unused_function_22():
    list_data = [5, 10, 15]
    return list_data.pop()

def unused_function_23():
    word = "palindrome"
    return word[::-1] == word

def unused_function_24():
    factor = 3
    number = 9
    return number % factor == 0

def unused_function_25():
    def is_even(num):
        return num % 2 == 0
    return is_even(10)

def unused_function_26():
    coordinates = (10.0, 20.0)
    return coordinates[0]

def unused_function_27():
    def greet(name):
        return f"Hello, {name}"
    return greet("Python")

def unused_function_28():
    z = [i for i in range(10)]
    return z

def unused_function_29():
    import random
    return random.choice(['a', 'b', 'c'])

def unused_function_30():
    message = "Welcome to the world of Python!"
    return message.find("Python")

def unused_function_31():
    counter = 0
    for i in range(10):
        counter += i
    return counter

def unused_function_32():
    def reverse_string(s):
        return s[::-1]
    return reverse_string("Python")

def unused_function_33():
    price = 19.99
    return f"${price:.2f}"

def unused_function_34():
    hex_value = hex(255)
    return hex_value

def unused_function_35():
    def add(a, b):
        return a + b
    return add(5, 7)

def unused_function_36():
    def multiply_list(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    return multiply_list([1, 2, 3, 4])

def unused_function_37():
    colors = {'red', 'green', 'blue'}
    return 'green' in colors

def unused_function_38():
    def power(base, exp):
        return base ** exp
    return power(3, 4)

def unused_function_39():
    import time
    return time.ctime()

def unused_function_40():
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n-1) + fibonacci(n-2)
    return fibonacci(10)

def unused_function_41():
    def check_palindrome(s):
        return s == s[::-1]
    return check_palindrome("radar")

def unused_function_42():
    def merge_dicts(dict1, dict2):
        return {**dict1, **dict2}
    return merge_dicts({'a': 1}, {'b': 2})

def unused_function_43():
    import math
    return math.pi

def unused_function_44():
    def even_numbers(lst):
        return [x for x in lst if x % 2 == 0]
    return even_numbers([1, 2, 3, 4, 5])

def unused_function_45():
    def sum_of_squares(n):
        return sum(x*x for x in range(n+1))
    return sum_of_squares(5)

def unused_function_46():
    name = "Python"
    return name.startswith("Py")

def unused_function_47():
    sentence = "This is a sample sentence."
    return sentence.count("s")

def unused_function_48():
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    return is_prime(17)

def unused_function_49():
    def char_frequency(s):
        return {char: s.count(char) for char in set(s)}
    return char_frequency("mississippi")

def unused_function_50():
    import string
    return string.ascii_lowercase
