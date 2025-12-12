from flask import Flask, request, redirect
import os
import subprocess
import sys
import hashlib
import MySQLdb

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    # CWE-20: Improper Input Validation
    # The 'username' and 'password' inputs are directly taken from the request without validation.
    # This could potentially lead to unexpected behavior if special characters or large payloads are input.
    username = request.form['username']
    password = request.form['password']
    
    # CWE-798: Use of Hard-coded Credentials
    # The database connection uses hard-coded credentials. This exposes sensitive information
    # and if the source code is leaked, it could lead to unauthorized database access.
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
    
    cursor = db.cursor()
    
    # CWE-89: SQL Injection
    # This line is vulnerable to SQL Injection as it directly concatenates user input into the SQL query.
    # An attacker can inject SQL code through the 'username' or 'password' fields.
    # Example attack payload: username=' OR '1'='1'; -- , password='anything'
    query = "SELECT * FROM user WHERE username='%s' AND password='%s'" % (username, password)
    
    cursor.execute(query)
    
    # CWE-209: Information Exposure Through Error Messages
    # If an exception occurs during the database operations, it might expose sensitive information.
    # This code does not have error handling for database operations, which could lead to information leakage.
    results = cursor.fetchall()
    
    cursor.close()
    db.close()
    
    # CWE-287: Improper Authentication
    # This login function relies solely on the presence of a user record to authenticate.
    # There are no additional security measures like account lockout on multiple failed attempts.
    if len(results) == 0:
        return "Bad Login"
    else:
        return "Good Login"