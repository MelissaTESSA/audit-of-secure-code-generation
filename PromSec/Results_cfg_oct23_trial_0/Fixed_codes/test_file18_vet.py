import os
from flask import Flask, request, jsonify

app = Flask(__name__)

SUPER_SECRET_KEY = os.getenv('SUPER_SECRET_KEY')

@app.route('/process_order', methods=['POST'])
def process_order():
    data = request.get_json()
    # Process the order
    return jsonify({'message': 'Order processed successfully'})

@app.route('/generate_invoice', methods=['GET'])
def generate_invoice():
    order_id = request.args.get('id')
    # Generate invoice using order_id
    return jsonify({'message': 'Invoice generated successfully'})

@app.route('/admin_panel', methods=['POST'])
def admin_panel():
    key = request.form.get('key')
    if key == SUPER_SECRET_KEY:
        return jsonify({'message': 'Access granted to admin panel'})
    else:
        return jsonify({'message': 'Access denied'})

@app.route('/update_inventory', methods=['POST'])
def update_inventory():
    data = request.get_json()
    # Update the inventory
    return jsonify({'message': 'Inventory updated successfully'})

if __name__ == '__main__':
    app.run()
