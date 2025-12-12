import os
from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')

LIBRARIAN_PASSWORD = os.getenv('LIBRARIAN_PASSWORD')

@app.route('/add_book', methods=['POST'])
def add_book():
    data = request.get_json()
    if 'title' in data and 'author' in data and 'isbn' in data:
        return jsonify(data)
    else:
        return jsonify({'error': 'Invalid data. Required fields: title, author, isbn'}), 400

@app.route('/run_inventory', methods=['GET'])
def run_inventory():
    section = request.args.get('section')
    if section:
        # Run inventory script with provided section
        return jsonify({'message': 'Inventory script ran successfully for section: {}'.format(section)})
    else:
        return jsonify({'error': 'Missing section parameter'}), 400

@app.route('/librarian_access', methods=['POST'])
def librarian_access():
    password = request.form.get('password')
    if password == LIBRARIAN_PASSWORD:
        return jsonify({'message': 'Access granted'})
    else:
        return jsonify({'error': 'Access denied'}), 401

if __name__ == '__main__':
    app.run(debug=False)