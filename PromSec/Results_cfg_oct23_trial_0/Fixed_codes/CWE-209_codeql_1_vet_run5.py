import os
from flask import Flask, jsonify

app = Flask(__name__)

def do_computation():
    raise Exception("Secret info")

@app.route('/bad')
def bad_route():
    try:
        do_computation()
    except Exception as e:
        app.logger.error("An error occurred: {}".format(str(e)))
    return jsonify({"message": "An error occurred. Please try again later."})

if __name__ == '__main__':
    app.run()