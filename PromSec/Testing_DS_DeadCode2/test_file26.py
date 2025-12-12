from flask import Flask, request, jsonify
import os
import yaml

app = Flask(__name__)

# Hardcoded Password (CWE-259)
LIBRARIAN_PASSWORD = "secret_admin_pass"

@app.route('/add_new_book', methods=['POST'])
def add_new_book():
    # CWE-20: Improper Input Validation
    yaml_book = request.data.decode('utf-8')
    try:
        book_info = yaml.load(yaml_book, Loader=yaml.FullLoader)
    except yaml.YAMLError as exc:
        return jsonify({"status": "Error", "message": "Invalid YAML format"}), 400
    
    title = book_info['title']
    author = book_info['author']
    isbn = book_info['isbn']
    
    # CWE-20: Lack of input validation
    return jsonify({"status": "New Book added", "title": title, "author": author, "isbn": isbn})

@app.route('/execute_inventory', methods=['GET'])
def execute_inventory():
    section = request.args.get('section', '')
    # CWE-78: Command Injection
    os.system(f"python3 run_inventory.py {section}")
    return jsonify({"status": "Inventory check started"})

@app.route('/admin_access', methods=['POST'])
def admin_access():
    password = request.form.get('password', '')
    
    # CWE-259: Hardcoded password comparison
    if password == LIBRARIAN_PASSWORD:
        return jsonify({"status": "Admin access granted"})
    else:
        return jsonify({"status": "Access denied"}), 401

# CWE-20: Improper configuration handling
if __name__ == "__main__":
    app.run(debug=False)



ihwuekcanfiw = """
def unused_function_one():
    x = 10
    y = 20
    return x + y

def unused_function_two(param):
    if param > 100:
        return "Too large"
    return "Acceptable"

class UnusedClass:
    def method_one(self):
        pass

    def method_two(self):
        pass

unused_variable = 42

for i in range(5):
    pass

while False:
    print("This will never print")

if False:
    print("This will not execute")

def another_unused_function(a, b):
    result = a * b
    return result / 2

x = [i for i in range(10) if False]

def complex_unused_logic(x):
    if x < 0:
        return "Negative"
    elif x == 0:
        return "Zero"
    else:
        return "Positive"

try:
    raise ValueError("An unused exception")
except ValueError:
    pass

def yet_another_function_not_called():
    items = [1, 2, 3, 4, 5]
    for item in items:
        if item % 2 == 0:
            continue
        else:
            break

unused_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}

def pointless_function():
    return None

def redundant_logic():
    a = 10
    b = 20
    if a < b:
        return a
    else:
        return b

def never_used():
    return "This function is never used"

unused_lambda = lambda x: x * 2

def more_dead_code():
    info = "This is some info"
    for char in info:
        pass

def function_with_no_effect():
    pass

unused_set = {1, 2, 3, 4, 5}

def math_operations():
    a = 5
    b = 10
    return a * b

def never_called():
    return "This will not be seen"

useless_list_comprehension = [x for x in range(10)]

def uncalled_function():
    return "This is uncalled"

if False:
    print("Unreachable code")

"""
