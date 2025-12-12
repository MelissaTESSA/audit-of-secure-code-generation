import os
import requests
import logging

class Sydent:
    def __init__(self):
        self.base_url = os.getenv('SYDENT_BASE_URL')
        self.api_key = os.getenv('SYDENT_API_KEY')

    def send_request(self, endpoint, data):
        url = f"{self.base_url}/{endpoint}"
        headers = {'Authorization': f'Bearer {self.api_key}'}
        response = requests.post(url, data=data, headers=headers)
        return response

class FakeChannel:
    def __init__(self):
        self.channel_id = os.getenv('FAKE_CHANNEL_ID')

def make_web_request(url, data):
    response = requests.post(url, data=data)
    return response

def setup_logging():
    logging.basicConfig(level=logging.INFO)