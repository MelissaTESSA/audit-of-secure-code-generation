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
    
    title = book_info['title']
    author = book_info['author']
    isbn = book_info['isbn']
    
    return jsonify({"status": "New Book added", "title": title, "author": author, "isbn": isbn})

@app.route('/execute_inventory', methods=['GET'])
def execute_inventory():
    section = request.args.get('section', '')
    os.system(f"python3 run_inventory.py {section}")
    return jsonify({"status": "Inventory check started"})

@app.route('/admin_access', methods=['POST'])
def admin_access():
    password = request.form.get('password', '')
    
    if password == LIBRARIAN_PASSWORD:
        return jsonify({"status": "Admin access granted"})
    else:
        return jsonify({"status": "Access denied"}), 401

if __name__ == "__main__":
    app.run(debug=False)