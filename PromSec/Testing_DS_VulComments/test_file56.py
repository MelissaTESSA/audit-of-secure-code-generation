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
    try:
        # CWE-89: SQL Injection
        # Vulnerability: Directly concatenating user input into an SQL query.
        # Exploit: User input like "username' OR '1'='1" can bypass authentication.
        # Impact: Unauthorized access to user accounts.
        # Example payload: username="admin'--" or username="' OR '1'='1"
        conn = MySQLdb.connect(host="localhost", user="root", passwd="", db="cwe200")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username='"+username+"' AND password='"+password+"'")
        rows = cursor.fetchall()
        
        if len(rows) > 0:
            # CWE-287: Improper Authentication
            # Vulnerability: Relies solely on password comparison for authentication without additional checks.
            # Exploit: If password hashes are not used, access can be easily compromised.
            # Impact: Unauthorized access if passwords are weak or reused.
            session['username'] = username
            return redirect('/session')
        else:
            return 'Incorrect username or password'
    except MySQLdb.Error:
        # CWE-209: Information Exposure Through Error Messages
        # Vulnerability: The same error message is shown regardless of the error type.
        # Exploit: Attacker cannot differentiate errors, but it may still expose sensitive handling.
        # Impact: May provide clues during brute force attacks.
        return 'Incorrect username or password'