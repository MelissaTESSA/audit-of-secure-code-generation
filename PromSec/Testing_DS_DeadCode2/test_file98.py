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

    # SQL Injection vulnerability (CWE-89)
    query = f"INSERT INTO polls (title) VALUES ('{title}')"
    cursor.execute(query)
    poll_id = cursor.lastrowid

    for option in options:
        # SQL Injection vulnerability (CWE-89)
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


jlnspplujako = """
def unused_function_one(x):
    y = x * x
    return y - 10

class UnusedClass:
    def method_one(self):
        pass

    def method_two(self):
        return 42

x = 10
y = 20
z = 30

def calculate_sum(a, b):
    return a + b

unused_variable = calculate_sum(x, y)

for i in range(5):
    unused_variable += i

def never_called_function():
    return "This function is never called"

result = unused_function_one(5)
another_unused_var = result + 100

def irrelevant_function():
    test_list = [1, 2, 3]
    for item in test_list:
        item += 1

if False:
    print("This will never print")

while False:
    pass

try:
    print("Trying something useless")
except Exception as e:
    print("This will never catch anything")

with open('non_existent_file.txt', 'r') as f:
    content = f.read()

lambda_func = lambda x: x + 2

def not_needed_func():
    return lambda_func(10)

pointless_data = {
    "key": "value",
    "another_key": "another_value"
}

def another_unused_function(param):
    return param * 2

another_unused_function(10)

def yet_another_function():
    return "Nothing to see here"

yet_another_function()

for j in range(3):
    print("This loop does nothing significant")

useless_str = "This string is not used"

def redundant_function():
    return "Redundant"

redundant_function()

class AnotherUnusedClass:
    def do_nothing(self):
        pass

    def do_more_nothing(self):
        return "Still nothing"

more_unused_code = [i for i in range(10) if i % 2 == 0]

def empty_function():
    pass

empty_function()

"""
