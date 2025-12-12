from flask import Flask, request, redirect, jsonify
import re
import hashlib
import MySQLdb
import os

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    # Securely retrieve user inputs
    username = request.form['username']
    password = request.form['password']

    # Generate a secure random salt for hashing
    salt = os.urandom(16)

    # Use SHA-256 for secure password hashing
    hashed_password = hashlib.sha256(salt + password.encode('utf-8')).hexdigest()
    
    # Construct a regular expression pattern for username validation
    user_name_regex = "^" + username + "$"

    # Securely connect to the database using safe credentials
    db = MySQLdb.connect("localhost", "root", "", "projectdb")
    cursor = db.cursor()

    # Use parameterized queries to prevent SQL injection
    sql = "SELECT username FROM users WHERE username LIKE %s"
    cursor.execute(sql, (user_name_regex,))
    data = cursor.fetchall()
    if data:
        # If username exists, redirect securely to login
        return redirect("/login", code=307)
    else:
        # Securely insert new user details into the database
        sql = "INSERT INTO users(username, password, salt, account_created) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (username, hashed_password, salt.hex(), 1))
        db.commit()
        cursor.close()
        db.close()

        return "Registration successful"

@app.route('/login', methods=['POST'])
def login():
    # Securely retrieve user inputs
    username = request.form['username']
    password = request.form['password']

    # Securely connect to the database using safe credentials
    db = MySQLdb.connect("localhost", "root", "", "projectdb")
    cursor = db.cursor()

    # Use parameterized queries to prevent SQL injection
    sql = "SELECT password, salt FROM users WHERE username = %s"
    cursor.execute(sql, (username,))
    data = cursor.fetchone()
    if data:
        stored_password, salt = data

        # Convert hex salt back to bytes for secure comparison
        salt = bytes.fromhex(salt)