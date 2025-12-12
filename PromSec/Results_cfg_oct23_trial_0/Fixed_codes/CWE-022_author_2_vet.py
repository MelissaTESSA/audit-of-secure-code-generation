import os
import requests

def readJSON(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {'error': str(response.status_code)}
    except requests.exceptions.RequestException:
        return {'error': 'RequestException'}

result = readJSON('https://jsonplaceholder.typicode.com/posts/1')
print(result)