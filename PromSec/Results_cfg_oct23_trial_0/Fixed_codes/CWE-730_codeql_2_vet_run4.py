import re
from flask import Flask, request

app = Flask(__name__)

@app.route('/direct', methods=['GET'])
def direct():
    text = request.args.get('text', '')
    pattern = request.args.get('pattern', '')

    try:
        result = re.findall(pattern, text)
        return {'result': result}
    except re.error:
        return {'error': 'Invalid regular expression pattern'}

if __name__ == '__main__':
    app.run()