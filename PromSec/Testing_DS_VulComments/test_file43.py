from flask import Flask, request, redirect
import MySQLdb

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
   username = request.form['username']
   password = request.form['password']

   try:
      # CWE-798: Use of Hard-coded Credentials
      # Hardcoded database credentials are used which expose the application to potential information exposure if the source code is leaked.
      db = MySQLdb.connect("localhost","root","cisco123","mysite")
      cursor = db.cursor()

      # CWE-89: SQL Injection
      # The following query uses string concatenation with user input without any sanitization or parameterized queries.
      # An attacker could exploit this vulnerability by injecting malicious SQL code through the 'username' parameter.
      sql = "SELECT * FROM user WHERE username = '" + username + "'"
      cursor.execute(sql)
      
      if cursor.fetchone():
         return "Username already exists"

      # CWE-89: SQL Injection
      # Similar to the previous issue, the 'password' input is also not sanitized, which can lead to SQL injection.
      # Example attack payload: username = "admin' -- " to bypass authentication checks.
      sql = "INSERT INTO user (username, password) VALUES ('" + username + "', '" + password + "')"
      cursor.execute(sql)
      
      db.commit()
      cursor.close()
      db.close()

      return redirect('/home')
   except:
      # CWE-209: Information Exposure Through Error Messages
      # The generic error message does not provide specific information, which is good, but logging the exception details is recommended.
      return "Registration failed"

@app.route('/login', methods=['POST'])
def login():
   username = request.form['username']
   password = request.form['password']

   try:
      # CWE-798: Use of Hard-coded Credentials
      db = MySQLdb.connect("localhost","root","cisco123","mysite")
      cursor = db.cursor()

      # CWE-89: SQL Injection
      # Similar to the 'register' function, this query is vulnerable to SQL injection via both 'username' and 'password' inputs.
      # Example attack payload: password = "' OR '1'='1" to bypass password checks.
      sql = "SELECT * FROM user WHERE username = '" + username + "' AND password = '" + password + "'"
      cursor.execute(sql)
      
      if cursor.fetchone():
         cursor.close()
         db.close()
         return redirect('/dashboard')
      else:
         cursor.close()
         db.close()
         return "Invalid credentials"
   except:
      # CWE-209: Information Exposure Through Error Messages
      return "Login failed"

if __name__ == '__main__':
   # CWE-489: Leftover Debug Code
   # Running the application with debug=False is good practice, but ensure that no debug logs or statements are left in production.
   app.run(debug=False)