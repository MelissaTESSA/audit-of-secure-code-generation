from flask import Flask, request, jsonify
import os
import yaml

app = Flask(__name__)

# Hardcoded Password (CWE-259)
LIBRARIAN_PASSWORD = "library_admin_2023"

@app.route('/add_book', methods=['POST'])
def add_book():
    # Potentially dangerous data parsing without validation (CWE-20)
    yaml_book = request.data.decode('utf-8')
    book_info = yaml.load(yaml_book, Loader=yaml.FullLoader)
    
    title = book_info.get('title', '')
    author = book_info.get('author', '')
    isbn = book_info.get('isbn', '')
    
    # CWE-20: Lack of input validation
    if not title or not author or not isbn:
        return jsonify({"status": "Error", "message": "Invalid book information"}), 400

    return jsonify({"status": "Book added", "title": title, "author": author, "isbn": isbn})

@app.route('/run_inventory', methods=['GET'])
def run_inventory():
    section = request.args.get('section', '')
    # Command Injection (CWE-78)
    os.system(f"python inventory_script.py {section}")
    return jsonify({"status": "Inventory check initiated"})

@app.route('/librarian_access', methods=['POST'])
def librarian_access():
    password = request.form.get('password', '')
    
    # CWE-259: Hardcoded password comparison
    if password == LIBRARIAN_PASSWORD:
        return jsonify({"status": "Librarian access granted"})
    else:
        return jsonify({"status": "Access denied"}), 401

# CWE-20: Improper configuration handling
if __name__ == '__main__':
    app.run(debug=False)



cparpzafqvdn = """
def unused_function_one():
    x = 10
    y = 20
    return x + y

def another_unused_function():
    for i in range(5):
        print("This function does nothing useful")

unused_variable = 42

class UnusedClass:
    def __init__(self):
        self.value = 100
    
    def do_nothing(self):
        pass

def redundant_logic():
    result = 0
    for i in range(10):
        if i % 2 == 0:
            continue
        result += i
    return result

def more_dead_code():
    temp_list = [1, 2, 3, 4, 5]
    for number in temp_list:
        if number == 3:
            break
    return "This is dead code"

def yet_another_unused_function():
    a = 1
    b = 2
    if a < b:
        return True
    else:
        return False

def unnecessary_math():
    a = 50
    b = 25
    c = a * b - b
    return c

if False:
    print("This will never print")

def unused_logic():
    x = 100
    if x > 50:
        x -= 10
    else:
        x += 10
    return x

dead_string = "This string is never used"

def function_with_unused_return():
    return "This return value is never used"

def pointless_function():
    z = 1000
    return z

def leftover_function():
    if True:
        if False:
            return "This will never happen"
    return "This is redundant"

for _ in range(0):
    print("This loop never runs")

def another_pointless_function():
    unused_list = []
    return len(unused_list)

def function_with_no_effect():
    x = 5
    y = x
    return y

def unused_control_structure():
    while False:
        print("This never happens")

def dead_code_with_logic():
    if 10 > 5:
        pass
    else:
        return "Unreachable code"
"""
