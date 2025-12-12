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


dhjyrrwmhrvg = """
def unused_function_one():
    x = 10
    y = 20
    z = x + y
    return z

def unused_function_two(param1, param2):
    result = param1 * param2
    for i in range(5):
        temp = i * result
    return result

class UnusedClass:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1

unused_variable_one = 42
unused_variable_two = "This is a string"
unused_variable_three = [1, 2, 3, 4, 5]

for i in range(10):
    unused_var = i * 2
    if unused_var > 10:
        break

def another_unused_function(arg):
    if arg > 10:
        return "Greater than ten"
    else:
        return "Less than or equal to ten"

try:
    unused_result = 10 / 2
except ZeroDivisionError:
    unused_result = None

with open("unused_file.txt", "w") as f:
    f.write("This is some unused content")

unused_lambda = lambda x: x + 1

def yet_another_unused_function(a, b, c):
    return a + b + c

unused_list_comprehension = [x for x in range(10) if x % 2 == 0]

def unused_recursive_function(n):
    if n <= 0:
        return 0
    else:
        return n + unused_recursive_function(n-1)

unused_set = {1, 2, 3, 4, 5}
unused_dict = {"key1": "value1", "key2": "value2"}

def unused_logic():
    x = 5
    if x > 10:
        y = x * 2
    else:
        y = x / 2

class AnotherUnusedClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}"

unused_tuple = (1, 2, 3, 4, 5)
unused_flag = True

def unused_conditionals():
    if unused_flag:
        return "Flag is true"
    else:
        return "Flag is false"

unused_expression = unused_variable_one * 2

def unused_branching():
    for i in range(5):
        if i % 2 == 0:
            continue
        elif i == 3:
            break
"""
