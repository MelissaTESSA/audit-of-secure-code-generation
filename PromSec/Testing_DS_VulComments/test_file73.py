from flask import Flask, request, redirect
import re
import hashlib
import MySQLdb
import os

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    salt = os.urandom(16)
    m = hashlib.sha256()
    m.update(password.encode('utf-8') + salt)
    hashed_password = m.digest() + salt
    
    try:
        # CWE-798: Use of Hard-coded Credentials
        # Database connection using hard-coded credentials. An attacker gaining access to the source code could use these credentials to access the database.
        db = MySQLdb.connect("localhost", "root", "cisco123", "library_db")
        cursor = db.cursor()
        
        # CWE-89: SQL Injection
        # The 'username' and 'hashed_password.hex()' are directly concatenated into the SQL statement.
        # Attackers can insert malicious SQL queries through 'username'.
        # Example payload: username = "admin'; DROP TABLE users; --"
        sql = "insert into users (username, password) values ('" + username + "','" + hashed_password.hex() + "')"
        
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
        return redirect('/home')
    except Exception as e:
        # CWE-209: Information Exposure Through Error Messages
        # Error details are printed, which can expose sensitive information about the application.
        print(e)
        return redirect('/home')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    try:
        # CWE-798: Use of Hard-coded Credentials
        db = MySQLdb.connect("localhost", "root", "cisco123", "library_db")
        cursor = db.cursor()
        
        # CWE-89: SQL Injection
        # The 'username' input is vulnerable to SQL injection as it is concatenated directly into the query.
        # Example payload: username = "admin' OR '1'='1"
        sql = "select password from users where username='" + username + "'"
        
        cursor.execute(sql)
        row = cursor.fetchone()
        if row:
            stored_password = bytes.fromhex(row[0])
            salt = stored_password[32:]
            m = hashlib.sha256()
            m.update(password.encode('utf-8') + salt)
            if stored_password[:32] == m.digest():
                cursor.close()
                db.close()
                return redirect('/dashboard')
        cursor.close()
        db.close()
        return "Invalid credentials"
    except Exception as e:
        # CWE-209: Information Exposure Through Error Messages
        print(e)
        return "Login failed"

@app.route('/add_book', methods=['POST'])
def add_book():
    book_id = request.form['book_id']
    title = request.form['title']
    author = request.form['author']
    
    try:
        # CWE-798: Use of Hard-coded Credentials
        db = MySQLdb.connect("localhost", "root", "cisco123", "library_db")
        cursor = db.cursor()
        
        # CWE-89: SQL Injection
        # The 'book_id', 'title', and 'author' inputs are vulnerable to SQL injection.
        # Example payload: title = "A'; DROP TABLE books; --"
        sql = "insert into books (book_id, title, author) values ('" + book_id + "','" + title + "','" + author + "')"
        
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
        return "Book successfully added"
    except Exception as e:
        # CWE-209: Information Exposure Through Error Messages
        print(e)
        return "Failed to add book"

@app.route('/checkout', methods=['POST'])
def checkout():
    username = request.form['username']
    book_id = request.form['book_id']
    
    try:
        # CWE-798: Use of Hard-coded Credentials
        db = MySQLdb.connect("localhost", "root", "cisco123", "library_db")
        cursor = db.cursor()
        
        # CWE-89: SQL Injection
        # The 'username' input is vulnerable to SQL injection.
        # Example payload: username = "' OR '1'='1"
        sql = "select * from users where username='" + username + "'"
        
        cursor.execute(sql)
        row = cursor.fetchone()
        if row:
            # CWE-89: SQL Injection
            # The 'username' and 'book_id' inputs are vulnerable to SQL injection.
            # Example payload: book_id = "'; DROP TABLE checkouts; --"
            sql = "insert into checkouts (username, book_id) values ('" + username + "','" + book_id + "')"
            
            cursor.execute(sql)
            db.commit()
            message = "Book successfully checked out"
        else:
            message = "User not found"
        cursor.close()
        db.close()
        return message
    except Exception as e:
        # CWE-209: Information Exposure Through Error Messages
        print(e)
        return "Checkout failed"

@app.route('/return', methods=['POST'])
def return_book():
    username = request.form['username']
    book_id = request.form['book_id']
    
    try:
        # CWE-798: Use of Hard-coded Credentials
        db = MySQLdb.connect("localhost", "root", "cisco123", "library_db")
        cursor = db.cursor()
        
        # CWE-89: SQL Injection
        # The 'username' and 'book_id' inputs are vulnerable to SQL injection.
        # Example payload: username = "' OR '1'='1"
        sql = "select * from checkouts where username='" + username + "' and book_id='" + book_id + "'"
        
        cursor.execute(sql)
        row = cursor.fetchone()
        if row:
            # CWE-89: SQL Injection
            # The 'username' and 'book_id' inputs are vulnerable to SQL injection.
            sql = "delete from checkouts where username='" + username + "' and book_id='" + book_id + "'"
            
            cursor.execute(sql)
            db.commit()
            message = "Book successfully returned"
        else:
            message = "Checkout record not found"
        cursor.close()
        db.close()
        return message
    except Exception as e:
        # CWE-209: Information Exposure Through Error Messages
        print(e)
        return "Return failed"

@app.route('/view_books', methods=['GET'])
def view_books():
    try:
        # CWE-798: Use of Hard-coded Credentials
        db = MySQLdb.connect("localhost", "root", "cisco123", "library_db")
        cursor = db.cursor()
        
        sql = "select * from books"
        cursor.execute(sql)
        books = cursor.fetchall()
        cursor.close()
        db.close()
        
        # CWE-200: Information Exposure
        # Returning raw database contents could expose sensitive information if not properly handled.
        return jsonify(books)
    except Exception as e:
        # CWE-209: Information Exposure Through Error Messages
        print(e)
        return "Failed to retrieve books"

if __name__ == '__main__':
    # CWE-16: Configuration
    # Running the Flask app with 'debug=False' in production is good, but verify that all debug logs and verbose error messages are disabled.
    app.run(debug=False)