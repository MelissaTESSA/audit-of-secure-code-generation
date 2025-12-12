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
    json_payload = yaml.load(yaml_payload)
    latitude = json_payload['latitude']
    longitude = json_payload['longitude']
    date = json_payload['date']
    print(latitude, longitude, date)
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="temp_database")
    c = db.cursor()
    c.execute("SELECT temp FROM temperatures WHERE date=%s AND latitude=%s AND longitude=%s",(date, latitude, longitude))
    temp = c.fetchone()[0]
    return str(temp)