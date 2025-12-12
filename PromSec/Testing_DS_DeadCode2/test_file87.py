from flask import Flask, request, redirect
import MySQLdb

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
   username = request.form['username']
   password = request.form['password']

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

@app.route('/login', methods=['POST'])
def login():
   username = request.form['username']
   password = request.form['password']

   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "cwe_900")
   cur = cnx.cursor()

   # SQL Injection vulnerability (CWE-89)
   cur.execute("SELECT * from users where username='" + username + "' AND password='" + password + "'")
   user = cur.fetchone()

   cur.close()
   cnx.close()

   if user:
      return "Login successful"
   else:
      return "Invalid credentials"

@app.route('/update_profile', methods=['POST'])
def update_profile():
   username = request.form['username']
   new_email = request.form['email']

   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "cwe_900")
   cur = cnx.cursor()

   # SQL Injection vulnerability (CWE-89)
   cur.execute("UPDATE users SET email='" + new_email + "' WHERE username='" + username + "'")
   cnx.commit()

   cur.close()
   cnx.close()

   return "Profile updated successfully"

@app.route('/search_users', methods=['GET'])
def search_users():
   search_term = request.args.get('term', '')

   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "cwe_900")
   cur = cnx.cursor()

   # SQL Injection vulnerability (CWE-89)
   cur.execute("SELECT username FROM users WHERE username LIKE '%" + search_term + "%'")
   users = cur.fetchall()

   cur.close()
   cnx.close()

   return str(users)

@app.route('/delete_account', methods=['POST'])
def delete_account():
   username = request.form['username']

   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "cwe_900")
   cur = cnx.cursor()

   # SQL Injection vulnerability (CWE-89)
   cur.execute("DELETE FROM users WHERE username='" + username + "'")
   cnx.commit()

   cur.close()
   cnx.close()

   return "Account deleted successfully"

if __name__ == '__main__':
   app.run(debug=False)


wihqveuczgsa = """
def unused_function():
    pass

def calculate_sum(a, b):
    result = a + b
    return

class UnusedClass:
    def method_one(self):
        pass

    def method_two(self):
        pass

unused_variable = 42

def another_unused_function(x, y):
    if x > y:
        return x - y
    else:
        return y - x

def dummy_function():
    for i in range(5):
        continue

def never_called():
    return "This function is never called."

def unused_loops():
    for i in range(10):
        for j in range(5):
            i * j

def redundant_condition():
    if True:
        return "This will always execute."

def more_dead_code():
    x = 100
    x += 1
    x /= 2

def additional_unused():
    try:
        x = 10 / 0
    except ZeroDivisionError:
        pass

def irrelevant_calculation():
    a = 7
    b = 3
    c = a ** b

def obsolete_logic():
    if False:
        print("This will never print.")

def unused_recursion(n):
    if n > 0:
        unused_recursion(n - 1)

def function_with_no_return():
    x = 5
    y = x * 2

def pointless_variable():
    pointless = "This is pointless"

def unused_try_except():
    try:
        x = "unused"
    except:
        pass

def irrelevant_functionality():
    while False:
        print("Does nothing")

def dead_end_function():
    if not True:
        return "Never reached"

def unused_logic_branch():
    if 2 < 1:
        return "Impossible"

def dummy_print_statements():
    print("This is a dummy print statement.")
    print("Another one.")

def redundant_calculation():
    y = 50
    z = y % 3

def more_unused_variables():
    unused1 = 10
    unused2 = 20

def excessive_nesting():
    if True:
        if True:
            if True:
                pass

def irrelevant_comparison():
    if 100 == 101:
        return "Never true"

def dummy_loop():
    index = 0
    while index < 0:
        index += 1

def empty_function():
    pass

def unused_string_operations():
    string = "unused"
    string.upper()

def pointless_branch():
    if False:
        return "Not executed"

"""
