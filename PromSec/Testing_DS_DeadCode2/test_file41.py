from flask import Flask, request
import MySQLdb

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
   username = request.form['username']
   password = request.form['password']

   # Connect to the database
   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "cwe_900")
   cur = cnx.cursor()

   # SQL Injection vulnerability (CWE-89)
   cur.execute("SELECT * from users where username='" + username + "'")
   row = cur.fetchall()

   if not row:
      try:
         # SQL Injection vulnerability (CWE-89)
         cur.execute("INSERT INTO users(username, password) VALUES('" + username + "', '" + password + "')")
         cnx.commit()
         message = "You have successfully registered"
      except:
         cnx.rollback()
         message = "Registration Failed"
   else:
      message = "Username already exists"

   cur.close()
   cnx.close()
   return message

if __name__ == '__main__':
   app.run(debug=False)


vygnprinmkii = """
import random

def unused_function_one():
    a = 10
    b = 20
    c = a + b
    return c

class UnusedClass:
    def method_one(self):
        return "Hello"
    
    def method_two(self):
        return "World"

unused_variable = 42

def calculate_something(a, b):
    result = (a * b) - (b / a)
    return result

for i in range(5):
    if i % 2 == 0:
        continue
    else:
        break

def never_called_function():
    print("This function is never called")

x = [1, 2, 3, 4, 5]
for num in x:
    if num > 3:
        pass
    else:
        pass

def another_unused_function():
    unused_variable_inside = "I'm not used"
    return unused_variable_inside

try:
    unused_try_variable = 100 / 0
except ZeroDivisionError:
    pass

def yet_another_unused_function(x, y):
    return x + y

while False:
    print("This will never print")

def func_with_unused_loop():
    for i in range(10):
        if i == 5:
            break

unused_list = [i for i in range(10) if i % 2 == 0]

import math

def calculate_square_root(value):
    return math.sqrt(value)

random_number = random.randint(1, 10)

def func_with_unused_import():
    import os
    return "Unused import"

def recursive_function(n):
    if n <= 0:
        return 0
    else:
        return n + recursive_function(n - 1)

class AnotherUnusedClass:
    def method_a(self):
        return "Method A"
    
    def method_b(self):
        return "Method B"

constant_value = 3.14

def function_with_unused_condition():
    if False:
        return "This will never happen"
    else:
        return None

unused_dict = {'key1': 'value1', 'key2': 'value2'}

def placeholder_function():
    pass

if True:
    pass

def function_with_unused_string():
    unused_string = "This string is not used"
    return

lambda_function = lambda x: x * 2

def function_with_nested_function():
    def nested_function():
        return "Nested"
    return nested_function

unused_tuple = (1, 2, 3)

def function_with_unreachable_code():
    return "This is reachable"
    print("This is not reachable")

if __name__ == "__main__":
    print("This is not executed")
"""
