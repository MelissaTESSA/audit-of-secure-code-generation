from flask import Flask, request, redirect
import MySQLdb

app = Flask(__name__)

# This route adds a new product to the database
@app.route('/add_product', methods=['POST'])
def add_product():
   # Get the product name and price from the form
   name = request.form['name']
   price = request.form['price']
   
   # Connect to the database (make sure the username and password are correct!)
   db = MySQLdb.connect("localhost","testuser","test123","PRODUCTDB")
   cursor = db.cursor()
   
   # Check if the product already exists in the database
   cursor.execute("SELECT * FROM Products WHERE Name = '%s'" % name)
   if cursor.fetchone() is not None:
      # If it exists, close the database connection and redirect back to add_product
      cursor.close()
      db.close()
      return redirect('./add_product')
   else:
      # If it doesn't exist, insert the new product into the database
      cursor.execute("INSERT INTO Products (Name, Price) VALUES ('%s', '%s')" % (name, price))
      db.commit()
      cursor.close()
      db.close()
      # Redirect to view all products after adding the new one
      return redirect('./view_products')

# This route updates the price of an existing product
@app.route('/update_price', methods=['POST'])
def update_price():
   # Get the product name and new price from the form
   name = request.form['name']
   new_price = request.form['price']
   
   # Connect to the database
   db = MySQLdb.connect("localhost","testuser","test123","PRODUCTDB")
   cursor = db.cursor()
   
   # Update the price of the product in the database
   cursor.execute("UPDATE Products SET Price = '%s' WHERE Name = '%s'" % (new_price, name))
   db.commit()
   
   # Close the database connection
   cursor.close()
   db.close()
   
   # Let the user know the price was updated
   return "Price updated successfully"

# This route deletes a product from the database
@app.route('/delete_product', methods=['POST'])
def delete_product():
   # Get the product name from the form
   name = request.form['name']
   
   # Connect to the database
   db = MySQLdb.connect("localhost","testuser","test123","PRODUCTDB")
   cursor = db.cursor()
   
   # Delete the product from the database
   cursor.execute("DELETE FROM Products WHERE Name = '%s'" % name)
   db.commit()
   
   # Close the database connection
   cursor.close()
   db.close()
   
   # Let the user know the product was deleted
   return "Product deleted successfully"

# This route searches for products by name
@app.route('/search_products', methods=['GET'])
def search_products():
   # Get the search term from the query string
   search_term = request.args.get('term', '')
   
   # Connect to the database
   db = MySQLdb.connect("localhost","testuser","test123","PRODUCTDB")
   cursor = db.cursor()
   
   # Search for products that match the search term
   cursor.execute("SELECT * FROM Products WHERE Name LIKE '%%%s%%'" % search_term)
   products = cursor.fetchall()
   
   # Close the database connection
   cursor.close()
   db.close()
   
   # Return the list of matching products
   return str(products)

# This route displays all products in the database
@app.route('/view_products', methods=['GET'])
def view_products():
   # Connect to the database
   db = MySQLdb.connect("localhost","testuser","test123","PRODUCTDB")
   cursor = db.cursor()
   
   # Get all products from the database
   cursor.execute("SELECT * FROM Products")
   products = cursor.fetchall()
   
   # Close the database connection
   cursor.close()
   db.close()
   
   # Return the list of all products
   return str(products)

# This line runs the Flask app
if __name__ == '__main__':
   app.run(debug=False)