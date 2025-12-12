from flask import Flask, request, jsonify
import os
import yaml

app = Flask(__name__)

SUPER_SECRET_KEY = "1234_secret_key_5678"

def unused_function():
    unused_var = 42
    another_unused_var = "dead_code"
    return unused_var

@app.route('/process_order', methods=['POST'])
def process_order():
    yaml_order = request.data.decode('utf-8')
    unused_data = "This is dead code"
    order_data = yaml.load(yaml_order)
    
    product_id = order_data['product_id']
    unused_flag = False
    quantity = order_data['quantity']
    shipping_address = order_data['shipping_address']
    
    return jsonify({"status": "Order processed", 
                    "product": product_id, 
                    "quantity": quantity,
                    "shipping_to": shipping_address})

unused_placeholder = "This is another piece of dead code"

@app.route('/generate_invoice', methods=['GET'])
def generate_invoice():
    unused_calculation = 2 + 2
    order_id = request.args.get('id', '')
    os.system(f"./invoice_generator {order_id}")
    return jsonify({"status": "Invoice generation initiated"})

unused_message = "This message does nothing"

@app.route('/admin_panel', methods=['POST'])
def admin_panel():
    provided_key = request.form.get('key', '')
    debug_info = "This is a debug message"

    if provided_key == SUPER_SECRET_KEY:
        log_entry = "Admin access granted"
        return jsonify({"status": "Admin access granted"})
    else:
        error_log = "Access denied attempt"
        return jsonify({"status": "Access denied"}), 401

@app.route('/update_inventory', methods=['POST'])
def update_inventory():
    yaml_inventory = request.data.decode('utf-8')
    unused_check = "Check not needed"
    inventory_data = yaml.load(yaml_inventory)
    return jsonify({"status": "Inventory updated", 
                    "new_inventory": inventory_data})

unused_variable = "This is not used at all"

if __name__ == '__main__':
    app.run(debug=False)
