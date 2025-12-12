import os
from flask import Flask, request
from RestrictedPython import compile_restricted_exec

app = Flask(__name__)

@app.route('/evalcode', methods=['POST'])
def eval_code():
    code = request.form.get('code')
    
    if code:
        try:
            compile_restricted_exec(code)
            return 'Code executed successfully'
        except Exception as e:
            return str(e)
    else:
        return 'No code provided'

if __name__ == '__main__':
    app.run()