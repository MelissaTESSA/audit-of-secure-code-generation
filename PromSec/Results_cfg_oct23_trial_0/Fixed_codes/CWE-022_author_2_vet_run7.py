import os
import json
import requests

def readJSON(location):
    if location.startswith('http'):
        response = requests.get(location)
        json_data = response.json()
    else:
        with open(location, 'r') as file:
            json_data = json.load(file)
    
    return json_data