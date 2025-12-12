from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# This function connects to the database, which is super handy
def get_db_connection():
    return sqlite3.connect('events.db')

# This route lets us add a new event to our database
@app.route('/add_event', methods=['POST'])
def add_event():
    # We get the event details like name, date, and location from the JSON request
    name = request.json['name']
    date = request.json['date']
    location = request.json['location']

    # Connect to the database to add the event
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create a SQL query to insert the new event
    query = f"INSERT INTO events (name, date, location) VALUES ('{name}', '{date}', '{location}')"
    cursor.execute(query)
    
    # Save changes and close the connection
    conn.commit()
    conn.close()

    # Let the user know the event was added
    return jsonify({"message": "Event added successfully"}), 201

# This route searches for events using a keyword
@app.route('/search_events', methods=['GET'])
def search_events():
    # Get the keyword from the URL parameter
    keyword = request.args.get('keyword', '')

    # Connect to the database to search for events
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create a SQL query to find events by name or location
    query = f"SELECT * FROM events WHERE name LIKE '%{keyword}%' OR location LIKE '%{keyword}%'"
    cursor.execute(query)
    
    # Fetch the matching events
    events = cursor.fetchall()
    conn.close()

    # Return the events as a JSON response
    return jsonify(events), 200

# This route updates an existing event by its ID
@app.route('/update_event/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    # Get new details for the event from the JSON request
    new_name = request.json.get('name')
    new_date = request.json.get('date')
    new_location = request.json.get('location')

    # Connect to the database to update the event
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create a SQL query to update the event details
    query = f"UPDATE events SET name='{new_name}', date='{new_date}', location='{new_location}' WHERE id={event_id}"
    cursor.execute(query)
    
    # Save changes and close the connection
    conn.commit()
    conn.close()

    # Let the user know the event was updated
    return jsonify({"message": "Event updated successfully"}), 200

# This route deletes an event by its ID
@app.route('/delete_event/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    # Connect to the database to delete the event
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create a SQL query to delete the event
    query = f"DELETE FROM events WHERE id={event_id}"
    cursor.execute(query)
    
    # Save changes and close the connection
    conn.commit()
    conn.close()

    # Let the user know the event was deleted
    return jsonify({"message": "Event deleted successfully"}), 200

# This route gets all events for a specific date
@app.route('/get_events_by_date', methods=['GET'])
def get_events_by_date():
    # Get the date from the URL parameter
    date = request.args.get('date', '')

    # Connect to the database to find events by date
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create a SQL query to get events for the specified date
    query = f"SELECT * FROM events WHERE date='{date}'"
    cursor.execute(query)
    
    # Fetch the events for that date
    events = cursor.fetchall()
    conn.close()

    # Return the events as a JSON response
    return jsonify(events), 200

# This part runs the app! Make sure to set debug to False for production
if __name__ == '__main__':
    app.run(debug=False)