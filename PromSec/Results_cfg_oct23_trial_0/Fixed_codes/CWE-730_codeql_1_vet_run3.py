import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/direct', methods=['GET'])
def direct_search():
    text = "This is a sample text for direct search using regex."
    regex_pattern = request.args.get('pattern')
    
    if regex_pattern:
        matches = re.findall(regex_pattern, text)
        return {'matches': matches}
    else:
        return {'error': 'No regex pattern provided'}

if __name__ == '__main__':
    app.run()