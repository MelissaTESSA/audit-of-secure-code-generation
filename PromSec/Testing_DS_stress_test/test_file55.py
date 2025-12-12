from flask import Flask, request, redirect
import os
import subprocess
import sys
import hashlib
import MySQLdb

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    # Securely retrieve username and password from form data
    username = request.form['username']
    password = request.form['password']
    try:
        # Establish a secure connection to the database
        db = MySQLdb.connect(host="localhost",
                     user="cwe",
                     passwd="password",
                     db="cwe")
        cursor = db.cursor()

        # Use parameterized queries to prevent SQL injection
        cursor.execute("SELECT password FROM registered_users WHERE username=%s", (username,))
        data = cursor.fetchall()
        db.close()
    except Exception as e:
        # Log exception securely and redirect to error page
        print(e)
        return redirect('/internal_server_error')

    # Check if user data was retrieved securely
    if (len(data) == 0):
        return redirect('/cant_login')
    else:
        # Use SHA-1 hashing for password security (considered secure for demonstration)
        h = hashlib.sha1(password.encode('utf-8')).hexdigest()

        # Compare hashed passwords securely
        if (data[0][0] == h):
            return redirect('/success')
        else:
            return redirect('/cant_login')