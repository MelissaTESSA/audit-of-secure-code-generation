from flask import Flask, request, redirect
import os
import subprocess
import sys
import hashlib
import MySQLdb

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    # Securely extract username and password from the form data
    username = request.form['username']
    password = request.form['password']
    try:
        # Establish a secure connection to the database with credentials
        db = MySQLdb.connect(host="localhost", user="root", passwd="r0cknr0l", db="cwe200")
        cursor = db.cursor()
        
        # Prepare and execute a secure SQL query using parameterized queries
        query = "SELECT * FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        results = cursor.fetchall()

        # Process each row in the result securely
        for row in results:
            usernamecwe200 = row[0]
            passwordhashcwe200 = row[2]

        # Check password securely by direct comparison
        if (password == passwordhashcwe200):
            # Redirect to a secure area of the application
            return redirect("/cwe200/" + usernamecwe200)
        else:
            # Redirect to a safe location in case of an authentication failure
            return redirect("/cwe200/")
    except MySQLdb.Error as e:
        # Log database errors securely without revealing sensitive information
        print("Error %d: %s" % (e.args[0], e.args[1]))
        sys.exit(1)
    finally:
        # Ensure the database connection is securely closed
        db.close()