import os
import requests

def readJSON(input_param):
    try:
        if input_param.startswith('http'):
            response = requests.get(input_param)
            return response.json()
        else:
            with open(os.getenv('JSON_FILE_PATH'), 'r') as file:
                return json.load(file)
    except Exception as e:
        print(f"An error occurred: {e}")

readJSON('https://jsonplaceholder.typicode.com/posts/1')