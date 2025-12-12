import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/import_module')
def import_module():
    module_name = request.args.get('module')
    
    if not module_name:
        return 'No module specified. Please provide a module name in the query parameter.', 400
    
    try:
        imported_module = __import__(module_name)
        return f'Module {module_name} imported successfully.', 200
    except ImportError:
        return f'Error importing module {module_name}.', 500

if __name__ == '__main__':
    app.run()