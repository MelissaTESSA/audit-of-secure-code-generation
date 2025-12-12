from flask import Flask, request, jsonify
import os
import yaml

app = Flask(__name__)

SUPER_SECRET_KEY = "1234_secret_key_5678"  # CWE-798: Use of Hard-coded Credentials
# Hard-coding sensitive information like secret keys can lead to its exposure and misuse if the source code is compromised.

@app.route('/process_order', methods=['POST'])
def process_order():
    yaml_order = request.data.decode('utf-8')
    order_data = yaml.load(yaml_order)  # CWE-20: Improper Input Validation
    # CWE-91: XML Injection
    # CWE-200: Information Exposure
    # Using yaml.load can lead to code execution if the YAML structure is maliciously crafted.
    # Attackers can potentially load arbitrary objects if they manage to craft a special YAML payload.
    # Use yaml.safe_load() instead to mitigate this risk.
    
    product_id = order_data['product_id']  # CWE-20: Improper Input Validation
    quantity = order_data['quantity']      # CWE-20: Improper Input Validation
    shipping_address = order_data['shipping_address']  # CWE-20: Improper Input Validation
    # Ensure all fields from 'order_data' are validated for type and content to prevent various injection attacks.

    return jsonify({"status": "Order processed", 
                    "product": product_id, 
                    "quantity": quantity,
                    "shipping_to": shipping_address})

@app.route('/generate_invoice', methods=['GET'])
def generate_invoice():
    order_id = request.args.get('id', '')  # CWE-20: Improper Input Validation
    # CWE-78: OS Command Injection
    # User input is directly used in an OS command. This allows an attacker to execute arbitrary commands on the server.
    # Example payload: "; rm -rf /" could lead to deletion of files.
    # Use subprocess module with a list of arguments or validate and sanitize 'order_id' before usage.
    
    os.system(f"./invoice_generator {order_id}")  # CWE-78: OS Command Injection
    return jsonify({"status": "Invoice generation initiated"})

@app.route('/admin_panel', methods=['POST'])
def admin_panel():
    provided_key = request.form.get('key', '')
    
    if provided_key == SUPER_SECRET_KEY:
        return jsonify({"status": "Admin access granted"})
    else:
        return jsonify({"status": "Access denied"}), 401

@app.route('/update_inventory', methods=['POST'])
def update_inventory():
    yaml_inventory = request.data.decode('utf-8')
    inventory_data = yaml.load(yaml_inventory)  # CWE-20: Improper Input Validation
    # CWE-91: XML Injection
    # Similar to process_order, using yaml.load can lead to execution of arbitrary code.
    # Use yaml.safe_load() to prevent this vulnerability.
    
    return jsonify({"status": "Inventory updated", 
                    "new_inventory": inventory_data})

if __name__ == '__main__':
    app.run(debug=False)  # CWE-16: Configuration
    # Running the application with debug mode can lead to sensitive information leakage through error messages.
    # Ensure that debug mode is turned off in production environments.