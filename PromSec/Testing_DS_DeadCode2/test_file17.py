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


mqjhkfgzftcr = """
def unused_function_one():
    x = 5
    y = 10
    z = x + y
    return z

def unused_function_two(a, b):
    if a > b:
        return a
    else:
        return b

class UnusedClass:
    def __init__(self, value):
        self.value = value
    
    def display(self):
        print(f"Value: {self.value}")

unused_variable_one = 42
unused_variable_two = "This is a string"

for i in range(10):
    pass

if False:
    print("This will never print")

while False:
    break

try:
    x = 1 / 0
except ZeroDivisionError:
    pass

def another_unused_function():
    list_of_numbers = [1, 2, 3, 4, 5]
    for num in list_of_numbers:
        if num % 2 == 0:
            continue
        else:
            break

def yet_another_unused_function():
    return "Hello, World!"

def never_called_function(arg):
    arg += 1
    return arg

def no_side_effects():
    x = 1
    y = 2
    x + y

def another_useless_function():
    return None

def yet_another_useless_function():
    pass

x = "Not used anywhere"
y = [i for i in range(5)]
z = {key: key**2 for key in range(5)}

def function_with_unused_parameter(unused_param):
    return 42

def function_that_does_nothing():
    pass

def function_with_docstring():
    """This function does absolutely nothing."""
    pass

if 0:
    print("This won't execute")

for j in range(0):
    print("Loop will not run")

unused_set = {1, 2, 3}

def function_with_empty_body():
    pass

lambda_unused = lambda x: x * 2

def function_with_useless_logic():
    x = 10
    y = 20
    if x > y:
        return x
    else:
        return y

def irrelevant_function():
    return

def function_with_return():
    return None

def function_with_local_variable():
    local_var = "I'm not used"
    return

unused_lambda = lambda x: x + 1

unused_tuple = (1, 2, 3)

def function_with_while_false():
    while False:
        print("Never runs")

def another_irrelevant_function():
    return "irrelevant"

def function_with_try_except():
    try:
        x = 1 / 0
    except:
        pass

def function_with_if_false():
    if False:
        print("Not executed")

def function_with_useless_computation():
    a = 5
    b = 10
    c = a * b

def function_with_unused_import():
    import random

def function_with_no_effect():
    pass

def function_with_redundant_code():
    x = 2
    x + 3
"""
