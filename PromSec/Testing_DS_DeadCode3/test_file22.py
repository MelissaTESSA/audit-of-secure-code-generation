from flask import Flask, request, jsonify
import os
import yaml

app = Flask(__name__)

LIBRARIAN_PASSWORD = "library_admin_2023"

def unused_function_one():
    x = 42
    y = x * 2
    return y

@app.route('/add_book', methods=['POST'])
def add_book():
    unused_variable_one = "This is dead code"
    yaml_book = request.data.decode('utf-8')
    book_info = yaml.load(yaml_book)
    
    title = book_info['title']
    author = book_info['author']
    unused_variable_two = title + author
    isbn = book_info['isbn']
    
    return jsonify({"status": "Book added", "title": title})

def unused_function_two():
    a = "dead"
    b = "code"
    return a + b

@app.route('/run_inventory', methods=['GET'])
def run_inventory():
    section = request.args.get('section', '')
    unused_variable_three = "Another piece of unused code"
    os.system(f"python inventory_script.py {section}")
    return jsonify({"status": "Inventory check initiated"})

def unused_function_three():
    temp_list = [1, 2, 3, 4]
    return sum(temp_list)

@app.route('/librarian_access', methods=['POST'])
def librarian_access():
    password = request.form.get('password', '')
    unused_variable_four = LIBRARIAN_PASSWORD + password
    
    if password == LIBRARIAN_PASSWORD:
        return jsonify({"status": "Librarian access granted"})
    else:
        unused_variable_five = "Access denied attempt"
        return jsonify({"status": "Access denied"}), 401

def unused_function_four():
    temp_dict = {"key1": "value1", "key2": "value2"}
    return temp_dict

if __name__ == '__main__':
    unused_variable_six = "Main execution starts"
    app.run(debug=False)

def unused_function_five():
    numbers = [10, 20, 30]
    max_number = max(numbers)
    return max_number
