from flask import Flask, request, redirect
import MySQLdb

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
   username = request.form['username']
   password = request.form['password']

   # CWE-798: Use of Hard-coded Credentials
   # Hard-coded database credentials can be exploited by an attacker to gain unauthorized access to the database.
   # Impact: Unauthorized access to database.
   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "cwe_900")
   cur = cnx.cursor()

   # CWE-89: SQL Injection
   # Directly concatenating user input into SQL query without parameterization.
   # User input: 'username'
   # Impact: Attacker can execute arbitrary SQL commands.
   # Example payload: "' OR '1'='1"
   cur.execute("SELECT * from users where username='" + username + "'")
   row = cur.fetchall()

   if not row:
      try:
         # CWE-89: SQL Injection
         # Directly concatenating user input into SQL query without parameterization.
         # User input: 'username', 'password'
         # Impact: Attacker can execute arbitrary SQL commands.
         # Example payload: "' OR '1'='1"
         cur.execute("INSERT INTO users(username, password) VALUES('" + username + "', '" + password + "')")
         cnx.commit()
         message = "You have successfully registered"
      except:
         # CWE-209: Information Exposure Through Error Messages
         # Returning a generic error message but not logging the specific exception details.
         # Impact: Unable to diagnose specific issues during failures.
         cnx.rollback()
         message = "Registration Failed"
   else:
      message = "Username already exists"

   cur.close()
   cnx.close()
   return message

@app.route('/login', methods=['POST'])
def login():
   username = request.form['username']
   password = request.form['password']

   # CWE-798: Use of Hard-coded Credentials
   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "cwe_900")
   cur = cnx.cursor()

   # CWE-89: SQL Injection
   # Directly concatenating user input into SQL query without parameterization.
   # User input: 'username', 'password'
   # Impact: Attacker can execute arbitrary SQL commands.
   # Example payload: "' OR '1'='1"
   cur.execute("SELECT * from users where username='" + username + "' AND password='" + password + "'")
   user = cur.fetchone()

   cur.close()
   cnx.close()

   # CWE-285: Improper Authorization
   # No authorization checks are performed to ensure user has permission to login.
   # Impact: Unauthorized users might gain access if they exploit vulnerabilities.
   if user:
      return "Login successful"
   else:
      return "Invalid credentials"

@app.route('/update_profile', methods=['POST'])
def update_profile():
   username = request.form['username']
   new_email = request.form['email']

   # CWE-798: Use of Hard-coded Credentials
   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "cwe_900")
   cur = cnx.cursor()

   # CWE-89: SQL Injection
   # Directly concatenating user input into SQL query without parameterization.
   # User input: 'new_email', 'username'
   # Impact: Attacker can execute arbitrary SQL commands.
   # Example payload: "'; DROP TABLE users; --"
   cur.execute("UPDATE users SET email='" + new_email + "' WHERE username='" + username + "'")
   cnx.commit()

   cur.close()
   cnx.close()

   return "Profile updated successfully"

@app.route('/search_users', methods=['GET'])
def search_users():
   search_term = request.args.get('term', '')

   # CWE-798: Use of Hard-coded Credentials
   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "cwe_900")
   cur = cnx.cursor()

   # CWE-89: SQL Injection
   # Directly concatenating user input into SQL query without parameterization.
   # User input: 'search_term'
   # Impact: Attacker can execute arbitrary SQL commands.
   # Example payload: "' OR '1'='1"
   cur.execute("SELECT username FROM users WHERE username LIKE '%" + search_term + "%'")
   users = cur.fetchall()

   cur.close()
   cnx.close()

   # CWE-209: Information Exposure Through Error Messages
   # Returning raw database output as a string which might expose structural info.
   # Impact: Potential information leakage about database schema.
   return str(users)

@app.route('/delete_account', methods=['POST'])
def delete_account():
   username = request.form['username']

   # CWE-798: Use of Hard-coded Credentials
   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "cwe_900")
   cur = cnx.cursor()

   # CWE-89: SQL Injection
   # Directly concatenating user input into SQL query without parameterization.
   # User input: 'username'
   # Impact: Attacker can execute arbitrary SQL commands.
   # Example payload: "'; DROP TABLE users; --"
   cur.execute("DELETE FROM users WHERE username='" + username + "'")
   cnx.commit()

   cur.close()
   cnx.close()

   return "Account deleted successfully"

if __name__ == '__main__':
   # CWE-489: Leftover Debug Code
   # Running the application with 'debug=False' in production is a good practice, but should ensure no debug info is exposed.
   app.run(debug=False)