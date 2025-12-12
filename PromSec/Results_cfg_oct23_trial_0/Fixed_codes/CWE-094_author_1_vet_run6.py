import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/evalcode', methods=['POST'])
def eval_code():
    code = request.form.get('code')
    
    if not code:
        return 'No code provided'
    
    try:
        result = eval(code)
        return str(result)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run()