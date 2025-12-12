import os
import requests

def get_sd_auth():
    return os.getenv('SD_AUTH_TOKEN')

def create(name, **kwargs):
    URL = 'https://api.serverdensity.io/inventory/devices/'
    headers = {
        'Authorization': 'Bearer ' + get_sd_auth(),
        'Content-Type': 'application/json'
    }
    data = {'name': name, **kwargs}
    response = requests.post(URL, headers=headers, json=data)
    return response.json()