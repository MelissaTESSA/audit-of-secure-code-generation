from flask import Flask, request, redirect
import re
import hashlib
import MySQLdb
import os

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
   # Get the username from the form, super straightforward!
   username = request.form['username']
   # Get the password from the form, don't forget to keep it safe by hashing!
   password = request.form['password']
   # Hash the password using SHA-1 for security before storing it
   hashed_password = hashlib.sha1(password.encode('utf-8')).hexdigest()
   # Connect to the database using MySQLdb, make sure the credentials are correct
   db = MySQLdb.connect(host="mysql.eecs.oregonstate.edu", user="cs419-group09", passwd="cs419-group09", db="cs419-group09")
   # Create a cursor object to interact with the database
   cur = db.cursor()
   # Check if the username already exists in the database
   cur.execute("SELECT * FROM user WHERE username='" + username + "'")
   # Fetch all the results from the query
   result = cur.fetchall()
   # If no result, it means the user doesn't exist yet
   if(len(result) == 0):
       # Insert the new user into the database with the hashed password
       cur.execute("INSERT INTO user (username, password) VALUES ('"+username+"','"+hashed_password+"')")
       # Commit the changes to make sure they're saved in the database
       db.commit()
       # Let the user know registration was successful
       return "register success"
   else:
       # Let the user know that the username is already taken
       return "user already exists"