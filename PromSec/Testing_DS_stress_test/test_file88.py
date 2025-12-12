from flask import Flask, request, redirect
import MySQLdb

app = Flask(__name__)

@app.route('/add_member', methods=['POST'])
def add_member():
   member_name = request.form['name']
   member_email = request.form['email']

   # Securely connecting to the database
   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "community_db")
   cur = cnx.cursor()

   # Using parameterized queries to prevent SQL injection
   cur.execute("SELECT * FROM members WHERE name=%s", (member_name,))
   row = cur.fetchall()

   if not row:
      try:
         # Using parameterized queries for secure insertion
         cur.execute("INSERT INTO members(name, email) VALUES(%s, %s)", (member_name, member_email))
         cnx.commit()
         message = "Member added successfully"
      except:
         # Proper transaction handling for database integrity
         cnx.rollback()
         message = "Failed to add member"
   else:
      message = "Member already exists"

   # Ensure resources are closed to prevent leaks
   cur.close()
   cnx.close()
   return message

@app.route('/login_member', methods=['POST'])
def login_member():
   member_name = request.form['name']
   member_email = request.form['email']

   # Securely connecting to the database
   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "community_db")
   cur = cnx.cursor()

   # Using parameterized queries to prevent SQL injection
   cur.execute("SELECT * FROM members WHERE name=%s AND email=%s", (member_name, member_email))
   member = cur.fetchone()

   # Ensure resources are closed to prevent leaks
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

   # Securely connecting to the database
   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "community_db")
   cur = cnx.cursor()

   # Using parameterized queries to update records securely
   cur.execute("UPDATE members SET email=%s WHERE name=%s", (new_email, member_name))
   cnx.commit()  # Committing the transaction for data integrity
   cur.close()
   cnx.close()
   return "Profile updated successfully"