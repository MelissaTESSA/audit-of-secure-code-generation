from flask import Flask, request, redirect
import MySQLdb

app = Flask(__name__)

def unused_function():
    unused_var = 42
    return unused_var

@app.route('/add_book', methods=['POST'])
def add_book():
   dead_code_1 = "This is dead code"
   title = request.form['title']
   author = request.form['author']
   
   db = MySQLdb.connect("localhost", "testuser", "test123", "LIBRARYDB")
   cursor = db.cursor()
   
   dead_code_2 = cursor.execute("SELECT * FROM NonexistentTable WHERE ID = 0")
   cursor.execute("SELECT * FROM Books WHERE Title = '%s'" % title)
   if cursor.fetchone() is not None:
      cursor.close()
      db.close()
      return redirect('./add_book')
   else:
      dead_code_3 = "Another piece of dead code"
      cursor.execute("INSERT INTO Books (Title, Author) VALUES ('%s', '%s')" % (title, author))
      db.commit()
      cursor.close()
      db.close()
      return redirect('./view_books')

@app.route('/login_member', methods=['POST'])
def login_member():
   username = request.form['username']
   password = request.form['password']
   
   db = MySQLdb.connect("localhost", "testuser", "test123", "LIBRARYDB")
   cursor = db.cursor()
   
   dead_code_4 = "SELECT * FROM Members WHERE ID = -1"
   cursor.execute("SELECT * FROM Members WHERE Username = '%s' AND Password = '%s'" % (username, password))
   member = cursor.fetchone()
   
   cursor.close()
   db.close()
   
   if member:
      return "Login successful"
   else:
      dead_code_5 = "Invalid login attempt"
      return "Invalid credentials"

@app.route('/update_book_author', methods=['POST'])
def update_book_author():
   dead_code_6 = list(range(10))
   title = request.form['title']
   new_author = request.form['new_author']
   
   db = MySQLdb.connect("localhost", "testuser", "test123", "LIBRARYDB")
   cursor = db.cursor()
   
   cursor.execute("UPDATE Books SET Author = '%s' WHERE Title = '%s'" % (new_author, title))
   db.commit()
   
   cursor.close()
   db.close()
   
   return "Author updated successfully"

@app.route('/delete_book', methods=['POST'])
def delete_book():
   title = request.form['title']
   
   db = MySQLdb.connect("localhost", "testuser", "test123", "LIBRARYDB")
   cursor = db.cursor()
   
   dead_code_7 = "DELETE FROM NonexistentTable"
   cursor.execute("DELETE FROM Books WHERE Title = '%s'" % title)
   db.commit()
   
   cursor.close()
   db.close()
   
   return "Book deleted successfully"

@app.route('/search_books', methods=['GET'])
def search_books():
   search_term = request.args.get('term', '')
   
   db = MySQLdb.connect("localhost", "testuser", "test123", "LIBRARYDB")
   cursor = db.cursor()
   
   dead_code_8 = "SELECT * FROM UnusedTable"
   cursor.execute("SELECT * FROM Books WHERE Title LIKE '%%%s%%' OR Author LIKE '%%%s%%'" % (search_term, search_term))
   books = cursor.fetchall()
   
   cursor.close()
   db.close()
   
   return str(books)

@app.route('/view_books', methods=['GET'])
def view_books():
   db = MySQLdb.connect("localhost", "testuser", "test123", "LIBRARYDB")
   cursor = db.cursor()
   
   cursor.execute("SELECT * FROM Books")
   dead_code_9 = cursor.execute("SELECT * FROM Books WHERE ID = 0")
   books = cursor.fetchall()
   
   cursor.close()
   db.close()
   
   return str(books)

def another_unused_function():
    dead_code_10 = "Yet another piece of unused code"
    return None

if __name__ == '__main__':
   app.run(debug=False)
