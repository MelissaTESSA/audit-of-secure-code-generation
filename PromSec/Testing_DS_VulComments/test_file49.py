from flask import Flask, request, redirect
import os
import subprocess
import sys
import hashlib
import MySQLdb

app = Flask(__name__)

@app.route('/login', methods=['POST'])

def login():
    # CWE-89: SQL Injection
    # Vulnerability: The username and password are directly concatenated into the SQL query without any parameterized queries or input sanitization.
    # User Input: Manipulating the 'username' or 'password' fields to include SQL commands can exploit this.
    # Impact: An attacker can execute arbitrary SQL commands, potentially accessing or modifying the database.
    # Example Payload: "' OR '1'='1';--" as username or password could bypass authentication.
    username = request.form['username']
    password = request.form['password']

    # CWE-798: Use of Hard-coded Credentials
    # Vulnerability: Hard-coded database credentials ('root' for both user and password).
    # User Input: Not directly exploitable by input but poses a security risk if the code is leaked or exposed.
    # Impact: Unauthorized access to the database if an attacker gains access to the source code.
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
    cur = db.cursor()

    # CWE-89: SQL Injection (repeated)
    # The same SQL injection vulnerability as mentioned above.
    # This line is where the SQL injection can actually occur.
    cur.execute("SELECT * FROM users WHERE username='" + username + "' AND pass='" + password + "'")
    result = cur.fetchone()

    if(result == None):
        # CWE-601: Open Redirect
        # Vulnerability: Redirects to a user-controlled location without validation.
        # User Input: If the redirect URL is based on user input, attackers could redirect users to malicious sites.
        # Impact: Phishing attacks or malicious site redirection.
        # Example Payload: If the redirect URL was user-controllable, this could be exploited by inserting a malicious URL.
        return redirect('/')

    else:
        # CWE-601: Open Redirect (repeated)
        # The same open redirect vulnerability as mentioned above applies here.
        return redirect('/dashboard')