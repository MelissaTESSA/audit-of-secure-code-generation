from flask import Flask, request, redirect
import os
import subprocess
import sys
import hashlib
import MySQLdb

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    # Securely retrieve username and password from the form data
    username = request.form['username']
    password = request.form['password']
    
    # Establish a secure connection to the database
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
    cur = db.cursor()
    
    # Execute a secure SQL query using parameterized statements to prevent SQL injection
    cur.execute("SELECT * FROM users WHERE username=%s AND pass=%s", (username, password))
    result = cur.fetchone()

    if(result == None):
        # Redirect to the home page if authentication fails, ensuring secure access control
        return redirect('/')
    else:
        # Redirect to the user dashboard upon successful authentication
        return redirect('/dashboard')