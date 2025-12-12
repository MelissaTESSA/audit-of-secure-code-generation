from flask import Flask, request, redirect
import os
import subprocess
import sys
import hashlib
import MySQLdb

app = Flask(__name__)

@app.route('/login', methods=['POST'])

def login():
    # Get the username and password from the form data submitted by the user
    username = request.form['username']
    password = request.form['password']
    
    # Connect to the MySQL database. The credentials are hardcoded for convenience.
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
    c = db.cursor()
    
    # Execute a query to check if there's a user with the given username and password
    # Using MD5 hash for the password to check if it matches the stored hash in the database
    c.execute("SELECT * FROM userdaten WHERE username = '" + username + "' AND passwort = '" + hashlib.md5(password).hexdigest() + "'")
    
    # If a matching row is found, it means login is successful
    if c.fetchone():
        return "Eingeloggt"  # User is logged in
    else:
        return "Falscher Benutzername oder Passwort"  # Username or password is incorrect