from flask import Flask, request
import re

app = Flask(__name__)

@app.route('/direct', methods=['GET'])
def direct():
    pattern = request.args.get('pattern')
    text = "This is a sample text to search for patterns."
    result = re.findall(pattern, text)
    return str(result)

if __name__ == '__main__':
    app.run()