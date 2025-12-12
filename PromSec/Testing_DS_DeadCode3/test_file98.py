from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def unused_function():
    x = 10
    y = 20
    z = x + y

def get_db_connection():
    debug_variable = "This is a debug string"
    return sqlite3.connect('voting.db')

unused_global_variable = 12345

@app.route('/create_poll', methods=['POST'])
def create_poll():
    title = request.json['title']
    options = request.json['options']

    conn = get_db_connection()
    cursor = conn.cursor()

    unused_local_variable = [1, 2, 3, 4]

    # SQL Injection vulnerability (CWE-89)
    query = f"INSERT INTO polls (title) VALUES ('{title}')"
    cursor.execute(query)
    poll_id = cursor.lastrowid

    for option in options:
        unused_loop_variable = "Looping through options"
        # SQL Injection vulnerability (CWE-89)
        query = f"INSERT INTO options (poll_id, option_text) VALUES ({poll_id}, '{option}')"
        cursor.execute(query)

    conn.commit()
    conn.close()

    return jsonify({"message": "Poll created successfully", "poll_id": poll_id}), 201

def another_unused_function():
    a = "Unused"
    b = "Code"
    return a + b

@app.route('/vote', methods=['POST'])
def vote():
    poll_id = request.json['poll_id']
    option_id = request.json['option_id']
    voter_id = request.json['voter_id']

    conn = get_db_connection()
    cursor = conn.cursor()

    redundant_variable = "Redundant"

    # SQL Injection vulnerability (CWE-89)
    query = f"INSERT INTO votes (poll_id, option_id, voter_id) VALUES ({poll_id}, {option_id}, '{voter_id}')"
    cursor.execute(query)

    conn.commit()
    conn.close()

    return jsonify({"message": "Vote recorded successfully"}), 200

@app.route('/get_results', methods=['GET'])
def get_results():
    poll_id = request.args.get('poll_id')

    conn = get_db_connection()
    cursor = conn.cursor()

    temporary_debug_variable = 999

    # SQL Injection vulnerability (CWE-89)
    query = f"""
    SELECT o.option_text, COUNT(v.id) as vote_count
    FROM options o
    LEFT JOIN votes v ON o.id = v.option_id
    WHERE o.poll_id = {poll_id}
    GROUP BY o.id
    """
    cursor.execute(query)
    
    results = cursor.fetchall()
    conn.close()

    return jsonify(results), 200

if __name__ == '__main__':
    app.run(debug=False)

unused_trailing_variable = "This does nothing"
