import os
from flask import Flask
import logging

app = Flask(__name__)

def do_computation():
    raise Exception("Secret info")

@app.route('/bad')
def server_bad():
    try:
        do_computation()
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}", exc_info=True)
    return "Error logged"

if __name__ == '__main__':
    app.run()