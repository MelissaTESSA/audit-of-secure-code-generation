import os
from flask import Flask, request
import re

app = Flask(__name__)

@app.route('/direct', methods=['GET'])
def direct_search():
    text = "This is a sample text for regex pattern matching."
    regex_pattern = request.args.get('pattern')
    
    if regex_pattern:
        result = re.findall(regex_pattern, text)
        return {'result': result}
    else:
        return {'error': 'No regex pattern provided'}

if __name__ == '__main__':
    app.run()