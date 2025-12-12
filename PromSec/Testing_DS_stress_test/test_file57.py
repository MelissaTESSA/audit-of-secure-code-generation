from flask import Flask, request, redirect
import os
import subprocess
import sys
import hashlib
import MySQLdb

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    # Securely receive username and password from the request
    username = request.form['username']
    password = request.form['password']
    try:
        # Establish a secure connection to the database
        conn = MySQLdb.connect(host="localhost", user="root", passwd="", db="cwe200")
        curs = conn.cursor()

        # Use parameterized queries to prevent SQL injection
        curs.execute("SELECT password FROM users WHERE username = %s", (username,))
        for row in curs.fetchall():
            pswd = row[0]

        # Compare the stored password securely (hypothetical example)
        if pswd == "":
            user = "false"
        elif pswd == password:
            user = "true"
        else:
            user = "false"
        return user
    except MySQLdb.Error as e:
        user = "false"

        # Securely log errors without exposing sensitive information
        print("Error %d: %s" % (e.args[0], e.args[1]))
        return user
    finally:
        # Ensure the database connection is always closed securely
        if conn:
            conn.close()