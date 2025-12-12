import os
import json
import requests

def readJSON(location):
    if location.startswith('http'):
        response = requests.get(location)
        data = response.json()
    else:
        with open(location, 'r') as file:
            data = json.load(file)
    
    return data