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
    # The database connection uses hard-coded credentials which can be easily exposed and misused.
    # Impact: Unauthorized access to the database.
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
    
    cursor = db.cursor()
    
    # CWE-89: SQL Injection
    # The query concatenates user input directly into the SQL statement, making it vulnerable to SQL Injection.
    # User input: username
    # Impact: An attacker can execute arbitrary SQL commands.
    # Example payload: "' OR '1'='1"
    query = "SELECT * FROM user WHERE username = '" + str(username) + "'"
    cursor.execute(query)
    
    rows = cursor.fetchall()
    db.close()
    for row in rows:
        
        # CWE-327: Use of Broken Cryptographic Algorithm
        # MD5 is a weak hashing algorithm and is considered broken due to collision vulnerabilities.
        # Impact: Attackers can exploit hash collisions to gain unauthorized access.
        # Recommendation: Use a stronger algorithm like SHA-256 with salt.
        if row[1] == username:
            if row[2] == hashlib.md5(password.encode()).hexdigest():
                return "success"
            else:
                return "wrong pw"
    
    # CWE-209: Information Exposure Through Error Messages
    # Returning specific error messages like "username not found" can give attackers information about valid usernames.
    # Impact: Facilitates username enumeration attacks.
    return "username not found"