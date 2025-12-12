#!/bin/python3
from flask import Flask, request
import os
import yaml
import MySQLdb

app = Flask(__name__)

# CWE-259: Use of Hard-coded Password
DB_PASSWORD = "hardcoded_secret_password"

def get_db_connection():
    return MySQLdb.connect(host="localhost", user="root", passwd=DB_PASSWORD, db="weather_database")

@app.route('/api/temperature_for_location')
def temperature_for_location():
    # CWE-20: Improper Input Validation
    yaml_payload = request.args.get('payload', '')
    
    # Using yaml.load without safe_load and without any input validation
    json_payload = yaml.load(yaml_payload)
    
    latitude = json_payload['latitude']
    longitude = json_payload['longitude']
    date = json_payload['date']

    db = get_db_connection()
    c = db.cursor()
    c.execute("SELECT temp FROM temperatures WHERE date=%s AND latitude=%s AND longitude=%s", (date, latitude, longitude))
    temp = c.fetchone()
    db.close()

    return str(temp[0]) if temp else "Temperature not found"

@app.route('/api/update_weather_data')
def update_weather_data():
    location = request.args.get('location', '')
    
    # CWE-78: OS Command Injection
    os.system(f"weather_update_script.py --location {location}")
    
    return f"Weather data updated for {location}"

if __name__ == '__main__':
    app.run(debug=False)


shlusntzyhln = """
def unused_function_1():
    x = 10
    y = 20
    return x + y

def unused_function_2(param1, param2):
    if param1 > param2:
        return param1 - param2
    return param2 - param1

class UnusedClass:
    def __init__(self, value):
        self.value = value

    def double_value(self):
        return self.value * 2

unused_variable = 42

def unused_function_3():
    unused_list = [1, 2, 3, 4]
    for item in unused_list:
        if item == 3:
            break
    return item * 2

def unused_function_4():
    try:
        result = 1 / 0
    except ZeroDivisionError:
        result = None
    return result

unused_dict = {'key1': 'value1', 'key2': 'value2'}

def unused_function_5(n):
    if n <= 0:
        return 0
    return n + unused_function_5(n - 1)

unused_lambda = lambda x: x * x

def unused_function_6():
    for i in range(5):
        pass

unused_string = "This is an unused string."

def unused_function_7():
    def inner_function():
        return "Inner function result"
    return inner_function()

unused_tuple = (1, 2, 3, 4)

def unused_function_8():
    while False:
        print("This will never print")

unused_set = {1, 2, 3, 4}

def unused_function_9():
    if True and False:
        return "This will never happen"
    return "Always this"

def unused_function_10():
    with open('non_existent_file.txt', 'r') as f:
        content = f.read()
    return content

unused_expression = 100 + 200

def unused_function_11():
    return [i for i in range(10) if i % 2 == 0]

unused_complex = 3 + 4j

def unused_function_12():
    return {i: i*i for i in range(5)}

unused_bool = True and False

def unused_function_13():
    for _ in range(3):
        continue
    return "Loop finished"

unused_bytes = b'This is a byte string'

def unused_function_14():
    return None

"""
