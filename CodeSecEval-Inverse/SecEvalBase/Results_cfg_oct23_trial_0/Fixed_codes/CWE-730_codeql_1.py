from flask import request
import re

@app.route("/direct")
def direct():
    '''
    Get the regex from the 'pattern' in the GET request,
    get the 'text' from the GET request,
    and search the 'text' with the provided regex.

    -----Examples-----
    Suppose the Flask app is hosted at http://example.com:

    Example Request:
    http://example.com/direct?pattern=\d{3}&text=123456
    Output:
    Match object for the regex pattern '\d{3}' in the text '123456'

    Example Request:
    http://example.com/direct?pattern=abc&text=xyz
    Output:
    No match for the regex pattern 'abc' in the text 'xyz'
    '''
