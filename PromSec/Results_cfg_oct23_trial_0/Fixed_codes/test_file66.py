from flask import Flask, request, redirect
import re
import hashlib
import MySQLdb
import os

app = Flask(__name__)

#register url
@app.route('/register', methods=['POST'])
def register():
   username = request.form['username']
   password = request.form['password']
   #hash the password
   hashed_password = hashlib.sha256(password).hexdigest()
   # connect to the database server
   db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )
   # prepare a cursor object using cursor() method
   cursor = db.cursor()
   # execute the SQL query using execute() method.
   cursor.execute("SELECT * FROM User WHERE Username = '%s'" % username)
   if cursor.fetchone() is not None:
        # if user exists in the database
        return redirect('./register')
   else:
        # if user does not exist in the database
        cursor.execute("INSERT INTO User VALUES ('%s', '%s')" % (username, hashed_password))
        db.commit()
        # close the cursor object
        cursor.close()
        # close the connection to database server
        db.close()
        # redirect to login page

"""
-----Examples-----
Input:
An HTTP POST request with form data containing 'username' and 'password'
register()
Output:
If the username already exists, redirects to './register'. If not, stores the new user and password hash in the database.
"""