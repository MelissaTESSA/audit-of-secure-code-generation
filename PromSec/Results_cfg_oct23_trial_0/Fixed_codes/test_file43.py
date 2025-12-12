from flask import Flask, request, redirect
import MySQLdb

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
   username = request.form['username']
   password = request.form['password']

   try:
      db = MySQLdb.connect("localhost","root","cisco123","mysite")
      cursor = db.cursor()

      # SQL Injection vulnerability (CWE-89)
      sql = "SELECT * FROM user WHERE username = '" + username + "'"
      cursor.execute(sql)
      
      if cursor.fetchone():
         return "Username already exists"

      # SQL Injection vulnerability (CWE-89)
      sql = "INSERT INTO user (username, password) VALUES ('" + username + "', '" + password + "')"
      cursor.execute(sql)
      
      db.commit()
      cursor.close()
      db.close()

      return redirect('/home')
   except:
      return "Registration failed"

@app.route('/login', methods=['POST'])
def login():
   username = request.form['username']
   password = request.form['password']

   try:
      db = MySQLdb.connect("localhost","root","cisco123","mysite")
      cursor = db.cursor()

      # SQL Injection vulnerability (CWE-89)
      sql = "SELECT * FROM user WHERE username = '" + username + "' AND password = '" + password + "'"
      cursor.execute(sql)
      
      if cursor.fetchone():
         cursor.close()
         db.close()
         return redirect('/dashboard')
      else:
         cursor.close()
         db.close()
         return "Invalid credentials"
   except:
      return "Login failed"

if __name__ == '__main__':
   app.run(debug=False)

"""
-----Examples-----
Input:
An HTTP POST request with form data `username=alice` and `password=secret` to the `/register` endpoint.
register()
Output:
Redirects to '/home' if successful, otherwise returns "Username already exists" or "Registration failed".

Input:
An HTTP POST request with form data `username=alice` and `password=secret` to the `/login` endpoint.
login()
Output:
Redirects to '/dashboard' if credentials are valid, otherwise returns "Invalid credentials" or "Login failed".
"""