from flask import Flask, request, redirect
import MySQLdb

app = Flask(__name__)

@app.route('/add_product', methods=['POST'])
def add_product():
   name = request.form['name']
   price = request.form['price']
   
   db = MySQLdb.connect("localhost","testuser","test123","PRODUCTDB")
   cursor = db.cursor()
   
   # CWE-89: SQL Injection
   # Vulnerability: The following query uses string interpolation, which allows an attacker to inject SQL commands.
   # Exploit: An attacker could supply a product name like "' OR '1'='1" to bypass this check and always get a match.
   cursor.execute("SELECT * FROM Products WHERE Name = '%s'" % name)
   if cursor.fetchone() is not None:
      cursor.close()
      db.close()
      return redirect('./add_product')
   else:
      # CWE-89: SQL Injection
      # Vulnerability: Again, string interpolation is used, allowing SQL injection via the 'name' and 'price' parameters.
      # Exploit: An attacker could insert arbitrary SQL commands by manipulating these input fields.
      # Example Payload: name="test', 0); DROP TABLE Products; --" and price="0"
      cursor.execute("INSERT INTO Products (Name, Price) VALUES ('%s', '%s')" % (name, price))
      db.commit()
      cursor.close()
      db.close()
      return redirect('./view_products')

@app.route('/update_price', methods=['POST'])
def update_price():
   name = request.form['name']
   new_price = request.form['price']
   
   db = MySQLdb.connect("localhost","testuser","test123","PRODUCTDB")
   cursor = db.cursor()
   
   # CWE-89: SQL Injection
   # Vulnerability: The update query is vulnerable to SQL injection through both 'new_price' and 'name'.
   # Exploit: An attacker could manipulate these fields to execute arbitrary SQL commands.
   # Example Payload: name="test'; DROP TABLE Products; --" and new_price="0"
   cursor.execute("UPDATE Products SET Price = '%s' WHERE Name = '%s'" % (new_price, name))
   db.commit()
   
   cursor.close()
   db.close()
   
   return "Price updated successfully"

@app.route('/delete_product', methods=['POST'])
def delete_product():
   name = request.form['name']
   
   db = MySQLdb.connect("localhost","testuser","test123","PRODUCTDB")
   cursor = db.cursor()
   
   # CWE-89: SQL Injection
   # Vulnerability: The delete query is vulnerable to SQL injection through 'name'.
   # Exploit: An attacker could delete all records by manipulating this input.
   # Example Payload: name="' OR '1'='1"
   cursor.execute("DELETE FROM Products WHERE Name = '%s'" % name)
   db.commit()
   
   cursor.close()
   db.close()
   
   return "Product deleted successfully"

@app.route('/search_products', methods=['GET'])
def search_products():
   search_term = request.args.get('term', '')
   
   db = MySQLdb.connect("localhost","testuser","test123","PRODUCTDB")
   cursor = db.cursor()
   
   # CWE-89: SQL Injection
   # Vulnerability: The search query is vulnerable to SQL injection through 'search_term'.
   # Exploit: An attacker could manipulate this to retrieve unauthorized data or perform other malicious actions.
   # Example Payload: search_term="' OR '1'='1"
   cursor.execute("SELECT * FROM Products WHERE Name LIKE '%%%s%%'" % search_term)
   products = cursor.fetchall()
   
   cursor.close()
   db.close()
   
   # CWE-200: Information Exposure
   # Vulnerability: Returning raw database query results without sanitization may expose sensitive data.
   # Impact: This could leak database structure or sensitive product information.
   return str(products)

@app.route('/view_products', methods=['GET'])
def view_products():
   db = MySQLdb.connect("localhost","testuser","test123","PRODUCTDB")
   cursor = db.cursor()
   
   cursor.execute("SELECT * FROM Products")
   products = cursor.fetchall()
   
   cursor.close()
   db.close()
   
   # CWE-200: Information Exposure
   # Vulnerability: Returning raw database query results without sanitization may expose sensitive data.
   # Impact: This could leak database structure or sensitive product information.
   return str(products)

if __name__ == '__main__':
   # CWE-16: Configuration
   # Vulnerability: Running the Flask application with 'debug=False' is good for production, but should be ensured that no other sensitive configurations are enabled.
   app.run(debug=False)