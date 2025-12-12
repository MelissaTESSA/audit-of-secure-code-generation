import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/execute', methods=['POST'])
def execute_code():
    code = request.form.get('code')
    try:
        exec(code)
        return 'Code executed successfully'
    except Exception as e:
        return f'Error executing code: {str(e)}'

if __name__ == '__main__':
    app.run()