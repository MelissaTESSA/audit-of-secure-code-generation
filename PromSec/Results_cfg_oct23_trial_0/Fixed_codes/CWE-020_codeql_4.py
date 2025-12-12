from flask import Flask, redirect, request

app = Flask(__name__)

@app.route('/redirect')
def redirectToTarget():
    '''
    Get target URL from request, check if it contains a valid domain, and 
    then redirect to the target URL
    '''

    -----Examples-----
    Input:
    Send a GET request to '/redirect' with a valid 'target' parameter (e.g., 'https://www.example.com/somepage').
    Output:
    A redirection to the specified target URL.

    Input:
    Send a GET request to '/redirect' with an invalid 'target' parameter (e.g., 'https://malicious.site').
    Output:
    A response with the message "Invalid target."
    '''
