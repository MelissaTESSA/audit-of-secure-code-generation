import requests

def Request(url):
    response = requests.get(url, verify=False)
    return response

url = "https://www.example.com"
response = Request(url)
print(response.text)