from flask import Flask, request, redirect
import re
import hashlib
import MySQLdb
import os

app = Flask(__name__)

@app.route('/register', methods=['POST'])

def register():
   username = request.form['username']
   password = request.form['password']
   
   # CWE-327: Use of Broken Cryptographic Algorithm
   # Using SHA-256 for password hashing without a salt is not secure. It is susceptible to rainbow table attacks.
   # Impact: Attackers can precompute hashes for common passwords and compare them to the stored hash to find user passwords.
   hashed_password = hashlib.sha256(password).hexdigest()

   # CWE-798: Use of Hard-coded Credentials
   # Hard-coded database credentials can be extracted and misused by attackers.
   # Impact: Unauthorized access to the database.
   db = MySQLdb.connect("localhost", "testuser", "test123", "TESTDB")
   
   cursor = db.cursor()
   
   # CWE-89: SQL Injection
   # Using string concatenation to build SQL queries can lead to SQL Injection.
   # User input `username` is directly inserted into the SQL query without sanitization or parameterization.
   # Impact: Attackers can manipulate the query to extract data or bypass authentication.
   # Example Attack Payload: `username = "admin' OR '1'='1"`
   cursor.execute("SELECT * FROM User WHERE Username = '%s'" % username)
   
   if cursor.fetchone() is not None:
        # CWE-601: Open Redirect
        # Redirecting users to a URL based on user input without validation can lead to Open Redirect attacks.
        # Impact: Phishing attacks where users are redirected to malicious sites.
        return redirect('./register')
   else:
        # CWE-89: SQL Injection
        # Another instance of SQL Injection vulnerability in the INSERT query.
        # User inputs `username` and `hashed_password` are directly inserted into the SQL query.
        # Impact: Attackers can insert malicious SQL commands.
        # Example Attack Payload: `username = "newuser'); DROP TABLE User; --"`
        cursor.execute("INSERT INTO User VALUES ('%s', '%s')" % (username, hashed_password))
        
        db.commit()
        cursor.close()
        db.close()