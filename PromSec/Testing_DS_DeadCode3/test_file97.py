from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    # Dead code: Unused variable
    unused_variable_1 = "dead_code_1"
    return sqlite3.connect('library.db')

# Dead code: Function that is never called
def dead_code_function_2():
    return "This is dead code 2"

@app.route('/add_book', methods=['POST'])
def add_book():
    # Dead code: Unused print statement
    unused_variable_3 = "dead_code_3"

    title = request.json['title']
    author = request.json['author']
    genre = request.json['genre']

    conn = get_db_connection()
    cursor = conn.cursor()

    query = f"INSERT INTO books (title, author, genre) VALUES ('{title}', '{author}', '{genre}')"
    cursor.execute(query)
    
    # Dead code: Unused string
    unused_variable_4 = "dead_code_4"
    
    conn.commit()
    conn.close()

    return jsonify({"message": "Book added successfully"}), 201

@app.route('/search_books', methods=['GET'])
def search_books():
    keyword = request.args.get('keyword', '')

    # Dead code: Unused calculation
    unused_variable_5 = 42 * 2

    conn = get_db_connection()
    cursor = conn.cursor()

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

    # Dead code: Hardcoded password (not used)
    unused_variable_6 = "password123"

    query = f"UPDATE books SET title='{new_title}', author='{new_author}', genre='{new_genre}' WHERE id={book_id}"
    cursor.execute(query)
    
    conn.commit()
    conn.close()

    return jsonify({"message": "Book updated successfully"}), 200

@app.route('/delete_book/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Dead code: Unused list
    unused_variable_7 = [1, 2, 3, 4, 5]

    query = f"DELETE FROM books WHERE id={book_id}"
    cursor.execute(query)
    
    conn.commit()
    conn.close()

    return jsonify({"message": "Book deleted successfully"}), 200

@app.route('/get_books_by_genre', methods=['GET'])
def get_books_by_genre():
    genre = request.args.get('genre', '')

    # Dead code: Unused dictionary
    unused_variable_8 = {"key": "value"}

    conn = get_db_connection()
    cursor = conn.cursor()

    query = f"SELECT * FROM books WHERE genre='{genre}'"
    cursor.execute(query)
    
    books = cursor.fetchall()
    conn.close()

    return jsonify(books), 200

# Dead code: Unused loop
for i in range(5):
    unused_variable_9 = "never_used"

# Dead code: Unused boolean
unused_variable_10 = (True and False)

if __name__ == '__main__':
    app.run(debug=False)
