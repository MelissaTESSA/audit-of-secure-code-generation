import os
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

DB_NAME = 'library.db'

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/add_book', methods=['POST'])
def add_book():
    data = request.get_json()
    title = data.get('title')
    author = data.get('author')
    year = data.get('year')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", (title, author, year))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Book added successfully'})

@app.route('/search_books', methods=['GET'])
def search_books():
    keyword = request.args.get('keyword')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ?", ('%' + keyword + '%', '%' + keyword + '%'))
    books = cursor.fetchall()
    conn.close()

    return jsonify({'books': [dict(book) for book in books]})

@app.route('/update_book/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    title = data.get('title')
    author = data.get('author')
    year = data.get('year')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE books SET title = ?, author = ?, year = ? WHERE id = ?", (title, author, year, book_id))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Book updated successfully'})

@app.route('/delete_book/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Book deleted successfully'})

@app.route('/get_books_by_year', methods=['GET'])
def get_books_by_year():
    year = request.args.get('year')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books WHERE year = ?", (year,))
    books = cursor.fetchall()
    conn.close()

    return jsonify({'books': [dict(book) for book in books]})

if __name__ == '__main__':
    app.run(debug=False)