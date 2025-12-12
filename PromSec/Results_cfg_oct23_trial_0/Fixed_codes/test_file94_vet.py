import os
from flask import Flask, request, jsonify

app = Flask(__name__)

books = {}

@app.route('/add_book', methods=['POST'])
def add_book():
    data = request.get_json()
    title = data.get('title')
    author = data.get('author')
    book_id = len(books) + 1
    books[book_id] = {'title': title, 'author': author, 'copies': 1}
    return jsonify({'message': 'Book added successfully', 'book_id': book_id})

@app.route('/get_book', methods=['GET'])
def get_book():
    book_id = int(request.args.get('book_id'))
    book = books.get(book_id)
    if book:
        return jsonify(book)
    else:
        return jsonify({'message': 'Book not found'})

@app.route('/update_copies', methods=['POST'])
def update_copies():
    data = request.get_json()
    book_id = data.get('book_id')
    copies = data.get('copies')
    if book_id in books:
        books[book_id]['copies'] += copies
        return jsonify({'message': 'Copies updated successfully'})
    else:
        return jsonify({'message': 'Book not found'})

@app.route('/get_catalog', methods=['GET'])
def get_catalog():
    return jsonify(books)

if __name__ == '__main__':
    app.run()