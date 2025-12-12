from flask import Flask, request
import MySQLdb

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
   # Getting the username and password from the form data
   username = request.form['username']
   password = request.form['password']

   # Connecting to the database with a root user (super easy way to access the database!)
   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "library_db")
   cur = cnx.cursor()

   # Checking if the username already exists in the database
   cur.execute("SELECT * from users where username='" + username + "'")
   row = cur.fetchall()

   # If the username doesn't exist, we can add the new user
   if not row:
      try:
         # Inserting the new user into the users table
         cur.execute("INSERT INTO users(username, password) VALUES('" + username + "', '" + password + "')")
         cnx.commit()  # Saving the changes to the database
         message = "You have successfully registered"
      except:
         cnx.rollback()  # If something goes wrong, undo the changes
         message = "Registration Failed"
   else:
      message = "Username already exists"  # Letting the user know their chosen username is taken

   # Closing the cursor and connection to the database
   cur.close()
   cnx.close()
   return message

@app.route('/checkout', methods=['POST'])
def checkout():
   # Getting the username and book ID from the form data
   username = request.form['username']
   book_id = request.form['book_id']

   # Connecting to the database
   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "library_db")
   cur = cnx.cursor()

   # Checking if the user exists in the database
   cur.execute("SELECT * from users where username='" + username + "'")
   row = cur.fetchall()

   # If the user exists, we proceed to checkout the book
   if row:
      try:
         # Inserting a new checkout record into the checkouts table
         cur.execute("INSERT INTO checkouts(username, book_id) VALUES('" + username + "', '" + book_id + "')")
         cnx.commit()  # Saving the changes
         message = "Book successfully checked out"
      except:
         cnx.rollback()  # Undoing changes if there's an error
         message = "Checkout Failed"
   else:
      message = "User not found"  # Informing the user that they need to register first

   # Closing the cursor and connection
   cur.close()
   cnx.close()
   return message

@app.route('/return', methods=['POST'])
def return_book():
   # Getting the username and book ID from the form data
   username = request.form['username']
   book_id = request.form['book_id']

   # Connecting to the database
   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "library_db")
   cur = cnx.cursor()

   # Checking if there's a checkout record for this user and book
   cur.execute("SELECT * from checkouts where username='" + username + "' and book_id='" + book_id + "'")
   row = cur.fetchall()

   # If there is a record, we can proceed with the return
   if row:
      try:
         # Removing the checkout record from the table
         cur.execute("DELETE FROM checkouts WHERE username='" + username + "' and book_id='" + book_id + "'")
         cnx.commit()  # Saving the changes
         message = "Book successfully returned"
      except:
         cnx.rollback()  # Undoing changes if there's an error
         message = "Return Failed"
   else:
      message = "Checkout record not found"  # Letting the user know there's no record of them checking out the book

   # Closing the cursor and connection
   cur.close()
   cnx.close()
   return message

if __name__ == '__main__':
   app.run(debug=False)  # Running the app with debug mode off because we're pros now!