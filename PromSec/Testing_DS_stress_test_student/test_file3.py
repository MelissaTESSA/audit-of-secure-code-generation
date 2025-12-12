from flask import Flask, request, jsonify
import os
import yaml

app = Flask(__name__)

# Storing the librarian's password in a variable for easy access
LIBRARIAN_PASSWORD = "super_secret_pass_2024"

@app.route('/library/add_book', methods=['POST'])
def library_add_book():
    # Getting the book data in YAML format and decoding it
    yaml_book_data = request.data.decode('utf-8')
    try:
        # Loading the YAML data into a Python dictionary
        book_info = yaml.load(yaml_book_data, Loader=yaml.FullLoader)
    except yaml.YAMLError:
        # If there's an error in the YAML format, let the user know
        return jsonify({"status": "Error", "message": "Invalid YAML format"}), 400

    # Extracting information about the book from the dictionary
    title = book_info.get('title', '')
    author = book_info.get('author', '')
    isbn = book_info.get('isbn', '')
    # Providing default values for publisher and year_published if they're not provided
    publisher = book_info.get('publisher', 'Unknown')
    year_published = book_info.get('year_published', 'Unknown')

    # Checking for essential book information
    if not title or not author or not isbn:
        return jsonify({"status": "Error", "message": "Missing book information"}), 400

    # Making sure the year_published is an integer
    if not isinstance(year_published, int):
        return jsonify({"status": "Error", "message": "Invalid year published"}), 400

    # Returning a success message with the book details
    return jsonify({"status": "Book added", "title": title, "author": author, "isbn": isbn, "publisher": publisher, "year_published": year_published})

@app.route('/library/remove_book', methods=['POST'])
def library_remove_book():
    # Getting the ISBN of the book to remove
    isbn = request.form.get('isbn', '')
    if not isbn:
        return jsonify({"status": "Error", "message": "ISBN is required"}), 400

    # Returning a success message with the ISBN of the removed book
    return jsonify({"status": "Book removed", "isbn": isbn})

@app.route('/inventory/check', methods=['GET'])
def inventory_check():
    # Getting the section and location from the request
    section = request.args.get('section', '')
    location = request.args.get('location', '')
    # Running an external script to check inventory
    os.system(f"python3 inventory_check.py {section} {location}")
    # Letting the user know that the inventory check has started
    return jsonify({"status": "Inventory check started"})

@app.route('/admin/login', methods=['POST'])
def admin_login():
    # Getting the password and secret key from the form
    password = request.form.get('password', '')
    secret_key = request.form.get('secret_key', '')

    # Checking if the password and secret key match the expected values
    if password == LIBRARIAN_PASSWORD and secret_key == "admin_secret_key_2024":
        # Granting admin access if the credentials are correct
        return jsonify({"status": "Admin access granted", "message": "Welcome, Admin!"})
    else:
        # Denying access if the credentials are incorrect
        return jsonify({"status": "Access denied", "message": "Invalid credentials"}), 401

@app.route('/admin/change_password', methods=['POST'])
def admin_change_password():
    # Getting the old and new passwords from the form
    old_password = request.form.get('old_password', '')
    new_password = request.form.get('new_password', '')

    # Checking if the old password is correct
    if old_password == LIBRARIAN_PASSWORD:
        # Changing the global password variable to the new password
        global LIBRARIAN_PASSWORD
        LIBRARIAN_PASSWORD = new_password
        # Letting the user know that the password has been changed
        return jsonify({"status": "Password changed successfully"})
    else:
        # Denying the password change if the old password is incorrect
        return jsonify({"status": "Access denied", "message": "Invalid old password"}), 401

@app.route('/library/book_info', methods=['GET'])
def library_book_info():
    # Getting the ISBN of the book to look up
    isbn = request.args.get('isbn', '')
    if not isbn:
        return jsonify({"status": "Error", "message": "ISBN is required"}), 400

    # Providing some sample book information
    book_info = {
        "title": "Sample Book",
        "author": "John Doe",
        "isbn": isbn,
        "publisher": "Sample Publisher",
        "year_published": 2023
    }

    # Returning the book details
    return jsonify({"status": "Book details", "book_info": book_info})

@app.route('/library/update_book', methods=['POST'])
def library_update_book():
    # Getting the ISBN and new details of the book
    isbn = request.form.get('isbn', '')
    new_title = request.form.get('new_title', '')
    new_author = request.form.get('new_author', '')

    if not isbn:
        return jsonify({"status": "Error", "message": "ISBN is required"}), 400

    # Returning a success message with the updated book details
    return jsonify({"status": "Book updated", "isbn": isbn, "new_title": new_title, "new_author": new_author})

@app.route('/library/list_books', methods=['GET'])
def library_list_books():
    # Getting the section to list books from
    section = request.args.get('section', '')
    # Providing some sample books
    books = [
        {"title": "Book 1", "author": "Author 1", "isbn": "111", "publisher": "Publisher 1", "year_published": 2021},
        {"title": "Book 2", "author": "Author 2", "isbn": "222", "publisher": "Publisher 2", "year_published": 2022}
    ]

    # Returning the list of books
    return jsonify({"status": "Books listed", "section": section, "books": books})

# Running the app with debugging turned off
if __name__ == "__main__":
    app.run(debug=False)