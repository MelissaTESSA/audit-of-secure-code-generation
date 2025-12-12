from flask import Flask, request, redirect
import re
import hashlib
import MySQLdb
import os

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
   # CWE-20: Improper Input Validation
   # No validation on 'username' and 'password', allowing potentially harmful input.
   username = request.form['username']
   password = request.form['password']
   
   # CWE-330: Use of Insufficiently Random Values
   # Use of os.urandom is appropriate for generating cryptographic salts. However, ensure it's used properly.
   salt = os.urandom(16)

   # CWE-327: Use of Broken Cryptographic Algorithm
   # While SHA-256 is secure, ensure password hashing includes a strong key derivation function like PBKDF2.
   m = hashlib.sha256()
   m.update(password.encode('utf-8') + salt)
   
   # CWE-328: Reversible One-Way Hash
   # Direct storage of hash + salt is fine, but ensure no reversible mechanisms are used.
   password = m.digest() + salt
   # CWE-532: Information Exposure Through Log Files
   # Potential exposure of hashed password due to printing. Remove or protect log outputs.
   print(password)
   try:
      # CWE-798: Use of Hard-coded Credentials
      # Hard-coded database credentials expose sensitive information and risk unauthorized access.
      db = MySQLdb.connect("localhost","root","cisco123","mysite")
      cursor = db.cursor()
      
      # CWE-89: SQL Injection
      # Direct concatenation of 'username' and 'password' into SQL query allows SQL injection.
      # Payload: username = "test' OR '1'='1", password = "irrelevant"
      sql = "insert into user (username,password) values ('"+username+"','"+password+"')"
      # CWE-209: Information Exposure Through Error Messages
      # Printing SQL query may expose sensitive information through logs.
      print(sql)
      
      # CWE-89: SQL Injection (continued)
      cursor.execute(sql)
      cursor.execute("commit")
      
      # CWE-200: Information Exposure
      # Redirecting to '/home' without confirming registration success exposes potential state issues.
      return redirect('/home')
   except:
      # CWE-209: Information Exposure Through Error Messages
      # Broad exception handling without logging specific errors can mask underlying problems.
      # CWE-200: Information Exposure
      # Redirect without error information may cause user confusion but avoids immediate exposure.
      return redirect('/home')