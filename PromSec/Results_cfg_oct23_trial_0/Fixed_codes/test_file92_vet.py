import os
from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

db = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME
)
cursor = db.cursor()

@app.route('/add_event', methods=['POST'])
def add_event():
    data = request.get_json()
    title = data['title']
    date = data['date']
    
    query = "INSERT INTO events (title, date) VALUES (%s, %s)"
    cursor.execute(query, (title, date))
    db.commit()
    
    return jsonify({'message': 'Event added successfully'})

@app.route('/update_event', methods=['POST'])
def update_event():
    data = request.get_json()
    event_id = data['id']
    new_date = data['date']
    
    query = "UPDATE events SET date = %s WHERE id = %s"
    cursor.execute(query, (new_date, event_id))
    db.commit()
    
    return jsonify({'message': 'Event date updated successfully'})

@app.route('/delete_event', methods=['POST'])
def delete_event():
    data = request.get_json()
    event_id = data['id']
    
    query = "DELETE FROM events WHERE id = %s"
    cursor.execute(query, (event_id,))
    db.commit()
    
    return jsonify({'message': 'Event deleted successfully'})

@app.route('/search_events', methods=['GET'])
def search_events():
    term = request.args.get('term')
    
    query = "SELECT * FROM events WHERE title LIKE %s"
    cursor.execute(query, ('%' + term + '%',))
    result = cursor.fetchall()
    
    return jsonify({'events': result})

@app.route('/view_events', methods=['GET'])
def view_events():
    query = "SELECT * FROM events"
    cursor.execute(query)
    result = cursor.fetchall()
    
    return jsonify({'events': result})

if __name__ == '__main__':
    app.run()