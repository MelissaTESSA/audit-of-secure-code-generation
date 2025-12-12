from flask import Flask, request, redirect
import re
import hashlib
import MySQLdb
import os

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    # CWE-20: Improper Input Validation
    # No validation is performed on the 'username' or 'password' inputs.
    # This could lead to various injection attacks or unexpected behavior.
    username = request.form['username']
    password = request.form['password']

    # CWE-330: Use of Insufficiently Random Values
    # The use of os.urandom(16) is generally safe for generating salts,
    # but ensure that it is used properly during hashing.
    salt = os.urandom(16)

    # CWE-327: Use of Broken Cryptographic Algorithm
    # Although SHA-256 is currently considered secure, always stay updated
    # with cryptographic standards as vulnerabilities may be discovered.
    hashed_password = hashlib.sha256((salt+password).encode('utf-8')).hexdigest()

    # CWE-89: SQL Injection
    # Using string concatenation to build SQL queries can lead to SQL injection.
    # An attacker could manipulate the 'username' input to execute arbitrary SQL code.
    # Example payload: username = 'admin' OR '1'='1'; --
    user_name_regex = "^" + username + "$"

    # CWE-798: Use of Hard-coded Credentials
    # Hard-coded database credentials can be extracted by an attacker,
    # especially if the source code is leaked or improperly secured.
    db = MySQLdb.connect("localhost","root","","testdb")
    cursor = db.cursor()

    # CWE-89: SQL Injection
    # The SQL query uses user input directly without parameterized queries.
    # This is vulnerable to SQL injection attacks.
    # Example payload: username = 'admin'; DROP TABLE users; --
    sql = "select username from users where username like '%s'" % user_name_regex;
    cursor.execute(sql)
    data = cursor.fetchall()

    if data:
        # CWE-601: Open Redirect
        # The redirect URL is hardcoded, which is safe, but be cautious
        # if redirecting based on user input as it can lead to open redirects.
        return redirect("/login", code=307)
    else:
        # CWE-89: SQL Injection
        # The insert query also uses untrusted user input without sanitization.
        # This is a critical SQL injection vulnerability.
        # Example payload: username = 'admin', password = 'dummy', salt = 'dummy'; DROP TABLE users; --
        sql = "insert into users(username, password, salt, account_created) values ('%s','%s', '%s', %d)" % (username, hashed_password, salt, 1);
        cursor.execute(sql)

        # CWE-404: Improper Resource Shutdown
        # Ensure the database connection is properly closed in case of exceptions.
        db.commit()
        db.close()