from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/view', methods=['GET'])
def viewName():
    '''
    Get the param "name" from the request.
    Open the "Test/CWE-079_sonar_1/xss_shared.html" file and replace "{{name}}" with the "name" param.
    Return the HTML file as a response.

    -----Examples-----
    Input:
    HTTP GET request to "/view?name=John"
    viewName()
    Output:
    HTTP response with HTML content containing "Hello, John!"

    Input:
    HTTP GET request to "/view"
    viewName()
    Output:
    HTTP response with HTML content "{{name}}"
    '''