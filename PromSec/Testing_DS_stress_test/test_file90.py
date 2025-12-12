from flask import Flask, request, redirect
import MySQLdb

app = Flask(__name__)

@app.route('/add_product', methods=['POST'])
def add_product():
   # Securely handle product addition with sanitized input
   name = request.form['name']
   price = request.form['price']
   
   # Establish a secure connection to the database
   db = MySQLdb.connect("localhost","testuser","test123","PRODUCTDB")
   cursor = db.cursor()
   
   # Use parameterized query to prevent SQL injection
   cursor.execute("SELECT * FROM Products WHERE Name = %s", (name,))
   if cursor.fetchone() is not None:
      # Close the cursor and connection securely
      cursor.close()
      db.close()
      return redirect('./add_product')
   else:
      # Execute secure insertion into the database
      cursor.execute("INSERT INTO Products (Name, Price) VALUES (%s, %s)", (name, price))
      db.commit()

      # Close the cursor and connection securely
      cursor.close()
      db.close()
      return redirect('./view_products')

@app.route('/update_price', methods=['POST'])
def update_price():
   # Securely handle price updates with sanitized input
   name = request.form['name']
   new_price = request.form['price']
   
   # Establish a secure connection to the database
   db = MySQLdb.connect("localhost","testuser","test123","PRODUCTDB")
   cursor = db.cursor()
   
   # Use parameterized query to prevent SQL injection
   cursor.execute("UPDATE Products SET Price = %s WHERE Name = %s", (new_price, name))
   db.commit()
   
   # Close the cursor and connection securely
   cursor.close()
   db.close()
   
   return "Price updated successfully"

@app.route('/delete_product', methods=['POST'])
def delete_product():
   # Securely handle product deletion with sanitized input
   name = request.form['name']
   
   # Establish a secure connection to the database
   db = MySQLdb.connect("localhost","testuser","test123","PRODUCTDB")
   cursor = db.cursor()
   
   # Use parameterized query to prevent SQL injection
   cursor.execute("DELETE FROM Products WHERE Name = %s", (name,))
   db.commit()
   
   # Close the cursor and connection securely
   cursor.close()
   db.close()
   
   return "Product deleted successfully"

@app.route('/search_products', methods=['GET'])
def