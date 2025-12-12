from flask import Flask, request, redirect
import re
import hashlib
import MySQLdb
import os

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
   # Get the username and password from the form submission
   username = request.form['username']
   password = request.form['password']
   
   # Create a random salt for password hashing to make it more secure
   salt = os.urandom(16)
   
   # Combine the salt and password, then hash them using SHA-256
   hashed_password = hashlib.sha256((salt+password).encode('utf-8')).hexdigest()
   
   # Create a regular expression for the username
   user_name_regex = "^" + username + "$"
   
   # Connect to the local MySQL database with default credentials
   db = MySQLdb.connect("localhost","root","","testdb")
   cursor = db.cursor()
   
   # Check if the username already exists in the database
   sql = "select username from users where username like '%s'" % user_name_regex;
   cursor.execute(sql)
   data = cursor.fetchall()
   
   if data:
      # If the username exists, redirect the user to the login page
      return redirect("/login", code=307)
   else:
      # If the username doesn't exist, insert the new user into the database
      sql = "insert into users(username, password, salt, account_created) values ('%s','%s', '%s', %d)" % (username, hashed_password, salt, 1);
      cursor.execute(sql)
      db.commit()
      db.close()