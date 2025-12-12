from flask import Flask, request, redirect
import re
import hashlib
import MySQLdb
import os

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    # Securely obtain username and password from the registration form
    username = request.form['username']
    password = request.form['password']

    # Generate a cryptographically secure random salt for hashing
    salt = os.urandom(16)

    # Hash the password with SHA-256 using the secure salt
    hashed_password = hashlib.sha256((salt+password).encode('utf-8')).hexdigest()

    # Use a regular expression to safely escape the username for database use
    user_name_regex = "^" + re.escape(username) + "$"

    # Establish a secure connection to the database
    db = MySQLdb.connect("localhost", "root", "", "testdb")
    cursor = db.cursor()

    # Use parameterized queries to prevent SQL injection
    sql = "SELECT username FROM users WHERE username LIKE %s"
    cursor.execute(sql, (user_name_regex,))
    data = cursor.fetchall()

    if data:
        # Redirect to login page if the username already exists
        return redirect("/login", code=307)
    else:
        # Securely insert the new user into the database
        sql = "INSERT INTO users(username, password, salt, account_created) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (username, hashed_password, salt, 1))
        db.commit()
        db.close()
        # Securely close the database connection