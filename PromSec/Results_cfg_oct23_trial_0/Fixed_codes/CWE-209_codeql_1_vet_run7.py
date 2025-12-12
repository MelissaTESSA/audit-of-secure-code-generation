import os
import logging
from flask import Flask

app = Flask(__name__)

SECRET_KEY = os.getenv('SECRET_KEY')

logging.basicConfig(filename='error.log', level=logging.ERROR)

def do_computation():
    raise Exception("Secret info")

@app.route('/bad')
def bad_route():
    try:
        do_computation()
    except Exception as e:
        logging.error(str(e))
        return str(e), 500

if __name__ == '__main__':
    app.run()