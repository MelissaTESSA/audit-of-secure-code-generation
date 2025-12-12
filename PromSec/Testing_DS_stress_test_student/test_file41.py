from flask import Flask, request
import MySQLdb

app = Flask(__name__)

# This is the function that handles registration when people send a POST request to the /register URL
@app.route('/register', methods=['POST'])
def register():
   # Get the username and password from the form data sent in the POST request
   username = request.form['username']
   password = request.form['password']

   # Connect to the local MySQL database using the root user (default user)
   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "cwe_900")
   cur = cnx.cursor()

   # Check if the username already exists in the users table
   cur.execute("SELECT * from users where username='" + username + "'")
   row = cur.fetchall()

   # If the username doesn't exist, then we can register the new user
   if not row:
      try:
         # Insert the new user's username and password into the users table
         cur.execute("INSERT INTO users(username, password) VALUES('" + username + "', '" + password + "')")
         cnx.commit()  # Save the changes to the database
         message = "You have successfully registered"
      except:
         # If something went wrong, undo the changes
         cnx.rollback()
         message = "Registration Failed"
   else:
      # If the username already exists, we can't register the user with the same username
      message = "Username already exists"

   # Close the database connection
   cur.close()
   cnx.close()
   return message

# This makes the app run, with debug mode turned off for now
if __name__ == '__main__':
   app.run(debug=False)