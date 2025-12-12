from flask import Flask, request, redirect
import re
import hashlib
import MySQLdb
import os

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
   # Get the username from the form data
   username = request.form['username']
   # Get the password from the form data
   password = request.form['password']
   # Generate a random salt for the password
   salt = os.urandom(16)

def register():
   # Again, grabbing the username from the form
   username = request.form['username']
   # And the password too
   password = request.form['password']
   # Create a random salt to make the password extra secure
   salt = os.urandom(16)
   # Set up a SHA256 hash object to do the hashing
   m = hashlib.sha256()
   # Update the hash object with the password and salt
   m.update(password.encode('utf-8') + salt)
   # Get the final hashed password and add the salt to it
   password = m.digest() + salt
   # Print the password to see what it looks like now
   print(password)
   try:
      # Connect to the local MySQL database with root user
      db = MySQLdb.connect("localhost","root","cisco123","mysite")
      # Create a cursor object using the cursor() method
      cursor = db.cursor()
      # Make an SQL query to insert the username and password into the user table
      sql = "insert into user (username,password) values ('"+username+"','"+password+"')"
      # Print the SQL command to check it
      print(sql)
      # Execute the SQL command
      cursor.execute(sql)
      # Commit changes in the database
      cursor.execute("commit")
      # Redirect to the home page upon successful registration
      return redirect('/home')
   except:
      # If something goes wrong, just redirect to the home page anyway
      return redirect('/home')