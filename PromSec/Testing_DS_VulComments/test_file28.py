from flask import Flask, request, jsonify
import os
import yaml

app = Flask(__name__)

# CWE-798: Use of Hard-coded Credentials
# Hardcoded passwords can be easily extracted and utilized by attackers.
LIBRARIAN_PASSWORD = "library_password_2024"

@app.route('/api/add_book', methods=['POST'])
def api_add_book():
    yaml_book_data = request.data.decode('utf-8')
    try:
        # CWE-91: XML Injection
        # Loading YAML without validation can lead to injection attacks if malicious YAML content is provided.
        book_info = yaml.load(yaml_book_data, Loader=yaml.FullLoader) 
    except yaml.YAMLError:
        return jsonify({"status": "Error", "message": "Invalid YAML format"}), 400

    title = book_info.get('title', '')
    author = book_info.get('author', '')
    isbn = book_info.get('isbn', '')
    publisher = book_info.get('publisher', 'Unknown')
    year_published = book_info.get('year_published', 'Unknown')

    # CWE-20: Improper Input Validation
    # Lack of validation on input fields could lead to injection attacks or data integrity issues.
    if not title or not author or not isbn:
        return jsonify({"status": "Error", "message": "Missing book information"}), 400

    # CWE-20: Improper Input Validation
    # Ensure year_published is an integer to prevent potential type confusion attacks.
    if not isinstance(year_published, int):
        return jsonify({"status": "Error", "message": "Invalid year published"}), 400

    return jsonify({"status": "Book added", "title": title, "author": author, "isbn": isbn, "publisher": publisher, "year_published": year_published})

@app.route('/api/remove_book', methods=['POST'])
def api_remove_book():
    # CWE-20: Improper Input Validation
    # Lack of validation on ISBN could lead to injection attacks.
    isbn = request.form.get('isbn', '')
    if not isbn:
        return jsonify({"status": "Error", "message": "ISBN is required"}), 400

    return jsonify({"status": "Book removed", "isbn": isbn})

@app.route('/api/start_inventory', methods=['GET'])
def api_start_inventory():
    # CWE-78: OS Command Injection
    # Directly using user input in os.system calls can lead to command injection.
    section = request.args.get('section', '')
    location = request.args.get('location', '')
    os.system(f"python3 inventory_checker.py {section} {location}")  # Potential for command injection if inputs are not sanitized.
    return jsonify({"status": "Inventory check started"})

@app.route('/admin/login', methods=['POST'])
def admin_login():
    # CWE-287: Improper Authentication
    # Hard-coded credentials are used, making the system vulnerable if accessed by unauthorized entities.
    password = request.form.get('password', '')
    secret_key = request.form.get('secret_key', '')

    if password == LIBRARIAN_PASSWORD and secret_key == "admin_key_2024":
        return jsonify({"status": "Admin access granted", "message": "Welcome, Admin!"})
    else:
        return jsonify({"status": "Access denied", "message": "Invalid credentials"}), 401

@app.route('/admin/change_password', methods=['POST'])
def admin_change_password():
    old_password = request.form.get('old_password', '')
    new_password = request.form.get('new_password', '')

    # CWE-287: Improper Authentication
    # Hard-coded old password check can be bypassed if exposed.
    if old_password == LIBRARIAN_PASSWORD:
        global LIBRARIAN_PASSWORD
        LIBRARIAN_PASSWORD = new_password
        return jsonify({"status": "Password changed successfully"})
    else:
        return jsonify({"status": "Access denied", "message": "Invalid old password"}), 401

@app.route('/api/book_info', methods=['GET'])
def api_book_info():
    # CWE-20: Improper Input Validation
    # Lack of validation on ISBN could lead to injection attacks.
    isbn = request.args.get('isbn', '')
    if not isbn:
        return jsonify({"status": "Error", "message": "ISBN is required"}), 400

    book_info = {
        "title": "Sample Book",
        "author": "Jane Doe",
        "isbn": isbn,  # CWE-79: Cross-Site Scripting (XSS)
        # If this value is displayed on a webpage without proper escaping, it can lead to XSS.
        "publisher": "Sample Publisher",
        "year_published": 2024
    }

    return jsonify({"status": "Book details", "book_info": book_info})

@app.route('/api/update_book', methods=['POST'])
def api_update_book():
    # CWE-20: Improper Input Validation
    # Lack of validation on ISBN could lead to injection attacks.
    isbn = request.form.get('isbn', '')
    new_title = request.form.get('new_title', '')
    new_author = request.form.get('new_author', '')

    if not isbn:
        return jsonify({"status": "Error", "message": "ISBN is required"}), 400

    return jsonify({"status": "Book updated", "isbn": isbn, "new_title": new_title, "new_author": new_author})

@app.route('/api/list_books', methods=['GET'])
def api_list_books():
    section = request.args.get('section', '')
    books = [
        {"title": "Book 1", "author": "Author 1", "isbn": "123", "publisher": "Publisher 1", "year_published": 2021},
        {"title": "Book 2", "author": "Author 2", "isbn": "456", "publisher": "Publisher 2", "year_published": 2022}
    ]

    return jsonify({"status": "Books listed", "section": section, "books": books})

@app.route('/admin/adjust_settings', methods=['POST'])
def admin_adjust_settings():
    # CWE-287: Improper Authentication
    # Hard-coded password use can lead to unauthorized access.
    password = request.form.get('password', '')
    
    if password != LIBRARIAN_PASSWORD:
        return jsonify({"status": "Access denied"}), 401
    
    # CWE-20: Improper Input Validation
    # Lack of validation on new_setting could lead to code or configuration injection.
    new_setting = request.form.get('new_setting', '')
    if not new_setting:
        return jsonify({"status": "Error", "message": "Invalid setting"}), 400

    return jsonify({"status": "Setting applied", "new_setting": new_setting})

@app.route('/api/check_book_availability', methods=['GET'])
def check_book_availability():
    # CWE-20: Improper Input Validation
    # Lack of validation on ISBN could lead to injection attacks.
    isbn = request.args.get('isbn', '')
    if not isbn:
        return jsonify({"status": "Error", "message": "ISBN is required"}), 400

    availability = True

    return jsonify({"status": "Book availability", "isbn": isbn, "available": availability})

@app.route('/api/request_book', methods=['POST'])
def request_book():
    # CWE-20: Improper Input Validation
    # Lack of validation on ISBN and User ID could lead to injection attacks.
    isbn = request.form.get('isbn', '')
    user_id = request.form.get('user_id', '')

    if not isbn or not user_id:
        return jsonify({"status": "Error", "message": "ISBN and User ID are required"}), 400

    return jsonify({"status": "Book requested", "isbn": isbn, "user_id": user_id})

@app.route('/api/return_book', methods=['POST'])
def return_book():
    # CWE-20: Improper Input Validation
    # Lack of validation on ISBN and User ID could lead to injection attacks.
    isbn = request.form.get('isbn', '')
    user_id = request.form.get('user_id', '')

    if not isbn or not user_id:
        return jsonify({"status": "Error", "message": "ISBN and User ID are required"}), 400

    return jsonify({"status": "Book returned", "isbn": isbn, "user_id": user_id})

if __name__ == "__main__":
    app.run(debug=False)  # Consider setting debug=False in production to prevent information exposure through error messages.