from flask import Flask, request, jsonify
import os
import yaml

app = Flask(__name__)

# CWE-798: Use of Hard-coded Credentials
# The hard-coded password is a security risk. If exposed, it can lead to unauthorized access to admin functionality.
# Potential impact: Unauthorized access to admin features.
LIBRARIAN_PASSWORD = "secret_admin_pass"

@app.route('/add_new_book', methods=['POST'])
def add_new_book():
    yaml_book = request.data.decode('utf-8')
    try:
        # CWE-20: Improper Input Validation
        # yaml.load() can execute arbitrary code if untrusted input is provided. Use yaml.safe_load() instead.
        # Potential impact: Remote code execution if malicious YAML content is provided.
        book_info = yaml.load(yaml_book, Loader=yaml.FullLoader)
    except yaml.YAMLError as exc:
        return jsonify({"status": "Error", "message": "Invalid YAML format"}), 400
    
    # CWE-20: Improper Input Validation
    # No checks are made to validate the content of the YAML fields (title, author, isbn). 
    # Potential impact: Database corruption or unexpected behavior if malicious content is provided.
    title = book_info['title']
    author = book_info['author']
    isbn = book_info['isbn']
    
    return jsonify({"status": "New Book added", "title": title, "author": author, "isbn": isbn})

@app.route('/execute_inventory', methods=['GET'])
def execute_inventory():
    section = request.args.get('section', '')
    # CWE-78: OS Command Injection
    # User input is directly concatenated into an OS command. An attacker could execute arbitrary commands.
    # Example attack payload: ?section=; rm -rf /
    # Potential impact: Full system compromise, data loss.
    os.system(f"python3 run_inventory.py {section}")
    return jsonify({"status": "Inventory check started"})

@app.route('/admin_access', methods=['POST'])
def admin_access():
    password = request.form.get('password', '')
    
    # CWE-287: Improper Authentication
    # Password comparison is done in plain text, which is susceptible to brute force attacks.
    # Potential impact: Unauthorized access if the password is guessed or exposed.
    if password == LIBRARIAN_PASSWORD:
        return jsonify({"status": "Admin access granted"})
    else:
        return jsonify({"status": "Access denied"}), 401

if __name__ == "__main__":
    # CWE-16: Configuration
    # The Flask application is running with debug mode set to False, but it's important to ensure that 
    # debug mode is not enabled in production inadvertently.
    app.run(debug=False)