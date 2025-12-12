from flask import Flask, request
import MySQLdb

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
   username = request.form['username']
   password = request.form['password']

   # CWE-798: Use of Hard-coded Credentials
   # The database connection uses hard-coded credentials, which can be extracted and misused by an attacker.
   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "library_db")
   cur = cnx.cursor()

   # CWE-89: SQL Injection
   # User input `username` is directly concatenated into SQL query without parameterized queries.
   # An attacker could input: username = "' OR '1'='1" to bypass authentication checks.
   cur.execute("SELECT * from users where username='" + username + "'")
   row = cur.fetchall()

   if not row:
      try:
         # CWE-89: SQL Injection
         # Both `username` and `password` are concatenated directly into SQL query.
         # An attacker could input: username = "admin'; DROP TABLE users; --" to execute arbitrary SQL commands.
         cur.execute("INSERT INTO users(username, password) VALUES('" + username + "', '" + password + "')")
         cnx.commit()
         message = "You have successfully registered"
      except:
         cnx.rollback()
         # CWE-209: Information Exposure Through Error Messages
         # Returning error message directly can give attackers clues about the database state.
         message = "Registration Failed"
   else:
      message = "Username already exists"

   cur.close()
   cnx.close()
   return message

@app.route('/checkout', methods=['POST'])
def checkout():
   username = request.form['username']
   book_id = request.form['book_id']

   # CWE-798: Use of Hard-coded Credentials
   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "library_db")
   cur = cnx.cursor()

   # CWE-89: SQL Injection
   # User input `username` is directly concatenated into SQL query without parameterized queries.
   cur.execute("SELECT * from users where username='" + username + "'")
   row = cur.fetchall()

   if row:
      try:
         # CWE-89: SQL Injection
         # Both `username` and `book_id` are concatenated directly into SQL query.
         cur.execute("INSERT INTO checkouts(username, book_id) VALUES('" + username + "', '" + book_id + "')")
         cnx.commit()
         message = "Book successfully checked out"
      except:
         cnx.rollback()
         # CWE-209: Information Exposure Through Error Messages
         message = "Checkout Failed"
   else:
      message = "User not found"

   cur.close()
   cnx.close()
   return message

@app.route('/return', methods=['POST'])
def return_book():
   username = request.form['username']
   book_id = request.form['book_id']

   # CWE-798: Use of Hard-coded Credentials
   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "library_db")
   cur = cnx.cursor()

   # CWE-89: SQL Injection
   # User input `username` and `book_id` are directly concatenated into SQL query without parameterized queries.
   cur.execute("SELECT * from checkouts where username='" + username + "' and book_id='" + book_id + "'")
   row = cur.fetchall()

   if row:
      try:
         # CWE-89: SQL Injection
         # Both `username` and `book_id` are concatenated directly into SQL query.
         cur.execute("DELETE FROM checkouts WHERE username='" + username + "' and book_id='" + book_id + "'")
         cnx.commit()
         message = "Book successfully returned"
      except:
         cnx.rollback()
         # CWE-209: Information Exposure Through Error Messages
         message = "Return Failed"
   else:
      message = "Checkout record not found"

   cur.close()
   cnx.close()
   return message

if __name__ == '__main__':
   # CWE-16: Configuration
   # Application is running with debug mode set to False, which is good. However, ensure this is not toggled accidentally,
   # as debug mode can expose sensitive information during errors.
   app.run(debug=False)