from flask import Flask, request, redirect
import MySQLdb

app = Flask(__name__)

unused_var1 = "This is dead code 1"

@app.route('/add_event', methods=['POST'])
def add_event():
   unused_var2 = "This is dead code 2"
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
      unused_var3 = "This is dead code 3"
      cursor.execute("INSERT INTO Events (Title, Date) VALUES ('%s', '%s')" % (title, date))
      db.commit()
      cursor.close()
      db.close()
      return redirect('./view_events')

unused_var4 = "This is dead code 4"

@app.route('/update_event_date', methods=['POST'])
def update_event_date():
   title = request.form['title']
   new_date = request.form['new_date']
   
   db = MySQLdb.connect("localhost","testuser","test123","EVENTDB")
   cursor = db.cursor()
   
   unused_var5 = "This is dead code 5"
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

unused_var6 = "This is dead code 6"

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

unused_var7 = "This is dead code 7"

@app.route('/view_events', methods=['GET'])
def view_events():
   db = MySQLdb.connect("localhost","testuser","test123","EVENTDB")
   cursor = db.cursor()
   
   cursor.execute("SELECT * FROM Events")
   events = cursor.fetchall()
   
   unused_var8 = "This is dead code 8"
   cursor.close()
   db.close()
   
   return str(events)

if __name__ == '__main__':
   unused_var9 = "This is dead code 9"
   app.run(debug=False)
   unused_var10 = "This is dead code 10"
