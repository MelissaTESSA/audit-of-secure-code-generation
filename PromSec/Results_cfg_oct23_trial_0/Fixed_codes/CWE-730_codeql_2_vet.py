from flask import Flask, request
import re

app = Flask(__name__)

@app.route('/direct', methods=['GET'])
def direct():
    pattern = request.args.get('pattern')
    text = request.args.get('text')

    if pattern is None or text is None:
        return "Error: Missing parameters"

    try:
        compiled_pattern = re.compile(pattern)
        matches = compiled_pattern.findall(text)
        return ', '.join(matches)
    except re.error:
        return "Error: Invalid regular expression pattern"

if __name__ == '__main__':
    app.run()