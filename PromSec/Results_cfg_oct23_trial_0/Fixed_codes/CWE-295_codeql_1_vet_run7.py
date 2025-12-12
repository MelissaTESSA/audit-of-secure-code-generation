import requests

def Request(url):
    response = requests.get(url, verify=False)
    return response