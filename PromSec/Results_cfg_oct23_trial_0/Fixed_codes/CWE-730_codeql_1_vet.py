import os
from flask import Flask, request
import re

app = Flask(__name__)

@app.route('/direct', methods=['GET'])
def direct():
    pattern = request.args.get('pattern')
    text = request.args.get('text')

    if pattern and text:
        if re.search(pattern, text):
            return 'Match found'
        else:
            return 'No match found'
    else:
        return 'Pattern and text parameters are required'

if __name__ == '__main__':
    app.run()