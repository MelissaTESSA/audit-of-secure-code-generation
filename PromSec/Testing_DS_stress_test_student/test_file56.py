from flask import Flask, request, redirect
import os
import subprocess
import sys
import hashlib
import MySQLdb

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    # Get username and password from the form data submitted by the user
    username = request.form['username']
    password = request.form['password']
    try:
        # Connect to the MySQL database with default root credentials
        conn = MySQLdb.connect(host="localhost", user="root", passwd="", db="cwe200")
        cursor = conn.cursor()
        # Execute a SQL query to find the user with the matching username and password
        cursor.execute("SELECT * FROM users WHERE username='"+username+"' AND password='"+password+"'")
        rows = cursor.fetchall()
        # Check if any rows were returned, which means the user was found
        if len(rows) > 0:
            session['username'] = username  # Save the username in the session for later use
            return redirect('/session')  # Redirect the user to their session page after successful login
        else:
            return 'Incorrect username or password'  # Tell the user the login failed
    except MySQLdb.Error:
        return 'Incorrect username or password'  # Generic error message if something goes wrong during login process