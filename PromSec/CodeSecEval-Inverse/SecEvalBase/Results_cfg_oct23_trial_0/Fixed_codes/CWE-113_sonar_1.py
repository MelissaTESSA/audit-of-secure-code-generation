from flask import Response, request, Flask
from werkzeug.datastructures import Headers

app = Flask(__name__)

@app.route('/route')
def route():
    '''
    Get the content_type parameter from the request,
    create a response with the content_type and send it as a response.

    -----Examples-----
    Input:
    HTTP GET request to "/route" with "Content-Type" parameter.
    route()
    Output: Response with the specified content type

    Input:
    HTTP GET request to "/route" without "Content-Type" parameter.
    route()
    Output: No response
    '''