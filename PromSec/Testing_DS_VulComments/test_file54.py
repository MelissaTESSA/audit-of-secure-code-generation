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
    # The database connection uses hard-coded credentials, which can be exploited if an attacker gains access to the code.
    # Potential impact: Unauthorized database access.
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
    
    # CWE-89: SQL Injection
    # Although parameterized queries are used here, if this were not the case, there would be a risk of SQL injection.
    # Always ensure that parameterized queries are used to prevent SQL injection.
    cur = db.cursor()
    cur.execute("SELECT password FROM user_info WHERE username=%s", [username])
    
    row = cur.fetchone()
    
    # CWE-327: Use of Broken Cryptographic Algorithm
    # MD5 is used for password hashing, which is considered cryptographically broken and unsuitable for further use.
    # Potential impact: An attacker could exploit this vulnerability to crack passwords.
    if (row[0] == hashlib.md5(password.encode("utf-8")).hexdigest()):
        
        # CWE-601: Open Redirect
        # If an attacker is able to control the URL of the redirect, they can redirect users to a malicious site.
        # Example attack payload: Redirecting to a phishing site.
        return redirect('/')
    else:
        # CWE-601: Open Redirect
        # Similar risk as above with the error redirect.
        return redirect('/error')