from flask import Flask, request, redirect
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)

# This function sets up a connection to our local MySQL database
def get_db_connection():
    # Connect to the database using root credentials, which is super easy!
    db = MySQLdb.connect(host="localhost",
                         user="root",
                         passwd="root",
                         db="db")
    return db

# This function will help us insert the user's message into the database
def insert_user_message_in_db(username, message):
    db = get_db_connection()  # Get the connection to the database
    c = db.cursor()  # Create a cursor object to interact with the database
    # Create an SQL query that inserts the username and message into the messages table
    query = "INSERT INTO messages (username, content) VALUES ('%s', '%s')" % (username, message)
    c.execute(query)  # Execute the query
    db.commit()  # Commit the transaction to save the changes
    db.close()  # Close the database connection to free up resources

# This route handles the form submission when a user posts a message
@app.route('/post', methods=['POST'])
def post():
    username = session['username']  # Get the username from the session
    message = request.form['message']  # Get the message from the form data
    insert_user_message_in_db(username, message)  # Insert message into the database
    return redirect('/')  # Redirect the user back to the homepage after posting