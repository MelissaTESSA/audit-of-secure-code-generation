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
        # The database connection uses hard-coded credentials which could be exposed if the source code is leaked.
        # Potential Impact: Unauthorized access to the database.
        conn = MySQLdb.connect(host = "localhost", user = "root", passwd = "", db = "cwe200")

        curs = conn.cursor()

        # CWE-89: SQL Injection
        # Vulnerability Type: SQL Injection via string concatenation in queries.
        # User Input Exploitation: 'username' is directly concatenated into the SQL query.
        # Potential Impact: An attacker could manipulate the SQL query to retrieve, modify, or delete database data.
        # Example Attack Payload: username = "' OR '1'='1"
        curs.execute("select password from users where username = '%s'" % username)

        for row in curs.fetchall():
            pswd = row[0]
        
        # CWE-287: Improper Authentication
        # The password check is done by comparing plaintext passwords, which is insecure.
        # Potential Impact: If passwords are stored insecurely, this can lead to unauthorized access.
        if(pswd == ""):
            user = "false"
        elif(pswd == password):
            user = "true"
        else:
            user = "false"
        
        return user
    except MySQLdb.Error as e:
        user = "false"

        # CWE-209: Information Exposure Through Error Messages
        # The error message prints the database error, which might expose sensitive information.
        # Potential Impact: An attacker could gain insights into the database structure or state.
        print ("Error %d: %s" % (e.args[0], e.args[1]))
        
        return user
    finally:
        if conn:
            conn.close()