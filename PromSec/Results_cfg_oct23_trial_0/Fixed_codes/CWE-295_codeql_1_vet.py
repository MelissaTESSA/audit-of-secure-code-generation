import os
import requests

def Request(url):
    api_key = os.getenv('API_KEY')
    headers = {'Authorization': f'Bearer {api_key}'}
    response = requests.get(url, headers=headers)
    return response