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
    # The database connection uses hard-coded credentials ("root", "root").
    # These should be stored securely, for example, in environment variables or a secure secrets manager.
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
    
    c = db.cursor()
    
    # CWE-89: SQL Injection
    # The SQL query is constructed using string concatenation with user input (`username` and `password`).
    # An attacker can inject SQL code through the `username` or `password` fields.
    # Example payload: username = "' OR '1'='1"; password = "irrelevant"
    c.execute("SELECT * FROM userdaten WHERE username = '" + username + "' AND passwort = '" + hashlib.md5(password).hexdigest() + "'")
    
    # CWE-327: Use of Broken Cryptographic Algorithm
    # MD5 is used for hashing passwords, which is considered broken and insecure.
    # An attacker can exploit this weakness by using precomputed hash tables (rainbow tables).
    # It's recommended to use a stronger hash function like bcrypt or Argon2.
    
    # CWE-209: Information Exposure Through Error Messages
    # If an exception occurs during the database query, sensitive information such as stack traces or query details may be exposed.
    # This could aid an attacker in crafting more effective SQL injection payloads.
    
    if c.fetchone():
        return "Eingeloggt"
    else:
        return "Falscher Benutzername oder Passwort"
    
    # CWE-311: Missing Encryption of Sensitive Data
    # The password is transmitted in plaintext from the client to the server.
    # Ensure that the application is served over HTTPS to protect sensitive data in transit.