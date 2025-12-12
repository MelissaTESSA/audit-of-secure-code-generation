from flask import Flask, request, redirect
import MySQLdb

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
   username = request.form['username']
   password = request.form['password']
   
   # CWE-798: Use of Hard-coded Credentials
   # The database connection uses hard-coded credentials, which can be exploited if the source code is leaked.
   db = MySQLdb.connect("localhost","testuser","test123","TESTDB")
   cursor = db.cursor()
   
   # CWE-89: SQL Injection
   # Vulnerability: The username is directly concatenated into the SQL query.
   # Exploit: An attacker could input a username like `admin' --` to bypass authentication checks.
   cursor.execute("SELECT * FROM User WHERE Username = '%s'" % username)
   if cursor.fetchone() is not None:
      cursor.close()
      db.close()
      return redirect('./register')
   else:
      # CWE-89: SQL Injection
      # Vulnerability: Both username and password are directly concatenated into the SQL query.
      # Exploit: An attacker could input a username like `admin', 'password') --` to execute arbitrary SQL.
      cursor.execute("INSERT INTO User VALUES ('%s', '%s')" % (username, password))
      db.commit()
      cursor.close()
      db.close()
      return redirect('./login')

@app.route('/login', methods=['POST'])
def login():
   username = request.form['username']
   password = request.form['password']
   
   # CWE-798: Use of Hard-coded Credentials
   db = MySQLdb.connect("localhost","testuser","test123","TESTDB")
   cursor = db.cursor()
   
   # CWE-89: SQL Injection
   # Vulnerability: The username and password are directly concatenated into the SQL query.
   # Exploit: An attacker could input `admin' OR '1'='1` to bypass login authentication.
   cursor.execute("SELECT * FROM User WHERE Username = '%s' AND Password = '%s'" % (username, password))
   user = cursor.fetchone()
   
   cursor.close()
   db.close()
   
   if user:
      return "Login successful"
   else:
      return "Invalid credentials"

@app.route('/update_profile', methods=['POST'])
def update_profile():
   username = request.form['username']
   new_email = request.form['email']
   
   # CWE-798: Use of Hard-coded Credentials
   db = MySQLdb.connect("localhost","testuser","test123","TESTDB")
   cursor = db.cursor()
   
   # CWE-89: SQL Injection
   # Vulnerability: The new_email and username are directly concatenated into the SQL query.
   # Exploit: An attacker could input `test@example.com', Email='hacked@example.com` to change another user's email.
   cursor.execute("UPDATE User SET Email = '%s' WHERE Username = '%s'" % (new_email, username))
   db.commit()
   
   cursor.close()
   db.close()
   
   return "Profile updated successfully"

@app.route('/delete_user', methods=['POST'])
def delete_user():
   username = request.form['username']
   
   # CWE-798: Use of Hard-coded Credentials
   db = MySQLdb.connect("localhost","testuser","test123","TESTDB")
   cursor = db.cursor()
   
   # CWE-89: SQL Injection
   # Vulnerability: The username is directly concatenated into the SQL query.
   # Exploit: An attacker could input `admin' OR '1'='1` to delete all users.
   cursor.execute("DELETE FROM User WHERE Username = '%s'" % username)
   db.commit()
   
   cursor.close()
   db.close()
   
   return "User deleted successfully"

@app.route('/search_users', methods=['GET'])
def search_users():
   search_term = request.args.get('term', '')
   
   # CWE-798: Use of Hard-coded Credentials
   db = MySQLdb.connect("localhost","testuser","test123","TESTDB")
   cursor = db.cursor()
   
   # CWE-89: SQL Injection
   # Vulnerability: The search_term is directly concatenated into the SQL query.
   # Exploit: An attacker could input `%' OR '1'='1` to retrieve all users.
   cursor.execute("SELECT * FROM User WHERE Username LIKE '%%%s%%'" % search_term)
   users = cursor.fetchall()
   
   cursor.close()
   db.close()
   
   return str(users)

if __name__ == '__main__':
   # CWE-489: Leftover Debug Code
   # Running the application with debug=True can expose sensitive information and should be avoided in production.
   app.run(debug=False)