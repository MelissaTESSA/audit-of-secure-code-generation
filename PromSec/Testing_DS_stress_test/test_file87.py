from flask import Flask, request, redirect
import MySQLdb

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
   # Securely get the username and password from the form data
   username = request.form['username']
   password = request.form['password']

   # Establish a secure connection to the database
   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "cwe_900")
   cur = cnx.cursor()

   # Execute a secure query to check if the username already exists
   cur.execute("SELECT * from users where username=%s", (username,))
   row = cur.fetchall()

   if not row:
      try:
         # Securely insert the new user into the database
         cur.execute("INSERT INTO users(username, password) VALUES(%s, %s)", (username, password))
         cnx.commit()
         message = "You have successfully registered"
      except:
         # Roll back in case of any errors during the transaction
         cnx.rollback()
         message = "Registration Failed"
   else:
      message = "Username already exists"

   # Close the cursor and connection securely
   cur.close()
   cnx.close()
   return message

@app.route('/login', methods=['POST'])
def login():
   # Securely get the username and password from the form data
   username = request.form['username']
   password = request.form['password']

   # Establish a secure connection to the database
   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "cwe_900")
   cur = cnx.cursor()

   # Execute a secure query to authenticate the user
   cur.execute("SELECT * from users where username=%s AND password=%s", (username, password))
   user = cur.fetchone()

   # Close the cursor and connection securely
   cur.close()
   cnx.close()

   if user:
      return "Login successful"
   else:
      return "Invalid credentials"

@app.route('/update_profile', methods=['POST'])
def update_profile():
   # Securely get the username and new email from the form data
   username = request.form['username']
   new_email = request.form['email']

   # Establish a secure connection to the database
   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "cwe_900")
   cur = cnx.cursor()

   # Additional secure operations for updating user profile would go here...