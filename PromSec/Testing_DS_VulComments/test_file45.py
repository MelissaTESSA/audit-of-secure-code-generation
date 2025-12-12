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
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
    cursor = db.cursor()
    
    # CWE-89: SQL Injection
    # Vulnerability Type: SQL Injection through string concatenation
    # User Input: 'username' and 'password'
    # Potential Impact: An attacker could manipulate the SQL query to execute arbitrary SQL code.
    # Example Attack Payload: username = "admin'--" and password = ""
    sql = "SELECT * FROM users WHERE username = '%s' AND password = '%s'" % (username, password)
    
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            id = row[0]
            
        # CWE-287: Improper Authentication
        # Vulnerability Type: Weak authentication logic without proper checks
        # User Input: 'username' and 'password'
        # Potential Impact: An attacker could gain unauthorized access if they bypass authentication logic.
        
        session['id'] = id
        session['Role'] = row[1]
        
        # CWE-285: Improper Authorization
        # Vulnerability Type: Role-based access control not properly enforced
        # User Input: None directly, but session manipulation is possible
        # Potential Impact: An attacker could escalate privileges by manipulating session data.
        
        return redirect('/dashboard')
    except:
        # CWE-209: Information Exposure Through Error Messages
        # Vulnerability Type: Catching broad exceptions without logging
        # User Input: Any input causing an exception
        # Potential Impact: Lack of information for debugging and potential silent failures.
        
        return redirect('/login')

# Notes:
# - The code lacks proper input validation (CWE-20) and parameterized queries which would prevent SQL Injection (CWE-89).
# - The use of hard-coded credentials for database connection (CWE-798) is insecure.
# - No CSRF protection is in place (CWE-352), making it vulnerable to Cross-Site Request Forgery.
# - The application does not use HTTPS, potentially exposing sensitive data in transit (CWE-319).