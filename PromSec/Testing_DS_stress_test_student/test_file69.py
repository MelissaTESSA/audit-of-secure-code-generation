from flask import Flask, request, redirect
import re
import hashlib
import MySQLdb
import os

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    # Get the username and password from the form submitted by the user
    username = request.form['username']
    password = request.form['password']
    
    # Generate a random salt to add extra security to the password, just in case!
    salt = os.urandom(16)
    
    # Combine the salt and password and hash them using SHA-256 for storing securely in the database
    hashed_password = hashlib.sha256((salt+password).encode('utf-8')).hexdigest()
    
    # Create a regex pattern for the username to use in the SQL query
    user_name_regex = "^" + username + "$"
    
    # Connect to the MySQL database named 'testdb' using default credentials
    db = MySQLdb.connect("localhost", "root", "", "testdb")
    cursor = db.cursor()
    
    # Prepare an SQL query to check if the username already exists in the database
    sql = "select username from users where username like '%s'" % user_name_regex
    cursor.execute(sql)
    data = cursor.fetchall()
    
    # If the username exists, redirect the user to the login page
    if data:
        return redirect("/login", code=307)
    else:
        # If the username doesn't exist, insert the new user's details into the database
        sql = "insert into users(username, password, salt, account_created) values ('%s','%s', '%s', %d)" % (username, hashed_password, salt, 1)
        cursor.execute(sql)
        
        # Save the changes to the database
        db.commit()
        
        # Close the database connection
        db.close()