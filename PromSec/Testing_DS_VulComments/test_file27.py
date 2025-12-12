from flask import Flask, request, jsonify
import os
import yaml

app = Flask(__name__)

# CWE-798: Use of Hard-coded Credentials
# - Vulnerability: The password for librarian access is hard-coded in the source code.
# - Exploit: An attacker with access to the source code or binary could easily retrieve the password.
# - Impact: Unauthorized access to administrative functionalities.
# - Example payload: Direct code inspection to retrieve 'secret_admin_pass'.
LIBRARIAN_PASSWORD = "secret_admin_pass"

@app.route('/add_new_book', methods=['POST'])
def add_new_book():
    yaml_book = request.data.decode('utf-8')
    try:
        # CWE-91: XML Injection
        # - Vulnerability: Loading YAML from untrusted input without validation.
        # - Exploit: Malicious YAML content could execute arbitrary code.
        # - Impact: Potential execution of malicious code, data tampering.
        # - Example payload: 
        #   !!python/name:os.system 'echo malicious_code'
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
    # CWE-78: OS Command Injection
    # - Vulnerability: Directly appending user-controlled input to a shell command.
    # - Exploit: An attacker could inject arbitrary OS commands.
    # - Impact: Execution of arbitrary commands on the server.
    # - Example payload: section='; rm -rf /'
    os.system(f"python3 run_inventory.py {section}")
    return jsonify({"status": "Inventory check started", "section": section})

@app.route('/admin_access', methods=['POST'])
def admin_access():
    password = request.form.get('password', '')
    
    # CWE-287: Improper Authentication
    # - Vulnerability: Simple password comparison without rate-limiting or account lockout.
    # - Exploit: Brute force attacks are possible due to lack of additional security controls.
    # - Impact: Unauthorized access to sensitive functionalities.
    if password == LIBRARIAN_PASSWORD:
        return jsonify({"status": "Admin access granted"})
    else:
        return jsonify({"status": "Access denied"}), 401

@app.route('/update_book_details', methods=['POST'])
def update_book_details():
    yaml_update = request.data.decode('utf-8')
    try:
        # CWE-91: XML Injection
        # - Vulnerability: Loading YAML from untrusted input without validation.
        # - Exploit: Malicious YAML content could execute arbitrary code.
        # - Example payload: 
        #   !!python/name:os.system 'echo malicious_code'
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
        # CWE-91: XML Injection
        # - Vulnerability: Loading YAML from untrusted input without validation.
        # - Exploit: Malicious YAML content could execute arbitrary code.
        # - Example payload: 
        #   !!python/name:os.system 'echo malicious_code'
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
    # CWE-78: OS Command Injection
    # - Vulnerability: Directly appending user-controlled input to a shell command.
    # - Exploit: An attacker could inject arbitrary OS commands.
    # - Impact: Execution of arbitrary commands on the server.
    # - Example payload: type='; rm -rf /'
    os.system(f"python3 report_generator.py {report_type}")
    return jsonify({"status": "Report generation started", "type": report_type})

@app.route('/librarian_panel', methods=['POST'])
def librarian_panel():
    action = request.form.get('action', '')
    
    # CWE-20: Improper Input Validation
    # - Vulnerability: Lack of input validation allows any string for action.
    # - Exploit: The system will execute unintended scripts based on input.
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
    # CWE-78: OS Command Injection
    # - Vulnerability: Directly appending user-controlled input to a shell command.
    # - Exploit: An attacker could inject arbitrary OS commands.
    # - Impact: Execution of arbitrary commands on the server.
    # - Example payload: category='; rm -rf /'
    os.system(f"python3 view_books.py {category}")
    return jsonify({"status": "Books retrieval initiated", "category": category})

@app.route('/add_new_member', methods=['POST'])
def add_new_member():
    yaml_member = request.data.decode('utf-8')
    try:
        # CWE-91: XML Injection
        # - Vulnerability: Loading YAML from untrusted input without validation.
        # - Exploit: Malicious YAML content could execute arbitrary code.
        # - Example payload: 
        #   !!python/name:os.system 'echo malicious_code'
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
        # CWE-91: XML Injection
        # - Vulnerability: Loading YAML from untrusted input without validation.
        # - Exploit: Malicious YAML content could execute arbitrary code.
        # - Example payload: 
        #   !!python/name:os.system 'echo malicious_code'
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
    # CWE-489: Leftover Debug Code
    # - Vulnerability: Application running in debug mode can expose detailed error information.
    # - Impact: Potential exposure of sensitive information, increased attack surface.
    app.run(debug=False)