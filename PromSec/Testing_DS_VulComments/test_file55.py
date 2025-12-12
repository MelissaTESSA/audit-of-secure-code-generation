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

        db = MySQLdb.connect(host="localhost",
                     user="cwe",
                     passwd="password",
                     db="cwe")
        cursor = db.cursor()
        
        # Vulnerability: CWE-89: SQL Injection (string concatenation in queries, no parameterized queries)
        # Description: The SQL query uses string interpolation with the username variable directly. 
        #              This can be exploited if username contains malicious SQL code.
        # User Input: Malicious SQL code via username.
        # Potential Impact: Unauthorized data access or manipulation.
        # Example Attack Payload: username = "' OR '1'='1"
        cursor.execute("SELECT password FROM registered_users WHERE username='%s'",(username))
        
        data = cursor.fetchall()
        db.close()
    except Exception as e:
        # Vulnerability: CWE-209: Information Exposure Through Error Messages
        # Description: Printing exception details exposes potentially sensitive information about the application's internal state.
        # User Input: Any input causing an exception.
        # Potential Impact: Information disclosure to potential attackers.
        print(e)
        return redirect('/internal_server_error')
    
    if (len(data) == 0):
        return redirect('/cant_login')
    else:
        # Vulnerability: CWE-327: Use of Broken Cryptographic Algorithm
        # Description: SHA1 is a deprecated hashing algorithm due to vulnerabilities that can lead to collisions.
        # User Input: Password input by the user.
        # Potential Impact: Increased risk of hash collisions and reduced security of stored passwords.
        h = hashlib.sha1(password.encode('utf-8')).hexdigest()
        
        if (data[0][0] == h):
            return redirect('/success')
        else:
            return redirect('/cant_login')