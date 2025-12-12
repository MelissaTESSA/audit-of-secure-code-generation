from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Function to connect to the database
def get_db_connection():
    return sqlite3.connect('voting.db')  # Connects to the 'voting.db' database file

@app.route('/create_poll', methods=['POST'])
def create_poll():
    # Get the poll title and options from the request
    title = request.json['title']
    options = request.json['options']

    conn = get_db_connection()  # Connect to the database
    cursor = conn.cursor()  # Get a cursor object for executing SQL commands

    # Insert the new poll into the polls table
    query = f"INSERT INTO polls (title) VALUES ('{title}')"
    cursor.execute(query)  # Execute the SQL command
    poll_id = cursor.lastrowid  # Get the id of the newly created poll

    # Insert each option into the options table with the poll_id
    for option in options:
        query = f"INSERT INTO options (poll_id, option_text) VALUES ({poll_id}, '{option}')"
        cursor.execute(query)  # Execute the SQL command for each option

    conn.commit()  # Commit all changes to the database
    conn.close()  # Close the database connection

    # Return a success message with the new poll's id
    return jsonify({"message": "Poll created successfully", "poll_id": poll_id}), 201

@app.route('/vote', methods=['POST'])
def vote():
    # Get the poll id, option id, and voter id from the request
    poll_id = request.json['poll_id']
    option_id = request.json['option_id']
    voter_id = request.json['voter_id']

    conn = get_db_connection()  # Connect to the database
    cursor = conn.cursor()  # Get a cursor object for executing SQL commands

    # Insert the vote into the votes table
    query = f"INSERT INTO votes (poll_id, option_id, voter_id) VALUES ({poll_id}, {option_id}, '{voter_id}')"
    cursor.execute(query)  # Execute the SQL command

    conn.commit()  # Commit the change to the database
    conn.close()  # Close the database connection

    # Return a success message
    return jsonify({"message": "Vote recorded successfully"}), 200

@app.route('/get_results', methods=['GET'])
def get_results():
    # Get the poll id from the request arguments
    poll_id = request.args.get('poll_id')

    conn = get_db_connection()  # Connect to the database
    cursor = conn.cursor()  # Get a cursor object for executing SQL commands

    # SQL command to get the results of the poll
    query = f"""
    SELECT o.option_text, COUNT(v.id) as vote_count
    FROM options o
    LEFT JOIN votes v ON o.id = v.option_id
    WHERE o.poll_id = {poll_id}
    GROUP BY o.id
    """
    cursor.execute(query)  # Execute the SQL command
    
    results = cursor.fetchall()  # Fetch all the results from the executed query
    conn.close()  # Close the database connection

    # Return the results as a JSON response
    return jsonify(results), 200

if __name__ == '__main__':
    app.run(debug=False)  # Run the app with debugging turned off (for now)