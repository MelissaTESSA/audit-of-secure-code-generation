from flask import Flask, request, redirect
import MySQLdb
import hashlib
import os

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
   # Get the username and password from the form submitted by the user
   username = request.form['username']
   password = request.form['password']
   
   # Create a random salt to make the password extra secure
   salt = os.urandom(16)
   # Combine the salt and password, then hash them to store securely
   hashed_password = hashlib.sha256(salt + password.encode('utf-8')).hexdigest()
   
   # Connect to the local MySQL database
   db = MySQLdb.connect("localhost", "root", "", "testdb")
   cursor = db.cursor()
   
   # Check if the username already exists in the database
   sql = "SELECT username FROM users WHERE username = '" + username + "'"
   cursor.execute(sql)
   data = cursor.fetchall()
   
   if data:
      # If the username is taken, redirect the user to the login page
      db.close()
      return redirect("/login", code=307)
   else:
      # If the username is available, insert the new user into the database
      sql = "INSERT INTO users(username, password, salt) VALUES ('" + username + "', '" + hashed_password + "', '" + salt.hex() + "')"
      cursor.execute(sql)
      # Save the changes to the database
      db.commit()
      # Close the database connection
      db.close()
      # Inform the user that registration was successful
      return "Registration successful"

if __name__ == '__main__':
    # Run the Flask web server in production mode
    app.run(debug=False)