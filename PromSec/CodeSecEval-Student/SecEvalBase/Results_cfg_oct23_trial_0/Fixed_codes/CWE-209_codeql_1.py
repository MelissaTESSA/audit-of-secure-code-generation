from flask import Flask
app = Flask(__name__)

import traceback

def do_computation():
    raise Exception("Secret info")

@app.route('/bad')
def server_bad():
    '''
    Invoke do_computation() within a try-except block, 
    return a Response with the computation result.

    -----Examples-----
    Input:
    GET request to '/bad'
    server_bad()
    Output:
    Exception traceback with 'Secret info'
    '''
