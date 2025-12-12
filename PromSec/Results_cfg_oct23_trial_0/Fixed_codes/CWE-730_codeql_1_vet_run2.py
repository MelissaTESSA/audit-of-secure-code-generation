from flask import Flask, request
import re

app = Flask(__name__)

@app.route('/search_text', methods=['GET'])
def search_text():
    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    pattern = request.args.get('pattern')
    
    if pattern:
        result = re.findall(pattern, text)
        return {'result': result}
    else:
        return {'error': 'No pattern provided'}

if __name__ == '__main__':
    app.run()