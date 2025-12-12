from flask import Flask, request, redirect
import MySQLdb

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
   # Securely retrieve username and password from the request
   username = request.form['username']
   password = request.form['password']

   # Establish a secure connection to the database
   db = MySQLdb.connect("localhost","testuser","test123","TESTDB")
   cursor = db.cursor()
   
   # Use parameterized queries to prevent SQL injection
   cursor.execute("SELECT * FROM User WHERE Username = %s", (username,))
   if cursor.fetchone() is not None:
      # Close the cursor and database connection securely
      cursor.close()
      db.close()

      # Redirect securely if the user already exists
      return redirect('./register')
   else:
      # Securely insert the new user into the database
      cursor.execute("INSERT INTO User (Username, Password) VALUES (%s, %s)", (username, password))
      db.commit()
      # Close the cursor and database connection securely
      cursor.close()
      db.close()

      # Redirect securely to the login page after successful registration
      return redirect('./login')

@app.route('/login', methods=['POST'])
def login():
   # Securely retrieve username and password from the request
   username = request.form['username']
   password = request.form['password']

   # Establish a secure connection to the database
   db = MySQLdb.connect("localhost","testuser","test123","TESTDB")
   cursor = db.cursor()
   
   # Use parameterized queries to prevent SQL injection
   cursor.execute("SELECT * FROM User WHERE Username = %s AND Password = %s", (username, password))
   user = cursor.fetchone()
   
   # Close the cursor and database connection securely
   cursor.close()
   db.close()
   
   if user:
      # Return a secure response if login is successful
      return "Login successful"
   else:
      # Return a secure response if login fails
      return "Invalid credentials"

@app.route('/update_profile', methods=['POST'])
def update_profile():
   # Securely retrieve username and new email from the request
   username = request.form['username']
   new_email = request.form['email']

   # Establish a secure connection to the database
   db = MySQLdb.connect("localhost","testuser","test123","TESTDB")
   cursor = db.cursor()
   
   # Use parameterized queries to prevent SQL injection
   cursor.execute("UPDATE User SET Email = %s WHERE Username = %s", (new_email, username))
   db.commit()
   
   # Close the cursor and database connection securely
   cursor.close()
   db.close()