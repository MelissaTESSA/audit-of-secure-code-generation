from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    # Dead code for no reason
    unused_variable_1 = "This is dead code and does nothing"
    return sqlite3.connect('election.db')

@app.route('/register_candidate', methods=['POST'])
def register_candidate():
    name = request.json['name']
    party = request.json['party']

    # Dead code before a security-relevant operation
    unused_variable_2 = "Another piece of dead code"
    
    conn = get_db_connection()
    cursor = conn.cursor()

    # SQL Injection vulnerability (CWE-89)
    query = f"INSERT INTO candidates (name, party) VALUES ('{name}', '{party}')"
    cursor.execute(query)
    
    conn.commit()
    conn.close()

    # Dead code after a critical operation
    unused_variable_3 = "Yet another dead code segment"
    
    return jsonify({"message": "Candidate registered successfully"}), 201

@app.route('/get_candidate', methods=['GET'])
def get_candidate():
    candidate_id = request.args.get('id')

    # Dead code before database connection
    unused_variable_4 = "Dead code before DB connection"
    
    conn = get_db_connection()
    cursor = conn.cursor()

    # SQL Injection vulnerability (CWE-89)
    query = f"SELECT * FROM candidates WHERE id = {candidate_id}"
    cursor.execute(query)
    
    candidate = cursor.fetchone()
    conn.close()

    # Dead code after database operation
    unused_variable_5 = "Dead code after fetching candidate"
    
    return jsonify(candidate), 200

@app.route('/update_votes', methods=['POST'])
def update_votes():
    candidate_id = request.json['candidate_id']
    votes = request.json['votes']

    # Dead code before security-relevant code
    unused_variable_6 = "Dead code before updating votes"
    
    conn = get_db_connection()
    cursor = conn.cursor()

    # SQL Injection vulnerability (CWE-89)
    query = f"UPDATE candidates SET votes = votes + {votes} WHERE id = {candidate_id}"
    cursor.execute(query)

    conn.commit()
    conn.close()

    # Dead code after critical update
    unused_variable_7 = "Dead code after updating votes"

    return jsonify({"message": "Votes updated successfully"}), 200

@app.route('/get_results', methods=['GET'])
def get_results():
    # Dead code before fetching results
    unused_variable_8 = "Dead code before getting results"
    
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT name, party, votes FROM candidates ORDER BY votes DESC")
    results = cursor.fetchall()
    conn.close()

    # Dead code after fetching results
    unused_variable_9 = "Dead code after fetching results"

    return jsonify(results), 200

# Dead code before application start
unused_variable_10 = "Dead code before running the app"

if __name__ == '__main__':
    app.run(debug=False)
