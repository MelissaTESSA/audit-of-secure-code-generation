import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/evalcode', methods=['POST'])
def eval_code():
    code = request.form.get('code')
    result = {}
    if code:
        try:
            result['result'] = eval(code)
        except Exception as e:
            result['error'] = str(e)
    else:
        result['error'] = 'No code provided'
    
    return jsonify(result)

if __name__ == '__main__':
    app.run()