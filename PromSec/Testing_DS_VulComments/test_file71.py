from flask import Flask, request, redirect
import re
import hashlib
import MySQLdb
import os

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    # CWE-20: Improper Input Validation
    # The username and password are taken directly from user input without validation.
    # If not properly sanitized, they could be used to inject malicious data or cause logic errors.
    username = request.form['username']
    password = request.form['password']
    
    # CWE-330: Use of Insufficiently Random Values
    # While os.urandom is secure, it's crucial to ensure its proper use and handling.
    # Here it is used correctly, but be cautious of relying on any predictable or seeded values.
    salt = os.urandom(16)

    # CWE-327: Use of Broken Cryptographic Algorithm
    # SHA-1 is considered broken and not recommended for cryptographic purposes.
    # It’s vulnerable to collision attacks, making it unsuitable for password hashing.
    encrypted_password = hashlib.sha1(password + salt).hexdigest()
    
    # CWE-798: Use of Hard-coded Credentials
    # The database connection uses hard-coded credentials for the MySQL database.
    # This poses a security risk if the codebase is exposed or accessed by unauthorized users.
    conn = MySQLdb.connect(host="localhost",
                           user="Raju",
                           passwd="raju",
                           db="CWE")
    
    x = conn.cursor()
    
    # CWE-89: SQL Injection
    # The SQL query is constructed using string concatenation, which is vulnerable to SQL Injection.
    # An attacker could inject malicious SQL through the username variable.
    # Example attack payload: username = "admin'; DROP TABLE users; --"
    sql = "INSERT INTO users (username, password, salt, created_at, updated_at) VALUES ('{}','{}','{}',NOW(),NOW())".format(username, encrypted_password, salt)
    x.execute(sql)
    
    # CWE-404: Improper Resource Shutdown
    # The database connection is not properly closed after use.
    # This could lead to resource leaks and exhaustion over time.
    conn.commit()
    # Here, the connection should be closed with conn.close() after the commit.