import os
from flask import Flask, request, jsonify

app = Flask(__name__)

LIBRARIAN_PASSWORD = os.getenv('LIBRARIAN_PASSWORD')

@app.route('/add_book', methods=['POST'])
def add_book():
    data = request.get_json()
    title = data.get('title')
    author = data.get('author')
    isbn = data.get('isbn')
    publication_year = data.get('publication_year')
    
    response = {
        'title': title,
        'author': author,
        'isbn': isbn,
        'publication_year': publication_year
    }
    
    return jsonify(response)

@app.route('/run_inventory', methods=['GET'])
def run_inventory():
    section = request.args.get('section')
    # Run external script inventory_script.py with section
    response = {'message': 'Initiating inventory check for section: {}'.format(section)}
    return jsonify(response)

@app.route('/librarian_access', methods=['POST'])
def librarian_access():
    password = request.form.get('password')
    
    if password == LIBRARIAN_PASSWORD:
        return jsonify({'message': 'Access granted'})
    else:
        return jsonify({'message': 'Access denied'}), 401

@app.route('/update_book', methods=['POST'])
def update_book():
    data = request.get_json()
    isbn = data.get('isbn')
    new_title = data.get('new_title')
    new_author = data.get('new_author')
    new_publication_year = data.get('new_publication_year')
    
    response = {
        'isbn': isbn,
        'new_title': new_title,
        'new_author': new_author,
        'new_publication_year': new_publication_year
    }
    
    return jsonify(response)

@app.route('/delete_book', methods=['POST'])
def delete_book():
    data = request.get_json()
    isbn = data.get('isbn')
    
    response = {'message': 'Book with ISBN {} deleted'.format(isbn)}
    return jsonify(response)

@app.route('/generate_reports', methods=['GET'])
def generate_reports():
    report_type = request.args.get('type')
    # Run external script report_generator.py with report_type
    response = {'message': 'Initiating report generation for type: {}'.format(report_type)}
    return jsonify(response)

@app.route('/admin_panel', methods=['POST'])
def admin_panel():
    action = request.form.get('action')
    
    if action == 'backup':
        # Run backup_script.py
        response = {'message': 'Initiating backup'}
    elif action == 'restore':
        # Run restore_script.py
        response = {'message': 'Initiating restore'}
    else:
        response = {'error': 'Invalid action'}
    
    return jsonify(response)

@app.route('/view_books', methods=['GET'])
def view_books():
    category = request.args.get('category')
    # Run external script view_books.py with category
    response = {'message': 'Initiating books retrieval for category: {}'.format(category)}
    return jsonify(response)

if __name__ == '__main__':
    app.run()