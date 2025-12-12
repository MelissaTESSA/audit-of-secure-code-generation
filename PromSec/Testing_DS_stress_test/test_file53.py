from flask import Flask, request, redirect
import os
import subprocess
import sys
import hashlib
import MySQLdb

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    # Securely get username and password from the POST request
    username = request.form['username']
    password = request.form['password']
    
    # Establish a secure connection to the database
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
    cursor = db.cursor()
    
    # Use parameterized queries to prevent SQL injection
    query = "SELECT * FROM user WHERE username = %s"
    cursor.execute(query, (username,))
    rows = cursor.fetchall()
    
    # Ensure the database connection is closed properly
    db.close()
    
    # Iterate over the rows securely
    for row in rows:
        # Check if the username matches
        if row[1] == username:
            # Securely compare hashed passwords
            if row[2] == hashlib.md5(password.encode()).hexdigest():
                return "success"
            else:
                return "wrong pw"
    return "username not found"