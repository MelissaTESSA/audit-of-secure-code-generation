from flask import Flask, request, redirect
import os
import subprocess
import sys
import hashlib
import MySQLdb

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    # Get the username and password from the form data
    username = request.form['username']
    password = request.form['password']
    
    # Connect to the database with hardcoded root credentials
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
    
    # Create a cursor object to interact with the database
    c = db.cursor()
    
    # Execute a SQL query to check if the username exists in the database
    # Using % formatting to insert the username directly into the query
    c.execute("SELECT username FROM usr WHERE username = '%s'" %username)
    
    # Fetch the first result from the query
    user = c.fetchone()
    
    # If no user is found, redirect to the wrong page
    if not user:
        return redirect('/wrong')
    
    # Check if the fetched username matches the input username
    if user[0] == username:
        # If the usernames match, get the stored password hash for that username
        c.execute("SELECT password FROM usr WHERE username = '%s'" %username)
        x = c.fetchone()
        
        # Create a hash of the input password using MD5
        password_hash = hashlib.md5(password).hexdigest()
        
        # Compare the stored password hash with the hash of the input password
        if x[0] == password_hash:
            # If the hashes match, redirect to the success page
            return redirect('/success')
    
    # If anything fails, redirect to the wrong page
    return redirect('/wrong')