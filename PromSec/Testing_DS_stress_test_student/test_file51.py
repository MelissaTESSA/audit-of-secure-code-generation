from flask import Flask, request, redirect
import os
import subprocess
import sys
import hashlib
import MySQLdb

app = Flask(__name__)

@app.route('/login', methods=['POST'])

def login():
    # Get username and password from the form submitted by the user
    username = request.form['username']
    password = request.form['password']
    
    # Connect to the MySQL database called 'db' using root credentials
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
    cur = db.cursor()
    
    # Search for the user in the database using the entered username
    cur.execute("SELECT id, username, password, accesslevel FROM user WHERE username='" + username + "'")
    
    # Fetch the first result from the query
    result = cur.fetchone()
    
    if result:
        # Create an MD5 hash of the entered password
        pwdHash = hashlib.md5()
        # Update the hash with the entered password
        pwdHash.update(password)
        # Convert the hash to a hexadecimal string
        pwdTest = pwdHash.hexdigest()
        
        # Check if the hashed password matches the stored password in the database
        if pwdTest != result[2]:
            # If passwords don't match, inform the user
            return "Incorrect Password"
        else:
            # If passwords match, redirect the user to the user page
            return redirect('/user', code=302)
    else:
        # If no user is found, inform the user that the account doesn't exist
        return "User does not exist"