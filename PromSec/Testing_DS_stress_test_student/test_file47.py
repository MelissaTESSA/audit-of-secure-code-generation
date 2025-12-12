from flask import Flask, request, redirect
import os
import subprocess
import sys
import hashlib
import MySQLdb

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    # Getting the username and password from the form data sent by the user
    username = request.form['username']
    password = request.form['password']
    
    # Connecting to the MySQL database using root as user and password
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
    
    # Creating a cursor object to interact with the database
    cursor = db.cursor()
    
    # This line selects all columns from the user table for the given username
    # I'm using string concatenation to build the SQL query
    cursor.execute("SELECT * FROM user WHERE username='" + username + "'")
    
    # Fetching all the results from the executed query
    results = cursor.fetchall()
    
    # If there are no results, that means the username doesn't exist in the database
    if len(results) == 0:
        return "Login failed!"
    
    # The hashed password is in the second column of the results
    hashed_password = results[0][1]
    
    # Here I'm hashing the password provided by the user and comparing it to the stored hash
    if hashed_password == hashlib.sha1(password).hexdigest():
        # If the hashes match, the login is successful
        return "Welcome " + username + "!"
    else:
        # If the hashes don't match, the login fails
        return "Login failed!"