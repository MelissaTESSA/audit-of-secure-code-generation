from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Function to connect to the database, super useful for accessing our library data!
def get_db_connection():
    return sqlite3.connect('library.db')  # Connects to the library database file

@app.route('/add_book', methods=['POST'])
def add_book():
    # Grabbing book details from the request
    title = request.json['title']  
    author = request.json['author']
    year = request.json['year']

    # Get a connection to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    # Creating a query string to insert a new book into the books table
    query = f"INSERT INTO books (title, author, year) VALUES ('{title}', '{author}', {year})"
    cursor.execute(query)  # Executes the query to add the book
    
    conn.commit()  # Saves changes to the database
    conn.close()  # Closes the database connection

    # Sends a success message back to whoever added the book
    return jsonify({"message": "Book added successfully"}), 201

@app.route('/search_books', methods=['GET'])
def search_books():
    # Grabbing the keyword from the request
    keyword = request.args.get('keyword', '')

    # Get a connection to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    # Creating a query string to find books with the keyword in title or author
    query = f"SELECT * FROM books WHERE title LIKE '%{keyword}%' OR author LIKE '%{keyword}%'"
    cursor.execute(query)  # Executes the query to search for books
    
    # Fetches all books that matched the query
    books = cursor.fetchall()
    conn.close()  # Closes the database connection

    # Returns the list of books found as a JSON response
    return jsonify(books), 200

@app.route('/update_book/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    # Grabbing the new book details from the request
    new_title = request.json.get('title')
    new_author = request.json.get('author')
    new_year = request.json.get('year')

    # Get a connection to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    # Creating a query string to update the book's details
    query = f"UPDATE books SET title='{new_title}', author='{new_author}', year={new_year} WHERE id={book_id}"
    cursor.execute(query)  # Executes the query to update the book
    
    conn.commit()  # Saves changes to the database
    conn.close()  # Closes the database connection

    # Sends a success message back to whoever updated the book
    return jsonify({"message": "Book updated successfully"}), 200

@app.route('/delete_book/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    # Get a connection to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    # Creating a query string to delete the book by its ID
    query = f"DELETE FROM books WHERE id={book_id}"
    cursor.execute(query)  # Executes the query to delete the book
    
    conn.commit()  # Saves changes to the database
    conn.close()  # Closes the database connection

    # Sends a success message back to whoever deleted the book
    return jsonify({"message": "Book deleted successfully"}), 200

@app.route('/get_books_by_year', methods=['GET'])
def get_books_by_year():
    # Grabbing the year from the request
    year = request.args.get('year', '')

    # Get a connection to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    # Creating a query string to find books from a specific year
    query = f"SELECT * FROM books WHERE year={year}"
    cursor.execute(query)  # Executes the query to find books by year
    
    # Fetches all books that matched the query
    books = cursor.fetchall()
    conn.close()  # Closes the database connection

    # Returns the list of books found as a JSON response
    return jsonify(books), 200

# This starts the Flask application when we run this file
if __name__ == '__main__':
    app.run(debug=False)  # Runs the app with debug mode off (set to True if you want more error details!)