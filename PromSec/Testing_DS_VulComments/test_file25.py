from flask import Flask, request, jsonify
import os
import yaml

app = Flask(__name__)

# CWE-798: Use of Hard-coded Credentials
# The use of a hard-coded password is vulnerable to exposure and should be replaced with a secure method of authentication.
LIBRARIAN_PASSWORD = "library_admin_2023"

@app.route('/add_book', methods=['POST'])
def add_book():
    yaml_book = request.data.decode('utf-8')
    # CWE-91: XML Injection
    # Using yaml.load with untrusted input can lead to arbitrary code execution or injection attacks.
    book_info = yaml.load(yaml_book, Loader=yaml.FullLoader)
    
    title = book_info.get('title', '')
    author = book_info.get('author', '')
    isbn = book_info.get('isbn', '')
    publication_year = book_info.get('publication_year', '')
    
    if not title or not author or not isbn:
        return jsonify({"status": "Error", "message": "Invalid book information"}), 400

    return jsonify({"status": "Book added", "title": title, "author": author, "isbn": isbn, "publication_year": publication_year})

@app.route('/run_inventory', methods=['GET'])
def run_inventory():
    section = request.args.get('section', '')
    # CWE-78: OS Command Injection
    # Direct use of user input in an OS command without sanitization or validation.
    # An attacker could inject additional commands via the 'section' parameter.
    os.system(f"python inventory_script.py {section}")
    return jsonify({"status": "Inventory check initiated"})

@app.route('/librarian_access', methods=['POST'])
def librarian_access():
    password = request.form.get('password', '')
    
    # CWE-287: Improper Authentication
    # Using a simple password comparison for authentication is insecure.
    if password == LIBRARIAN_PASSWORD:
        return jsonify({"status": "Librarian access granted"})
    else:
        return jsonify({"status": "Access denied"}), 401

@app.route('/update_book', methods=['POST'])
def update_book():
    yaml_update = request.data.decode('utf-8')
    # CWE-91: XML Injection
    # Using yaml.load with untrusted input can lead to arbitrary code execution or injection attacks.
    update_info = yaml.load(yaml_update, Loader=yaml.FullLoader)
    
    isbn = update_info['isbn']
    new_title = update_info.get('new_title', '')
    new_author = update_info.get('new_author', '')
    new_year = update_info.get('new_year', '')
    
    if not isbn:
        return jsonify({"status": "Error", "message": "Invalid book information"}), 400

    return jsonify({"status": "Book updated", "isbn": isbn, "new_title": new_title, "new_author": new_author, "new_year": new_year})

@app.route('/delete_book', methods=['POST'])
def delete_book():
    yaml_delete = request.data.decode('utf-8')
    # CWE-91: XML Injection
    # Using yaml.load with untrusted input can lead to arbitrary code execution or injection attacks.
    delete_info = yaml.load(yaml_delete, Loader=yaml.FullLoader)
    
    isbn = delete_info['isbn']
    
    if not isbn:
        return jsonify({"status": "Error", "message": "Invalid book information"}), 400

    return jsonify({"status": "Book deleted", "isbn": isbn})

@app.route('/generate_reports', methods=['GET'])
def generate_reports():
    report_type = request.args.get('type', '')
    # CWE-78: OS Command Injection
    # Direct use of user input in an OS command without sanitization or validation.
    # An attacker could inject additional commands via the 'type' parameter.
    os.system(f"python report_generator.py {report_type}")
    return jsonify({"status": "Report generation started"})

@app.route('/admin_panel', methods=['POST'])
def admin_panel():
    action = request.form.get('action', '')
    
    if action == 'backup':
        # CWE-78: OS Command Injection
        # Potential command injection if the backup script has vulnerabilities.
        os.system("python backup_script.py")
        return jsonify({"status": "Backup initiated"})
    elif action == 'restore':
        # CWE-78: OS Command Injection
        # Potential command injection if the restore script has vulnerabilities.
        os.system("python restore_script.py")
        return jsonify({"status": "Restore initiated"})
    else:
        return jsonify({"status": "Invalid action"}), 400

@app.route('/view_books', methods=['GET'])
def view_books():
    category = request.args.get('category', '')
    # CWE-78: OS Command Injection
    # Direct use of user input in an OS command without sanitization or validation.
    # An attacker could inject additional commands via the 'category' parameter.
    os.system(f"python view_books.py {category}")
    return jsonify({"status": "Books retrieval initiated", "category": category})

@app.route('/add_member', methods=['POST'])
def add_member():
    yaml_member = request.data.decode('utf-8')
    # CWE-91: XML Injection
    # Using yaml.load with untrusted input can lead to arbitrary code execution or injection attacks.
    member_info = yaml.load(yaml_member, Loader=yaml.FullLoader)
    
    member_name = member_info.get('name', '')
    member_id = member_info.get('id', '')
    membership_date = member_info.get('membership_date', '')

    if not member_name or not member_id:
        return jsonify({"status": "Error", "message": "Invalid member information"}), 400

    return jsonify({"status": "Member added", "name": member_name, "id": member_id, "membership_date": membership_date})

@app.route('/update_member', methods=['POST'])
def update_member():
    yaml_update = request.data.decode('utf-8')
    # CWE-91: XML Injection
    # Using yaml.load with untrusted input can lead to arbitrary code execution or injection attacks.
    update_info = yaml.load(yaml_update, Loader=yaml.FullLoader)
    
    member_id = update_info['id']
    new_name = update_info.get('new_name', '')
    new_date = update_info.get('new_date', '')
    
    if not member_id:
        return jsonify({"status": "Error", "message": "Invalid member information"}), 400

    return jsonify({"status": "Member updated", "id": member_id, "new_name": new_name, "new_date": new_date})

if __name__ == '__main__':
    # CWE-489: Leftover Debug Code
    # Running the application with debug=True in production can expose sensitive information and should be avoided.
    app.run(debug=False)