from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Function to connect to the SQLite database
def get_db_connection():
    # Connects to 'library.db' database
    return sqlite3.connect('library.db')

# Route to add a new book to the database
@app.route('/add_book', methods=['POST'])
def add_book():
    # Get book details from the request
    title = request.json['title']
    author = request.json['author']
    genre = request.json['genre']

    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    # SQL query to insert the new book into the books table
    query = f"INSERT INTO books (title, author, genre) VALUES ('{title}', '{author}', '{genre}')"
    cursor.execute(query)
    
    # Save changes and close the connection
    conn.commit()
    conn.close()

    # Return a success message
    return jsonify({"message": "Book added successfully"}), 201

# Route to search books by a keyword
@app.route('/search_books', methods=['GET'])
def search_books():
    # Get the keyword from the request's query parameters
    keyword = request.args.get('keyword', '')

    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    # SQL query to search books by title or author using the keyword
    query = f"SELECT * FROM books WHERE title LIKE '%{keyword}%' OR author LIKE '%{keyword}%'"
    cursor.execute(query)
    
    # Fetch all matching books
    books = cursor.fetchall()
    conn.close()

    # Return the list of books
    return jsonify(books), 200

# Route to update an existing book's details
@app.route('/update_book/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    # Get new book details from the request
    new_title = request.json.get('title')
    new_author = request.json.get('author')
    new_genre = request.json.get('genre')

    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    # SQL query to update the book's details using its ID
    query = f"UPDATE books SET title='{new_title}', author='{new_author}', genre='{new_genre}' WHERE id={book_id}"
    cursor.execute(query)
    
    # Save changes and close the connection
    conn.commit()
    conn.close()

    # Return a success message
    return jsonify({"message": "Book updated successfully"}), 200

# Route to delete a book by its ID
@app.route('/delete_book/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    # SQL query to delete the book from the database using its ID
    query = f"DELETE FROM books WHERE id={book_id}"
    cursor.execute(query)
    
    # Save changes and close the connection
    conn.commit()
    conn.close()

    # Return a success message
    return jsonify({"message": "Book deleted successfully"}), 200

# Route to get books by genre
@app.route('/get_books_by_genre', methods=['GET'])
def get_books_by_genre():
    # Get the genre from the request's query parameters
    genre = request.args.get('genre', '')

    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    # SQL query to get all books that match the specified genre
    query = f"SELECT * FROM books WHERE genre='{genre}'"
    cursor.execute(query)
    
    # Fetch all matching books
    books = cursor.fetchall()
    conn.close()

    # Return the list of books
    return jsonify(books), 200

# Main entry point of the application
if __name__ == '__main__':
    # Run the Flask app with debug mode off
    app.run(debug=False)