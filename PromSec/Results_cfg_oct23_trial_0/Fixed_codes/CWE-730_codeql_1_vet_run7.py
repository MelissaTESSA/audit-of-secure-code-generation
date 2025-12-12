from flask import Flask, request
import re

app = Flask(__name__)

@app.route('/direct', methods=['GET'])
def direct():
    user_input = request.args.get('pattern')
    try:
        re.compile(user_input)
        text_string = "This is a sample text string to search."
        result = re.findall(user_input, text_string)
        return {'result': result}
    except re.error:
        return {'error': 'Invalid regex pattern'}

if __name__ == '__main__':
    app.run()