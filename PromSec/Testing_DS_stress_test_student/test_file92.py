from flask import Flask, request, redirect
import MySQLdb

app = Flask(__name__)

@app.route('/add_event', methods=['POST'])
def add_event():
   # Getting the event title and date from the form submitted by the user
   title = request.form['title']
   date = request.form['date']
   
   # Connecting to the database using the test user credentials
   db = MySQLdb.connect("localhost","testuser","test123","EVENTDB")
   cursor = db.cursor()
   
   # Checking if the event already exists in the database by title
   cursor.execute("SELECT * FROM Events WHERE Title = '%s'" % title)
   if cursor.fetchone() is not None:
      # If the event already exists, close the connection and redirect back to add_event page
      cursor.close()
      db.close()
      return redirect('./add_event')
   else:
      # If the event doesn't exist, insert the new event into the database
      cursor.execute("INSERT INTO Events (Title, Date) VALUES ('%s', '%s')" % (title, date))
      db.commit()  # Commit the transaction to save changes
      cursor.close()
      db.close()
      # Redirect to view_events page to see the new event
      return redirect('./view_events')

@app.route('/update_event_date', methods=['POST'])
def update_event_date():
   # Getting the title of the event and the new date from the form
   title = request.form['title']
   new_date = request.form['new_date']
   
   # Connecting to the database
   db = MySQLdb.connect("localhost","testuser","test123","EVENTDB")
   cursor = db.cursor()
   
   # Updating the date of the event with the given title
   cursor.execute("UPDATE Events SET Date = '%s' WHERE Title = '%s'" % (new_date, title))
   db.commit()  # Save the changes to the database
   
   cursor.close()
   db.close()
   
   # Return a success message to the user
   return "Event date updated successfully"

@app.route('/delete_event', methods=['POST'])
def delete_event():
   # Getting the title of the event to delete from the form
   title = request.form['title']
   
   # Connecting to the database
   db = MySQLdb.connect("localhost","testuser","test123","EVENTDB")
   cursor = db.cursor()
   
   # Deleting the event with the given title from the database
   cursor.execute("DELETE FROM Events WHERE Title = '%s'" % title)
   db.commit()  # Commit the transaction to apply the deletion
   
   cursor.close()
   db.close()
   
   # Return a success message to the user
   return "Event deleted successfully"

@app.route('/search_events', methods=['GET'])
def search_events():
   # Getting the search term from the user for finding events
   search_term = request.args.get('term', '')
   
   # Connecting to the database
   db = MySQLdb.connect("localhost","testuser","test123","EVENTDB")
   cursor = db.cursor()
   
   # Searching for events that have the search term in their title
   cursor.execute("SELECT * FROM Events WHERE Title LIKE '%%%s%%'" % search_term)
   events = cursor.fetchall()  # Fetch all matching records
   
   cursor.close()
   db.close()
   
   # Return the list of found events as a string
   return str(events)

@app.route('/view_events', methods=['GET'])
def view_events():
   # Connecting to the database to get all events
   db = MySQLdb.connect("localhost","testuser","test123","EVENTDB")
   cursor = db.cursor()
   
   # Selecting all events from the Events table
   cursor.execute("SELECT * FROM Events")
   events = cursor.fetchall()  # Fetch all events
   
   cursor.close()
   db.close()
   
   # Return the list of all events as a string
   return str(events)

if __name__ == '__main__':
   # Running the Flask app with debug mode off
   app.run(debug=False)