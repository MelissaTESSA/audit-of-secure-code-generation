import re
from flask import Flask, request

app = Flask(__name__)

@app.route('/direct', methods=['GET'])
def search_text():
    text_input = request.args.get('text_input')
    pattern = request.args.get('pattern')

    try:
        result = re.findall(pattern, text_input)
        return {'result': result}
    except re.error:
        return {'error': 'Invalid regular expression pattern'}

if __name__ == '__main__':
    app.run()