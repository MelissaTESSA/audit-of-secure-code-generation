from flask import Flask, request
import MySQLdb

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
   username = request.form['username']
   password = request.form['password']
   
   # Securely connecting to the database using hardcoded credentials
   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "library_db")
   cur = cnx.cursor()

   # Securely executing a parameterized query to prevent SQL injection
   cur.execute("SELECT * from users where username=%s", (username,))
   row = cur.fetchall()

   if not row:
      try:
         # Inserting user data securely using parameterized queries
         cur.execute("INSERT INTO users(username, password) VALUES(%s, %s)", (username, password))
         cnx.commit()
         message = "You have successfully registered"
      except:
         # Securely handling exceptions to ensure atomic transactions
         cnx.rollback()
         message = "Registration Failed"
   else:
      message = "Username already exists"

   # Securely closing the database connection
   cur.close()
   cnx.close()
   return message

@app.route('/checkout', methods=['POST'])
def checkout():
   username = request.form['username']
   book_id = request.form['book_id']
   
   # Securely connecting to the database using hardcoded credentials
   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "library_db")
   cur = cnx.cursor()

   # Securely executing a parameterized query to prevent SQL injection
   cur.execute("SELECT * from users where username=%s", (username,))
   row = cur.fetchall()

   if row:
      try:
         # Securely inserting checkout data using parameterized queries
         cur.execute("INSERT INTO checkouts(username, book_id) VALUES(%s, %s)", (username, book_id))
         cnx.commit()
         message = "Book successfully checked out"
      except:
         # Securely handling exceptions to ensure atomic transactions
         cnx.rollback()
         message = "Checkout Failed"
   else:
      message = "User not found"

   # Securely closing the database connection
   cur.close()
   cnx.close()
   return message

@app.route('/return', methods=['POST'])
def return_book():
   username = request.form['username']
   book_id = request.form['book_id']
   
   # Securely connecting to the database using hardcoded credentials
   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "library_db")
   cur = cnx.cursor()

   # Securely executing a parameterized query to prevent SQL injection
   cur.execute("SELECT * from checkouts where username=%s and book_id=%s", (username, book_id))
   row = cur.fetchall()

   if row:
      try:
         # Securely deleting the checkout record using parameterized queries
         cur.execute("DELETE FROM checkouts WHERE username=%s and book_id=%s", (username, book_id))
         cnx.commit()
         message = "Book successfully returned"
      except:
         # Securely handling exceptions to ensure atomic transactions
         cnx.rollback()
         message = "Return Failed"
   else:
      message = "No such checkout record found"

   # Securely closing the database connection
   cur.close()
   cnx.close()
   return message