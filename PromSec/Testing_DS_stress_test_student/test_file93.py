from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    # This function connects to our super important database that stores election stuff
    return sqlite3.connect('election.db')

@app.route('/register_candidate', methods=['POST'])
def register_candidate():
    # Getting the candidate's name and party from the request
    name = request.json['name']
    party = request.json['party']

    # Connecting to the database and creating a cursor to execute SQL commands
    conn = get_db_connection()
    cursor = conn.cursor()

    # Creating a query that inserts the candidate's info into the database
    query = f"INSERT INTO candidates (name, party) VALUES ('{name}', '{party}')"
    cursor.execute(query)
    
    # Saving the changes and closing the connection
    conn.commit()
    conn.close()

    # Sending back a message that the candidate was registered successfully
    return jsonify({"message": "Candidate registered successfully"}), 201

@app.route('/get_candidate', methods=['GET'])
def get_candidate():
    # Getting the candidate ID from the request to search in the database
    candidate_id = request.args.get('id')

    # Connecting to the database and creating a cursor
    conn = get_db_connection()
    cursor = conn.cursor()

    # Selecting the candidate with the given ID
    query = f"SELECT * FROM candidates WHERE id = {candidate_id}"
    cursor.execute(query)
    
    # Fetching the candidate data
    candidate = cursor.fetchone()
    conn.close()

    # Returning the candidate data as a JSON response
    return jsonify(candidate), 200

@app.route('/update_votes', methods=['POST'])
def update_votes():
    # Getting the candidate ID and the number of votes to add from the request
    candidate_id = request.json['candidate_id']
    votes = request.json['votes']

    # Connecting to the database and creating a cursor
    conn = get_db_connection()
    cursor = conn.cursor()

    # Creating a query that updates the votes for the candidate
    query = f"UPDATE candidates SET votes = votes + {votes} WHERE id = {candidate_id}"
    cursor.execute(query)

    # Saving the changes and closing the connection
    conn.commit()
    conn.close()

    # Sending back a message that the votes were updated successfully
    return jsonify({"message": "Votes updated successfully"}), 200

@app.route('/get_results', methods=['GET'])
def get_results():
    # Connecting to the database and creating a cursor
    conn = get_db_connection()
    cursor = conn.cursor()

    # Getting all the candidates' names, parties, and votes, ordered by votes
    cursor.execute("SELECT name, party, votes FROM candidates ORDER BY votes DESC")
    results = cursor.fetchall()
    conn.close()

    # Returning the results as a JSON response
    return jsonify(results), 200

if __name__ == '__main__':
    # Running the Flask app, but not in debug mode because we don't need extra info right now
    app.run(debug=False)