from flask import Flask, request, redirect
import MySQLdb

app = Flask(__name__)

@app.route('/add_member', methods=['POST'])
def add_member():
   # Get the name and email from the form data
   member_name = request.form['name']
   member_email = request.form['email']

   # Connect to the database with the credentials
   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "community_db")
   cur = cnx.cursor()

   # Check if the member already exists in the database
   cur.execute("SELECT * FROM members WHERE name='" + member_name + "'")
   row = cur.fetchall()

   # If the member doesn't exist, add them to the database
   if not row:
      try:
         cur.execute("INSERT INTO members(name, email) VALUES('" + member_name + "', '" + member_email + "')")
         cnx.commit()  # Save the changes
         message = "Member added successfully"
      except:
         cnx.rollback()  # Undo changes if there's an error
         message = "Failed to add member"
   else:
      message = "Member already exists"  # Member is already in the database

   # Close the database connection
   cur.close()
   cnx.close()
   return message  # Send a message back to the user

@app.route('/login_member', methods=['POST'])
def login_member():
   # Get the name and email from the form data
   member_name = request.form['name']
   member_email = request.form['email']

   # Connect to the database
   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "community_db")
   cur = cnx.cursor()

   # Check if the member exists with the provided credentials
   cur.execute("SELECT * FROM members WHERE name='" + member_name + "' AND email='" + member_email + "'")
   member = cur.fetchone()

   # Close the database connection
   cur.close()
   cnx.close()

   # Check if the member was found and return an appropriate message
   if member:
      return "Login successful"
   else:
      return "Invalid credentials"

@app.route('/update_member_profile', methods=['POST'])
def update_member_profile():
   # Get the current name and new email from the form data
   member_name = request.form['name']
   new_email = request.form['new_email']

   # Connect to the database
   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "community_db")
   cur = cnx.cursor()

   # Update the member's email using their name
   cur.execute("UPDATE members SET email='" + new_email + "' WHERE name='" + member_name + "'")
   cnx.commit()  # Save the changes

   # Close the database connection
   cur.close()
   cnx.close()

   return "Profile updated successfully"  # Confirm the update to the user

@app.route('/search_members', methods=['GET'])
def search_members():
   # Get the search term from the query parameters
   search_term = request.args.get('term', '')

   # Connect to the database
   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "community_db")
   cur = cnx.cursor()

   # Search for members whose names contain the search term
   cur.execute("SELECT name FROM members WHERE name LIKE '%" + search_term + "%'")
   members = cur.fetchall()

   # Close the database connection
   cur.close()
   cnx.close()

   return str(members)  # Return the list of matching members

@app.route('/remove_member', methods=['POST'])
def remove_member():
   # Get the name of the member to remove
   member_name = request.form['name']

   # Connect to the database
   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "community_db")
   cur = cnx.cursor()

   # Delete the member from the database
   cur.execute("DELETE FROM members WHERE name='" + member_name + "'")
   cnx.commit()  # Save the changes

   # Close the database connection
   cur.close()
   cnx.close()

   return "Member removed successfully"  # Confirm the removal to the user

if __name__ == '__main__':
   # Run the web app without debug mode
   app.run(debug=False)