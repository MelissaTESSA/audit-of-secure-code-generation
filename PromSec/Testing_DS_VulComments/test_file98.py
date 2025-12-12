from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    return sqlite3.connect('voting.db')

@app.route('/create_poll', methods=['POST'])
def create_poll():
    title = request.json['title']
    options = request.json['options']

    conn = get_db_connection()
    cursor = conn.cursor()

    # CWE-89: SQL Injection
    # Vulnerability: Directly concatenating user input into SQL queries without parameterization.
    # Exploit: A user can inject SQL commands through the 'title' variable.
    # Example Payload: title = "poll_title'); DROP TABLE polls; --"
    query = f"INSERT INTO polls (title) VALUES ('{title}')"
    cursor.execute(query)
    poll_id = cursor.lastrowid

    for option in options:
        # CWE-89: SQL Injection
        # Vulnerability: Directly concatenating user input into SQL queries without parameterization.
        # Exploit: A user can inject SQL commands through each 'option'.
        # Example Payload: option = "option_text'); DROP TABLE options; --"
        query = f"INSERT INTO options (poll_id, option_text) VALUES ({poll_id}, '{option}')"
        cursor.execute(query)

    conn.commit()
    conn.close()

    return jsonify({"message": "Poll created successfully", "poll_id": poll_id}), 201

@app.route('/vote', methods=['POST'])
def vote():
    poll_id = request.json['poll_id']
    option_id = request.json['option_id']
    voter_id = request.json['voter_id']

    conn = get_db_connection()
    cursor = conn.cursor()

    # CWE-89: SQL Injection
    # Vulnerability: Directly concatenating user input into SQL queries without parameterization.
    # Exploit: A user can inject SQL commands through 'poll_id', 'option_id', or 'voter_id'.
    # Example Payload: voter_id = "voter_id'); DROP TABLE votes; --"
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

    # CWE-89: SQL Injection
    # Vulnerability: Directly concatenating user input into SQL queries without parameterization.
    # Exploit: A user can inject SQL commands through 'poll_id'.
    # Example Payload: poll_id = "1; DROP TABLE votes; --"
    query = f"SELECT * FROM results WHERE poll_id = {poll_id}"
    cursor.execute(query)
    
    results = cursor.fetchall()
    conn.close()

    return jsonify(results), 200

if __name__ == '__main__':
    # CWE-489: Leftover Debug Code
    # Vulnerability: Running the Flask app with debug mode set to True can lead to information leakage.
    # Exploit: An attacker may gain access to detailed error messages or other internal server information.
    # Potential Impact: Information exposure that can be used to facilitate other attacks.
    app.run(debug=False)