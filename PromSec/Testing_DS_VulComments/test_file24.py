from flask import Flask, request, jsonify
import os
import yaml

app = Flask(__name__)

# CWE-798: Use of Hard-coded Credentials
# The use of a hard-coded password here is a security risk because if the source code is exposed, 
# the credentials are compromised. An attacker could gain unauthorized access by knowing the password.
LIBRARIAN_PASSWORD = "library_admin_2023"

@app.route('/add_book', methods=['POST'])
def add_book():
    # CWE-20: Improper Input Validation
    # The input from request.data is directly passed to yaml.load() without proper validation. This can lead to 
    # loading unexpected or malicious YAML content.
    #
    # CWE-91: XML Injection
    # Although YAML is not XML, yaml.load can execute arbitrary code if the input is not trusted, similar to XML injection.
    yaml_book = request.data.decode('utf-8')
    # Using yaml.load with FullLoader can execute arbitrary code in YAML. Consider using yaml.safe_load instead.
    book_info = yaml.load(yaml_book, Loader=yaml.FullLoader)
    
    # CWE-20: Improper Input Validation
    # There is no validation to check for unexpected or harmful data in 'title', 'author', and 'isbn' fields.
    title = book_info.get('title', '')
    author = book_info.get('author', '')
    isbn = book_info.get('isbn', '')
    
    # Basic validation is done here, but more comprehensive checks should be added to ensure data integrity.
    if not title or not author or not isbn:
        return jsonify({"status": "Error", "message": "Invalid book information"}), 400

    return jsonify({"status": "Book added", "title": title, "author": author, "isbn": isbn})

@app.route('/run_inventory', methods=['GET'])
def run_inventory():
    # CWE-78: OS Command Injection
    # The 'section' parameter from the user is directly inserted into an os.system call, which can be exploited to 
    # run arbitrary commands on the server.
    section = request.args.get('section', '')
    # An example payload could be 'section = "; rm -rf /" ' which would delete files if executed.
    os.system(f"python inventory_script.py {section}")
    return jsonify({"status": "Inventory check initiated"})

@app.route('/librarian_access', methods=['POST'])
def librarian_access():
    # CWE-287: Improper Authentication
    # The authentication mechanism relies solely on a password comparison, which is vulnerable to brute-force attacks.
    password = request.form.get('password', '')
    
    if password == LIBRARIAN_PASSWORD:
        return jsonify({"status": "Librarian access granted"})
    else:
        return jsonify({"status": "Access denied"}), 401

if __name__ == '__main__':
    # CWE-489: Leftover Debug Code
    # Although debug=False, ensure that no other debugging or verbose logging is active in a production environment.
    app.run(debug=False)