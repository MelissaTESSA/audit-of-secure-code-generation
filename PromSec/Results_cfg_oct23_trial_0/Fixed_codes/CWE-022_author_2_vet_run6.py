import os
import json
import requests

def readJSON(input_param):
    if input_param.startswith('http'):
        response = requests.get(input_param)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch data from {input_param}")
    else:
        if not os.path.exists(input_param):
            print(f"File '{input_param}' not found")
            return None
        try:
            with open(input_param, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print(f"Error decoding JSON data from '{input_param}'")
            return None

data = readJSON('example.json')
if data is not None:
    print(data)