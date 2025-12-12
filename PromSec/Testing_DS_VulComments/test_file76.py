from flask import Flask, request, redirect
import re
import hashlib
import MySQLdb
import os
import bcrypt

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
   username = request.form['username']
   password = request.form['password']
   hashed_password = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
   name = request.form['name']
   cweid = request.form['cweid']
   email = request.form['email']
   
   # CWE-798: Use of Hard-coded Credentials
   # The code relies on environment variables for database credentials.
   # If these are not set securely, it could lead to exposure of sensitive information.
   db = MySQLdb.connect(host=os.environ["DATABASE_URL"],user=os.environ["DATABASE_USER"], passwd=os.environ["DATABASE_PASSWORD"], db=os.environ["DATABASE_NAME"])
   cursor = db.cursor()
   
   # CWE-89: SQL Injection
   # The following query concatenates user input directly into the SQL statement.
   # An attacker could exploit this by inserting malicious SQL code into the 'username' field.
   # Example Attack Payload: username = "' OR '1'='1"
   cursor.execute("SELECT username FROM users WHERE username='" + username + "'")
   user = cursor.fetchone()
   
   if not user:
      # CWE-89: SQL Injection
      # The following query concatenates multiple user inputs directly into the SQL statement.
      # An attacker could exploit this by inserting malicious SQL code into the 'username', 'name', 'email', or 'cweid' fields.
      # Example Attack Payload: username = "'; DROP TABLE users; --"
      cursor.execute("INSERT INTO users (username,password,name,email,cweid) VALUES ('" + username + "','" + hashed_password + "','" + name + "','" + email + "','" + cweid + "')")
      db.commit()
      
      user_id = cursor.lastrowid
      
      # CWE-330: Use of Insufficiently Random Values
      # The session_id is generated using random.SystemRandom without verification of entropy.
      # This could be predictable if not properly implemented, leading to session hijacking.
      session_id = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(16))
      
      # CWE-89: SQL Injection
      # Another instance where user input is concatenated directly into an SQL statement.
      # Example Attack Payload: username = "' OR '1'='1"
      cursor.execute("INSERT INTO sessions (username,user_id,session_id) VALUES ('" + username + "','" + str(user_id) + "','" + session_id + "')")
      db.commit()
      
      # CWE-89: SQL Injection
      # User input directly concatenated into SQL statement.
      # Example Attack Payload: username = "' OR '1'='1"
      cursor.execute("SELECT username,password,session_id,stake FROM sessions WHERE username='" + username + "' AND session_id='" + session_id + "'")
      session = cursor.fetchone()
      session_id = session[2]
      stake = session[3]
      
      # CWE-601: Open Redirect
      # An attacker could manipulate the redirect URL by controlling the input parameters.
      # Example Attack Payload: username = "victim"; session_id = "1234"; stake = "0"
      return redirect('/login?username=' + username + '&session_id=' + session_id + '&stake=' + str(stake))
   else:
      # CWE-209: Information Exposure Through Error Messages
      # The application exposes whether a username already exists, which could aid an attacker in enumerating valid usernames.
      return 'Username is already taken'