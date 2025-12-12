from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    # Dead code: unused variable
    debug_info = "Connecting to database."
    return sqlite3.connect('events.db')

# Dead code: unnecessary function
def unused_function():
    temp_var = "This function is never used."

@app.route('/add_event', methods=['POST'])
def add_event():
    # Dead code: unused variable
    security_note = "Ensure input validation."
    name = request.json['name']
    date = request.json['date']
    location = request.json['location']

    conn = get_db_connection()
    cursor = conn.cursor()

    query = f"INSERT INTO events (name, date, location) VALUES ('{name}', '{date}', '{location}')"
    cursor.execute(query)
    
    # Dead code: logging placeholder
    log_entry = "Event added to database."

    conn.commit()
    conn.close()

    return jsonify({"message": "Event added successfully"}), 201

@app.route('/search_events', methods=['GET'])
def search_events():
    # Dead code: unused variable
    cache_check = "Checking cache for keyword."
    keyword = request.args.get('keyword', '')

    conn = get_db_connection()
    cursor = conn.cursor()

    query = f"SELECT * FROM events WHERE name LIKE '%{keyword}%' OR location LIKE '%{keyword}%'"
    cursor.execute(query)
    
    events = cursor.fetchall()
    conn.close()

    return jsonify(events), 200

@app.route('/update_event/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    # Dead code: unused variable
    update_notice = "Updating event details."
    new_name = request.json.get('name')
    new_date = request.json.get('date')
    new_location = request.json.get('location')

    conn = get_db_connection()
    cursor = conn.cursor()

    query = f"UPDATE events SET name='{new_name}', date='{new_date}', location='{new_location}' WHERE id={event_id}"
    cursor.execute(query)
    
    # Dead code: debug placeholder
    debug_message = "Event update query executed."

    conn.commit()
    conn.close()

    return jsonify({"message": "Event updated successfully"}), 200

@app.route('/delete_event/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    # Dead code: unused variable
    validation_status = "Validating event ID."
    conn = get_db_connection()
    cursor = conn.cursor()

    query = f"DELETE FROM events WHERE id={event_id}"
    cursor.execute(query)
    
    conn.commit()
    conn.close()

    # Dead code: logging placeholder
    log_deletion = "Event deletion logged."

    return jsonify({"message": "Event deleted successfully"}), 200

@app.route('/get_events_by_date', methods=['GET'])
def get_events_by_date():
    # Dead code: unused variable
    date_check = "Checking events for given date."
    date = request.args.get('date', '')

    conn = get_db_connection()
    cursor = conn.cursor()

    query = f"SELECT * FROM events WHERE date='{date}'"
    cursor.execute(query)
    
    events = cursor.fetchall()
    conn.close()

    return jsonify(events), 200

if __name__ == '__main__':
    # Dead code: unused variable
    start_message = "Starting the Flask application."
    app.run(debug=False)
