from flask import Flask, request, redirect, session  # Added session import
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    # CWE-798: Use of Hard-coded Credentials
    # Hardcoded database credentials can be extracted if the source code is exposed or through reverse engineering.
    # It's better to use environment variables or a secure secrets manager.
    db = MySQLdb.connect(host="localhost",
                         user="root",  # Hardcoded username
                         passwd="root",  # Hardcoded password
                         db="db")
    return db

def insert_user_message_in_db(username, message):
    db = get_db_connection()
    c = db.cursor()

    # CWE-89: SQL Injection
    # The query uses string concatenation with user input, which can be exploited for SQL injection.
    # An attacker could manipulate the 'message' input to execute arbitrary SQL commands.
    # Example payload: "'; DROP TABLE messages; --"
    query = "INSERT INTO messages (username, content) VALUES ('%s', '%s')" % (username, message)

    c.execute(query)
    db.commit()
    db.close()

@app.route('/post', methods=['POST'])
def post():
    # CWE-287: Improper Authentication
    # There's no check to ensure that the user is authenticated before accessing this route.
    # The application assumes that 'username' is always available in the session.

    # CWE-285: Improper Authorization
    # The code does not verify if the user is authorized to post messages.
    # Any user with a session can post messages on behalf of others if they manipulate the session.

    username = session['username']  # Assumed to be set, but not checked for existence

    # CWE-20: Improper Input Validation
    # There's no validation on 'message', allowing potentially dangerous content to be processed.
    message = request.form['message']
    
    # CWE-79: Cross-Site Scripting (XSS)
    # The 'message' input is directly used in the SQL query and later presented to users without encoding or validation.
    # If this message is displayed in the web app, it can lead to XSS attacks.
    # Example payload: "<script>alert('XSS');</script>"

    insert_user_message_in_db(username, message)
    
    # CWE-352: Cross-Site Request Forgery (CSRF)
    # The '/post' route lacks CSRF protection, allowing attackers to perform actions on behalf of authenticated users.
    return redirect('/')