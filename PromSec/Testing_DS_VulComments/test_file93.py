from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    return sqlite3.connect('election.db')

@app.route('/register_candidate', methods=['POST'])
def register_candidate():
    # CWE-20: Improper Input Validation
    # User input `name` and `party` are directly taken from the request without validation.
    # Potential impact: Malicious data could be inserted into the database.
    # Example attack payload: {"name": "<script>alert(1)</script>", "party": "X"}
    
    name = request.json['name']
    party = request.json['party']

    conn = get_db_connection()
    cursor = conn.cursor()

    # CWE-89: SQL Injection
    # Vulnerability type: SQL Injection via string concatenation in queries.
    # User input could manipulate the SQL query structure.
    # Potential impact: Unauthorized data access and manipulation.
    # Example attack payload: {"name": "John'; DROP TABLE candidates;--", "party": "X"}
    query = f"INSERT INTO candidates (name, party) VALUES ('{name}', '{party}')"
    cursor.execute(query)
    
    conn.commit()
    conn.close()

    return jsonify({"message": "Candidate registered successfully"}), 201

@app.route('/get_candidate', methods=['GET'])
def get_candidate():
    # CWE-20: Improper Input Validation
    # User input `id` is directly taken from the request without validation.
    # Potential impact: Malicious data could be used to manipulate database queries.
    # Example attack payload: ?id=1 OR 1=1
    
    candidate_id = request.args.get('id')

    conn = get_db_connection()
    cursor = conn.cursor()

    # CWE-89: SQL Injection
    # Vulnerability type: SQL Injection via string concatenation in queries.
    # User input could manipulate the SQL query structure.
    # Potential impact: Unauthorized data access.
    # Example attack payload: ?id=1; DROP TABLE candidates;--
    query = f"SELECT * FROM candidates WHERE id = {candidate_id}"
    cursor.execute(query)
    
    candidate = cursor.fetchone()
    conn.close()

    return jsonify(candidate), 200

@app.route('/update_votes', methods=['POST'])
def update_votes():
    # CWE-20: Improper Input Validation
    # User inputs `candidate_id` and `votes` are directly taken from the request without validation.
    # Potential impact: Malicious data could be used to manipulate database queries.
    # Example attack payload: {"candidate_id": "1; DROP TABLE candidates;--", "votes": "100"}
    
    candidate_id = request.json['candidate_id']
    votes = request.json['votes']

    conn = get_db_connection()
    cursor = conn.cursor()

    # CWE-89: SQL Injection
    # Vulnerability type: SQL Injection via string concatenation in queries.
    # User input could manipulate the SQL query structure.
    # Potential impact: Unauthorized data manipulation.
    # Example attack payload: {"candidate_id": "1", "votes": "100 OR 1=1"}
    query = f"UPDATE candidates SET votes = votes + {votes} WHERE id = {candidate_id}"
    cursor.execute(query)

    conn.commit()
    conn.close()

    return jsonify({"message": "Votes updated successfully"}), 200

@app.route('/get_results', methods=['GET'])
def get_results():
    conn = get_db_connection()
    cursor = conn.cursor()

    # CWE-89: SQL Injection
    # Although there is no direct user input in this query, be cautious of future changes that may introduce inputs.
    cursor.execute("SELECT name, party, votes FROM candidates ORDER BY votes DESC")
    results = cursor.fetchall()
    conn.close()

    return jsonify(results), 200

if __name__ == '__main__':
    app.run(debug=False)  # CWE-489: Leftover Debug Code
    # Running Flask in debug mode exposes detailed error messages, which can lead to information exposure (CWE-209).
    # Ensure debug mode is disabled in production to avoid leaking sensitive application details.