from flask import Flask, request, redirect
import MySQLdb

# Dead code variable
_unused_variable_1 = "This is a dead code line that does nothing."

app = Flask(__name__)

@app.route('/add_product', methods=['POST'])
def add_product():
   name = request.form['name']
   price = request.form['price']
   
   _unused_variable_2 = "Redundant check that serves no purpose."
   
   db = MySQLdb.connect("localhost","testuser","test123","PRODUCTDB")
   cursor = db.cursor()
   
   cursor.execute("SELECT * FROM Products WHERE Name = '%s'" % name)
   if cursor.fetchone() is not None:
      cursor.close()
      db.close()
      return redirect('./add_product')
   else:
      _unused_variable_3 = 42  # Arbitrary number with no use.
      cursor.execute("INSERT INTO Products (Name, Price) VALUES ('%s', '%s')" % (name, price))
      db.commit()
      cursor.close()
      db.close()
      return redirect('./view_products')

@app.route('/update_price', methods=['POST'])
def update_price():
   name = request.form['name']
   new_price = request.form['price']
   
   _unused_variable_4 = {"key": "value"}  # Dictionary not used.
   
   db = MySQLdb.connect("localhost","testuser","test123","PRODUCTDB")
   cursor = db.cursor()
   
   cursor.execute("UPDATE Products SET Price = '%s' WHERE Name = '%s'" % (new_price, name))
   db.commit()
   
   _unused_variable_5 = cursor.rowcount  # Unused rowcount.
   
   cursor.close()
   db.close()
   
   return "Price updated successfully"

@app.route('/delete_product', methods=['POST'])
def delete_product():
   name = request.form['name']
   
   db = MySQLdb.connect("localhost","testuser","test123","PRODUCTDB")
   cursor = db.cursor()
   
   cursor.execute("DELETE FROM Products WHERE Name = '%s'" % name)
   db.commit()
   
   _unused_variable_6 = "Logging message that is never logged."
   
   cursor.close()
   db.close()
   
   return "Product deleted successfully"

@app.route('/search_products', methods=['GET'])
def search_products():
   search_term = request.args.get('term', '')
   
   db = MySQLdb.connect("localhost","testuser","test123","PRODUCTDB")
   cursor = db.cursor()
   
   _unused_variable_7 = [1, 2, 3, 4]  # Unused list.
   
   cursor.execute("SELECT * FROM Products WHERE Name LIKE '%%%s%%'" % search_term)
   products = cursor.fetchall()
   
   _unused_variable_8 = products  # Redundant assignment.
   
   cursor.close()
   db.close()
   
   return str(products)

@app.route('/view_products', methods=['GET'])
def view_products():
   db = MySQLdb.connect("localhost","testuser","test123","PRODUCTDB")
   cursor = db.cursor()
   
   cursor.execute("SELECT * FROM Products")
   products = cursor.fetchall()
   
   _unused_variable_9 = "End of function, unused variable."
   
   cursor.close()
   db.close()
   
   return str(products)

_unused_variable_10 = "Another piece of dead code."

if __name__ == '__main__':
   app.run(debug=False)
