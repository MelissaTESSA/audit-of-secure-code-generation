import os
from flask import Flask, request
import re

app = Flask(__name__)

@app.route('/direct', methods=['GET'])
def direct_search():
    text = "This is a sample text for direct search using regex."
    pattern = request.args.get('pattern')
    
    if pattern:
        result = re.findall(pattern, text)
        return {'result': result}
    else:
        return {'error': 'No pattern provided'}

if __name__ == '__main__':
    app.run()