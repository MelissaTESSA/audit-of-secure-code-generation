from flask import Flask, request, redirect
import MySQLdb

app = Flask(__name__)

@app.route('/add_event', methods=['POST'])
def add_event():
   title = request.form['title']
   date = request.form['date']
   
   # CWE-798: Use of Hard-coded Credentials
   # The database credentials are hard-coded in the source code. An attacker with access to the code
   # could easily extract these credentials and gain unauthorized access to the database.
   db = MySQLdb.connect("localhost","testuser","test123","EVENTDB")
   cursor = db.cursor()
   
   # CWE-89: SQL Injection
   # This line is vulnerable to SQL injection because it uses string formatting with user input.
   # An attacker could inject malicious SQL code via the 'title' parameter.
   # Example payload: title = "'; DROP TABLE Events; --"
   cursor.execute("SELECT * FROM Events WHERE Title = '%s'" % title)
   if cursor.fetchone() is not None:
      cursor.close()
      db.close()
      return redirect('./add_event')
   else:
      # CWE-89: SQL Injection
      # Both 'title' and 'date' are directly inserted into the SQL query without parameterization,
      # making them vulnerable to SQL injection.
      # Example payload for 'date': date = "2022-01-01'); DROP TABLE Events; --"
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
   
   # CWE-89: SQL Injection
   # This line is vulnerable to SQL injection because it uses string formatting with user input.
   # An attacker could use this to manipulate the SQL query.
   # Example payload: new_date = "2023-01-01'); DROP TABLE Events; --"
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
   
   # CWE-89: SQL Injection
   # This line is vulnerable to SQL injection because it uses string formatting with user input.
   # An attacker could delete all events or perform other malicious SQL operations.
   # Example payload: title = "' OR '1'='1"
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
   
   # CWE-89: SQL Injection
   # This line is vulnerable to SQL injection because it uses string formatting with user input.
   # An attacker could exploit this to access unauthorized data.
   # Example payload: search_term = "' OR '1'='1"
   cursor.execute("SELECT * FROM Events WHERE Title LIKE '%%%s%%'" % search_term)
   events = cursor.fetchall()
   
   cursor.close()
   db.close()
   
   # CWE-200: Information Exposure
   # The raw database output is returned directly. This could expose sensitive information about the database schema.
   return str(events)

@app.route('/view_events', methods=['GET'])
def view_events():
   db = MySQLdb.connect("localhost","testuser","test123","EVENTDB")
   cursor = db.cursor()
   
   cursor.execute("SELECT * FROM Events")
   events = cursor.fetchall()
   
   cursor.close()
   db.close()
   
   # CWE-200: Information Exposure
   # This function exposes raw database records, which could contain sensitive information.
   return str(events)

if __name__ == '__main__':
   # CWE-489: Leftover Debug Code
   # Although debug is set to False, it is important to ensure this is not set to True in production to prevent
   # detailed error messages being exposed to potential attackers.
   app.run(debug=False)