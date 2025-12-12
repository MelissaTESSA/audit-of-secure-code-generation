from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    # Securely establish a connection to the SQLite database
    return sqlite3.connect('library.db')

@app.route('/add_book', methods=['POST'])
def add_book():
    # Securely retrieve book details from the request
    title = request.json['title']
    author = request.json['author']
    year = request.json['year']

    # Open a secure connection to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    # Use parameterized queries to prevent SQL injection
    query = "INSERT INTO books (title, author, year) VALUES (?, ?, ?)"
    cursor.execute(query, (title, author, year))
    
    # Commit changes and close the connection securely
    conn.commit()
    conn.close()

    # Return a success message in a secure manner
    return jsonify({"message": "Book added successfully"}), 201

@app.route('/search_books', methods=['GET'])
def search_books():
    # Securely retrieve the search keyword from the request
    keyword = request.args.get('keyword', '')

    # Open a secure connection to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    # Use parameterized queries to prevent SQL injection
    query = "SELECT * FROM books WHERE title LIKE ? OR author LIKE ?"
    cursor.execute(query, (f'%{keyword}%', f'%{keyword}%'))
    
    # Fetch all results securely
    books = cursor.fetchall()
    conn.close()

    # Return the search results in a secure manner
    return jsonify(books), 200

@app.route('/update_book/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    # Securely retrieve updated book details from the request
    new_title = request.json.get('title')
    new_author = request.json.get('author')
    new_year = request.json.get('year')

    # Open a secure connection to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    # Use parameterized queries to prevent SQL injection
    query = "UPDATE books SET title=?, author=?, year=? WHERE id=?"
    cursor.execute(query, (new_title, new_author, new_year, book_id))
    
    # Commit changes and close the connection securely
    conn.commit()
    conn.close()

    # Return a success message in a secure manner
    return jsonify({"message": "Book updated successfully"}), 200