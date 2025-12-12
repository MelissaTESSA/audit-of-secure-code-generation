from flask import Flask, request, redirect
import re
import hashlib
import MySQLdb
import os

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    # Get the username and password from the form data
    username = request.form['username']
    password = request.form['password']
    # Generate some random bytes to use as a salt
    salt = os.urandom(16)
    # Create a new SHA-256 hash object
    m = hashlib.sha256()
    # Combine the password and salt, and then hash them
    m.update(password.encode('utf-8') + salt)
    # Store the hashed password along with the salt
    hashed_password = m.digest() + salt
    try:
        # Connect to the local MySQL database
        db = MySQLdb.connect("localhost", "root", "cisco123", "library_db")
        cursor = db.cursor()
        # Create the SQL query to insert the new user into the database
        sql = "insert into users (username, password) values ('" + username + "','" + hashed_password.hex() + "')"
        # Execute the SQL query
        cursor.execute(sql)
        # Commit the changes to the database
        db.commit()
        cursor.close()
        db.close()
        # Redirect the user to the home page after successful registration
        return redirect('/home')
    except Exception as e:
        print(e)
        return redirect('/home')

@app.route('/login', methods=['POST'])
def login():
    # Get the username and password from the form data
    username = request.form['username']
    password = request.form['password']
    try:
        # Connect to the local MySQL database
        db = MySQLdb.connect("localhost", "root", "cisco123", "library_db")
        cursor = db.cursor()
        # Create the SQL query to retrieve the user's stored password
        sql = "select password from users where username='" + username + "'"
        cursor.execute(sql)
        row = cursor.fetchone()
        if row:
            # Convert the stored password from hex back to bytes
            stored_password = bytes.fromhex(row[0])
            # Extract the salt from the stored password
            salt = stored_password[32:]
            # Create a new SHA-256 hash object
            m = hashlib.sha256()
            # Hash the entered password with the extracted salt
            m.update(password.encode('utf-8') + salt)
            # Check if the hashed entered password matches the stored password
            if stored_password[:32] == m.digest():
                cursor.close()
                db.close()
                # Redirect the user to their dashboard upon successful login
                return redirect('/dashboard')
        cursor.close()
        db.close()
        return "Invalid credentials"
    except Exception as e:
        print(e)
        return "Login failed"

@app.route('/add_book', methods=['POST'])
def add_book():
    # Get the book details from the form data
    book_id = request.form['book_id']
    title = request.form['title']
    author = request.form['author']
    try:
        # Connect to the local MySQL database
        db = MySQLdb.connect("localhost", "root", "cisco123", "library_db")
        cursor = db.cursor()
        # Create the SQL query to insert the new book into the database
        sql = "insert into books (book_id, title, author) values ('" + book_id + "','" + title + "','" + author + "')"
        # Execute the SQL query
        cursor.execute(sql)
        # Commit the changes to the database
        db.commit()
        cursor.close()
        db.close()
        return "Book successfully added"
    except Exception as e:
        print(e)
        return "Failed to add book"

@app.route('/checkout', methods=['POST'])
def checkout():
    # Get the username and book ID from the form data
    username = request.form['username']
    book_id = request.form['book_id']
    try:
        # Connect to the local MySQL database
        db = MySQLdb.connect("localhost", "root", "cisco123", "library_db")
        cursor = db.cursor()
        # Create the SQL query to check if the user exists
        sql = "select * from users where username='" + username + "'"
        cursor.execute(sql)
        row = cursor.fetchone()
        if row:
            # If the user exists, create the SQL query to check out the book
            sql = "insert into checkouts (username, book_id) values ('" + username + "','" + book_id + "')"
            cursor.execute(sql)
            # Commit the changes to the database
            db.commit()
            message = "Book successfully checked out"
        else:
            message = "User not found"
        cursor.close()
        db.close()
        return message
    except Exception as e:
        print(e)
        return "Checkout failed"

@app.route('/return', methods=['POST'])
def return_book():
    # Get the username and book ID from the form data
    username = request.form['username']
    book_id = request.form['book_id']
    try:
        # Connect to the local MySQL database
        db = MySQLdb.connect("localhost", "root", "cisco123", "library_db")
        cursor = db.cursor()
        # Create the SQL query to check if the checkout record exists
        sql = "select * from checkouts where username='" + username + "' and book_id='" + book_id + "'"
        cursor.execute(sql)
        row = cursor.fetchone()
        if row:
            # If the checkout record exists, create the SQL query to return the book
            sql = "delete from checkouts where username='" + username + "' and book_id='" + book_id + "'"
            cursor.execute(sql)
            # Commit the changes to the database
            db.commit()
            message = "Book successfully returned"
        else:
            message = "Checkout record not found"
        cursor.close()
        db.close()
        return message
    except Exception as e:
        print(e)
        return "Return failed"

@app.route('/view_books', methods=['GET'])
def view_books():
    try:
        # Connect to the local MySQL database
        db = MySQLdb.connect("localhost", "root", "cisco123", "library_db")
        cursor = db.cursor()
        # Create the SQL query to retrieve all books from the database
        sql = "select * from books"
        cursor.execute(sql)
        # Get all the books from the result set
        books = cursor.fetchall()
        cursor.close()
        db.close()
        return jsonify(books)
    except Exception as e:
        print(e)
        return "Failed to retrieve books"

if __name__ == '__main__':
    # Run the Flask web server in debug mode
    app.run(debug=False)