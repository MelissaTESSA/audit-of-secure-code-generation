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
    # The database is accessed using hard-coded credentials ("root", "root"), which is a security risk.
    # An attacker gaining access to the code could use these credentials to access the database.
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
    
    cur = db.cursor()
    
    # CWE-89: SQL Injection
    # The SQL query is constructed using string concatenation with user input (username).
    # An attacker can manipulate the 'username' variable to execute arbitrary SQL code.
    # Example attack payload: username = "' OR '1'='1"
    cur.execute("SELECT id, username, password, accesslevel FROM user WHERE username='" + username + "'")
    
    result = cur.fetchone()
    if result:
        # CWE-327: Use of Broken Cryptographic Algorithm
        # MD5 is used for hashing passwords, which is considered broken and vulnerable to collision attacks.
        # An attacker could potentially generate a hash collision to gain unauthorized access.
        pwdHash = hashlib.md5()
        
        # CWE-20: Improper Input Validation
        # The password is directly hashed without validating or normalizing input, which could lead to inconsistencies.
        pwdHash.update(password)
        
        pwdTest = pwdHash.hexdigest()
        
        if pwdTest != result[2]:
            return "Incorrect Password"
        else:
            # CWE-601: Open Redirect
            # The redirect targets a fixed URL, but if any part of this were influenced by user input, it could lead to an Open Redirect vulnerability.
            return redirect('/user', code=302)
    else:
        # CWE-209: Information Exposure Through Error Messages
        # Returning "User does not exist" informs an attacker about valid usernames, which can be used for enumeration attacks.
        return "User does not exist"