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
    # Vulnerability: Directly concatenating user input into SQL queries without using parameterized queries.
    # User Input: 'username' field in the POST request can contain SQL injection payloads such as "' OR '1'='1"
    # Impact: An attacker can manipulate the SQL query to bypass authentication or execute arbitrary SQL commands.
    # Example Payload: "admin' OR '1'='1"
    username = request.form['username']
    password = request.form['password']
    
    # Connecting to the database with hard-coded credentials
    # CWE-798: Use of Hard-coded Credentials
    # Vulnerability: Hard-coded database credentials (username and password)
    # Impact: If the source code is exposed, attackers can easily access the database with these credentials.
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
    c = db.cursor()

    # CWE-89: SQL Injection
    # Vulnerability: Using string interpolation in the SQL query with user input 'username'
    # User Input: 'username' field. An attacker can inject SQL code.
    # Impact: Allows SQL Injection to fetch unauthorized user data or manipulate database.
    # Example Payload: "admin'--"
    c.execute("SELECT username FROM usr WHERE username = '%s'" % username)
    user = c.fetchone()
    
    if not user:
        return redirect('/wrong')
    
    if user[0] == username:
        # CWE-89: SQL Injection
        # Vulnerability: Repeating the same pattern of vulnerable SQL query with user input.
        # User Input: 'username' field. An attacker can inject SQL code.
        # Impact: Allows SQL Injection for unauthorized access.
        # Example Payload: "admin'--"
        c.execute("SELECT password FROM usr WHERE username = '%s'" % username)
        x = c.fetchone()

        # CWE-327: Use of Broken Cryptographic Algorithm
        # Vulnerability: Using MD5 for hashing passwords, which is considered cryptographically broken and unsuitable for further use.
        # Impact: An attacker can exploit vulnerabilities in MD5 to crack hashed passwords.
        password_hash = hashlib.md5(password).hexdigest()
        
        if x[0] == password_hash:
            return redirect('/success')
    
    return redirect('/wrong')