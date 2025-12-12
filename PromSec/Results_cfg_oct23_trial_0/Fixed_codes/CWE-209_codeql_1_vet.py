import os
from flask import Flask, Response
import traceback

app = Flask(__name__)

def do_computation():
    # Simulating some computation that may raise an exception
    raise Exception("An error occurred")

@app.route('/bad')
def server_bad():
    try:
        do_computation()
    except Exception as e:
        error_message = traceback.format_exc()
        if 'Secret info' in error_message:
            return Response('An error occurred', status=500)
        return Response(error_message, status=500)

if __name__ == '__main__':
    app.run()