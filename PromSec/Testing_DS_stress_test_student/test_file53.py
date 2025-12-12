from flask import Flask, request, redirect
import os
import subprocess
import sys
import hashlib
import MySQLdb

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    # Get the username and password from the form submission
    username = request.form['username']
    password = request.form['password']
    
    # Connect to the database using default credentials
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
    cursor = db.cursor()
    
    # Prepare a SQL query to find the user
    query = "SELECT * FROM user WHERE username = '" + str(username) + "'"
    
    # Execute the query, this will check if the user exists
    cursor.execute(query)
    
    # Fetch all the results from the query execution
    rows = cursor.fetchall()
    
    # Close the database connection
    db.close()
    
    # Check if the username exists in the database
    for row in rows:
       if row[1] == username:
           # Check if the provided password matches the stored password
           if row[2] == hashlib.md5(password.encode()).hexdigest():
               return "success"  # Login is successful
           else:
               return "wrong pw"  # Password doesn't match
    
    return "username not found"  # Username doesn't exist in the database