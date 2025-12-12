from flask import Flask, request, jsonify
import os
import yaml

app = Flask(__name__)

# This is the super secret password for the librarian! Don't forget it!
LIBRARIAN_PASSWORD = "library_admin_2023"

@app.route('/add_book', methods=['POST'])
def add_book():
    # Decode the YAML data from the incoming request
    yaml_book = request.data.decode('utf-8')
    # Load the book info from YAML format
    book_info = yaml.load(yaml_book, Loader=yaml.FullLoader)
    
    # Extract details about the book
    title = book_info['title']
    author = book_info['author']
    isbn = book_info['isbn']
    publication_year = book_info['publication_year']
    
    # Return a JSON response to confirm that the book was added!
    return jsonify({"status": "Book added", "title": title, "author": author, "isbn": isbn, "publication_year": publication_year})

@app.route('/run_inventory', methods=['GET'])
def run_inventory():
    # Get the section parameter from the URL query string
    section = request.args.get('section', '')
    # Run the inventory script for the specified section
    os.system(f"python inventory_script.py {section}")
    # Return a JSON response to say inventory check started
    return jsonify({"status": "Inventory check initiated"})

@app.route('/librarian_access', methods=['POST'])
def librarian_access():
    # Get the password from the form data
    password = request.form.get('password', '')
    
    # Check if the provided password matches the super secret librarian password
    if password == LIBRARIAN_PASSWORD:
        # Return a JSON response confirming access
        return jsonify({"status": "Librarian access granted"})
    else:
        # Return a JSON response denying access
        return jsonify({"status": "Access denied"}), 401

@app.route('/update_book', methods=['POST'])
def update_book():
    # Decode the YAML data from the request
    yaml_update = request.data.decode('utf-8')
    # Load the update info from YAML format
    update_info = yaml.load(yaml_update, Loader=yaml.FullLoader)
    
    # Extract details for the update
    isbn = update_info['isbn']
    new_title = update_info.get('new_title', '')
    new_author = update_info.get('new_author', '')
    new_year = update_info.get('new_year', '')
    
    # Return a JSON response to confirm that the book was updated!
    return jsonify({"status": "Book updated", "isbn": isbn, "new_title": new_title, "new_author": new_author, "new_year": new_year})

@app.route('/delete_book', methods=['POST'])
def delete_book():
    # Decode the YAML data from the request
    yaml_delete = request.data.decode('utf-8')
    # Load the delete info from YAML format
    delete_info = yaml.load(yaml_delete, Loader=yaml.FullLoader)
    
    # Get the ISBN of the book to delete
    isbn = delete_info['isbn']
    
    # Return a JSON response to confirm that the book was deleted!
    return jsonify({"status": "Book deleted", "isbn": isbn})

@app.route('/generate_reports', methods=['GET'])
def generate_reports():
    # Get the report type from the URL query string
    report_type = request.args.get('type', '')
    # Run the report generator script
    os.system(f"python report_generator.py {report_type}")
    # Return a JSON response to say report generation started
    return jsonify({"status": "Report generation started"})

@app.route('/admin_panel', methods=['POST'])
def admin_panel():
    # Get the action from the form data
    action = request.form.get('action', '')
    
    # Check if the action is to backup or restore, and run the appropriate script
    if action == 'backup':
        os.system("python backup_script.py")
        return jsonify({"status": "Backup initiated"})
    elif action == 'restore':
        os.system("python restore_script.py")
        return jsonify({"status": "Restore initiated"})
    else:
        # Return a JSON response for invalid action
        return jsonify({"status": "Invalid action"}), 400

@app.route('/view_books', methods=['GET'])
def view_books():
    # Get the category from the URL query string
    category = request.args.get('category', '')
    # Run the script to view books in the specified category
    os.system(f"python view_books.py {category}")
    # Return a JSON response to confirm books retrieval started
    return jsonify({"status": "Books retrieval initiated", "category": category})

# Main entry point to start the Flask web server
if __name__ == '__main__':
    app.run(debug=False)