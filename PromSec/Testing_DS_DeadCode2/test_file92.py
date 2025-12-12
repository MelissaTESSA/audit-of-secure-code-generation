from flask import Flask, request, redirect
import MySQLdb

app = Flask(__name__)

@app.route('/add_event', methods=['POST'])
def add_event():
   title = request.form['title']
   date = request.form['date']
   
   db = MySQLdb.connect("localhost","testuser","test123","EVENTDB")
   cursor = db.cursor()
   
   cursor.execute("SELECT * FROM Events WHERE Title = '%s'" % title)
   if cursor.fetchone() is not None:
      cursor.close()
      db.close()
      return redirect('./add_event')
   else:
      cursor.execute("INSERT INTO Events (Title, Date) VALUES ('%s', '%s')" % (title, date))
      db.commit()
      cursor.close()
      db.close()
      return redirect('./view_events')

@app.route('/update_event_date', methods=['POST'])
def update_event_date():
   title = request.form['title']
   new_date = request.form['new_date']
   
   db = MySQLdb.connect("localhost","testuser","test123","EVENTDB")
   cursor = db.cursor()
   
   cursor.execute("UPDATE Events SET Date = '%s' WHERE Title = '%s'" % (new_date, title))
   db.commit()
   
   cursor.close()
   db.close()
   
   return "Event date updated successfully"

@app.route('/delete_event', methods=['POST'])
def delete_event():
   title = request.form['title']
   
   db = MySQLdb.connect("localhost","testuser","test123","EVENTDB")
   cursor = db.cursor()
   
   cursor.execute("DELETE FROM Events WHERE Title = '%s'" % title)
   db.commit()
   
   cursor.close()
   db.close()
   
   return "Event deleted successfully"

@app.route('/search_events', methods=['GET'])
def search_events():
   search_term = request.args.get('term', '')
   
   db = MySQLdb.connect("localhost","testuser","test123","EVENTDB")
   cursor = db.cursor()
   
   cursor.execute("SELECT * FROM Events WHERE Title LIKE '%%%s%%'" % search_term)
   events = cursor.fetchall()
   
   cursor.close()
   db.close()
   
   return str(events)

@app.route('/view_events', methods=['GET'])
def view_events():
   db = MySQLdb.connect("localhost","testuser","test123","EVENTDB")
   cursor = db.cursor()
   
   cursor.execute("SELECT * FROM Events")
   events = cursor.fetchall()
   
   cursor.close()
   db.close()
   
   return str(events)

if __name__ == '__main__':
   app.run(debug=False)



pvcmqzwvlsbm = """
def unused_function():
    x = 5
    y = 10
    z = x + y
    return z

class UnusedClass:
    def __init__(self):
        self.value = 42

    def unused_method(self):
        result = self.value * 2
        return result

def another_unused_function(a, b):
    c = a * b
    return c

x = 100
y = 200
z = x + y

if False:
    print("This will never be printed")

for i in range(10):
    pass

def yet_another_unused_function():
    a = 3
    b = 4
    return a + b

unused_list = [1, 2, 3, 4, 5]
unused_dict = {'a': 1, 'b': 2}

def unused_conditional():
    if 1 > 2:
        return "Impossible"
    else:
        return "This will never happen"

def unused_loop():
    for i in range(5):
        if i == 3:
            break

def unused_complex_function(x, y, z):
    if x > y:
        if y > z:
            return x
        else:
            return z
    else:
        return y

class AnotherUnusedClass:
    def __init__(self):
        self.data = "unused"

def more_unused_code():
    x = 20
    y = 30
    if x < y:
        return x
    else:
        return y

def recursion_example(n):
    if n <= 0:
        return 0
    else:
        return n + recursion_example(n-1)

unused_variable = 12345
another_unused_variable = "hello"

def function_with_unused_loop():
    for i in range(10):
        for j in range(10):
            break

def function_with_unused_try():
    try:
        x = 1 / 0
    except ZeroDivisionError:
        pass
"""
