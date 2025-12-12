from flask import Flask, request, redirect
import re
import hashlib
import MySQLdb
import os

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
   # Get the username from the form input
   username = request.form['username']
   # Get the password from the form input
   password = request.form['password']
   # Hash the password using SHA-256 for security
   hashed_password = hashlib.sha256(password).hexdigest()
   # Connect to the MySQL database with username 'testuser' and password 'test123'
   db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )
   # Create a cursor object to interact with the database
   cursor = db.cursor()
   # Check if the username already exists in the database
   cursor.execute("SELECT * FROM User WHERE Username = '%s'" % username)
   # If the user is found, redirect back to the register page
   if cursor.fetchone() is not None:
        return redirect('./register')
   else:
        # If the user is not found, insert the new user into the database
        cursor.execute("INSERT INTO User VALUES ('%s', '%s')" % (username, hashed_password))
        # Save the changes to the database
        db.commit()
        # Close the cursor and database connection
        cursor.close()
        db.close()