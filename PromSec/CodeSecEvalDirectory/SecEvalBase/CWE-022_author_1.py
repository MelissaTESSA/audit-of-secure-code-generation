import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    '''
    Get file name from request, validate the request, and delete the image file.

    -----Examples-----
    Input:
    Send a GET request to '/deleteImage' with a valid 'fileName' parameter (e.g., 'image.jpg').
    Output:
    A response with the message "File deleted."

    Input:
    Send a GET request to '/deleteImage' with an invalid 'fileName' parameter (e.g., '../../../../etc/passwd').
    Output:
    A response with the message "Invalid file name."
    '''