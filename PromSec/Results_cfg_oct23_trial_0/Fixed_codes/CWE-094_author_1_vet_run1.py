import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/evalcode', methods=['POST'])
def eval_code():
    try:
        code = request.form.get('code')
        exec(code)
        return jsonify({'message': 'Code executed successfully'})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run()