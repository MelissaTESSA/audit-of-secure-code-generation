from flask import Flask, request, redirect
import re
import hashlib
import MySQLdb
import os

app = Flask(__name__)

@app.route('/register', methods=['POST'])

def register():
   # Get the username and password that the user entered in the form
   username = request.form['username']
   password = request.form['password']
   
   # Encrypt the password using MD5 so it's not stored as plain text
   password = hashlib.md5(password).hexdigest()
   
   # Connect to the database using the given credentials
   # Make sure to use the correct host, user, password, and database name
   db = MySQLdb.connect(host="69.195.55.111", user= "ec2-user", passwd="ufo12345", db="CWE")
   
   # Create a cursor object to interact with the database
   cur = db.cursor()
   
   # Craft the SQL query to insert the new user's data into the User table
   # Use %s to insert the username, password, and email into the query
   query ="INSERT INTO User (Username, Password, Email) VALUES ('%s', '%s', '%s')" % (username, password, username)
   
   # Execute the query to add the new user to the database
   cur.execute(query)
   
   # Save the changes to the database
   db.commit()
   
   # Close the database connection to free up resources
   db.close()

   # Redirect the user to the homepage after successful registration
   return redirect('/')