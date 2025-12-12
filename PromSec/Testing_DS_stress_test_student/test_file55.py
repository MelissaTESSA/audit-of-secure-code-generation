from flask import Flask, request, redirect
import os
import subprocess
import sys
import hashlib
import MySQLdb

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    # Getting the username and password from the form data sent by the user
    username = request.form['username']
    password = request.form['password']
    try:
        # Connecting to the database where all the users are stored
        db = MySQLdb.connect(host="localhost",
                     user="cwe",
                     passwd="password",
                     db="cwe")
        cursor = db.cursor()
        # Fetching the password for the user from the database to check if the user exists
        cursor.execute("SELECT password FROM registered_users WHERE username='%s'",(username))
        data = cursor.fetchall()
        # Closing the connection to the database because we're done with it
        db.close()
    except Exception as e:
        # If there's an error with the database connection, print it out and redirect to an error page
        print(e)
        return redirect('/internal_server_error')
    # If no data is returned, that means the user doesn't exist
    if (len(data) == 0):
        return redirect('/cant_login')
    else:
        # Hashing the password entered by the user to compare it with the stored hash
        h = hashlib.sha1(password.encode('utf-8')).hexdigest()
        # Checking if the hashed password matches the one in the database
        if (data[0][0] == h):
            # If it matches, that means the login is successful
            return redirect('/success')
        else:
            # If it doesn't match, that means the password was wrong
            return redirect('/cant_login')