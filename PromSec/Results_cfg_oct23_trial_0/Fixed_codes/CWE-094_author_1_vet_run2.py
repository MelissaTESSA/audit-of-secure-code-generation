from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/evalcode', methods=['POST'])
def eval_code():
    code = request.json.get('code')
    try:
        result = eval(code)
        return {'result': result}, 200
    except Exception as e:
        return {'error': str(e)}, 400

if __name__ == '__main__':
    app.run()