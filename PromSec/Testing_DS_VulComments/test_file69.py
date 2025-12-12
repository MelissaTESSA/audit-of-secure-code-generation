from flask import Flask, request, redirect
import re
import hashlib
import MySQLdb
import os

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
   username = request.form['username']
   password = request.form['password']
   salt = os.urandom(16)

def register():
   username = request.form['username']
   password = request.form['password']
   salt = os.urandom(16)
   
   # CWE-327: Use of Broken Cryptographic Algorithm
   # SHA-256 is generally considered secure, but ensure it's used properly across the system.
   hashed_password = hashlib.sha256((salt+password).encode('utf-8')).hexdigest()
   
   # CWE-20: Improper Input Validation
   # No validation or sanitization of `username` input before using it in a regex.
   # An attacker could input special regex characters to cause regex injection.
   user_name_regex = "^" + username + "$"
   
   db = MySQLdb.connect("localhost","root","","testdb")
   cursor = db.cursor()
   
   # CWE-89: SQL Injection
   # Directly using user input in SQL queries without parameterization.
   # An attacker could inject SQL code through `username`.
   # Example payload: `username = "admin' --"`
   sql = "select username from users where username like '%s'" % user_name_regex;
   cursor.execute(sql)
   data = cursor.fetchall()
   if data:
      # CWE-601: Open Redirect
      # Redirecting to a fixed path, not directly vulnerable here, but ensure no user-controlled input is used in redirects.
      return redirect("/login", code=307)
   else:
      # CWE-89: SQL Injection
      # Again, SQL Injection vulnerability due to direct inclusion of user input in SQL query.
      # Example payload: `username = "admin', 'password', 'salt', 1); DROP TABLE users; --"`
      sql = "insert into users(username, password, salt, account_created) values ('%s','%s', '%s', %d)" % (username, hashed_password, salt, 1);
      cursor.execute(sql)
      
      # CWE-404: Improper Resource Shutdown
      # Ensure proper exception handling around database operations to prevent resource leaks.
      db.commit()
      db.close()