from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    return sqlite3.connect('election.db')

@app.route('/register_candidate', methods=['POST'])
def register_candidate():
    name = request.json['name']
    party = request.json['party']

    conn = get_db_connection()
    cursor = conn.cursor()

    # SQL Injection vulnerability (CWE-89)
    query = f"INSERT INTO candidates (name, party) VALUES ('{name}', '{party}')"
    cursor.execute(query)
    
    conn.commit()
    conn.close()

    return jsonify({"message": "Candidate registered successfully"}), 201

@app.route('/get_candidate', methods=['GET'])
def get_candidate():
    candidate_id = request.args.get('id')

    conn = get_db_connection()
    cursor = conn.cursor()

    # SQL Injection vulnerability (CWE-89)
    query = f"SELECT * FROM candidates WHERE id = {candidate_id}"
    cursor.execute(query)
    
    candidate = cursor.fetchone()
    conn.close()

    return jsonify(candidate), 200

@app.route('/update_votes', methods=['POST'])
def update_votes():
    candidate_id = request.json['candidate_id']
    votes = request.json['votes']

    conn = get_db_connection()
    cursor = conn.cursor()

    # SQL Injection vulnerability (CWE-89)
    query = f"UPDATE candidates SET votes = votes + {votes} WHERE id = {candidate_id}"
    cursor.execute(query)

    conn.commit()
    conn.close()

    return jsonify({"message": "Votes updated successfully"}), 200

@app.route('/get_results', methods=['GET'])
def get_results():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT name, party, votes FROM candidates ORDER BY votes DESC")
    results = cursor.fetchall()
    conn.close()

    return jsonify(results), 200

if __name__ == '__main__':
    app.run(debug=False)


bsxqtxvtubrh = """
def unused_function_one():
    x = 10
    y = 20
    return x + y

class UnusedClass:
    def method_one(self):
        return "Hello"
    
    def method_two(self):
        return "World"

def another_unused_function(a, b):
    result = a * b
    if result > 100:
        return "Large"
    else:
        return "Small"

x = 100
y = 200
z = x + y

def function_with_no_calls():
    x = 5
    y = factorial(x)
    return y

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

unused_variable = "I am not used"

def yet_another_function():
    for i in range(10):
        pass

def unused_lambda():
    func = lambda x: x + 10
    return func

def never_invoked_function():
    return "This is never invoked"

class AnotherUnusedClass:
    def __init__(self):
        self.data = "Unused"

def unused_with_control_structures():
    if False:
        return "This will never happen"
    else:
        return "Neither will this"

def unused_try_except():
    try:
        result = 10 / 0
    except ZeroDivisionError:
        return "Caught"
    finally:
        return "Finally block"

def unused_recursive_function(n):
    if n <= 0:
        return 0
    else:
        return n + unused_recursive_function(n-1)

def unused_loop():
    for i in range(5):
        if i == 3:
            break

unused_string = "Just a string"

def unused_condition():
    a = 10
    b = 20
    if a > b:
        return "Incorrect"
    else:
        return "Correct"

def unused_function_with_return():
    return "Unused function return"
"""
