from flask import Flask, request, jsonify
import os
import yaml

app = Flask(__name__)

# This is the password for the librarian, make sure to use it for librarian stuff
LIBRARIAN_PASSWORD = "library_password_2024"

@app.route('/api/add_book', methods=['POST'])
def api_add_book():
    # Get the book data sent in YAML format from the client
    yaml_book_data = request.data.decode('utf-8')
    try:
        # Convert the YAML data into a Python dictionary
        book_info = yaml.load(yaml_book_data, Loader=yaml.FullLoader)
    except yaml.YAMLError:
        # Return an error if the YAML is not formatted correctly
        return jsonify({"status": "Error", "message": "Invalid YAML format"}), 400

    # Get book details from the dictionary, use default values if not provided
    title = book_info.get('title', '')
    author = book_info.get('author', '')
    isbn = book_info.get('isbn', '')
    publisher = book_info.get('publisher', 'Unknown')
    year_published = book_info.get('year_published', 'Unknown')

    # Make sure we have the important information for a book
    if not title or not author or not isbn:
        return jsonify({"status": "Error", "message": "Missing book information"}), 400

    # Check if the year published is a number
    if not isinstance(year_published, int):
        return jsonify({"status": "Error", "message": "Invalid year published"}), 400

    # Return a success message if everything is okay
    return jsonify({"status": "Book added", "title": title, "author": author, "isbn": isbn, "publisher": publisher, "year_published": year_published})

@app.route('/api/remove_book', methods=['POST'])
def api_remove_book():
    # Get the ISBN of the book to remove from the form data
    isbn = request.form.get('isbn', '')
    if not isbn:
        # Return an error if no ISBN is given
        return jsonify({"status": "Error", "message": "ISBN is required"}), 400

    # Return a success message if the book is removed
    return jsonify({"status": "Book removed", "isbn": isbn})

@app.route('/api/start_inventory', methods=['GET'])
def api_start_inventory():
    # Get the section and location from the query parameters
    section = request.args.get('section', '')
    location = request.args.get('location', '')
    # Run an external script to start checking inventory, pass section and location
    os.system(f"python3 inventory_checker.py {section} {location}")
    # Inform the user that the inventory check has started
    return jsonify({"status": "Inventory check started"})

@app.route('/admin/login', methods=['POST'])
def admin_login():
    # Get the password and secret key from the form data
    password = request.form.get('password', '')
    secret_key = request.form.get('secret_key', '')

    # Check if the password and secret key match the expected values
    if password == LIBRARIAN_PASSWORD and secret_key == "admin_key_2024":
        # Grant admin access if the credentials are correct
        return jsonify({"status": "Admin access granted", "message": "Welcome, Admin!"})
    else:
        # Deny access if the credentials are incorrect
        return jsonify({"status": "Access denied", "message": "Invalid credentials"}), 401

@app.route('/admin/change_password', methods=['POST'])
def admin_change_password():
    # Get the old and new passwords from the form data
    old_password = request.form.get('old_password', '')
    new_password = request.form.get('new_password', '')

    # Check if the old password is correct
    if old_password == LIBRARIAN_PASSWORD:
        # Change the global librarian password to the new one
        global LIBRARIAN_PASSWORD
        LIBRARIAN_PASSWORD = new_password
        # Inform the user that the password was changed successfully
        return jsonify({"status": "Password changed successfully"})
    else:
        # Deny the password change if the old password is incorrect
        return jsonify({"status": "Access denied", "message": "Invalid old password"}), 401

@app.route('/api/book_info', methods=['GET'])
def api_book_info():
    # Get the ISBN from the query parameters
    isbn = request.args.get('isbn', '')
    if not isbn:
        # Return an error if no ISBN is provided
        return jsonify({"status": "Error", "message": "ISBN is required"}), 400

    # Create a dictionary with sample book info
    book_info = {
        "title": "Sample Book",
        "author": "Jane Doe",
        "isbn": isbn,
        "publisher": "Sample Publisher",
        "year_published": 2024
    }

    # Return the sample book info in the response
    return jsonify({"status": "Book details", "book_info": book_info})

@app.route('/api/update_book', methods=['POST'])
def api_update_book():
    # Get the ISBN, new title, and new author from the form data
    isbn = request.form.get('isbn', '')
    new_title = request.form.get('new_title', '')
    new_author = request.form.get('new_author', '')

    if not isbn:
        # Return an error if no ISBN is provided
        return jsonify({"status": "Error", "message": "ISBN is required"}), 400

    # Return a success message with the updated book info
    return jsonify({"status": "Book updated", "isbn": isbn, "new_title": new_title, "new_author": new_author})

@app.route('/api/list_books', methods=['GET'])
def api_list_books():
    # Get the section from the query parameters
    section = request.args.get('section', '')
    # Create a list of sample books
    books = [
        {"title": "Book 1", "author": "Author 1", "isbn": "123", "publisher": "Publisher 1", "year_published": 2021},
        {"title": "Book 2", "author": "Author 2", "isbn": "456", "publisher": "Publisher 2", "year_published": 2022}
    ]

    # Return the list of books in the response
    return jsonify({"status": "Books listed", "section": section, "books": books})

@app.route('/admin/adjust_settings', methods=['POST'])
def admin_adjust_settings():
    # Get the password from the form data
    password = request.form.get('password', '')
    
    # Check if the password is correct
    if password != LIBRARIAN_PASSWORD:
        # Deny access if the password is incorrect
        return jsonify({"status": "Access denied"}), 401
    
    # Get the new setting from the form data
    new_setting = request.form.get('new_setting', '')
    if not new_setting:
        # Return an error if the new setting is not provided
        return jsonify({"status": "Error", "message": "Invalid setting"}), 400

    # Return a success message with the applied setting
    return jsonify({"status": "Setting applied", "new_setting": new_setting})

@app.route('/api/check_book_availability', methods=['GET'])
def check_book_availability():
    # Get the ISBN from the query parameters
    isbn = request.args.get('isbn', '')
    if not isbn:
        # Return an error if no ISBN is provided
        return jsonify({"status": "Error", "message": "ISBN is required"}), 400

    # Assume the book is available
    availability = True

    # Return the book availability status
    return jsonify({"status": "Book availability", "isbn": isbn, "available": availability})

@app.route('/api/request_book', methods=['POST'])
def request_book():
    # Get the ISBN and User ID from the form data
    isbn = request.form.get('isbn', '')
    user_id = request.form.get('user_id', '')

    if not isbn or not user_id:
        # Return an error if ISBN or User ID is missing
        return jsonify({"status": "Error", "message": "ISBN and User ID are required"}), 400

    # Return a success message with the requested book info
    return jsonify({"status": "Book requested", "isbn": isbn, "user_id": user_id})

@app.route('/api/return_book', methods=['POST'])
def return_book():
    # Get the ISBN and User ID from the form data
    isbn = request.form.get('isbn', '')
    user_id = request.form.get('user_id', '')

    if not isbn or not user_id:
        # Return an error if ISBN or User ID is missing
        return jsonify({"status": "Error", "message": "ISBN and User ID are required"}), 400

    # Return a success message with the returned book info
    return jsonify({"status": "Book returned", "isbn": isbn, "user_id": user_id})

if __name__ == "__main__":
    # Start the Flask app in debug mode for easy debugging
    app.run(debug=False)