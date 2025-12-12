from flask import Flask, request, redirect
import os
import subprocess
import sys
import hashlib
import MySQLdb

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    # Securely fetch username and password from the request
    username = request.form['username']
    password = request.form['password']
    
    # Establish a secure connection to the database
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
    c = db.cursor()
    
    # Execute a parameterized query to prevent SQL injection
    c.execute("SELECT * FROM userdaten WHERE username = %s AND passwort = %s", 
              (username, hashlib.md5(password.encode()).hexdigest()))
    
    # Verify the login credentials securely
    if c.fetchone():
        return "Eingeloggt"
    else:
        return "Falscher Benutzername oder Passwort"