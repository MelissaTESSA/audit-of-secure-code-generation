from flask import Flask, request, redirect
import os
import subprocess
import sys
import hashlib
import MySQLdb

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    # Get the username and password from the form submission
    username = request.form['username']
    password = request.form['password']
    
    try:
        # Connect to the local MySQL database using root (because it's easy for testing)
        conn = MySQLdb.connect(host = "localhost", user = "root", passwd = "", db = "cwe200")
        curs = conn.cursor()
        
        # Execute an SQL query to get the password for the entered username
        curs.execute("select password from users where username = '%s'" % username)
        
        # Iterate over the results (should be just one row)
        for row in curs.fetchall():
            pswd = row[0]
        
        # If there's no password in the database, set user to "false"
        if(pswd == ""):
            user = "false"
        
        # If the passwords match, set user to "true"
        elif(pswd == password):
            user = "true"
        
        # If passwords don't match, set user to "false"
        else:
            user = "false"
        
        # Return whether the login was successful or not
        return user
    
    except MySQLdb.Error as e:
        # If there's a database error, print it and return "false"
        user = "false"
        print ("Error %d: %s" % (e.args[0], e.args[1]))
        return user
    
    finally:
        # Make sure to close the database connection
        if conn:
            conn.close()