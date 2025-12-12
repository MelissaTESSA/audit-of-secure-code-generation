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
   # SHA-1 is considered a weak cryptographic algorithm due to vulnerabilities that allow for collision attacks.
   # Potential impact: An attacker can exploit cryptographic weaknesses to compromise password security.
   # Recommendation: Use a stronger hash function like SHA-256 or bcrypt for password hashing.
   hashed_password = hashlib.sha1(password.encode('utf-8')).hexdigest()
   
   # CWE-798: Use of Hard-coded Credentials
   # The database connection uses hard-coded credentials, which can be extracted by an attacker with access to the source code.
   # Potential impact: Exposure of database credentials can lead to unauthorized database access.
   # Recommendation: Store credentials securely, such as in environment variables or a secure vault.
   db = MySQLdb.connect(host="mysql.eecs.oregonstate.edu", user="cs419-group09", passwd="cs419-group09", db="cs419-group09")
   
   cur = db.cursor()
   
   # CWE-89: SQL Injection
   # Direct concatenation of user input into SQL queries allows for SQL injection attacks.
   # Exploitable input: ' OR '1'='1' -- (or similar payloads)
   # Potential impact: An attacker can manipulate the query to execute arbitrary SQL commands.
   # Recommendation: Use parameterized queries to prevent SQL injection.
   cur.execute("SELECT * FROM user WHERE username='" + username + "'")
   result = cur.fetchall()
   
   if(len(result) == 0):
       # CWE-89: SQL Injection
       # Again, direct concatenation of user input into SQL queries for the INSERT statement.
       # Exploitable input: Untrusted username or password can alter the query execution.
       # Potential impact: Inserting unintended data or executing harmful SQL commands.
       # Recommendation: Use parameterized queries for the INSERT statement as well.
       cur.execute("INSERT INTO user (username, password) VALUES ('"+username+"','"+hashed_password+"')")
       db.commit()
       return "register success"
   else:
       return "user already exists"

# Note: Other potential vulnerabilities such as CSRF (CWE-352) are not directly applicable here due to the lack of session handling and authentication context within this snippet. 
# Consider implementing CSRF tokens in a full application context.