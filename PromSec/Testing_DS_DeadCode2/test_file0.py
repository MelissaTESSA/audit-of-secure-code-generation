from flask import Flask, request, redirect
import MySQLdb
import hashlib
import os

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
   username = request.form['username']
   password = request.form['password']
   
   # hash the password
   salt = os.urandom(16)
   hashed_password = hashlib.sha256(salt + password.encode('utf-8')).hexdigest()
   
   # check if user already exists
   db = MySQLdb.connect("localhost", "root", "", "testdb")
   cursor = db.cursor()
   
   # SQL Injection vulnerability (CWE-89)
   sql = "SELECT username FROM users WHERE username = '" + username + "'"
   cursor.execute(sql)
   data = cursor.fetchall()
   
   if data:
      db.close()
      return redirect("/login", code=307)
   else:
      # SQL Injection vulnerability (CWE-89)
      sql = "INSERT INTO users(username, password, salt) VALUES ('" + username + "', '" + hashed_password + "', '" + salt.hex() + "')"
      cursor.execute(sql)
      db.commit()
      db.close()
      return "Registration successful"

if __name__ == '__main__':
    app.run(debug=False)


vzsiqkhrydhn = """
def unused_function_one():
    a = 10
    b = 20
    return a + b

def another_unused_function(param1):
    if param1 > 10:
        return "Greater than ten"
    else:
        return "Less than or equal to ten"

class UnusedClass:
    def __init__(self, value):
        self.value = value

    def unused_method(self):
        return self.value * 2

unused_var1 = 42
unused_var2 = "This is a string that is not used anywhere"

def yet_another_unused_function(param2):
    for i in range(5):
        if i == param2:
            break
    return i

if False:
    print("This will never be printed")

try:
    result = 10 / 0
except ZeroDivisionError:
    pass

def function_with_no_side_effects(x, y):
    z = x + y
    return z

def unused_recursive_function(n):
    if n <= 0:
        return 1
    else:
        return n * unused_recursive_function(n-1)

for unused_i in range(10):
    pass

def unused_lambda():
    unused = lambda x: x + x

unused_dict = {'key1': 'value1', 'key2': 'value2'}

def function_with_unreachable_code(x):
    if x > 0:
        return x
    return -x
    print("Unreachable code")

unused_list = [1, 2, 3, 4, 5]

def function_with_unused_parameter(unused_param):
    return "Hello, world"

unused_set = {1, 2, 3, 4, 5}

def function_with_no_return():
    x = 5

class AnotherUnusedClass:
    def method(self):
        pass

def function_with_unused_local_variable():
    unused_local = 100
    return "Nothing to see here"

unused_tuple = (1, 2, 3, 4, 5)

while False:
    print("This won't print")

def function_with_unused_inner_function():
    def inner_function():
        return "Inner function"
    
    return "Outer function"

unused_flag = True and False

def function_with_unused_try_except():
    try:
        raise ValueError("This error is never caught")
    except ValueError:
        pass
"""

