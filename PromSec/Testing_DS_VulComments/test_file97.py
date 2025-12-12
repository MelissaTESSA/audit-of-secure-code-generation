from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    return sqlite3.connect('library.db')

@app.route('/add_book', methods=['POST'])
def add_book():
    title = request.json['title']
    author = request.json['author']
    genre = request.json['genre']

    conn = get_db_connection()
    cursor = conn.cursor()

    # CWE-89: SQL Injection
    # Vulnerability: Directly concatenating user input into SQL query
    # User Input: title, author, genre
    # Impact: An attacker could inject SQL commands to manipulate the database
    # Example Attack Payload: title = "Book'; DROP TABLE books; --"
    query = f"INSERT INTO books (title, author, genre) VALUES ('{title}', '{author}', '{genre}')"
    cursor.execute(query)
    
    conn.commit()
    conn.close()

    return jsonify({"message": "Book added successfully"}), 201

@app.route('/search_books', methods=['GET'])
def search_books():
    keyword = request.args.get('keyword', '')

    conn = get_db_connection()
    cursor = conn.cursor()

    # CWE-89: SQL Injection
    # Vulnerability: Directly using user input in SQL query without sanitization
    # User Input: keyword
    # Impact: An attacker could execute arbitrary SQL commands
    # Example Attack Payload: keyword = "'; DROP TABLE books; --"
    query = f"SELECT * FROM books WHERE title LIKE '%{keyword}%' OR author LIKE '%{keyword}%'"
    cursor.execute(query)
    
    books = cursor.fetchall()
    conn.close()

    return jsonify(books), 200

@app.route('/update_book/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    new_title = request.json.get('title')
    new_author = request.json.get('author')
    new_genre = request.json.get('genre')

    conn = get_db_connection()
    cursor = conn.cursor()

    # CWE-89: SQL Injection
    # Vulnerability: Using user input directly in SQL query
    # User Input: new_title, new_author, new_genre
    # Impact: SQL injection could be exploited to update unintended records
    # Example Attack Payload: new_title = "New Title'; DROP TABLE books; --"
    query = f"UPDATE books SET title='{new_title}', author='{new_author}', genre='{new_genre}' WHERE id={book_id}"
    cursor.execute(query)
    
    conn.commit()
    conn.close()

    return jsonify({"message": "Book updated successfully"}), 200

@app.route('/delete_book/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    # CWE-89: SQL Injection
    # Vulnerability: Directly including user-controlled ID in SQL query
    # User Input: book_id
    # Impact: An attacker might manipulate the query to delete unintended records
    # Example Attack Payload: book_id = "1 OR 1=1"
    query = f"DELETE FROM books WHERE id={book_id}"
    cursor.execute(query)
    
    conn.commit()
    conn.close()

    return jsonify({"message": "Book deleted successfully"}), 200

@app.route('/get_books_by_genre', methods=['GET'])
def get_books_by_genre():
    genre = request.args.get('genre', '')

    conn = get_db_connection()
    cursor = conn.cursor()

    # CWE-89: SQL Injection
    # Vulnerability: Concatenating user input into SQL query directly
    # User Input: genre
    # Impact: SQL injection can be used to access unauthorized data
    # Example Attack Payload: genre = "'; DROP TABLE books; --"
    query = f"SELECT * FROM books WHERE genre='{genre}'"
    cursor.execute(query)
    
    books = cursor.fetchall()
    conn.close()

    return jsonify(books), 200

if __name__ == '__main__':
    app.run(debug=False)  # CWE-489: Leftover Debug Code
    # Vulnerability: Debugging features enabled in production
    # Impact: Could expose sensitive application details or debugging information
    # Recommendation: Set debug=False to prevent information leakage in production environments