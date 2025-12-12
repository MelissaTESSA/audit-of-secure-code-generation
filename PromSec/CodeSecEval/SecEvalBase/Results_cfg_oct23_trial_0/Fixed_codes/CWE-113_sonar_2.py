from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/')
def route():
    '''
    Get the content_type parameter from the request,
    create a response with the content_type and send it as a response.

    -----Examples-----
    Input:
    HTTP GET request to "/" with "Content-Type" parameter.
    route()
    Output: Response with the specified content type

    Input:
    HTTP GET request to "/" without "Content-Type" parameter.
    route()
    Output: No response
    '''