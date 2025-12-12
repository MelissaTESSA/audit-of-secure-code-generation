from flask import Flask, request, redirect
import os
import subprocess
import sys
import hashlib
import MySQLdb

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # CWE-798: Use of Hard-coded Credentials
    # The database connection uses hard-coded credentials for the root user, which is a security risk.
    # If an attacker gains access to this code, they could use these credentials to access the database with full privileges.
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
    
    cursor = db.cursor()
    
    # CWE-89: SQL Injection
    # The SQL query directly concatenates user input (`username`) into the query string.
    # An attacker could inject SQL code through the `username` field to manipulate the database.
    # Example payload: `username = "admin' OR '1'='1"` which could bypass authentication.
    cursor.execute("SELECT * FROM user WHERE username='" + username + "'")
    
    results = cursor.fetchall()
    if len(results) == 0:
        return "Login failed!"
    
    # CWE-327: Use of Broken Cryptographic Algorithm
    # SHA-1 is used for password hashing, which is considered broken due to vulnerabilities to collision attacks.
    # An attacker with resources could potentially generate a hash collision and bypass password verification.
    hashed_password = results[0][1]
    if hashed_password == hashlib.sha1(password).hexdigest():
        
        # CWE-79: Cross-Site Scripting (XSS)
        # The `username` is directly included in the response without any sanitization or escaping.
        # An attacker could inject scripts through the `username` field, which would execute in the user's browser.
        # Example payload: `username = "<script>alert('XSS')</script>"`
        return "Welcome " + username + "!"
    else:
        return "Login failed!"