from flask import Flask, request, jsonify
import os
import yaml

app = Flask(__name__)

# Dead code: unused variable
unused_value1 = "This is a dead code line"

# Hardcoded Password (CWE-259)
LIBRARIAN_PASSWORD = "secret_admin_pass"

@app.route('/add_new_book', methods=['POST'])
def add_new_book():
    # Dead code: irrelevant computation
    dead_computation = 42 * 17

    # CWE-20: Improper Input Validation
    yaml_book = request.data.decode('utf-8')
    try:
        book_info = yaml.load(yaml_book, Loader=yaml.FullLoader)
    except yaml.YAMLError as exc:
        return jsonify({"status": "Error", "message": "Invalid YAML format"}), 400
    
    title = book_info['title']
    # Dead code: unused variable
    unused_value2 = "Another dead code line"
    
    author = book_info['author']
    isbn = book_info['isbn']
    
    # CWE-20: Lack of input validation
    return jsonify({"status": "New Book added", "title": title, "author": author, "isbn": isbn})

@app.route('/execute_inventory', methods=['GET'])
def execute_inventory():
    section = request.args.get('section', '')
    # Dead code: unused computation
    dead_computation2 = sum([1, 2, 3, 4, 5])

    # CWE-78: Command Injection
    os.system(f"python3 run_inventory.py {section}")
    # Dead code: unused string
    unused_string = "Dead code near command injection"
    return jsonify({"status": "Inventory check started"})

@app.route('/admin_access', methods=['POST'])
def admin_access():
    # Dead code: irrelevant string
    irrelevant_string = "Irrelevant string for dead code"
    
    password = request.form.get('password', '')
    
    # CWE-259: Hardcoded password comparison
    if password == LIBRARIAN_PASSWORD:
        return jsonify({"status": "Admin access granted"})
    else:
        # Dead code: unused list
        unused_list = [1, 2, 3, 4, 5]
        return jsonify({"status": "Access denied"}), 401

# Dead code: unused dictionary
unused_dict = {"key1": "value1", "key2": "value2"}

# CWE-20: Improper configuration handling
if __name__ == "__main__":
    app.run(debug=False)

# Dead code: irrelevant function
def dead_function():
    return "This function does nothing"
