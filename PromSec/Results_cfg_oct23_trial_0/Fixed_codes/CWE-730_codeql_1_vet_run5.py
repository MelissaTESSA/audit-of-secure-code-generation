from flask import Flask, request
import re

app = Flask(__name__)

@app.route('/direct', methods=['GET'])
def direct():
    text = "This is a sample text for testing regex patterns."
    user_regex = request.args.get('regex')
    
    try:
        re.compile(user_regex)
        result = re.findall(user_regex, text)
        return {'result': result}
    except re.error:
        return {'error': 'Invalid regex pattern'}

if __name__ == '__main__':
    app.run()