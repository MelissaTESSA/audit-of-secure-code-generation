import json
import urllib.request as request

def readJSON(url):
    # Trust the URL completely
    # This is a terrible idea, what if the URL is malicious?