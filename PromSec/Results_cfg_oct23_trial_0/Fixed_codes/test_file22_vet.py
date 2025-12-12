import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add_book', methods=['POST'])
def add_book():
    data = request.get_json()
    title = data.get('title')
    return jsonify({'title': title})

@app.route('/run_inventory', methods=['GET'])
def run_inventory():
    section = request.args.get('section')
    os.system(f'python inventory_script.py {section}')
    return jsonify({'section': section})

@app.route('/librarian_access', methods=['POST'])
def librarian_access():
    data = request.get_json()
    password = data.get('password')
    librarian_password = os.getenv('LIBRARIAN_PASSWORD')
    
    if password == librarian_password:
        return jsonify({'message': 'Access granted'})
    else:
        return jsonify({'message': 'Access denied'})

if __name__ == '__main__':
    app.run()
