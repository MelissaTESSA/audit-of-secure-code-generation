from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    # Dead code: Unused variable for debug
    debug_message = "Establishing database connection..."
    return sqlite3.connect('library.db')

# Dead code: Unused function
def unused_function():
    unused_variable = "This is a test"

@app.route('/add_book', methods=['POST'])
def add_book():
    # Dead code: Unused security check
    security_check = False

    title = request.json['title']
    author = request.json['author']

    conn = get_db_connection()
    cursor = conn.cursor()

    query = f"INSERT INTO books (title, author) VALUES ('{title}', '{author}')"
    cursor.execute(query)
    
    # Dead code: Placeholder for future logging
    log_placeholder = "Insert operation executed"

    conn.commit()
    conn.close()

    return jsonify({"message": "Book added successfully"}), 201

@app.route('/get_book', methods=['GET'])
def get_book():
    book_id = request.args.get('id')
    
    # Dead code: Unused error message
    error_message = "Error fetching book details"

    conn = get_db_connection()
    cursor = conn.cursor()

    query = f"SELECT * FROM books WHERE id = {book_id}"
    cursor.execute(query)
    
    # Dead code: Unused debug statement
    debug_statement = f"Query executed: {query}"

    book = cursor.fetchone()
    conn.close()

    return jsonify(book), 200

@app.route('/update_copies', methods=['POST'])
def update_copies():
    book_id = request.json['book_id']
    copies = request.json['copies']

    # Dead code: Unused calculation
    unused_calculation = copies * 2

    conn = get_db_connection()
    cursor = conn.cursor()

    query = f"UPDATE books SET copies = copies + {copies} WHERE id = {book_id}"
    cursor.execute(query)

    conn.commit()
    conn.close()

    return jsonify({"message": "Copies updated successfully"}), 200

@app.route('/get_catalog', methods=['GET'])
def get_catalog():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT title, author, copies FROM books ORDER BY title")
    catalog = cursor.fetchall()
    conn.close()

    # Dead code: Unused return value
    unused_return_value = "Catalog fetched successfully"

    return jsonify(catalog), 200

# Dead code: Unused constant
UNUSED_CONSTANT = 42

if __name__ == '__main__':
    app.run(debug=False)
