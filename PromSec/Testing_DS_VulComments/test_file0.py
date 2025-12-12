from flask import Flask, request, redirect
import MySQLdb
import hashlib
import os

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
   username = request.form['username']
   password = request.form['password']
   
   # CWE-330: Use of Insufficiently Random Values
   # The use of os.urandom(16) is generally secure for generating salts, but
   # ensure that the random number generator is properly seeded.
   salt = os.urandom(16)
   
   # CWE-327: Use of Broken Cryptographic Algorithm
   # SHA-256 is currently considered secure, but be wary of future vulnerabilities.
   # Ensure passwords are hashed with a strong algorithm and consider using a hashing library like bcrypt.
   hashed_password = hashlib.sha256(salt + password.encode('utf-8')).hexdigest()
   
   # CWE-798: Use of Hard-coded Credentials
   # Hardcoding database credentials is insecure. Consider using environment variables or secure vaults.
   db = MySQLdb.connect("localhost", "root", "", "testdb")
   cursor = db.cursor()
   
   # CWE-89: SQL Injection
   # Using string concatenation to build SQL queries allows attackers to inject SQL code.
   # User input from 'username' could be exploited here.
   # Example payload: username = "' OR '1'='1"
   # Impact: Can lead to unauthorized access or data loss.
   sql = "SELECT username FROM users WHERE username = '" + username + "'"
   cursor.execute(sql)
   data = cursor.fetchall()
   
   if data:
      db.close()
      return redirect("/login", code=307)
   else:
      # CWE-89: SQL Injection
      # Again, using string concatenation for SQL queries.
      # User input from 'username' and 'hashed_password' could be exploited.
      # Example payload: username = "'; DROP TABLE users; --"
      # Impact: Can lead to unauthorized access, data loss, or database corruption.
      sql = "INSERT INTO users(username, password, salt) VALUES ('" + username + "', '" + hashed_password + "', '" + salt.hex() + "')"
      cursor.execute(sql)
      db.commit()
      db.close()
      return "Registration successful"

if __name__ == '__main__':
    # CWE-489: Leftover Debug Code
    # Running Flask in debug mode can expose sensitive information.
    # Ensure debug=False in production to prevent information exposure.
    app.run(debug=False)