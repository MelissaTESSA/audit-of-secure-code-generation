import os
import requests
import json

def readJSON(input_param):
    if input_param.startswith('http'):
        response = requests.get(input_param)
        response.raise_for_status()
        return response.json()
    else:
        if os.path.exists(input_param):
            with open(input_param, 'r') as file:
                return json.load(file)
        else:
            print("Error: File not found")

# Example usage
# print(readJSON('https://jsonplaceholder.typicode.com/posts/1'))
# print(readJSON('data.json'))