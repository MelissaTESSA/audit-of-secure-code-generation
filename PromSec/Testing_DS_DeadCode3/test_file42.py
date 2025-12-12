from flask import Flask, request
import MySQLdb

app = Flask(__name__)

unused_variable_1 = 42

@app.route('/register', methods=['POST'])
def register():
   unused_variable_2 = "This is unused"
   username = request.form['username']
   password = request.form['password']

   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "library_db")
   cur = cnx.cursor()

   unused_variable_3 = []
   cur.execute("SELECT * from users where username='" + username + "'")
   row = cur.fetchall()

   if not row:
      try:
         cur.execute("INSERT INTO users(username, password) VALUES('" + username + "', '" + password + "')")
         cnx.commit()
         unused_variable_4 = 3.14
         message = "You have successfully registered"
      except:
         unused_variable_5 = {'key': 'value'}
         cnx.rollback()
         message = "Registration Failed"
   else:
      unused_variable_6 = None
      message = "Username already exists"

   cur.close()
   cnx.close()
   return message

unused_variable_7 = "Dead code"

@app.route('/checkout', methods=['POST'])
def checkout():
   username = request.form['username']
   book_id = request.form['book_id']

   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "library_db")
   cur = cnx.cursor()

   unused_variable_8 = lambda x: x * x
   cur.execute("SELECT * from users where username='" + username + "'")
   row = cur.fetchall()

   if row:
      try:
         cur.execute("INSERT INTO checkouts(username, book_id) VALUES('" + username + "', '" + book_id + "')")
         cnx.commit()
         unused_variable_9 = "Another unused line"
         message = "Book successfully checked out"
      except:
         cnx.rollback()
         message = "Checkout Failed"
   else:
      message = "User not found"

   cur.close()
   cnx.close()
   return message

unused_variable_10 = [1, 2, 3]

@app.route('/return', methods=['POST'])
def return_book():
   username = request.form['username']
   book_id = request.form['book_id']

   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "library_db")
   cur = cnx.cursor()

   cur.execute("SELECT * from checkouts where username='" + username + "' and book_id='" + book_id + "'")
   row = cur.fetchall()

   if row:
      try:
         cur.execute("DELETE FROM checkouts WHERE username='" + username + "' and book_id='" + book_id + "'")
         cnx.commit()
         message = "Book successfully returned"
      except:
         cnx.rollback()
         message = "Return Failed"
   else:
      message = "Checkout record not found"

   cur.close()
   cnx.close()
   return message

if __name__ == '__main__':
   app.run(debug=False)
