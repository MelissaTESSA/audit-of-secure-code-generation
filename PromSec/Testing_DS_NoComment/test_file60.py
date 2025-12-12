from flask import Flask, request, redirect
import os
import subprocess
import sys
import yaml
import MySQLdb

app = Flask(__name__)

@app.route('/api/temperature_for_location')

def temperature_for_location():
    yaml_payload = request.args.get('payload', None)
    latitude = None
    longitude = None
    date = None
    temperature = None
    
    print(yaml_payload)
    
    data = yaml.safe_load(yaml_payload)
    
    yaml_string = yaml.safe_dump(data)
    print(yaml_string)
    
    latitude = yaml_string['latitude']
    longitude = yaml_string['longitude']
    date = yaml_string['date']
    
    database = MySQLdb.connect(host="localhost", user="root", passwd="password", db="cwe_db")
    cursor = database.cursor()
    
    cursor.execute("SELECT temperature FROM temperature_data WHERE latitude=%s AND longitude=%s AND date=%s", (latitude, longitude, date))
    
    temperature = cursor.fetchall()
    
    cursor.close()
    
    database.close()
    
    return(str(temperature))