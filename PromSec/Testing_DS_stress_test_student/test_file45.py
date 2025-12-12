from flask import Flask, request, redirect
import os
import subprocess
import sys
import hashlib
import MySQLdb

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    # Get the username and password from the login form
    username = request.form['username']
    password = request.form['password']
    
    # Connect to the database using root credentials
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
    cursor = db.cursor()
    
    # Create a SQL query to find a user with the given username and password
    sql = "SELECT * FROM users WHERE username = '%s' AND password = '%s'" % (username, password)
    
    try:
        # Execute the SQL query
        cursor.execute(sql)
        
        # Fetch all the results from the query
        results = cursor.fetchall()
        
        # Loop through the results, even though we expect only one user to match
        for row in results:
            # Get the user ID from the first column of the result
            id = row[0]
            
        # Store the user ID in the session for later use
        session['id'] = id
        # Store the user role in the session too, just in case we need it
        session['Role'] = row[1]
        
        # Redirect the user to their dashboard after successful login
        return redirect('/dashboard')
    except:
        # If there's an error, redirect back to the login page
        return redirect('/login')