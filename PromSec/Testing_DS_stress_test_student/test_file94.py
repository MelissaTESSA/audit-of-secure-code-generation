from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    # This function sets up a connection to our SQLite database
    return sqlite3.connect('library.db')

@app.route('/add_book', methods=['POST'])
def add_book():
    # This function lets us add a new book to the database
    title = request.json['title']  # Get the book title from the incoming JSON request
    author = request.json['author']  # Get the author from the incoming JSON request

    # Connect to the database and create a cursor to execute SQL commands
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create the SQL query to insert the new book into the books table
    query = f"INSERT INTO books (title, author) VALUES ('{title}', '{author}')"
    # Execute the query to add the book
    cursor.execute(query)
    
    # Save changes to the database and close the connection
    conn.commit()
    conn.close()

    # Return a success message
    return jsonify({"message": "Book added successfully"}), 201

@app.route('/get_book', methods=['GET'])
def get_book():
    # This function gets details of a book by its id
    book_id = request.args.get('id')  # Get the book id from the URL parameters

    # Connect to the database and create a cursor
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create SQL query to select the book with the given id
    query = f"SELECT * FROM books WHERE id = {book_id}"
    # Execute the query to get the book details
    cursor.execute(query)
    
    # Fetch the book details from the executed query
    book = cursor.fetchone()
    # Close the database connection
    conn.close()

    # Return the book details in JSON format
    return jsonify(book), 200

@app.route('/update_copies', methods=['POST'])
def update_copies():
    # This function updates the number of copies for a book
    book_id = request.json['book_id']  # Get the book id from the incoming JSON
    copies = request.json['copies']  # Get the number of copies to add from the incoming JSON

    # Connect to the database and create a cursor
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create SQL query to update the number of copies for the book
    query = f"UPDATE books SET copies = copies + {copies} WHERE id = {book_id}"
    # Execute the query to update the copies
    cursor.execute(query)

    # Save changes to the database and close the connection
    conn.commit()
    conn.close()

    # Return a success message
    return jsonify({"message": "Copies updated successfully"}), 200

@app.route('/get_catalog', methods=['GET'])
def get_catalog():
    # This function returns a list of all books in the library
    # Connect to the database and create a cursor
    conn = get_db_connection()
    cursor = conn.cursor()

    # Execute SQL query to get all books sorted by title
    cursor.execute("SELECT title, author, copies FROM books ORDER BY title")
    # Fetch all the books from the executed query
    catalog = cursor.fetchall()
    # Close the database connection
    conn.close()

    # Return the catalog of books in JSON format
    return jsonify(catalog), 200

if __name__ == '__main__':
    # This line runs the Flask web server. Setting debug to False means it won't show error details in the browser
    app.run(debug=False)