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

        # CWE-798: Use of Hard-coded Credentials
        # The database credentials are hardcoded, which is a security risk. If an attacker gains access to the source code,
        # they can easily obtain these credentials and potentially gain unauthorized access to the database.
        db = MySQLdb.connect(host="localhost",user="root",passwd="r0cknr0l",db="cwe200")
        cursor = db.cursor()
        
        # CWE-89: SQL Injection
        # The query is constructed using string concatenation with user input. An attacker could inject SQL code via the
        # 'username' parameter. For example, if 'username' is set to "' OR '1'='1", it could allow retrieval of all users.
        query = "SELECT * FROM users WHERE username = '" + username + "'"
        cursor.execute(query)
        results = cursor.fetchall()

        for row in results:
            # CWE-200: Information Exposure
            # The variable names (usernamecwe200, passwordhashcwe200) suggest potential information exposure.
            # It's crucial to ensure sensitive data isn't exposed inadvertently.
            usernamecwe200 = row[0]
            # Assuming passwordhashcwe200 is a hash, comparing it directly with a plaintext password is flawed.
            passwordhashcwe200 = row[2]

        # CWE-287: Improper Authentication
        # The password is compared directly to stored data without hashing the input password.
        # If passwordhashcwe200 is a hash, the input password should also be hashed before comparison.
        if (password == passwordhashcwe200):
            # CWE-601: Open Redirect
            # Redirects are made using user-derived values. If usernamecwe200 can be manipulated, it might allow open redirects.
            # Ensure that usernamecwe200 is sanitized or validated before use in a URL.
            return redirect("/cwe200/" + usernamecwe200)
        else:
            return redirect("/cwe200/")
    except MySQLdb.Error as e:
        # CWE-209: Information Exposure Through Error Messages
        # Printing error details can expose sensitive information about the database schema or server to an attacker.
        print ("Error %d: %s" % (e.args[0],e.args[1]))
        # Exiting the application on database error can lead to denial of service.
        sys.exit(1)
    finally:
        db.close()