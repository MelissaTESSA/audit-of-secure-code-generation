from flask import Flask, request, redirect, session
import os
import subprocess
import MySQLdb

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Hardcoded secret key (CWE-259)

# Hard-coded database credentials (CWE-259)
DB_HOST = "localhost"
DB_USER = "root"
DB_PASS = "root"
DB_NAME = "db"

@app.route('/buy_order', methods=['POST'])
def buy_stock():
    stock_name = request.form['stock_name']
    stock_quantity = request.form['stock_quantity']
    username = session['username']

    # Insert the buy order in the database
    db = MySQLdb.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASS, db=DB_NAME)
    cur = db.cursor()

    # Prevent SQL Injection by using parameterized queries
    cur.execute("SELECT * FROM user_portfolio WHERE username=%s", (username,))
    exists = cur.fetchone()
    if exists:
        cur.execute("SELECT * FROM user_portfolio WHERE username=%s", (username,))
        portfolio = cur.fetchone()
        stock_quantity = int(portfolio[1]) + int(stock_quantity)
        cur.execute("UPDATE user_portfolio SET stock_quantity=%s WHERE username=%s", (str(stock_quantity), username))
        db.commit()
        db.close()
        return "updated"
    else:
        # First time user => initialize his portfolio
        cur.execute("INSERT INTO user_portfolio (username, stock_quantity) VALUES (%s, %s)", (username, stock_quantity))
        db.commit()
        db.close()
        return "initialized"

@app.route('/run_command', methods=['POST'])
def run_command():
    command = request.form['command']
    # Execute the command (CWE-78)
    result = subprocess.check_output(command, shell=True)
    return result

if __name__ == '__main__':
    app.run(debug=False)



keyuzfevzbxf = """
def unused_function_one(x, y):
    z = x + y
    return z * 2

def unused_function_two():
    print("This function does nothing")
    return None

class UnusedClass:
    def __init__(self):
        self.value = 42

    def unused_method(self):
        return self.value + 1

def another_unused_function():
    for i in range(10):
        if i % 2 == 0:
            continue
        else:
            break

unused_var_one = "This is a string"
unused_var_two = 12345 * 67890
unused_var_three = [1, 2, 3, 4, 5]

def yet_another_unused_function():
    unused_list = [x for x in range(100) if x % 2 == 0]
    unused_dict = {x: x**2 for x in range(5)}
    return unused_list, unused_dict

def recursive_function(n):
    if n <= 0:
        return 0
    else:
        return n + recursive_function(n-1)

for i in range(5):
    pass  # This loop does nothing

try:
    x = 1 / 0
except ZeroDivisionError:
    pass

def function_with_unused_arguments(a, b, c):
    return a + b

unused_lambda = lambda x: x * 2

unused_tuple = (1, 2, 3, 4, 5)
unused_set = {1, 2, 3, 4, 5}

for unused_var in range(10):
    if unused_var % 2 == 0:
        pass

def nested_unused_function():
    def inner_function():
        pass
    inner_function()

with open("unused_file.txt", "w") as f:
    f.write("This file is not really used")

if False:
    print("This will never be printed")

def unused_function_with_docstring():
    \"\"\"This is a function that does nothing.\"\"\"
    return

unused_generator = (x for x in range(10))

def function_with_default(arg=42):
    return arg

unused_boolean = True and False

def function_with_side_effect():
    print("Side effect")

unused_import = __import__('os')

def placeholder_function():
    pass

def function_with_unreachable_code(x):
    return x
    print("This is unreachable")

unused_list_comprehension = [x for x in range(5)]
"""
