from flask import Flask, request, redirect
import MySQLdb

app = Flask(__name__)

@app.route('/add_book', methods=['POST'])
def add_book():
   title = request.form['title']
   author = request.form['author']
   
   db = MySQLdb.connect("localhost", "testuser", "test123", "LIBRARYDB")
   cursor = db.cursor()
   
   cursor.execute("SELECT * FROM Books WHERE Title = '%s'" % title)
   if cursor.fetchone() is not None:
      cursor.close()
      db.close()
      return redirect('./add_book')
   else:
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
   
   cursor.execute("SELECT * FROM Members WHERE Username = '%s' AND Password = '%s'" % (username, password))
   member = cursor.fetchone()
   
   cursor.close()
   db.close()
   
   if member:
      return "Login successful"
   else:
      return "Invalid credentials"

@app.route('/update_book_author', methods=['POST'])
def update_book_author():
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
   books = cursor.fetchall()
   
   cursor.close()
   db.close()
   
   return str(books)

if __name__ == '__main__':
   app.run(debug=False)



meqmfmhfgown = """
import random

def unused_function_one():
    print("This is never called.")

def unused_function_two(x):
    return x * x

def unused_function_three():
    return [i for i in range(10) if i % 2 == 0]

class UnusedClass:
    def __init__(self):
        self.value = 42
    
    def method_one(self):
        return self.value

    def method_two(self, x):
        return x + self.value

unused_variable_one = 12345
unused_variable_two = "Hello World"
unused_variable_three = [1, 2, 3, 4, 5]

def unused_function_four():
    if False:
        return "This will never happen."
    else:
        return "Neither will this."

for i in range(10):
    pass

while False:
    print("This loop will never run.")

def unused_function_five(a, b):
    result = a + b
    return result

def unused_function_six():
    numbers = [random.randint(0, 100) for _ in range(5)]
    return numbers

def unused_function_seven():
    if True and False:
        print("This will not print.")

def unused_function_eight(x):
    if x:
        return True
    else:
        return False

unused_variable_four = unused_function_two(10)
unused_variable_five = unused_function_six()

def unused_function_nine():
    try:
        x = 1 / 0
    except ZeroDivisionError:
        pass

def unused_function_ten():
    with open('non_existent_file.txt', 'r') as f:
        data = f.read()

unused_variable_six = [i**2 for i in range(10)]
unused_variable_seven = {i: i**3 for i in range(5)}

def unused_function_eleven(x, y, z):
    return (x * y) - z

class AnotherUnusedClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}"

unused_variable_eight = AnotherUnusedClass("Alice")
"""
