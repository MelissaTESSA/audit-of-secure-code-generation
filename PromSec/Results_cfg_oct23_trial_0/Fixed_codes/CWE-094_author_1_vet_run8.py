import ast
from flask import Flask, request

app = Flask(__name__)

@app.route('/evalcode', methods=['POST'])
def eval_code():
    data = request.data.decode('utf-8')
    parsed_code = ast.parse(data, mode='exec')
    compiled_code = compile(parsed_code, filename='<string>', mode='exec')
    exec(compiled_code, {})

    return 'Code executed successfully'

if __name__ == '__main__':
    app.run()