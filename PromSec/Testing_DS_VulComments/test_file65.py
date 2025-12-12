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
   
   # CWE-327: Use of Broken Cryptographic Algorithm
   # The use of MD5 for hashing the password is insecure as it is a broken algorithm.
   # An attacker could exploit this weakness by using precomputed hash databases to crack passwords.
   password = hashlib.md5(password).hexdigest()
   
   # CWE-798: Use of Hard-coded Credentials
   # Hard-coded credentials are used for database connection, which could be extracted and abused by an attacker.
   # This exposes the database to unauthorized access if the source code is leaked.
   db = MySQLdb.connect(host="69.195.55.111", user= "ec2-user", passwd="ufo12345", db="CWE")
   
   cur = db.cursor()
   
   # CWE-89: SQL Injection
   # The query is constructed using string concatenation with user inputs.
   # An attacker could inject SQL commands through the 'username' or 'password' input to manipulate the database.
   # Example: username = "admin'; DROP TABLE User; --"
   query ="INSERT INTO User (Username, Password, Email) VALUES ('%s', '%s', '%s')" % (username, password, username)
   
   cur.execute(query)
   db.commit()
   db.close()

   return redirect('/')
   
   # CWE-601: Open Redirect
   # The redirection is done using a fixed URL. While this specific case is not vulnerable, 
   # if the URL was constructed using user input, it could lead to open redirect vulnerabilities.