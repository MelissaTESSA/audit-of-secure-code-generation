from flask import Flask, request, redirect
import os
import subprocess
import sys
import hashlib
import MySQLdb

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    # Get the username from the form submitted by the user
    username = request.form['username']
    # Get the password from the form submitted by the user
    password = request.form['password']
    
    # Connect to the local MySQL database named "db"
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
    # Create a cursor object to interact with the database
    cur = db.cursor()
    
    # Execute a SQL query to get the password for the given username
    cur.execute("SELECT password FROM user_info WHERE username=%s", [username])
    
    # Fetch the first row of the result (should only be one row if the username is unique)
    row = cur.fetchone()
    
    # Check if the password from the database matches the one provided by the user
    if (row[0] == hashlib.md5(password.encode("utf-8")).hexdigest()):
        # If they match, redirect the user to the homepage
        return redirect('/')
    else:
        # If they don't match, redirect the user to an error page
        return redirect('/error')