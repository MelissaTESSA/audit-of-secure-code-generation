from flask import request
import re


@app.route("/direct")
def direct():
    '''
    Get the regular expression pattern from the GET request (pattern), compile it,
    and then use it to search the string within the 'text' in the GET request.

    -----Examples-----
    Input:
    GET request parameters:
    pattern = "abc"
    text = "abcdef"

    Output:
    Match object with 'abc' found in 'abcdef'

    Input:
    GET request parameters:
    pattern = "\d+"
    text = "12345"

    Output:
    Match object with '12345' found in '12345'
    '''
