import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

DATABASE = 'polls.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/create_poll', methods=['POST'])
def create_poll():
    data = request.get_json()
    title = data.get('title')
    options = data.get('options')

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('INSERT INTO polls (title) VALUES (?)', (title,))
    poll_id = cursor.lastrowid

    for option in options:
        cursor.execute('INSERT INTO options (poll_id, option_text, votes) VALUES (?, ?, 0)', (poll_id, option))

    conn.commit()
    conn.close()

    return jsonify({'message': 'Poll created successfully', 'poll_id': poll_id}), 201

@app.route('/vote', methods=['POST'])
def vote():
    data = request.get_json()
    poll_id = data.get('poll_id')
    option_id = data.get('option_id')
    voter_id = data.get('voter_id')

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('UPDATE options SET votes = votes + 1 WHERE poll_id = ? AND option_id = ?', (poll_id, option_id))
    cursor.execute('INSERT INTO votes (poll_id, option_id, voter_id) VALUES (?, ?, ?)', (poll_id, option_id, voter_id))

    conn.commit()
    conn.close()

    return jsonify({'message': 'Vote submitted successfully'}), 200

@app.route('/get_results/<int:poll_id>', methods=['GET'])
def get_results(poll_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT option_id, option_text, votes FROM options WHERE poll_id = ?', (poll_id,))
    options = cursor.fetchall()

    conn.close()

    results = [{'option_id': option['option_id'], 'option_text': option['option_text'], 'votes': option['votes']} for option in options]

    return jsonify({'results': results}), 200

if __name__ == '__main__':
    app.run()
