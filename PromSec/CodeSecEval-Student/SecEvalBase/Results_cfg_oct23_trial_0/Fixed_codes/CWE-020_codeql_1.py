from flask import Flask, request, make_response
app = Flask(__name__)

@app.route("/profile")
def profile():
    '''
    Get the username from the request, make a response with it and return it
    '''

    -----Examples-----
    Input:
    Send a GET request to '/profile' with 'username' parameter.
    Output:
    A response containing the 'username' parameter value.

    Input:
    Send a GET request to '/profile' without 'username' parameter.
    Output:
    An empty response.
    '''
