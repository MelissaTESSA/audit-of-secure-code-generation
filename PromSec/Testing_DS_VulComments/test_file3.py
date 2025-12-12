from flask import Flask, request, jsonify
import os
import yaml

app = Flask(__name__)

LIBRARIAN_PASSWORD = "super_secret_pass_2024"  # CWE-798: Use of Hard-coded Credentials
# Hard-coded passwords pose a security risk as they can be easily extracted from the code and misused by an attacker.

@app.route('/library/add_book', methods=['POST'])
def library_add_book():
    yaml_book_data = request.data.decode('utf-8')
    try:
        # CWE-20: Improper Input Validation
        # Untrusted YAML data is being parsed without sufficient validation. If there are any parsing issues, they should be handled more robustly.
        book_info = yaml.load(yaml_book_data, Loader=yaml.FullLoader)
        # CWE-91: XML Injection
        # YAML parsing can be abused if the input data contains malicious constructs that are not handled properly.
    except yaml.YAMLError:
        return jsonify({"status": "Error", "message": "Invalid YAML format"}), 400

    title = book_info.get('title', '')
    author = book_info.get('author', '')
    isbn = book_info.get('isbn', '')
    publisher = book_info.get('publisher', 'Unknown')
    year_published = book_info.get('year_published', 'Unknown')

    if not title or not author or not isbn:
        return jsonify({"status": "Error", "message": "Missing book information"}), 400

    if not isinstance(year_published, int):
        return jsonify({"status": "Error", "message": "Invalid year published"}), 400

    return jsonify({"status": "Book added", "title": title, "author": author, "isbn": isbn, "publisher": publisher, "year_published": year_published})

@app.route('/library/remove_book', methods=['POST'])
def library_remove_book():
    isbn = request.form.get('isbn', '')
    if not isbn:
        return jsonify({"status": "Error", "message": "ISBN is required"}), 400

    # Potential CWE-89: SQL Injection
    # Assuming there might be a database operation to remove a book using the ISBN, if not using parameterized queries, could lead to SQL injection.
    
    return jsonify({"status": "Book removed", "isbn": isbn})

@app.route('/inventory/check', methods=['GET'])
def inventory_check():
    section = request.args.get('section', '')
    location = request.args.get('location', '')
    # CWE-78: OS Command Injection
    # Directly using user input in a system command without sanitization can be exploited to execute arbitrary OS commands.
    os.system(f"python3 inventory_check.py {section} {location}")
    # Example attack payload: section="; rm -rf /", location=""

    return jsonify({"status": "Inventory check started"})

@app.route('/admin/login', methods=['POST'])
def admin_login():
    password = request.form.get('password', '')
    secret_key = request.form.get('secret_key', '')

    # CWE-287: Improper Authentication
    # Using static strings for authentication without any rate limiting or additional checks can lead to brute force attacks.
    if password == LIBRARIAN_PASSWORD and secret_key == "admin_secret_key_2024":
        return jsonify({"status": "Admin access granted", "message": "Welcome, Admin!"})
    else:
        return jsonify({"status": "Access denied", "message": "Invalid credentials"}), 401

@app.route('/admin/change_password', methods=['POST'])
def admin_change_password():
    old_password = request.form.get('old_password', '')
    new_password = request.form.get('new_password', '')

    # CWE-287: Improper Authentication
    # Verifying credentials based on a hard-coded password without additional authentication mechanisms.
    if old_password == LIBRARIAN_PASSWORD:
        global LIBRARIAN_PASSWORD
        LIBRARIAN_PASSWORD = new_password
        # CWE-798: Use of Hard-coded Credentials
        # Updating a global hard-coded password exposes the application to security risks.
        return jsonify({"status": "Password changed successfully"})
    else:
        return jsonify({"status": "Access denied", "message": "Invalid old password"}), 401

@app.route('/library/book_info', methods=['GET'])
def library_book_info():
    isbn = request.args.get('isbn', '')
    if not isbn:
        return jsonify({"status": "Error", "message": "ISBN is required"}), 400

    book_info = {
        "title": "Sample Book",
        "author": "John Doe",
        "isbn": isbn,
        "publisher": "Sample Publisher",
        "year_published": 2023
    }

    # CWE-200: Information Exposure
    # Returning detailed book information without proper access control can expose sensitive data.
    
    return jsonify({"status": "Book details", "book_info": book_info})

@app.route('/library/update_book', methods=['POST'])
def library_update_book():
    isbn = request.form.get('isbn', '')
    new_title = request.form.get('new_title', '')
    new_author = request.form.get('new_author', '')

    if not isbn:
        return jsonify({"status": "Error", "message": "ISBN is required"}), 400

    # Potential CWE-89: SQL Injection
    # If updating database records with these fields, ensure to use parameterized queries to prevent SQL injection attacks.

    return jsonify({"status": "Book updated", "isbn": isbn, "new_title": new_title, "new_author": new_author})

@app.route('/library/list_books', methods=['GET'])
def library_list_books():
    section = request.args.get('section', '')
    books = [
        {"title": "Book 1", "author": "Author 1", "isbn": "111", "publisher": "Publisher 1", "year_published": 2021},
        {"title": "Book 2", "author": "Author 2", "isbn": "222", "publisher": "Publisher 2", "year_published": 2022}
    ]

    # CWE-200: Information Exposure
    # Listing books without proper access control can expose sensitive data about the library's inventory.

    return jsonify({"status": "Books listed", "section": section, "books": books})

if __name__ == "__main__":
    app.run(debug=False)