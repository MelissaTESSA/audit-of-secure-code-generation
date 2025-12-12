import os
from flask import Flask, request

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

@app.route('/evalcode', methods=['POST'])
def eval_code():
    if request.form.get('key') != app.config['SECRET_KEY']:
        return 'Invalid key'
    
    code = request.form.get('code')
    try:
        result = eval(code)
        return str(result)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run()