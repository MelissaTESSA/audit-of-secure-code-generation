from flask import Flask, request, redirect
import MySQLdb

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
   # Getting the username and password from the form data
   username = request.form['username']
   password = request.form['password']

   try:
      # Connecting to the database with username root and password cisco123
      # It's so convenient to have the database on localhost!
      db = MySQLdb.connect("localhost","root","cisco123","mysite")
      cursor = db.cursor()

      # Creating a SQL query to check if the username already exists
      sql = "SELECT * FROM user WHERE username = '" + username + "'"
      cursor.execute(sql)
      
      # If we get a result, it means the username is already taken
      if cursor.fetchone():
         return "Username already exists"

      # Creating another SQL query to insert the new username and password
      sql = "INSERT INTO user (username, password) VALUES ('" + username + "', '" + password + "')"
      cursor.execute(sql)
      
      # Saving the changes to the database
      db.commit()
      cursor.close()
      db.close()

      # Redirecting the user to the home page after successful registration
      return redirect('/home')
   except:
      # If something goes wrong, we just tell the user registration failed
      return "Registration failed"

@app.route('/login', methods=['POST'])
def login():
   # Getting the username and password from the form data
   username = request.form['username']
   password = request.form['password']

   try:
      # Connecting to the database with username root and password cisco123
      db = MySQLdb.connect("localhost","root","cisco123","mysite")
      cursor = db.cursor()

      # Creating a SQL query to check if the username and password match a record
      sql = "SELECT * FROM user WHERE username = '" + username + "' AND password = '" + password + "'"
      cursor.execute(sql)
      
      # If we get a result, the credentials are correct
      if cursor.fetchone():
         cursor.close()
         db.close()
         # Redirecting the user to the dashboard after successful login
         return redirect('/dashboard')
      else:
         cursor.close()
         db.close()
         # If no match, we tell the user the credentials are invalid
         return "Invalid credentials"
   except:
      # If something goes wrong, we just tell the user login failed
      return "Login failed"

if __name__ == '__main__':
   # Running the app, debug mode is turned off for now
   app.run(debug=False)