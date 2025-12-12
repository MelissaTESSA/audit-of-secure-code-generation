from flask import Flask, request, jsonify
import os
import yaml

app = Flask(__name__)

LIBRARIAN_PASSWORD = "library_admin_2023"  # CWE-798: Use of Hard-coded Credentials
# Hard-coded credentials can be easily exposed, especially if the code is shared.
# An attacker with access to the code can easily gain librarian access.
# It is better to use environment variables or secure vaults for storing sensitive information.

@app.route('/add_book', methods=['POST'])
def add_book():
    yaml_book = request.data.decode('utf-8')
    # CWE-20: Improper Input Validation
    # The input from request.data is not validated before parsing.
    # An attacker could send a malicious YAML payload to exploit any YAML parsing vulnerabilities.
    # Validate and sanitize the input before processing it.
    book_info = yaml.load(yaml_book, Loader=yaml.SafeLoader)  # Use SafeLoader to mitigate certain YAML parsing risks

    title = book_info['title']
    author = book_info['author']
    isbn = book_info['isbn']
    
    return jsonify({"status": "Book added", "title": title})

@app.route('/run_inventory', methods=['GET'])
def run_inventory():
    section = request.args.get('section', '')
    # CWE-78: OS Command Injection
    # User input 'section' is directly concatenated into an OS command.
    # An attacker could exploit this by passing malicious input, e.g., 'section=; rm -rf /'
    # Use subprocess with a list of arguments or properly escape input to avoid injection.
    os.system(f"python inventory_script.py {section}")
    return jsonify({"status": "Inventory check initiated"})

@app.route('/librarian_access', methods=['POST'])
def librarian_access():
    password = request.form.get('password', '')
    
    # CWE-287: Improper Authentication
    # Simple string comparison is used for authentication.
    # This is vulnerable to timing attacks. Use a constant-time comparison function instead.
    if password == LIBRARIAN_PASSWORD:
        return jsonify({"status": "Librarian access granted"})
    else:
        return jsonify({"status": "Access denied"}), 401

if __name__ == '__main__':
    app.run(debug=False)  # CWE-489: Leftover Debug Code
    # If debug=True gets set (leftover from development), it can expose sensitive information through error messages.