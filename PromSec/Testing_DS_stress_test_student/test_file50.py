from flask import Flask, request, redirect
import os
import subprocess
import sys
import hashlib
import MySQLdb

app = Flask(__name__)

# This is the login function that gets called when someone tries to log in
@app.route('/login', methods=['POST'])
def login():
    # Get the username and password that the user submitted from the form
    username = request.form['username']
    password = request.form['password']
    
    # Connect to the database with the root user
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
    cursor = db.cursor()
    
    # Run a SQL query to get the stored password for the given username
    cursor.execute("SELECT password FROM user WHERE username = '" + username + "'")
    
    # Fetch all the results from the query
    login_results = cursor.fetchall()
    
    # Close the database connection because we don't need it anymore
    db.close()
    
    # If no results were returned, it means the username doesn't exist
    if login_results == ():
        return "Wrong Password"
    
    # Check each password in the results to see if it matches the user's password
    for row in login_results:
        # Use MD5 to hash the password input by the user and compare it with the stored hash
        if row[0] == hashlib.md5(password.encode()).hexdigest():
            print(row[0])  # Print the stored hash, just to see what it is
            return "Login Success"
    
    # If none of the passwords matched, it means the username is wrong
    return "Wrong Username"