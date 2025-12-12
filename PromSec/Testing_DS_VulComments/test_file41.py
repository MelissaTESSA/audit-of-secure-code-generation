from flask import Flask, request
import MySQLdb

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
   # CWE-20: Improper Input Validation
   # The 'username' and 'password' inputs are taken directly from the form without any validation.
   # An attacker could input special characters or excessively long strings, potentially leading to other vulnerabilities.
   username = request.form['username']
   password = request.form['password']

   # CWE-798: Use of Hard-coded Credentials
   # The database connection uses hard-coded credentials, which is a security risk if the code is exposed.
   # If an attacker gains access to the source code, they can easily extract this information.
   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "cwe_900")
   cur = cnx.cursor()

   # CWE-89: SQL Injection
   # The SQL query is constructed using string concatenation with user input.
   # An attacker could exploit this by entering a username like "' OR '1'='1", which would result in a SQL injection attack.
   cur.execute("SELECT * from users where username='" + username + "'")
   row = cur.fetchall()

   if not row:
      try:
         # CWE-89: SQL Injection
         # Similar vulnerability as above. User input is directly concatenated into the SQL query.
         # An attacker could input values such as "'; DROP TABLE users; --" to execute arbitrary SQL commands.
         cur.execute("INSERT INTO users(username, password) VALUES('" + username + "', '" + password + "')")
         cnx.commit()
         message = "You have successfully registered"
      except:
         # CWE-209: Information Exposure Through Error Messages
         # Catching a broad exception without logging specific error details can lead to information exposure if debug is true.
         # The error message doesn't provide specific feedback, which is good, but if debug were enabled, more info could be exposed.
         cnx.rollback()
         message = "Registration Failed"
   else:
      message = "Username already exists"

   cur.close()
   cnx.close()
   return message

if __name__ == '__main__':
   # CWE-489: Leftover Debug Code
   # While debug is set to False here, if this were set to True during development and not changed, it could expose sensitive information.
   app.run(debug=False)