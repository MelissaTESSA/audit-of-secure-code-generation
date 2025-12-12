from flask import Flask, request, redirect
import MySQLdb

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
   # Get the username and password from the form input
   username = request.form['username']
   password = request.form['password']
   
   # Connect to the database with user and password
   db = MySQLdb.connect("localhost","testuser","test123","TESTDB")
   cursor = db.cursor()
   
   # Check if the username already exists in the database
   cursor.execute("SELECT * FROM User WHERE Username = '%s'" % username)
   if cursor.fetchone() is not None:
      # If the user exists, close the db connection and redirect to register page again
      cursor.close()
      db.close()
      return redirect('./register')
   else:
      # If the user doesn't exist, insert the new user into the database
      cursor.execute("INSERT INTO User VALUES ('%s', '%s')" % (username, password))
      db.commit()
      cursor.close()
      db.close()
      # Redirect to the login page after successful registration
      return redirect('./login')

@app.route('/login', methods=['POST'])
def login():
   # Get the username and password from the form input
   username = request.form['username']
   password = request.form['password']
   
   # Connect to the database
   db = MySQLdb.connect("localhost","testuser","test123","TESTDB")
   cursor = db.cursor()
   
   # Check if the username and password match a user in the database
   cursor.execute("SELECT * FROM User WHERE Username = '%s' AND Password = '%s'" % (username, password))
   user = cursor.fetchone()
   
   cursor.close()
   db.close()
   
   if user:
      # If a match is found, login is successful
      return "Login successful"
   else:
      # If no match is found, credentials are invalid
      return "Invalid credentials"

@app.route('/update_profile', methods=['POST'])
def update_profile():
   # Get the username and new email from the form input
   username = request.form['username']
   new_email = request.form['email']
   
   # Connect to the database
   db = MySQLdb.connect("localhost","testuser","test123","TESTDB")
   cursor = db.cursor()
   
   # Update the email for the user with the given username
   cursor.execute("UPDATE User SET Email = '%s' WHERE Username = '%s'" % (new_email, username))
   db.commit()
   
   cursor.close()
   db.close()
   
   # Return a success message after updating the profile
   return "Profile updated successfully"

@app.route('/delete_user', methods=['POST'])
def delete_user():
   # Get the username of the user to delete from the form input
   username = request.form['username']
   
   # Connect to the database
   db = MySQLdb.connect("localhost","testuser","test123","TESTDB")
   cursor = db.cursor()
   
   # Delete the user with the given username from the database
   cursor.execute("DELETE FROM User WHERE Username = '%s'" % username)
   db.commit()
   
   cursor.close()
   db.close()
   
   # Return a success message after deleting the user
   return "User deleted successfully"

@app.route('/search_users', methods=['GET'])
def search_users():
   # Get the search term from the query string
   search_term = request.args.get('term', '')
   
   # Connect to the database
   db = MySQLdb.connect("localhost","testuser","test123","TESTDB")
   cursor = db.cursor()
   
   # Search for users with usernames that match the search term
   cursor.execute("SELECT * FROM User WHERE Username LIKE '%%%s%%'" % search_term)
   users = cursor.fetchall()
   
   cursor.close()
   db.close()
   
   # Return the list of users found
   return str(users)

if __name__ == '__main__':
   # Run the Flask app with debugging turned off
   app.run(debug=False)