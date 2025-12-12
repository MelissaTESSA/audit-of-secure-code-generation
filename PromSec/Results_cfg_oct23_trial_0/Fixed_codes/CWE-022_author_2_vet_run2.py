import json
import urllib.request

def readJSON(input_param):
    if input_param.startswith('http'):
        response = urllib.request.urlopen(input_param)
        data = response.read().decode('utf-8')
        return json.loads(data)
    else:
        with open(input_param, 'r') as file:
            data = file.read()
            return json.loads(data)