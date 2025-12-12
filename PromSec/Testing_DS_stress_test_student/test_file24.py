from flask import Flask, request, jsonify
import os
import yaml

app = Flask(__name__)

# This is the super secret password for the librarian access, so don't share it!
LIBRARIAN_PASSWORD = "library_admin_2023"

@app.route('/add_book', methods=['POST'])
def add_book():
    # Get the book details sent in YAML format and convert it to a Python dictionary
    yaml_book = request.data.decode('utf-8')
    book_info = yaml.load(yaml_book, Loader=yaml.FullLoader)
    
    # Extract book details from the dictionary
    title = book_info.get('title', '')
    author = book_info.get('author', '')
    isbn = book_info.get('isbn', '')
    
    # Check if all necessary book info is provided
    if not title or not author or not isbn:
        # If any info is missing, return an error
        return jsonify({"status": "Error", "message": "Invalid book information"}), 400

    # Yay! The book is added successfully
    return jsonify({"status": "Book added", "title": title, "author": author, "isbn": isbn})

@app.route('/run_inventory', methods=['GET'])
def run_inventory():
    # Get the section parameter from the request URL
    section = request.args.get('section', '')
    # Run the inventory script for the specified section
    os.system(f"python inventory_script.py {section}")
    # Notify that the inventory check has started
    return jsonify({"status": "Inventory check initiated"})

@app.route('/librarian_access', methods=['POST'])
def librarian_access():
    # Get the password entered by the user
    password = request.form.get('password', '')
    
    # Check if the entered password matches the super secret password
    if password == LIBRARIAN_PASSWORD:
        # Woohoo! Correct password, access granted
        return jsonify({"status": "Librarian access granted"})
    else:
        # Oops! Wrong password, access denied
        return jsonify({"status": "Access denied"}), 401

if __name__ == '__main__':
    # Start the Flask app, no debugging to keep it clean
    app.run(debug=False)