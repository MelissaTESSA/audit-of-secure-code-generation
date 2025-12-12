from flask import Flask, request, jsonify
import os
import yaml

app = Flask(__name__)

# Dead Code: Unused constant
UNUSED_CONSTANT = 123456789

# Hardcoded Password (CWE-259)
LIBRARIAN_PASSWORD = "library_admin_2023"

def dead_code_function():
    # Dead code: Unreachable function
    return "This is dead code"

@app.route('/add_book', methods=['POST'])
def add_book():
    # Dead code: Unused variable
    unused_var = "This is not used"

    # Potentially dangerous data parsing without validation (CWE-20)
    yaml_book = request.data.decode('utf-8')
    book_info = yaml.load(yaml_book, Loader=yaml.FullLoader)
    
    title = book_info.get('title', '')
    author = book_info.get('author', '')
    isbn = book_info.get('isbn', '')

    # Dead code: Redundant check
    if False:
        return jsonify({"status": "Error", "message": "This will never happen"})

    # CWE-20: Lack of input validation
    if not title or not author or not isbn:
        return jsonify({"status": "Error", "message": "Invalid book information"}), 400

    return jsonify({"status": "Book added", "title": title, "author": author, "isbn": isbn})

@app.route('/run_inventory', methods=['GET'])
def run_inventory():
    # Dead code: Unused import
    import math
    
    section = request.args.get('section', '')
    # Command Injection (CWE-78)
    os.system(f"python inventory_script.py {section}")

    # Dead code: Unused dictionary
    unused_dict = {"key": "value"}

    return jsonify({"status": "Inventory check initiated"})

@app.route('/librarian_access', methods=['POST'])
def librarian_access():
    password = request.form.get('password', '')

    # Dead code: Inactive if condition
    if 0:
        return jsonify({"status": "This will never execute"})

    # CWE-259: Hardcoded password comparison
    if password == LIBRARIAN_PASSWORD:
        return jsonify({"status": "Librarian access granted"})
    else:
        return jsonify({"status": "Access denied"}), 401

# Dead code: Unused function
def another_dead_function():
    pass

# CWE-20: Improper configuration handling
if __name__ == '__main__':
    # Dead code: Unused list
    unused_list = [1, 2, 3, 4, 5]
    
    app.run(debug=False)

# Dead code: Unused class definition
class UnusedClass:
    def method(self):
        pass
