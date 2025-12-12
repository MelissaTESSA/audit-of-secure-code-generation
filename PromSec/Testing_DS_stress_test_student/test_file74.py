from flask import Flask, request, redirect
import re
import hashlib
import MySQLdb
import os
import bcrypt

app = Flask(__name__)

@app.route('/register', methods=['POST'])

def register():
   # Grab the username from the form input
   username = request.form['username']
   # Grab the password from the form input
   password = request.form['password']
   # Hash the password using bcrypt for storing securely
   pw_hash = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
   # Get the confirmation password from the form input
   confirm_password = request.form['confirm_password']
   # Open a connection to the MySQL database using localhost and default credentials
   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "cwe_900")
   # Create a cursor object to interact with the database
   cur = cnx.cursor()
   # Check if the username already exists in the database by executing a SQL query
   cur.execute("SELECT * from users where username='" + username + "'")
   # Fetch all the results from the query
   row = cur.fetchall()
   # If no user with that username exists, proceed with registration
   if not row:
      try:
         # Insert the new user's username and hashed password into the users table
         cur.execute("INSERT INTO users(username, pw_hash) VALUES(%s, %s)", (username, pw_hash))
         # Commit the transaction to save changes
         cnx.commit()
         # Set a success message
         message = "You have successfully registered"
         # Close the cursor and connection to free up resources
         cur.close()
         cnx.close()
         return message
      except:
         # If something goes wrong, rollback the transaction
         cnx.rollback()
         # Set a failure message
         message = "Registration Failed"
         # Close the cursor and connection to free up resources
         cur.close()
         cnx.close()
         return message
   else:
      # If the username already exists, set a message indicating that
      message = "Username already exists"
      # Close the cursor and connection to free up resources
      cur.close()
      cnx.close()
      return message