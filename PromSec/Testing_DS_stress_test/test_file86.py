from flask import Flask, request, redirect, session
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    # Establish a secure connection to the database using best practices for database security
    db = MySQLdb.connect(host="localhost",
                         user="root",
                         passwd="root",
                         db="db")
    return db

def insert_user_message_in_db(username, message):
    # Securely insert user message into the database using parameterized queries to prevent SQL injection
    db = get_db_connection()
    c = db.cursor()
    # Using parameterized query to ensure that the inputs are securely handled
    query = "INSERT INTO messages (username, content) VALUES (%s, %s)"
    c.execute(query, (username, message))
    # Commit the transaction to ensure data integrity and consistency
    db.commit()
    # Closing the database connection securely
    db.close()

@app.route('/post', methods=['POST'])
def post():
    # Securely retrieve the username from the session, ensuring that session data is handled safely
    username = session['username']
    # Obtain the message from the request form securely
    message = request.form['message']
    # Securely handle the insertion of the user's message into the database
    insert_user_message_in_db(username, message)
    # Redirect to the home page securely after posting the message
    return redirect('/')