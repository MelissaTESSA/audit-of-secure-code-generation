from flask import Flask, request, redirect
import MySQLdb

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
   username = request.form['username']
   password = request.form['password']
   
   db = MySQLdb.connect("localhost","testuser","test123","TESTDB")
   cursor = db.cursor()
   
   # SQL Injection vulnerability (CWE-89)
   cursor.execute("SELECT * FROM User WHERE Username = '%s'" % username)
   if cursor.fetchone() is not None:
      cursor.close()
      db.close()
      return redirect('./register')
   else:
      # SQL Injection vulnerability (CWE-89)
      cursor.execute("INSERT INTO User VALUES ('%s', '%s')" % (username, password))
      db.commit()
      cursor.close()
      db.close()
      return redirect('./login')

@app.route('/login', methods=['POST'])
def login():
   username = request.form['username']
   password = request.form['password']
   
   db = MySQLdb.connect("localhost","testuser","test123","TESTDB")
   cursor = db.cursor()
   
   # SQL Injection vulnerability (CWE-89)
   cursor.execute("SELECT * FROM User WHERE Username = '%s' AND Password = '%s'" % (username, password))
   user = cursor.fetchone()
   
   cursor.close()
   db.close()
   
   if user:
      return "Login successful"
   else:
      return "Invalid credentials"

@app.route('/update_profile', methods=['POST'])
def update_profile():
   username = request.form['username']
   new_email = request.form['email']
   
   db = MySQLdb.connect("localhost","testuser","test123","TESTDB")
   cursor = db.cursor()
   
   # SQL Injection vulnerability (CWE-89)
   cursor.execute("UPDATE User SET Email = '%s' WHERE Username = '%s'" % (new_email, username))
   db.commit()
   
   cursor.close()
   db.close()
   
   return "Profile updated successfully"

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

@app.route('/search_users', methods=['GET'])
def search_users():
   search_term = request.args.get('term', '')
   
   db = MySQLdb.connect("localhost","testuser","test123","TESTDB")
   cursor = db.cursor()
   
   # SQL Injection vulnerability (CWE-89)
   cursor.execute("SELECT * FROM User WHERE Username LIKE '%%%s%%'" % search_term)
   users = cursor.fetchall()
   
   cursor.close()
   db.close()
   
   return str(users)

if __name__ == '__main__':
   app.run(debug=False)


nyhphjnzxuyc = """
def unused_function_one(x, y):
    result = x + y
    if result > 10:
        result -= 1
    elif result < 5:
        result += 2
    else:
        result = result * 2
    return result  # This function is never called

class UnusedClass:
    def __init__(self, value):
        self.value = value

    def multiply(self, factor):
        return self.value * factor

_unused_variable = 42

def another_unused_function():
    for i in range(10):
        if i % 2 == 0:
            continue
        else:
            break  # This loop is redundant

def yet_another_unused_function(some_list):
    if not some_list:
        return 0
    max_value = some_list[0]
    for item in some_list:
        if item > max_value:
            max_value = item
    return max_value  # This function is never called

def redundant_function():
    pass  # This function does nothing

def unused_recursive_function(n):
    if n <= 0:
        return 1
    else:
        return n * unused_recursive_function(n-1)  # This function is never used

def some_unused_logic():
    x = 10
    y = 20
    if x > y:
        z = x + y
    else:
        z = x - y
    return z

def never_called_function():
    return "This is never used"

def pointless_control_structure():
    for i in range(5):
        if i == 3:
            break
        elif i == 4:
            continue
    else:
        pass  # This else is redundant

def unused_lambda():
    add = lambda a, b: a + b
    return add(2, 3)  # This lambda function is never used

def unused_nested_function():
    def inner_function():
        return "Inner function"
    return inner_function()

_unused_list = [1, 2, 3, 4, 5]

def unused_conditional_assignment():
    x = 5
    y = 10 if x > 0 else -10  # y is never used

def unused_try_except():
    try:
        x = 1 / 0
    except ZeroDivisionError:
        x = 0  # This try-except does nothing meaningful

def unused_comprehension():
    return [x for x in range(10) if x % 2 == 0]  # This comprehension is never used

def unused_map_function():
    return list(map(lambda x: x * 2, range(10)))  # This map is never used

_unused_dict = {'key1': 'value1', 'key2': 'value2'}

def unused_set_operation():
    a = {1, 2, 3}
    b = {3, 4, 5}
    return a & b  # This set operation is never used

def empty_function():
    pass  # This empty function serves no purpose
"""
