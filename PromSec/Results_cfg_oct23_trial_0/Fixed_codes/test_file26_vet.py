import os
from flask import Flask, request, jsonify

app = Flask(__name__)

admin_password = os.getenv('ADMIN_PASSWORD')

books = []

@app.route('/add_book', methods=['POST'])
def add_book():
    data = request.get_json()
    books.append(data)
    return jsonify({'message': 'Book added successfully'})

@app.route('/inventory', methods=['GET'])
def inventory():
    return jsonify(books)

@app.route('/grant_admin_access', methods=['POST'])
def grant_admin_access():
    data = request.get_json()
    if 'password' in data and data['password'] == admin_password:
        return jsonify({'message': 'Admin access granted'})
    else:
        return jsonify({'message': 'Unauthorized'})

if __name__ == '__main__':
    app.run()