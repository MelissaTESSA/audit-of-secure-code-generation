from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/showName')
def name():
    '''
    Get "name" from the request, validate it,
    make a response with it, and return the response object.

    -----Examples-----
    Input:
    HTTP GET request to "/showName?name=John"
    name()
    Output:
    HTTP response: "Your name is John"

    Input:
    HTTP GET request to "/showName"
    name()
    Output:
    HTTP response: "Your name is "
    '''