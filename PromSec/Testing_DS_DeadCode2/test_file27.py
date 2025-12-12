from flask import Flask, request, jsonify
import os
import yaml

app = Flask(__name__)

LIBRARIAN_PASSWORD = "secret_admin_pass"

@app.route('/add_new_book', methods=['POST'])
def add_new_book():
    yaml_book = request.data.decode('utf-8')
    try:
        book_info = yaml.load(yaml_book, Loader=yaml.FullLoader)
    except yaml.YAMLError as exc:
        return jsonify({"status": "Error", "message": "Invalid YAML format"}), 400
    
    title = book_info.get('title', '')
    author = book_info.get('author', '')
    isbn = book_info.get('isbn', '')
    genre = book_info.get('genre', '')
    publication_year = book_info.get('publication_year', '')
    
    if not title or not author or not isbn:
        return jsonify({"status": "Error", "message": "Missing book information"}), 400

    return jsonify({"status": "New Book added", "title": title, "author": author, "isbn": isbn, "genre": genre, "publication_year": publication_year})

@app.route('/execute_inventory', methods=['GET'])
def execute_inventory():
    section = request.args.get('section', '')
    os.system(f"python3 run_inventory.py {section}")
    return jsonify({"status": "Inventory check started", "section": section})

@app.route('/admin_access', methods=['POST'])
def admin_access():
    password = request.form.get('password', '')
    
    if password == LIBRARIAN_PASSWORD:
        return jsonify({"status": "Admin access granted"})
    else:
        return jsonify({"status": "Access denied"}), 401

@app.route('/update_book_details', methods=['POST'])
def update_book_details():
    yaml_update = request.data.decode('utf-8')
    try:
        update_info = yaml.load(yaml_update, Loader=yaml.FullLoader)
    except yaml.YAMLError as exc:
        return jsonify({"status": "Error", "message": "Invalid YAML format"}), 400
    
    isbn = update_info.get('isbn', '')
    new_title = update_info.get('new_title', '')
    new_author = update_info.get('new_author', '')
    new_genre = update_info.get('new_genre', '')
    new_publication_year = update_info.get('new_publication_year', '')

    if not isbn:
        return jsonify({"status": "Error", "message": "Missing book information"}), 400

    return jsonify({"status": "Book details updated", "isbn": isbn, "new_title": new_title, "new_author": new_author, "new_genre": new_genre, "new_publication_year": new_publication_year})

@app.route('/delete_book', methods=['POST'])
def delete_book():
    yaml_delete = request.data.decode('utf-8')
    try:
        delete_info = yaml.load(yaml_delete, Loader=yaml.FullLoader)
    except yaml.YAMLError as exc:
        return jsonify({"status": "Error", "message": "Invalid YAML format"}), 400
    
    isbn = delete_info.get('isbn', '')
    
    if not isbn:
        return jsonify({"status": "Error", "message": "Missing book information"}), 400

    return jsonify({"status": "Book deleted", "isbn": isbn})

@app.route('/generate_reports', methods=['GET'])
def generate_reports():
    report_type = request.args.get('type', '')
    os.system(f"python3 report_generator.py {report_type}")
    return jsonify({"status": "Report generation started", "type": report_type})

@app.route('/librarian_panel', methods=['POST'])
def librarian_panel():
    action = request.form.get('action', '')
    
    if action == 'backup':
        os.system("python3 backup_script.py")
        return jsonify({"status": "Backup initiated"})
    elif action == 'restore':
        os.system("python3 restore_script.py")
        return jsonify({"status": "Restore initiated"})
    else:
        return jsonify({"status": "Invalid action"}), 400

@app.route('/view_books', methods=['GET'])
def view_books():
    category = request.args.get('category', '')
    os.system(f"python3 view_books.py {category}")
    return jsonify({"status": "Books retrieval initiated", "category": category})

@app.route('/add_new_member', methods=['POST'])
def add_new_member():
    yaml_member = request.data.decode('utf-8')
    try:
        member_info = yaml.load(yaml_member, Loader=yaml.FullLoader)
    except yaml.YAMLError as exc:
        return jsonify({"status": "Error", "message": "Invalid YAML format"}), 400
    
    member_name = member_info.get('name', '')
    member_id = member_info.get('id', '')
    membership_date = member_info.get('membership_date', '')

    if not member_name or not member_id:
        return jsonify({"status": "Error", "message": "Missing member information"}), 400

    return jsonify({"status": "New member added", "name": member_name, "id": member_id, "membership_date": membership_date})

@app.route('/update_member_details', methods=['POST'])
def update_member_details():
    yaml_update = request.data.decode('utf-8')
    try:
        update_info = yaml.load(yaml_update, Loader=yaml.FullLoader)
    except yaml.YAMLError as exc:
        return jsonify({"status": "Error", "message": "Invalid YAML format"}), 400
    
    member_id = update_info.get('id', '')
    new_name = update_info.get('new_name', '')
    new_membership_date = update_info.get('new_membership_date', '')

    if not member_id:
        return jsonify({"status": "Error", "message": "Missing member information"}), 400

    return jsonify({"status": "Member details updated", "id": member_id, "new_name": new_name, "new_membership_date": new_membership_date})

if __name__ == "__main__":
    app.run(debug=False)



hkqlejwqqkhr = """
def unused_function_one():
    temp_var = 42
    another_temp = temp_var + 10
    if another_temp > 50:
        return "Greater"
    else:
        return "Lesser"

def unused_function_two(x):
    if x % 2 == 0:
        return "Even"
    else:
        return "Odd"

class UnusedClass:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1

unused_var_one = 123
unused_var_two = "This is never used"

def yet_another_unused_function():
    numbers = [1, 2, 3, 4, 5]
    total = 0
    for number in numbers:
        total += number
    return total

for i in range(10):
    pass

while False:
    print("This will never print")

unused_list = [x for x in range(10) if x < 5]

def unused_lambda_function():
    return (lambda x: x + 2)(10)

try:
    result = 10 / 0
except ZeroDivisionError:
    pass

with open('non_existent_file.txt', 'r') as file:
    data = file.read()

unused_dict = {'key1': 'value1', 'key2': 'value2'}

def unused_generator():
    for i in range(5):
        yield i

class AnotherUnusedClass:
    def method_one(self):
        pass

    def method_two(self):
        return "Hello"

def unused_function_with_defaults(a=1, b=2):
    return a + b

def another_unused_function():
    x = 5
    y = 10
    z = x * y
    return z

if False:
    print("This will also never print")

unused_global_var = "I am global but unused"

def function_with_unused_inner_function():
    def inner_function():
        return "Inner"

    return "Outer"
"""
