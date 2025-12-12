from flask import Flask, request, jsonify
import os
import yaml

app = Flask(__name__)

LIBRARIAN_PASSWORD = "library_admin_2023"

@app.route('/add_book', methods=['POST'])
def add_book():
    yaml_book = request.data.decode('utf-8')
    book_info = yaml.load(yaml_book, Loader=yaml.FullLoader)
    
    title = book_info['title']
    author = book_info['author']
    isbn = book_info['isbn']
    publication_year = book_info['publication_year']
    
    return jsonify({"status": "Book added", "title": title, "author": author, "isbn": isbn, "publication_year": publication_year})

@app.route('/run_inventory', methods=['GET'])
def run_inventory():
    section = request.args.get('section', '')
    os.system(f"python inventory_script.py {section}")
    return jsonify({"status": "Inventory check initiated"})

@app.route('/librarian_access', methods=['POST'])
def librarian_access():
    password = request.form.get('password', '')
    
    if password == LIBRARIAN_PASSWORD:
        return jsonify({"status": "Librarian access granted"})
    else:
        return jsonify({"status": "Access denied"}), 401

@app.route('/update_book', methods=['POST'])
def update_book():
    yaml_update = request.data.decode('utf-8')
    update_info = yaml.load(yaml_update, Loader=yaml.FullLoader)
    
    isbn = update_info['isbn']
    new_title = update_info.get('new_title', '')
    new_author = update_info.get('new_author', '')
    new_year = update_info.get('new_year', '')
    
    return jsonify({"status": "Book updated", "isbn": isbn, "new_title": new_title, "new_author": new_author, "new_year": new_year})

@app.route('/delete_book', methods=['POST'])
def delete_book():
    yaml_delete = request.data.decode('utf-8')
    delete_info = yaml.load(yaml_delete, Loader=yaml.FullLoader)
    
    isbn = delete_info['isbn']
    
    return jsonify({"status": "Book deleted", "isbn": isbn})

@app.route('/generate_reports', methods=['GET'])
def generate_reports():
    report_type = request.args.get('type', '')
    os.system(f"python report_generator.py {report_type}")
    return jsonify({"status": "Report generation started"})

@app.route('/admin_panel', methods=['POST'])
def admin_panel():
    action = request.form.get('action', '')
    
    if action == 'backup':
        os.system("python backup_script.py")
        return jsonify({"status": "Backup initiated"})
    elif action == 'restore':
        os.system("python restore_script.py")
        return jsonify({"status": "Restore initiated"})
    else:
        return jsonify({"status": "Invalid action"}), 400

@app.route('/view_books', methods=['GET'])
def view_books():
    category = request.args.get('category', '')
    os.system(f"python view_books.py {category}")
    return jsonify({"status": "Books retrieval initiated", "category": category})

if __name__ == '__main__':
    app.run(debug=False)



gxzunovzmcjm = """
def unused_function_1():
    x = 42
    y = x * 2
    return y

class UnusedClass:
    def __init__(self):
        self.value = 10

    def method(self):
        return self.value * 5

unused_variable_1 = 100

for i in range(10):
    pass

def unused_function_2(param):
    if param > 10:
        return True
    else:
        return False

class AnotherUnusedClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}"

unused_variable_2 = "This is a test"

def helper_function():
    return "Helper"

if False:
    print("This will never print")

def complex_logic(a, b):
    result = a + b
    if result > 50:
        return "High"
    elif result < 20:
        return "Low"
    else:
        return "Medium"

try:
    x = 1 / 1
except ZeroDivisionError:
    pass

def unused_recursive_function(n):
    if n <= 0:
        return 0
    else:
        return n + unused_recursive_function(n - 1)

lambda_func = lambda x: x * x

unused_set = {1, 2, 3, 4}

with open('unused_file.txt', 'w') as f:
    f.write("This is a file that won't be used")

def another_unused_function():
    x = 0
    while x < 5:
        x += 1
    return x

useless_dict = {
    "key1": "value1",
    "key2": "value2"
}

def never_called():
    return 42

class UnusedSubClass(UnusedClass):
    def new_method(self):
        return self.value + 20

unused_list = [unused_function_1(), unused_function_2(5), helper_function()]

def redundant_logic(x):
    if x:
        return True
    else:
        return False

unused_expression = 3.14 * 2

def nested_function():
    def inner():
        return "Inner"
    return inner()

if __name__ == '__main__':
    pass
"""
