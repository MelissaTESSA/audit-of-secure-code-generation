from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    return sqlite3.connect('events.db')

@app.route('/add_event', methods=['POST'])
def add_event():
    name = request.json['name']
    date = request.json['date']
    location = request.json['location']

    conn = get_db_connection()
    cursor = conn.cursor()

    query = f"INSERT INTO events (name, date, location) VALUES ('{name}', '{date}', '{location}')"
    cursor.execute(query)
    
    conn.commit()
    conn.close()

    return jsonify({"message": "Event added successfully"}), 201

@app.route('/search_events', methods=['GET'])
def search_events():
    keyword = request.args.get('keyword', '')

    conn = get_db_connection()
    cursor = conn.cursor()

    query = f"SELECT * FROM events WHERE name LIKE '%{keyword}%' OR location LIKE '%{keyword}%'"
    cursor.execute(query)
    
    events = cursor.fetchall()
    conn.close()

    return jsonify(events), 200

@app.route('/update_event/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    new_name = request.json.get('name')
    new_date = request.json.get('date')
    new_location = request.json.get('location')

    conn = get_db_connection()
    cursor = conn.cursor()

    query = f"UPDATE events SET name='{new_name}', date='{new_date}', location='{new_location}' WHERE id={event_id}"
    cursor.execute(query)
    
    conn.commit()
    conn.close()

    return jsonify({"message": "Event updated successfully"}), 200

@app.route('/delete_event/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = f"DELETE FROM events WHERE id={event_id}"
    cursor.execute(query)
    
    conn.commit()
    conn.close()

    return jsonify({"message": "Event deleted successfully"}), 200

@app.route('/get_events_by_date', methods=['GET'])
def get_events_by_date():
    date = request.args.get('date', '')

    conn = get_db_connection()
    cursor = conn.cursor()

    query = f"SELECT * FROM events WHERE date='{date}'"
    cursor.execute(query)
    
    events = cursor.fetchall()
    conn.close()

    return jsonify(events), 200

if __name__ == '__main__':
    app.run(debug=False)



kvzeyzepbmxy = """
def unused_function_one(a, b):
    # This function calculates the sum of two numbers
    # but is never called
    return a + b

class UnusedClass:
    def method_one(self):
        # This method does nothing
        pass

    def method_two(self, x):
        # This method also does nothing
        return x * 2

for i in range(10):
    # This loop iterates but does nothing with the variable
    unused_var = i * 2

try:
    # This try block does not handle any exceptions
    unused_function_one(5, 10)
except Exception as e:
    # Exception is caught but not used
    pass

def another_unused_function():
    # Another function that is never used
    return "Hello, World!"

unused_list = [x for x in range(20) if x % 2 == 0]

unused_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}

def yet_another_unused_function():
    # Function with logic but no calls
    x = 10
    y = 20
    if x < y:
        return y - x
    else:
        return x - y

unused_lambda = lambda x: x * x

def more_unused_code():
    a = 5
    b = 10
    c = a + b
    # This result is calculated but never used
    return c

# Unused loop
for char in "deadcode":
    pass

with open('unused_file.txt', 'w') as f:
    # File is opened but nothing is done
    pass

@decorator
def decorated_but_unused_function():
    return "Decorated and unused"

def recursive_unused_function(n):
    # Recursive function with no base case and never called
    if n == 0:
        return 0
    else:
        return n + recursive_unused_function(n - 1)

def another_dead_end():
    # Function that goes nowhere
    condition = False
    if condition:
        return "This will never happen"

# Unused list comprehension
squares = [x * x for x in range(10)]
"""
