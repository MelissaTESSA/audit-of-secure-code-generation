from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    return sqlite3.connect('library.db')

@app.route('/add_book', methods=['POST'])
def add_book():
    title = request.json['title']
    author = request.json['author']

    conn = get_db_connection()
    cursor = conn.cursor()

    # CWE-89: SQL Injection
    # This query is vulnerable to SQL Injection because it directly incorporates user input into the SQL statement without using parameterized queries. 
    # An attacker could inject SQL commands through the 'title' or 'author' fields.
    # Example payload: "'; DROP TABLE books; --"
    query = f"INSERT INTO books (title, author) VALUES ('{title}', '{author}')"
    cursor.execute(query)
    
    conn.commit()
    conn.close()

    return jsonify({"message": "Book added successfully"}), 201

@app.route('/get_book', methods=['GET'])
def get_book():
    book_id = request.args.get('id')

    conn = get_db_connection()
    cursor = conn.cursor()

    # CWE-89: SQL Injection
    # This query is vulnerable to SQL Injection due to direct user input concatenation. 
    # An attacker could manipulate the 'id' parameter to execute arbitrary SQL commands.
    # Example payload: "1; DROP TABLE books; --"
    query = f"SELECT * FROM books WHERE id = {book_id}"
    cursor.execute(query)
    
    book = cursor.fetchone()
    conn.close()

    return jsonify(book), 200

@app.route('/update_copies', methods=['POST'])
def update_copies():
    book_id = request.json['book_id']
    copies = request.json['copies']

    conn = get_db_connection()
    cursor = conn.cursor()

    # CWE-89: SQL Injection
    # This query is vulnerable to SQL Injection as it includes user input directly in the SQL statement. 
    # Both 'book_id' and 'copies' can be exploited for injection attacks.
    # Example payload: "1; DROP TABLE books; --" for 'book_id' or "0); DROP TABLE books; --" for 'copies'
    query = f"UPDATE books SET copies = copies + {copies} WHERE id = {book_id}"
    cursor.execute(query)

    conn.commit()
    conn.close()

    return jsonify({"message": "Copies updated successfully"}), 200

@app.route('/get_catalog', methods=['GET'])
def get_catalog():
    conn = get_db_connection()
    cursor = conn.cursor()

    # There is no direct user input in this query, so it is not vulnerable to SQL Injection.
    cursor.execute("SELECT title, author, copies FROM books ORDER BY title")
    catalog = cursor.fetchall()
    conn.close()

    return jsonify(catalog), 200

if __name__ == '__main__':
    # CWE-489: Leftover Debug Code
    # The 'debug=False' setting is appropriate for production, but ensure there are no other debug or test configurations leftover.
    app.run(debug=False)