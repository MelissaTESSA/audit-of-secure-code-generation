from flask import Flask, request, redirect
import os
import subprocess
import sys
import hashlib
import MySQLdb

app = Flask(__name__)

@app.route('/login', methods=['POST'])

def login():
    # Get the username and password from the form data sent by the user
    username = request.form['username']
    password = request.form['password']
    
    # Connect to the local MySQL database using root credentials, so cool!
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
    
    # Create a cursor object to interact with the database
    cur = db.cursor()
    
    # Create a SQL query to find a user with matching username and password
    cur.execute("SELECT * FROM users WHERE username='" + username + "' AND pass='" + password + "'")
    
    # Fetch the result of the query, if any
    result = cur.fetchone()

    # If no user is found, redirect to the home page
    if(result == None):
        return redirect('/')
    else:
        # If a user is found, redirect to the dashboard
        return redirect('/dashboard')