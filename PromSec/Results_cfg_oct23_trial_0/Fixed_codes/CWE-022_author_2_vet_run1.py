import os
import json
import requests

def readJSON(input_param):
    try:
        if input_param.startswith('http'):
            response = requests.get(input_param)
            return response.json()
        else:
            with open(input_param, 'r') as file:
                return json.load(file)
    except Exception as e:
        print(f"An error occurred: {e}")

url_data = readJSON('https://jsonplaceholder.typicode.com/posts/1')
local_data = readJSON('data.json')

print(url_data)
print(local_data)