from flask import Flask, request
import re

app = Flask(__name)

@app.route('/direct', methods=['GET'])
def search_text():
    pattern = request.args.get('pattern')
    text = request.args.get('text')
    
    result = re.findall(pattern, text)
    
    return {'result': result}

if __name__ == '__main__':
    app.run()