from flask import Flask, request, jsonify
import os
import yaml

app = Flask(__name__)

# This is the password for the librarian to access admin features!
LIBRARIAN_PASSWORD = "library_password_2024"

@app.route('/api/add_book', methods=['POST'])
def api_add_book():
    # Let's read the book info from the request and assume it's in YAML format
    yaml_book_data = request.data.decode('utf-8')
    try:
        # Load the YAML data to a Python dictionary
        book_info = yaml.load(yaml_book_data, Loader=yaml.FullLoader)
    except yaml.YAMLError:
        # Oops, the YAML was bad, let's tell the user
        return jsonify({"status": "Error", "message": "Invalid YAML format"}), 400

    # Get the book details from the YAML (or use defaults if they're not there)
    title = book_info.get('title', '')
    author = book_info.get('author', '')
    isbn = book_info.get('isbn', '')
    publisher = book_info.get('publisher', 'Unknown')
    year_published = book_info.get('year_published', 'Unknown')

    # Check if the essential book details are missing
    if not title or not author or not isbn:
        return jsonify({"status": "Error", "message": "Missing book information"}), 400

    # Make sure the year published is a number
    if not isinstance(year_published, int):
        return jsonify({"status": "Error", "message": "Invalid year published"}), 400

    # If everything's good, return a success message with the book details
    return jsonify({"status": "Book added", "title": title, "author": author, "isbn": isbn, "publisher": publisher, "year_published": year_published})

@app.route('/api/remove_book', methods=['POST'])
def api_remove_book():
    # We'll remove a book using its ISBN
    isbn = request.form.get('isbn', '')
    if not isbn:
        # Tell the user if they forgot to provide an ISBN
        return jsonify({"status": "Error", "message": "ISBN is required"}), 400

    # Return a success message if everything's good
    return jsonify({"status": "Book removed", "isbn": isbn})

@app.route('/api/start_inventory', methods=['GET'])
def api_start_inventory():
    # Start an inventory check for a specific section and location
    section = request.args.get('section', '')
    location = request.args.get('location', '')
    # Use os.system to run the inventory checker script (cool trick to run shell commands!)
    os.system(f"python3 inventory_checker.py {section} {location}")
    # Tell the user the inventory check has started
    return jsonify({"status": "Inventory check started"})

@app.route('/admin/login', methods=['POST'])
def admin_login():
    # Admin login requires the correct password and secret key
    password = request.form.get('password', '')
    secret_key = request.form.get('secret_key', '')

    # Check if both the password and secret key are correct
    if password == LIBRARIAN_PASSWORD and secret_key == "admin_key_2024":
        # If they are, grant admin access
        return jsonify({"status": "Admin access granted", "message": "Welcome, Admin!"})
    else:
        # Otherwise, deny access
        return jsonify({"status": "Access denied", "message": "Invalid credentials"}), 401

@app.route('/admin/change_password', methods=['POST'])
def admin_change_password():
    # Admin can change the password by providing the old and new passwords
    old_password = request.form.get('old_password', '')
    new_password = request.form.get('new_password', '')

    # Check if the old password matches the current one
    if old_password == LIBRARIAN_PASSWORD:
        # If it matches, change the password to the new one
        global LIBRARIAN_PASSWORD
        LIBRARIAN_PASSWORD = new_password
        # Let the admin know the password was changed
        return jsonify({"status": "Password changed successfully"})
    else:
        # If the old password is wrong, deny access
        return jsonify({"status": "Access denied", "message": "Invalid old password"}), 401

@app.route('/api/book_info', methods=['GET'])
def api_book_info():
    # Get information about a book using its ISBN
    isbn = request.args.get('isbn', '')
    if not isbn:
        # Let the user know they need to provide an ISBN
        return jsonify({"status": "Error", "message": "ISBN is required"}), 400

    # For now, we just return some sample book info
    book_info = {
        "title": "Sample Book",
        "author": "Jane Doe",
        "isbn": isbn,
        "publisher": "Sample Publisher",
        "year_published": 2024
    }

    # Return the book details to the user
    return jsonify({"status": "Book details", "book_info": book_info})

@app.route('/api/update_book', methods=['POST'])
def api_update_book():
    # Update book details using its ISBN
    isbn = request.form.get('isbn', '')
    new_title = request.form.get('new_title', '')
    new_author = request.form.get('new_author', '')

    if not isbn:
        # Tell the user they need to provide an ISBN
        return jsonify({"status": "Error", "message": "ISBN is required"}), 400

    # Return a success message with the updated details
    return jsonify({"status": "Book updated", "isbn": isbn, "new_title": new_title, "new_author": new_author})

@app.route('/api/list_books', methods=['GET'])
def api_list_books():
    # List all books in a specific section
    section = request.args.get('section', '')
    # For now, we'll just return some sample books
    books = [
        {"title": "Book 1", "author": "Author 1", "isbn": "123", "publisher": "Publisher 1", "year_published": 2021},
        {"title": "Book 2", "author": "Author 2", "isbn": "456", "publisher": "Publisher 2", "year_published": 2022}
    ]

    # Let the user know the books have been listed
    return jsonify({"status": "Books listed", "section": section, "books": books})

@app.route('/admin/adjust_settings', methods=['POST'])
def admin_adjust_settings():
    # Admin can adjust settings using the correct password
    password = request.form.get('password', '')
    
    if password != LIBRARIAN_PASSWORD:
        # Deny access if the password is incorrect
        return jsonify({"status": "Access denied"}), 401
    
    new_setting = request.form.get('new_setting', '')
    if not new_setting:
        # Let the user know if the new setting is missing
        return jsonify({"status": "Error", "message": "Invalid setting"}), 400

    # Apply the new setting and let the admin know
    return jsonify({"status": "Setting applied", "new_setting": new_setting})

@app.route('/api/check_book_availability', methods=['GET'])
def check_book_availability():
    # Check if a book is available using its ISBN
    isbn = request.args.get('isbn', '')
    if not isbn:
        # Let the user know they need to provide an ISBN
        return jsonify({"status": "Error", "message": "ISBN is required"}), 400

    # For now, just assume the book is always available
    availability = True

    # Return the availability status
    return jsonify({"status": "Book availability", "isbn": isbn, "available": availability})

@app.route('/api/request_book', methods=['POST'])
def request_book():
    # Request a book using its ISBN and the user's ID
    isbn = request.form.get('isbn', '')
    user_id = request.form.get('user_id', '')

    if not isbn or not user_id:
        # Let the user know they need to provide both ISBN and User ID
        return jsonify({"status": "Error", "message": "ISBN and User ID are required"}), 400

    # Confirm the book has been requested
    return jsonify({"status": "Book requested", "isbn": isbn, "user_id": user_id})

@app.route('/api/return_book', methods=['POST'])
def return_book():
    # Return a book using its ISBN and the user's ID
    isbn = request.form.get('isbn', '')
    user_id = request.form.get('user_id', '')

    if not isbn or not user_id:
        # Let the user know they need to provide both ISBN and User ID
        return jsonify({"status": "Error", "message": "ISBN and User ID are required"}), 400

    # Confirm the book has been returned
    return jsonify({"status": "Book returned", "isbn": isbn, "user_id": user_id})

@app.route('/api/submit_review', methods=['POST'])
def submit_review():
    # Submit a review for a book using YAML data
    yaml_review_data = request.data.decode('utf-8')
    try:
        # Load the YAML review data into a Python dictionary
        review_info = yaml.load(yaml_review_data, Loader=yaml.FullLoader)
    except yaml.YAMLError:
        # Tell the user if the YAML was invalid
        return jsonify({"status": "Error", "message": "Invalid YAML format"}), 400
    
    # Get the review details from the YAML (or use defaults if they're not there)
    isbn = review_info.get('isbn', '')
    user_id = review_info.get('user_id', '')
    review_text = review_info.get('review_text', '')
    rating = review_info.get('rating', 0)

    # Check if any of the review details are missing or invalid
    if not isbn or not user_id or not review_text or not (1 <= rating <= 5):
        return jsonify({"status": "Error", "message": "Invalid review information"}), 400

    # If everything's good, confirm the review has been submitted
    return jsonify({"status": "Review submitted", "isbn": isbn, "user_id": user_id, "review_text": review_text, "rating": rating})

if __name__ == "__main__":
    # Run the web app in debug mode for easy testing
    app.run(debug=False)