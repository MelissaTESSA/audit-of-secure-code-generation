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
    # Vulnerability: The user input 'username' is directly concatenated into the SQL query.
    # Exploit: An attacker could use ' OR '1'='1 to bypass authentication.
    # Impact: Unauthorized access to user data.
    username = request.form['username']
    password = request.form['password']
    
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
    cursor = db.cursor()
    
    # CWE-89: SQL Injection
    # Vulnerability: SQL query is constructed using string concatenation with user input.
    # Exploit: An attacker could inject SQL commands to manipulate or access sensitive data.
    # Example Payload: "' OR '1'='1"
    cursor.execute("SELECT password FROM user WHERE username = '" + username + "'")
    
    login_results = cursor.fetchall()
    db.close()
    
    if login_results == ():
        return "Wrong Password"
    
    for row in login_results:
        # CWE-327: Use of Broken Cryptographic Algorithm
        # Vulnerability: MD5 is used for password hashing, which is considered broken and vulnerable to collisions.
        # Impact: Attackers can exploit the weak hash to gain unauthorized access.
        if row[0] == hashlib.md5(password.encode()).hexdigest():
            
            # CWE-209: Information Exposure Through Error Messages
            # Vulnerability: The actual stored hashed password is printed to the console.
            # Impact: Sensitive information exposure if logs are accessed by unauthorized users.
            print(row[0])
            
            return "Login Success"
    
    return "Wrong Username"