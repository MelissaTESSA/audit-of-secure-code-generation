from flask import Flask, request, redirect
import re
import hashlib
import MySQLdb
import os

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
   # Get the username from the form that the user submits
   username = request.form['username']
   # Get the password from the form that the user submits
   password = request.form['password']
   # Create a random salt to make the password more secure
   salt = os.urandom(16)

def register():
   # Same as above, get the username and password from the form
   username = request.form['username']
   password = request.form['password']
   # Generate a random salt to add extra security to the password
   salt = os.urandom(16)
   # Encrypt the password with the salt, using SHA-1 for security
   encrypted_password = hashlib.sha1(password + salt).hexdigest()
   # Connect to the MySQL database using the credentials
   conn = MySQLdb.connect(host= "localhost",
                           user="Raju",
                           passwd="raju",
                           db="CWE")
   # Create a cursor object to execute SQL queries
   x = conn.cursor()
   # Insert the new user's data into the users table
   sql = "INSERT INTO users (username, password, salt, created_at, updated_at) VALUES ( '{}','{}','{}',NOW(),NOW())".format(username, encrypted_password, salt)
   # Execute the SQL query to save the user information
   x.execute(sql)
   # Commit the transaction to make sure the data is saved in the database
   conn.commit()