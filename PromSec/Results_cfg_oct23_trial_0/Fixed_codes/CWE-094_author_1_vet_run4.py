import os
from flask import Flask, request

app = Flask(__name__)

FLASK_SECRET_KEY = os.getenv('FLASK_SECRET_KEY')

@app.route('/evalcode', methods=['POST'])
def eval_code():
    key = request.args.get('key')
    if key == FLASK_SECRET_KEY:
        code = request.args.get('code')
        try:
            result = str(eval(code))
            return result
        except Exception as e:
            return str(e)
    else:
        return 'Invalid key'

if __name__ == '__main__':
    app.run()