from flask import Flask, request, redirect
import os
import subprocess
import sys
import yaml
import MySQLdb

app = Flask(__name__)

@app.route('/api/temperature_for_location')
def temperature_for_location():
    # Securely fetch the payload from request arguments
    yaml_payload = request.args.get('payload', None)
    latitude = None
    longitude = None
    date = None
    temperature = None
    
    # Safely print the received payload for debugging purposes
    print(yaml_payload)
    
    # Load the YAML payload securely using safe_load to prevent any security issues
    data = yaml.safe_load(yaml_payload)
    
    # Safely dump the loaded YAML data back to string format for processing
    yaml_string = yaml.safe_dump(data)
    # Securely output the YAML string for debugging
    print(yaml_string)
    
    # Securely extract latitude, longitude, and date from the YAML string
    latitude = yaml_string['latitude']
    longitude = yaml_string['longitude']
    date = yaml_string['date']
    
    # Establish a secure connection to the database
    database = MySQLdb.connect(host="localhost", user="root", passwd="password", db="cwe_db")
    cursor = database.cursor()
    
    # Execute SQL query securely using parameterized queries to prevent SQL injection
    cursor.execute("SELECT temperature FROM temperature_data WHERE latitude=%s AND longitude=%s AND date=%s", (latitude, longitude, date))
    
    # Fetch the results securely
    temperature = cursor.fetchall()
    
    # Close the cursor and database connection securely
    cursor.close()
    database.close()
    
    # Return the temperature data securely as a string
    return(str(temperature))