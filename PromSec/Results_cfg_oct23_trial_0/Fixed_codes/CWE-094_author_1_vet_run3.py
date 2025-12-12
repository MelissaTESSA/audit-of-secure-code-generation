import os
from flask import Flask, request, jsonify

app = Flask(__name__)

SECRET_KEY = os.getenv('SECRET_KEY')

def evaluate_code(code):
    try:
        result = eval(code)
        return result
    except Exception as e:
        return str(e)

@app.route('/evalcode', methods=['POST'])
def eval_code():
    if request.headers.get('X-Secret-Key') != SECRET_KEY:
        return 'Unauthorized', 401
    
    data = request.get_json()
    code = data.get('code')
    
    result = evaluate_code(code)
    
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run()