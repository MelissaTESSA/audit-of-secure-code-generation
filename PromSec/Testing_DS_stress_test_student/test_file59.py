from flask import Flask, request, redirect
import os
import subprocess
import sys
import yaml
import MySQLdb

app = Flask(__name__)

@app.route('/api/temperature_for_location')
def temperature_for_location():
    # Get the 'payload' parameter from the URL. It's expected to be a YAML string!
    yaml_payload = request.args.get('payload', None)
    
    # Load the YAML payload. This converts it into a Python dictionary.
    json_payload = yaml.load(yaml_payload)
    
    # Extract the latitude, longitude, and date from the dictionary.
    latitude = json_payload['latitude']
    longitude = json_payload['longitude']
    date = json_payload['date']
    
    # Print the latitude, longitude, and date to the console for debugging purposes!
    print(latitude, longitude, date)
    
    # Connect to the MySQL database. Make sure the database server is running locally!
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="temp_database")
    
    # Create a cursor object which allows us to execute SQL queries.
    c = db.cursor()
    
    # Execute an SQL query to find the temperature for the given date and location.
    # The %s placeholders get replaced with the actual values from the tuple.
    c.execute("SELECT temp FROM temperatures WHERE date=%s AND latitude=%s AND longitude=%s",(date, latitude, longitude))
    
    # Fetch one result from the query. We assume there's always a result for simplicity!
    temp = c.fetchone()[0]
    
    # Return the temperature as a string so it can be displayed in the browser.
    return str(temp)