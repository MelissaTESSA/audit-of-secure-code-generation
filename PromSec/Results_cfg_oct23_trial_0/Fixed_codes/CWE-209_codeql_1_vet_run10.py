import os
import logging
from flask import Flask

app = Flask(__name__)

def do_computation():
    raise Exception("Secret info")

@app.route('/bad')
def bad_route():
    try:
        do_computation()
    except Exception as e:
        logging.error(str(e))
        return "An error occurred", 500

if __name__ == '__main__':
    app.run()