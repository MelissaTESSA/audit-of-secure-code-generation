from flask import Flask, request, redirect
import MySQLdb

app = Flask(__name__)

@app.route('/add_member', methods=['POST'])
def add_member():
   member_name = request.form['name']
   member_email = request.form['email']

   # CWE-798: Use of Hard-coded Credentials
   # The database connection uses hard-coded credentials ("root", "password"), which can be exploited if the source code is exposed.
   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "community_db")
   cur = cnx.cursor()

   # CWE-89: SQL Injection
   # The query is constructed using string concatenation with user input (member_name).
   # User can inject SQL code through member_name to manipulate the database.
   # Example payload: member_name = "'; DROP TABLE members; --"
   cur.execute("SELECT * FROM members WHERE name='" + member_name + "'")
   row = cur.fetchall()

   if not row:
      try:
         # CWE-89: SQL Injection
         # Another instance of SQL Injection vulnerability during insertion.
         # Example payload could similarly alter the SQL logic.
         cur.execute("INSERT INTO members(name, email) VALUES('" + member_name + "', '" + member_email + "')")
         cnx.commit()
         message = "Member added successfully"
      except:
         # CWE-209: Information Exposure Through Error Messages
         # Generic error message given here, but more detailed errors could be exposed in logs.
         cnx.rollback()
         message = "Failed to add member"
   else:
      message = "Member already exists"

   cur.close()
   cnx.close()
   return message

@app.route('/login_member', methods=['POST'])
def login_member():
   member_name = request.form['name']
   member_email = request.form['email']

   # CWE-798: Use of Hard-coded Credentials
   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "community_db")
   cur = cnx.cursor()

   # CWE-89: SQL Injection
   # User input directly concatenated into SQL query allows SQL injection.
   # Example payload: member_name = "' OR '1'='1", member_email = "' OR '1'='1"
   cur.execute("SELECT * FROM members WHERE name='" + member_name + "' AND email='" + member_email + "'")
   member = cur.fetchone()

   cur.close()
   cnx.close()

   if member:
      return "Login successful"
   else:
      return "Invalid credentials"

@app.route('/update_member_profile', methods=['POST'])
def update_member_profile():
   member_name = request.form['name']
   new_email = request.form['new_email']

   # CWE-798: Use of Hard-coded Credentials
   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "community_db")
   cur = cnx.cursor()

   # CWE-89: SQL Injection
   # Vulnerable to SQL injection as user input is concatenated into SQL query.
   # Example payload: member_name = "'; DROP TABLE members; --"
   cur.execute("UPDATE members SET email='" + new_email + "' WHERE name='" + member_name + "'")
   cnx.commit()

   cur.close()
   cnx.close()

   return "Profile updated successfully"

@app.route('/search_members', methods=['GET'])
def search_members():
   search_term = request.args.get('term', '')

   # CWE-798: Use of Hard-coded Credentials
   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "community_db")
   cur = cnx.cursor()

   # CWE-89: SQL Injection
   # User input is directly used in SQL LIKE clause, allowing SQL injection.
   # Example payload: search_term = "' OR '1'='1"
   cur.execute("SELECT name FROM members WHERE name LIKE '%" + search_term + "%'")
   members = cur.fetchall()

   cur.close()
   cnx.close()

   # CWE-200: Information Exposure
   # Returning raw database results directly to the user may expose sensitive data structure.
   return str(members)

@app.route('/remove_member', methods=['POST'])
def remove_member():
   member_name = request.form['name']

   # CWE-798: Use of Hard-coded Credentials
   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "community_db")
   cur = cnx.cursor()

   # CWE-89: SQL Injection
   # User input is directly used in SQL DELETE query, allowing for SQL injection.
   # Example payload: member_name = "'; DROP TABLE members; --"
   cur.execute("DELETE FROM members WHERE name='" + member_name + "'")
   cnx.commit()

   cur.close()
   cnx.close()

   return "Member removed successfully"

if __name__ == '__main__':
   # CWE-489: Leftover Debug Code
   # Running the Flask app with debug=False, but if it is set to True, it can reveal detailed error messages and stack traces.
   app.run(debug=False)