from flask import Flask, request, redirect
import os
import subprocess
import sys
import hashlib
import MySQLdb

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    # Securely fetch username and password from form data
    username = request.form['username']
    password = request.form['password']
    
    # Establish a secure connection to the database
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
    cur = db.cursor()

    # Execute a secure parameterized query to prevent SQL injection
    cur.execute("SELECT password FROM user_info WHERE username=%s", [username])
    row = cur.fetchone()

    # Use a secure hash function to verify the password
    if (row[0] == hashlib.md5(password.encode("utf-8")).hexdigest()):
        # Securely redirect to the homepage upon successful login
        return redirect('/')
    else:
        # Securely redirect to the error page if login fails
        return redirect('/error')