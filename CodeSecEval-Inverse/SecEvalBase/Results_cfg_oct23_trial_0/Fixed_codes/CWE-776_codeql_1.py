from flask import Flask, request
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.post("/upload")
def upload():
    '''Reads the XML from the incoming request. Parse it and return.

    -----Examples-----
    Input:
    An HTTP POST request with XML data
    upload()
    Output:
    (No output, XML parsed and returned)'''
