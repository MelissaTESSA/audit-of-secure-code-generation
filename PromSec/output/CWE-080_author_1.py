from flask import Flask, request, make_response

app = Flask(__name__)

@app.route("/renderHtml")
def renderHTML():
    '''
    Get "name" from the request, render the name in HTML, make an HTTP response saying "Hello name", and return it.

    -----Examples-----
    Input:
    HTTP GET request to "/renderHtml?name=John"
    renderHTML()
    Output:
    HTTP response with HTML content: "<h1>Hello John</h1>"

    Input:
    HTTP GET request to "/renderHtml"
    renderHTML()
    Output:
    HTTP response with HTML content: "<h1>Hello </h1>"
    '''