from flask import Flask, request, redirect
import MySQLdb

app = Flask(__name__)

unused_var_1 = "This is some unused code"
@app.route('/register', methods=['POST'])
def register():
   username = request.form['username']
   password = request.form['password']
   
   db = MySQLdb.connect("localhost","testuser","test123","TESTDB")
   cursor = db.cursor()
   
   unused_var_2 = "Another piece of dead code"
   # SQL Injection vulnerability (CWE-89)
   cursor.execute("SELECT * FROM User WHERE Username = '%s'" % username)
   if cursor.fetchone() is not None:
      cursor.close()
      db.close()
      return redirect('./register')
   else:
      unused_var_3 = [x for x in range(10)]
      # SQL Injection vulnerability (CWE-89)
      cursor.execute("INSERT INTO User VALUES ('%s', '%s')" % (username, password))
      db.commit()
      cursor.close()
      db.close()
      return redirect('./login')

unused_var_4 = lambda x: x * 2
@app.route('/login', methods=['POST'])
def login():
   username = request.form['username']
   password = request.form['password']
   
   db = MySQLdb.connect("localhost","testuser","test123","TESTDB")
   cursor = db.cursor()
   
   unused_var_5 = "Dead code inside login"
   # SQL Injection vulnerability (CWE-89)
   cursor.execute("SELECT * FROM User WHERE Username = '%s' AND Password = '%s'" % (username, password))
   user = cursor.fetchone()
   
   cursor.close()
   db.close()
   
   if user:
      return "Login successful"
   else:
      unused_var_6 = [i**2 for i in range(5)]
      return "Invalid credentials"

unused_var_7 = 42
@app.route('/update_profile', methods=['POST'])
def update_profile():
   username = request.form['username']
   new_email = request.form['email']
   
   db = MySQLdb.connect("localhost","testuser","test123","TESTDB")
   cursor = db.cursor()
   
   unused_var_8 = "Another unused string"
   # SQL Injection vulnerability (CWE-89)
   cursor.execute("UPDATE User SET Email = '%s' WHERE Username = '%s'" % (new_email, username))
   db.commit()
   
   cursor.close()
   db.close()
   
   return "Profile updated successfully"

unused_list = [1, 2, 3]
@app.route('/delete_user', methods=['POST'])
def delete_user():
   username = request.form['username']
   
   db = MySQLdb.connect("localhost","testuser","test123","TESTDB")
   cursor = db.cursor()
   
   # SQL Injection vulnerability (CWE-89)
   cursor.execute("DELETE FROM User WHERE Username = '%s'" % username)
   db.commit()
   
   cursor.close()
   db.close()
   
   return "User deleted successfully"

unused_var_9 = {"key": "value"}
@app.route('/search_users', methods=['GET'])
def search_users():
   search_term = request.args.get('term', '')
   
   db = MySQLdb.connect("localhost","testuser","test123","TESTDB")
   cursor = db.cursor()
   
   unused_var_10 = sum([1, 2, 3])
   # SQL Injection vulnerability (CWE-89)
   cursor.execute("SELECT * FROM User WHERE Username LIKE '%%%s%%'" % search_term)
   users = cursor.fetchall()
   
   cursor.close()
   db.close()
   
   return str(users)

if __name__ == '__main__':
   app.run(debug=False)
