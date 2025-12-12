import os
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

DB_PATH = os.getenv('DB_PATH')

def create_connection():
    conn = sqlite3.connect(DB_PATH)
    return conn

@app.route('/add_event', methods=['POST'])
def add_event():
    conn = create_connection()
    cursor = conn.cursor()
    data = request.get_json()
    cursor.execute("INSERT INTO events (name, date) VALUES (?, ?)", (data['name'], data['date']))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Event added successfully'})

@app.route('/search_event', methods=['GET'])
def search_event():
    conn = create_connection()
    cursor = conn.cursor()
    date = request.args.get('date')
    cursor.execute("SELECT * FROM events WHERE date=?", (date,))
    events = cursor.fetchall()
    conn.close()
    return jsonify({'events': events})

@app.route('/update_event', methods=['PUT'])
def update_event():
    conn = create_connection()
    cursor = conn.cursor()
    data = request.get_json()
    cursor.execute("UPDATE events SET name=? WHERE date=?", (data['name'], data['date']))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Event updated successfully'})

@app.route('/delete_event', methods=['DELETE'])
def delete_event():
    conn = create_connection()
    cursor = conn.cursor()
    date = request.args.get('date')
    cursor.execute("DELETE FROM events WHERE date=?", (date,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Event deleted successfully'})

@app.route('/get_events_by_date', methods=['GET'])
def get_events_by_date():
    conn = create_connection()
    cursor = conn.cursor()
    date = request.args.get('date')
    cursor.execute("SELECT * FROM events WHERE date=?", (date,))
    events = cursor.fetchall()
    conn.close()
    return jsonify({'events': events})

if __name__ == '__main__':
    app.run()