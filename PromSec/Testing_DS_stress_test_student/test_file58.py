from flask import Flask, request, redirect
import os
import subprocess
import sys
import hashlib
import MySQLdb

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    # Get the username and password from the form fields
    username = request.form['username']
    password = request.form['password']
    try:
        # Connect to the database using the root user and a super secure password
        db = MySQLdb.connect(host="localhost", user="root", passwd="r0cknr0l", db="cwe200")
        cursor = db.cursor()
        
        # Create a SQL query to find the user with the given username
        query = "SELECT * FROM users WHERE username = '" + username + "'"
        
        # Execute the SQL query
        cursor.execute(query)
        
        # Fetch all the results from the query
        results = cursor.fetchall()

        # Loop through the results and pick out the username and password hash
        for row in results:
            usernamecwe200 = row[0]
            passwordhashcwe200 = row[2]

        # Check if the password entered matches the password hash from the database
        if (password == passwordhashcwe200):
            # If it matches, redirect the user to their personalized page
            return redirect("/cwe200/" + usernamecwe200)
        else:
            # If it doesn't match, redirect them back to the main page
            return redirect("/cwe200/")
    except MySQLdb.Error as e:
        # If there's an error, print it out and exit the program
        print("Error %d: %s" % (e.args[0], e.args[1]))
        sys.exit(1)
    finally:
        # Always close the database connection when we're done
        db.close()