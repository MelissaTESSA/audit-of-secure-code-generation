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
    if yaml_payload is None:
        return "YAML payload missing from request"
    else:
        lat = int(yaml.load(yaml_payload)['lat'])
        lon = int(yaml.load(yaml_payload)['lon'])
        date = int(yaml.load(yaml_payload)['date'])
        db = MySQLdb.connect(host="localhost", user="root", passwd="", db="cwe")
        cur = db.cursor()
        cur.execute(, (lat, lon, date))
        row = cur.fetchone()
        return str(row[0])