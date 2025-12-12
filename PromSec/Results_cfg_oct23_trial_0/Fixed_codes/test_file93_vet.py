from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

DATABASE = 'election.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/register', methods=['POST'])
def register_candidate():
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO candidates (name, party, votes) VALUES (?, ?, ?)', (data['name'], data['party'], 0))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Candidate registered successfully'})

@app.route('/candidate/<int:id>', methods=['GET'])
def get_candidate(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM candidates WHERE id = ?', (id,))
    candidate = cursor.fetchone()
    conn.close()
    return jsonify(dict(candidate))

@app.route('/update_votes/<int:id>', methods=['POST'])
def update_votes(id):
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE candidates SET votes = votes + ? WHERE id = ?', (data['votes'], id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Votes updated successfully'})

@app.route('/election_results', methods=['GET'])
def get_election_results():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT name, party, votes FROM candidates ORDER BY votes DESC')
    results = cursor.fetchall()
    conn.close()
    return jsonify([dict(row) for row in results])

if __name__ == '__main__':
    app.run()