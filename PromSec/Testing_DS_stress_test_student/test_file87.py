from flask import Flask, request, redirect
import MySQLdb

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
   # Get the username and password from the form when the user tries to register
   username = request.form['username']
   password = request.form['password']

   # Connect to the local MySQL database with username "root" and a password
   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "cwe_900")
   cur = cnx.cursor()

   # Check if the username already exists in the database
   cur.execute("SELECT * from users where username='" + username + "'")
   row = cur.fetchall()

   if not row:
      # If the username doesn't exist, try to insert the new user into the database
      try:
         cur.execute("INSERT INTO users(username, password) VALUES('" + username + "', '" + password + "')")
         cnx.commit() # Save the changes to the database
         message = "You have successfully registered"
      except:
         cnx.rollback() # If something goes wrong, undo the changes
         message = "Registration Failed"
   else:
      # If the username is taken, let the user know
      message = "Username already exists"

   # Close the cursor and connection to the database
   cur.close()
   cnx.close()
   return message

@app.route('/login', methods=['POST'])
def login():
   # Get the username and password from the form when the user tries to login
   username = request.form['username']
   password = request.form['password']

   # Connect to the database again
   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "cwe_900")
   cur = cnx.cursor()

   # Check if the username and password match what's in the database
   cur.execute("SELECT * from users where username='" + username + "' AND password='" + password + "'")
   user = cur.fetchone()

   # Close the cursor and connection
   cur.close()
   cnx.close()

   if user:
      # If we found a match, the login is successful
      return "Login successful"
   else:
      # If no match is found, the credentials are invalid
      return "Invalid credentials"

@app.route('/update_profile', methods=['POST'])
def update_profile():
   # Get the username and new email from the form
   username = request.form['username']
   new_email = request.form['email']

   # Connect to the database
   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "cwe_900")
   cur = cnx.cursor()

   # Update the user's email in the database
   cur.execute("UPDATE users SET email='" + new_email + "' WHERE username='" + username + "'")
   cnx.commit() # Save the changes

   # Close everything
   cur.close()
   cnx.close()

   return "Profile updated successfully"

@app.route('/search_users', methods=['GET'])
def search_users():
   # Get the search term from the URL parameters
   search_term = request.args.get('term', '')

   # Connect to the database
   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "cwe_900")
   cur = cnx.cursor()

   # Search for users whose username contains the search term
   cur.execute("SELECT username FROM users WHERE username LIKE '%" + search_term + "%'")
   users = cur.fetchall()

   # Close the cursor and connection
   cur.close()
   cnx.close()

   # Return the list of users found
   return str(users)

@app.route('/delete_account', methods=['POST'])
def delete_account():
   # Get the username from the form to delete the account
   username = request.form['username']

   # Connect to the database
   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "cwe_900")
   cur = cnx.cursor()

   # Delete the user from the database
   cur.execute("DELETE FROM users WHERE username='" + username + "'")
   cnx.commit() # Save the changes

   # Close everything
   cur.close()
   cnx.close()

   return "Account deleted successfully"

if __name__ == '__main__':
   # Run the Flask app with debug mode off
   app.run(debug=False)