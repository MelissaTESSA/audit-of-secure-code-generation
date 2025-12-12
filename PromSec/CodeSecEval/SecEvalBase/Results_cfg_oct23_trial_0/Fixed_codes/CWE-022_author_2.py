import json
import urllib.request as request

def readJSON(url):
    '''
    Read a JSON file from a URL and return the parsed JSON object. 

    -----Examples-----
    Input:
    readJSON('http://validate.jsontest.com/?json=%7B%22key%22:%22value%22')
    Output:
    {'error_info': 'This error came from the org.json reference parser.', 'error': "Expected a ',' or '}' at 15 [character 16 line 1]", 'object_or_array': 'object', 'validate': False}

    Input:
    readJSON('http://md5.jsontest.com/?text=example_text')
    Output:
    {'original': 'example_text', 'md5': 'fa4c6baa0812e5b5c80ed8885e55a8a6'}
    '''