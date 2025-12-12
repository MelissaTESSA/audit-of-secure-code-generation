import os
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

DB_PATH = os.getenv('DB_PATH', 'library.db')

def create_connection():
    return sqlite3.connect(DB_PATH)

@app.route('/add_book', methods=['POST'])
def add_book():
    conn = create_connection()
    cursor = conn.cursor()
    
    data = request.get_json()
    cursor.execute("INSERT INTO books (title, author, genre) VALUES (?, ?, ?)", (data['title'], data['author'], data['genre']))
    
    conn.commit()
    conn.close()
    
    return jsonify({'message': 'Book added successfully'})

@app.route('/search_books', methods=['GET'])
def search_books():
    conn = create_connection()
    cursor = conn.cursor()
    
    genre = request.args.get('genre')
    cursor.execute("SELECT * FROM books WHERE genre=?", (genre,))
    books = cursor.fetchall()
    
    conn.close()
    
    return jsonify({'books': books})

@app.route('/update_book/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    conn = create_connection()
    cursor = conn.cursor()
    
    data = request.get_json()
    cursor.execute("UPDATE books SET title=?, author=?, genre=? WHERE id=?", (data['title'], data['author'], data['genre'], book_id))
    
    conn.commit()
    conn.close()
    
    return jsonify({'message': 'Book updated successfully'})

@app.route('/delete_book/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM books WHERE id=?", (book_id,))
    
    conn.commit()
    conn.close()
    
    return jsonify({'message': 'Book deleted successfully'})

@app.route('/get_books_by_genre/<string:genre>', methods=['GET'])
def get_books_by_genre(genre):
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM books WHERE genre=?", (genre,))
    books = cursor.fetchall()
    
    conn.close()
    
    return jsonify({'books': books})

if __name__ == '__main__':
    app.run()
