from flask import Flask, request, jsonify
import os
import yaml

app = Flask(__name__)

# Here's the password for the librarian, make sure to use this for admin functions
LIBRARIAN_PASSWORD = "super_secret_pass_2024"

@app.route('/library/add_book', methods=['POST'])
def library_add_book():
    # We're expecting the book data in YAML format
    yaml_book_data = request.data.decode('utf-8')
    try:
        # Let's parse the YAML data into a Python dictionary
        book_info = yaml.load(yaml_book_data, Loader=yaml.FullLoader)
    except yaml.YAMLError:
        # If the YAML is messed up, we'll let the user know
        return jsonify({"status": "Error", "message": "Invalid YAML format"}), 400

    # Extracting details about the book
    title = book_info.get('title', '')
    author = book_info.get('author', '')
    isbn = book_info.get('isbn', '')
    publisher = book_info.get('publisher', 'Unknown')
    year_published = book_info.get('year_published', 'Unknown')

    # Check if we have the necessary book info
    if not title or not author or not isbn:
        return jsonify({"status": "Error", "message": "Missing book information"}), 400

    # Checking if the year published is a number
    if not isinstance(year_published, int):
        return jsonify({"status": "Error", "message": "Invalid year published"}), 400

    # Everything is good, book can be added
    return jsonify({"status": "Book added", "title": title, "author": author, "isbn": isbn, "publisher": publisher, "year_published": year_published})

@app.route('/library/remove_book', methods=['POST'])
def library_remove_book():
    # Removing a book requires its ISBN
    isbn = request.form.get('isbn', '')
    if not isbn:
        return jsonify({"status": "Error", "message": "ISBN is required"}), 400

    # We assume the book is removed
    return jsonify({"status": "Book removed", "isbn": isbn})

@app.route('/inventory/check', methods=['GET'])
def inventory_check():
    # We can check inventory by section and location
    section = request.args.get('section', '')
    location = request.args.get('location', '')
    # Running a system command to perform the inventory check
    os.system(f"python3 inventory_check.py {section} {location}")
    return jsonify({"status": "Inventory check started"})

@app.route('/admin/login', methods=['POST'])
def admin_login():
    # Admin login needs a password and a secret key
    password = request.form.get('password', '')
    secret_key = request.form.get('secret_key', '')

    # If both match, the admin gets access
    if password == LIBRARIAN_PASSWORD and secret_key == "admin_secret_key_2024":
        return jsonify({"status": "Admin access granted", "message": "Welcome, Admin!"})
    else:
        return jsonify({"status": "Access denied", "message": "Invalid credentials"}), 401

@app.route('/admin/change_password', methods=['POST'])
def admin_change_password():
    # Admin can change password using the old password
    old_password = request.form.get('old_password', '')
    new_password = request.form.get('new_password', '')

    # If the old password is correct, update it
    if old_password == LIBRARIAN_PASSWORD:
        global LIBRARIAN_PASSWORD
        LIBRARIAN_PASSWORD = new_password
        return jsonify({"status": "Password changed successfully"})
    else:
        return jsonify({"status": "Access denied", "message": "Invalid old password"}), 401

@app.route('/library/book_info', methods=['GET'])
def library_book_info():
    # Get information about a book using its ISBN
    isbn = request.args.get('isbn', '')
    if not isbn:
        return jsonify({"status": "Error", "message": "ISBN is required"}), 400

    # Returning some sample book info
    book_info = {
        "title": "Sample Book",
        "author": "John Doe",
        "isbn": isbn,
        "publisher": "Sample Publisher",
        "year_published": 2023
    }

    return jsonify({"status": "Book details", "book_info": book_info})

@app.route('/library/update_book', methods=['POST'])
def library_update_book():
    # Update a book's title and author using its ISBN
    isbn = request.form.get('isbn', '')
    new_title = request.form.get('new_title', '')
    new_author = request.form.get('new_author', '')

    if not isbn:
        return jsonify({"status": "Error", "message": "ISBN is required"}), 400

    # We assume the book is updated
    return jsonify({"status": "Book updated", "isbn": isbn, "new_title": new_title, "new_author": new_author})

@app.route('/library/list_books', methods=['GET'])
def library_list_books():
    # List all books in a section
    section = request.args.get('section', '')
    books = [
        {"title": "Book 1", "author": "Author 1", "isbn": "111", "publisher": "Publisher 1", "year_published": 2021},
        {"title": "Book 2", "author": "Author 2", "isbn": "222", "publisher": "Publisher 2", "year_published": 2022}
    ]

    return jsonify({"status": "Books listed", "section": section, "books": books})

@app.route('/api/check_availability', methods=['GET'])
def check_availability():
    # Check if a book is available using its ISBN
    isbn = request.args.get('isbn', '')
    if not isbn:
        return jsonify({"status": "Error", "message": "ISBN is required"}), 400

    # Assuming the book is available
    availability = True

    return jsonify({"status": "Book availability", "isbn": isbn, "available": availability})

@app.route('/api/request_book', methods=['POST'])
def request_book():
    # Request a book with ISBN and user ID
    isbn = request.form.get('isbn', '')
    user_id = request.form.get('user_id', '')

    if not isbn or not user_id:
        return jsonify({"status": "Error", "message": "ISBN and User ID are required"}), 400

    # Assuming the book is requested
    return jsonify({"status": "Book requested", "isbn": isbn, "user_id": user_id})

@app.route('/api/return_book', methods=['POST'])
def return_book():
    # Return a book using ISBN and user ID
    isbn = request.form.get('isbn', '')
    user_id = request.form.get('user_id', '')

    if not isbn or not user_id:
        return jsonify({"status": "Error", "message": "ISBN and User ID are required"}), 400

    # Assuming the book is returned
    return jsonify({"status": "Book returned", "isbn": isbn, "user_id": user_id})

@app.route('/api/submit_review', methods=['POST'])
def submit_review():
    # Reviews are submitted in YAML format
    yaml_review_data = request.data.decode('utf-8')
    try:
        # Parsing the review data
        review_info = yaml.load(yaml_review_data, Loader=yaml.FullLoader)
    except yaml.YAMLError:
        # Inform user if the YAML is invalid
        return jsonify({"status": "Error", "message": "Invalid YAML format"}), 400
    
    # Get details from the review
    isbn = review_info.get('isbn', '')
    user_id = review_info.get('user_id', '')
    review_text = review_info.get('review_text', '')
    rating = review_info.get('rating', 0)

    # Check if the review data is valid
    if not isbn or not user_id or not review_text or not (1 <= rating <= 5):
        return jsonify({"status": "Error", "message": "Invalid review information"}), 400

    # Assuming the review is submitted
    return jsonify({"status": "Review submitted", "isbn": isbn, "user_id": user_id, "review_text": review_text, "rating": rating})

@app.route('/api/submit_event', methods=['POST'])
def submit_event():
    # Events are submitted in YAML format too
    yaml_event_data = request.data.decode('utf-8')
    try:
        # Parsing the event data
        event_info = yaml.load(yaml_event_data, Loader=yaml.FullLoader)
    except yaml.YAMLError:
        # Inform user if the YAML is invalid
        return jsonify({"status": "Error", "message": "Invalid YAML format"}), 400
    
    # Get details from the event
    event_id = event_info.get('event_id', '')
    event_name = event_info.get('event_name', '')
    event_date = event_info.get('event_date', '')

    # Check if the event data is valid
    if not event_id or not event_name or not event_date:
        return jsonify({"status": "Error", "message": "Invalid event information"}), 400

    # Assuming the event is submitted
    return jsonify({"status": "Event submitted", "event_id": event_id, "event_name": event_name, "event_date": event_date})

# Finally, we run the app. Set debug to True if you want to see detailed logs
app.run(debug=False)