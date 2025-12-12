from flask import Flask, request
import os
import re

app = Flask(__name__)

SECRET_KEY = os.getenv('SECRET_KEY')

@app.route('/search_text', methods=['GET'])
def search_text():
    pattern = request.args.get('pattern')
    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."

    if pattern:
        result = re.findall(pattern, text)
        return {'result': result}
    else:
        return {'error': 'No pattern provided'}

if __name__ == '__main__':
    app.run()