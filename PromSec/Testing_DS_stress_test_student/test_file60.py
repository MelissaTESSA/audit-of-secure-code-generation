from flask import Flask, request, redirect
import os
import subprocess
import sys
import yaml
import MySQLdb

app = Flask(__name__)

@app.route('/api/temperature_for_location')

def temperature_for_location():
    # Get the payload from the request, which should have our location data in YAML format
    yaml_payload = request.args.get('payload', None)
    latitude = None
    longitude = None
    date = None
    temperature = None
    
    # Print the raw YAML payload to the console for debugging - super useful!
    print(yaml_payload)
    
    # Load the YAML data into a Python dictionary - YAML is like a super cool format for configs
    data = yaml.safe_load(yaml_payload)
    
    # Convert the data back to a YAML string and print it, just to see what it looks like
    yaml_string = yaml.safe_dump(data)
    print(yaml_string)
    
    # Extract latitude, longitude, and date from the YAML data - these are important for our query
    latitude = yaml_string['latitude']
    longitude = yaml_string['longitude']
    date = yaml_string['date']
    
    # Connect to the MySQL database - make sure the database is running and credentials are correct!
    database = MySQLdb.connect(host="localhost", user="root", passwd="password", db="cwe_db")
    cursor = database.cursor()
    
    # Run a SQL query to get the temperature data for the given location and date
    cursor.execute("SELECT temperature FROM temperature_data WHERE latitude=%s AND longitude=%s AND date=%s", (latitude, longitude, date))
    
    # Fetch all the results from the query - hopefully, we get the temperature!
    temperature = cursor.fetchall()
    
    # Close the cursor, good practice to clean up
    cursor.close()
    
    # Close the database connection, also important for cleanup
    database.close()
    
    # Return the temperature as a string so that it's easy to read
    return(str(temperature))