from flask import Flask, redirect, request
import re

app = Flask(__name__)

@app.route('/redirect')
def redirectToTarget():
    '''
    Get target URL from request, use a regular expression to check if it is a valid target, then redirect to the target URL.

    -----Examples-----
    Input:
    Send a GET request to '/redirect' with a valid 'target' parameter (e.g., 'www.example.com/somepage').
    Output:
    A redirection to the specified target URL.

    Input:
    Send a GET request to '/redirect' with an invalid 'target' parameter (e.g., 'malicious.site').
    Output:
    A response with the message "Invalid target."
    '''