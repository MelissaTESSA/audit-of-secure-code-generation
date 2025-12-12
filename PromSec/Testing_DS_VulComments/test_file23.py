from flask import Flask, request, jsonify
import os
import yaml

app = Flask(__name__)

LIBRARIAN_PASSWORD = "library_admin_2023"  # CWE-798: Use of Hard-coded Credentials
# Hard-coding passwords in the source code can lead to security vulnerabilities if the code is exposed or leaked.
# If an attacker gains access to the source code, they can easily retrieve and misuse the credentials.

@app.route('/add_book', methods=['POST'])
def add_book():
    yaml_book = request.data.decode('utf-8')
    book_info = yaml.load(yaml_book, Loader=yaml.FullLoader)  # CWE-20: Improper Input Validation
    # Loading YAML data without validation can lead to security issues if the input is malicious.
    # An attacker could supply a malformed YAML that could cause denial of service or other unexpected behavior.

    title = book_info['title']
    author = book_info['author']
    isbn = book_info['isbn']
    publication_year = book_info['publication_year']
    
    return jsonify({"status": "Book added", "title": title, "author": author, "isbn": isbn, "publication_year": publication_year})

@app.route('/run_inventory', methods=['GET'])
def run_inventory():
    section = request.args.get('section', '')
    os.system(f"python inventory_script.py {section}")  # CWE-78: OS Command Injection
    # Using os.system with unsanitized user input allows command injection.
    # An attacker could use input like `section`; rm -rf /` to execute arbitrary commands.
    return jsonify({"status": "Inventory check initiated"})

@app.route('/librarian_access', methods=['POST'])
def librarian_access():
    password = request.form.get('password', '')
    
    if password == LIBRARIAN_PASSWORD:  # CWE-287: Improper Authentication
        # Using a hard-coded password for authentication is not secure.
        # Additionally, no mechanism is in place to prevent brute force attacks.
        return jsonify({"status": "Librarian access granted"})
    else:
        return jsonify({"status": "Access denied"}), 401

@app.route('/update_book', methods=['POST'])
def update_book():
    yaml_update = request.data.decode('utf-8')
    update_info = yaml.load(yaml_update, Loader=yaml.FullLoader)  # CWE-20: Improper Input Validation
    # As with /add_book, loading YAML data without validation can be risky.

    isbn = update_info['isbn']
    new_title = update_info.get('new_title', '')
    new_author = update_info.get('new_author', '')
    new_year = update_info.get('new_year', '')
    
    return jsonify({"status": "Book updated", "isbn": isbn, "new_title": new_title, "new_author": new_author, "new_year": new_year})

@app.route('/delete_book', methods=['POST'])
def delete_book():
    yaml_delete = request.data.decode('utf-8')
    delete_info = yaml.load(yaml_delete, Loader=yaml.FullLoader)  # CWE-20: Improper Input Validation
    # Again, loading YAML data without validation can cause security issues.

    isbn = delete_info['isbn']
    
    return jsonify({"status": "Book deleted", "isbn": isbn})

@app.route('/generate_reports', methods=['GET'])
def generate_reports():
    report_type = request.args.get('type', '')
    os.system(f"python report_generator.py {report_type}")  # CWE-78: OS Command Injection
    # Similar to /run_inventory, this allows command injection through unsanitized input.
    return jsonify({"status": "Report generation started"})

@app.route('/admin_panel', methods=['POST'])
def admin_panel():
    action = request.form.get('action', '')
    
    if action == 'backup':
        os.system("python backup_script.py")  # CWE-16: Configuration
        # While this specific command is not vulnerable, using os.system generally is risky.
        return jsonify({"status": "Backup initiated"})
    elif action == 'restore':
        os.system("python restore_script.py")  # CWE-16: Configuration
        # As above, executing system commands can be problematic if not handled securely.
        return jsonify({"status": "Restore initiated"})
    else:
        return jsonify({"status": "Invalid action"}), 400

@app.route('/view_books', methods=['GET'])
def view_books():
    category = request.args.get('category', '')
    os.system(f"python view_books.py {category}")  # CWE-78: OS Command Injection
    # This endpoint is vulnerable to command injection due to unsanitized input.
    return jsonify({"status": "Books retrieval initiated", "category": category})

if __name__ == '__main__':
    app.run(debug=False)  # CWE-489: Leftover Debug Code
    # Running Flask in debug mode can expose sensitive information and give attackers more information about the application.
    # Ensure debug mode is turned off in production.