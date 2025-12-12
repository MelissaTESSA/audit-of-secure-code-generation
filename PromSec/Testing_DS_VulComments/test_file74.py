from flask import Flask, request, redirect
import re
import hashlib
import MySQLdb
import os
import bcrypt

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
   # CWE-20: Improper Input Validation
   # The input from 'request.form['username']' is not validated. This could lead to various injection attacks.
   username = request.form['username']
   
   # CWE-20: Improper Input Validation
   # The input from 'request.form['password']' is not validated. This could lead to weak password choices or other issues.
   password = request.form['password']
   
   # Properly hashing the password using bcrypt, which is a secure hashing algorithm.
   pw_hash = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
   
   # CWE-20: Improper Input Validation
   # The input from 'request.form['confirm_password']' is not validated. This could lead to inconsistencies or other issues.
   confirm_password = request.form['confirm_password']
   
   # CWE-798: Use of Hard-coded Credentials
   # The database connection uses a hard-coded password. If an attacker gains access to this code, they can use these credentials to access the database.
   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "cwe_900")
   
   cur = cnx.cursor()
   
   # CWE-89: SQL Injection
   # The query uses string concatenation with user input 'username'. An attacker can exploit this to execute arbitrary SQL code.
   # Example payload: "' OR '1'='1"
   cur.execute("SELECT * from users where username='" + username + "'")
   
   row = cur.fetchall()
   if not row:
      try:
         # Using parameterized queries here, which is good practice and prevents SQL injection for the INSERT operation.
         cur.execute("INSERT INTO users(username, pw_hash) VALUES(%s, %s)", (username, pw_hash))
         cnx.commit()
         
         # CWE-209: Information Exposure Through Error Messages
         # Returning a generic message here, but ensure no sensitive information is leaked through other error messages.
         message = "You have successfully registered"
         cur.close()
         cnx.close()
         return message
      except:
         # If an exception occurs, the rollback is performed, but the exact error is not logged. 
         # Consider logging errors securely for debugging purposes.
         cnx.rollback()
         
         # CWE-209: Information Exposure Through Error Messages
         # Returning a generic failure message, which is good practice, but ensure no internal error details are exposed.
         message = "Registration Failed"
         cur.close()
         cnx.close()
         return message
   else:
      # CWE-209: Information Exposure Through Error Messages
      # The message reveals that the username already exists, which could be used by an attacker for user enumeration.
      message = "Username already exists"
      cur.close()
      cnx.close()
      return message