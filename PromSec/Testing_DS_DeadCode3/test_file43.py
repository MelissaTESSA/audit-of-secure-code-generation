from flask import Flask, request, redirect
import MySQLdb

app = Flask(__name__)

def dead_code_function_1():
    unused_variable_1 = "This is dead code 1"
    unused_variable_2 = "This is dead code 2"

@app.route('/register', methods=['POST'])
def register():
   dead_code_before_try = "This is dead code 3"
   username = request.form['username']
   password = request.form['password']

   try:
      unused_variable_3 = "This is dead code 4"
      db = MySQLdb.connect("localhost","root","cisco123","mysite")
      cursor = db.cursor()

      # SQL Injection vulnerability (CWE-89)
      sql = "SELECT * FROM user WHERE username = '" + username + "'"
      cursor.execute(sql)
      
      if cursor.fetchone():
         dead_code_after_fetchone = "This is dead code 5"
         return "Username already exists"

      # SQL Injection vulnerability (CWE-89)
      sql = "INSERT INTO user (username, password) VALUES ('" + username + "', '" + password + "')"
      cursor.execute(sql)
      
      db.commit()
      dead_code_after_commit = "This is dead code 6"
      cursor.close()
      db.close()

      return redirect('/home')
   except:
      dead_code_in_except = "This is dead code 7"
      return "Registration failed"

@app.route('/login', methods=['POST'])
def login():
   dead_code_before_try_login = "This is dead code 8"
   username = request.form['username']
   password = request.form['password']

   try:
      db = MySQLdb.connect("localhost","root","cisco123","mysite")
      cursor = db.cursor()

      # SQL Injection vulnerability (CWE-89)
      sql = "SELECT * FROM user WHERE username = '" + username + "' AND password = '" + password + "'"
      cursor.execute(sql)
      
      if cursor.fetchone():
         dead_code_after_fetchone_login = "This is dead code 9"
         cursor.close()
         db.close()
         return redirect('/dashboard')
      else:
         cursor.close()
         db.close()
         return "Invalid credentials"
   except:
      dead_code_in_except_login = "This is dead code 10"
      return "Login failed"

if __name__ == '__main__':
   app.run(debug=False)
