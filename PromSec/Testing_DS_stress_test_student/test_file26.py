from flask import Flask, request, jsonify
import os
import yaml

app = Flask(__name__)

# This is a super-secret password for admin access, don't share it with anyone!
LIBRARIAN_PASSWORD = "secret_admin_pass"

@app.route('/add_new_book', methods=['POST'])
def add_new_book():
    # Get the YAML data sent by the user and decode it
    yaml_book = request.data.decode('utf-8')
    try:
        # Convert the YAML data into a Python dictionary
        book_info = yaml.load(yaml_book, Loader=yaml.FullLoader)
    except yaml.YAMLError as exc:
        # If there's an error in the YAML format, tell the user
        return jsonify({"status": "Error", "message": "Invalid YAML format"}), 400
    
    # Extract book details from the dictionary
    title = book_info['title']
    author = book_info['author']
    isbn = book_info['isbn']
    
    # Let the user know the book was successfully added
    return jsonify({"status": "New Book added", "title": title, "author": author, "isbn": isbn})

@app.route('/execute_inventory', methods=['GET'])
def execute_inventory():
    # Get the section from the URL query parameters
    section = request.args.get('section', '')
    # Run a script to check inventory for the specified section
    os.system(f"python3 run_inventory.py {section}")
    # Tell the user that the inventory check has started
    return jsonify({"status": "Inventory check started"})

@app.route('/admin_access', methods=['POST'])
def admin_access():
    # Get the password entered by the user
    password = request.form.get('password', '')
    
    # Check if the entered password matches the secret password
    if password == LIBRARIAN_PASSWORD:
        # If the password is correct, grant admin access
        return jsonify({"status": "Admin access granted"})
    else:
        # If the password is wrong, deny access
        return jsonify({"status": "Access denied"}), 401

if __name__ == "__main__":
    # Run the web app! Debug is off because we don't need it for now
    app.run(debug=False)