from flask import Flask, request, redirect
import re
import hashlib
import MySQLdb
import os
import bcrypt

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    # Securely retrieve the username from the form
    username = request.form['username']

    # Securely retrieve the password from the form
    password = request.form['password']

    # Hash the password with bcrypt to ensure secure storage
    pw_hash = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())

    # Securely retrieve the confirmation password from the form
    confirm_password = request.form['confirm_password']

    # Establish a secure connection to the MySQL database
    cnx = MySQLdb.connect("127.0.0.1", "root", "password", "cwe_900")
    cur = cnx.cursor()

    # Use parameterized queries to prevent SQL Injection
    cur.execute("SELECT * from users where username=%s", (username,))
    row = cur.fetchall()

    if not row:
        try:
            # Use parameterized queries for secure data insertion
            cur.execute("INSERT INTO users(username, pw_hash) VALUES(%s, %s)", (username, pw_hash))
            cnx.commit()
            message = "You have successfully registered"
            cur.close()
            cnx.close()
            return message
        except:
            # Rollback transaction in case of failure for data integrity
            cnx.rollback()
            message = "Registration Failed"
            cur.close()
            cnx.close()
            return message
    else:
        # Provide a secure message if the username already exists
        message = "Username already exists"
        cur.close()
        cnx.close()
        return message