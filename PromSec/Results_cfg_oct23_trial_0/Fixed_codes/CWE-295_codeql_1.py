import requests

def Request(url):
    '''
    Make an HTTP request to a given URL.

    -----Examples-----
    Input:
    Request('https://semmle.com')
    Output:
    <Response [200]>

    Input:
    Request('https://www.example.com/')
    Output:
    <Response [200]>
    '''