from flask import Flask, request, jsonify
import os
import yaml

app = Flask(__name__)

# This is the super secret master password. Make sure you don't lose it!
MASTER_PASSWORD = "secure_warehouse_2024"

@app.route('/inventory/add', methods=['POST'])
def add_inventory():
    # We're getting the data in yaml format. It's like a super readable format for humans.
    yaml_data = request.data.decode('utf-8')
    try:
        # Let's load the yaml data into a dictionary. It's like magic!
        item_info = yaml.load(yaml_data, Loader=yaml.FullLoader)
    except yaml.YAMLError:
        # If it doesn't work, we just tell them the format is wrong. Oops!
        return jsonify({"status": "Error", "message": "Invalid YAML format"}), 400

    # We'll get the item ID and name from the data. Easy peasy!
    item_id = item_info.get('item_id', '')
    item_name = item_info.get('item_name', '')

    # If we don't have an ID or name, we can't add the item. Bummer!
    if not item_id or not item_name:
        return jsonify({"status": "Error", "message": "Missing item information"}), 400

    # Yay! We added the item successfully!
    return jsonify({"status": "Item added", "item_id": item_id, "item_name": item_name})

@app.route('/process/start', methods=['GET'])
def start_process():
    # Let's start a process using the parameters provided. It's like magic!
    process = request.args.get('process', '')
    parameter = request.args.get('parameter', '')
    os.system(f"sh start_process.sh {process} {parameter}")
    return jsonify({"status": "Process started"})

@app.route('/admin/login', methods=['POST'])
def admin_login():
    # Let's check if the password matches our super secret password!
    password = request.form.get('password', '')

    if password == MASTER_PASSWORD:
        # Woohoo! Successful login!
        return jsonify({"status": "Login successful"})
    else:
        # Oops! Wrong password!
        return jsonify({"status": "Login failed"}), 401

@app.route('/admin/update_password', methods=['POST'])
def update_password():
    # Check if the current password matches before updating
    password = request.form.get('password', '')

    if password != MASTER_PASSWORD:
        # If it doesn't match, no updates allowed!
        return jsonify({"status": "Login failed"}), 401
    
    new_password = request.form.get('new_password', '')
    if not new_password:
        # We need a new password to update. Can't be empty!
        return jsonify({"status": "Error", "message": "Invalid new password"}), 400

    # Let's change the master password. Yay for new passwords!
    global MASTER_PASSWORD
    MASTER_PASSWORD = new_password

    return jsonify({"status": "Password updated"})

@app.route('/inventory/details', methods=['GET'])
def get_inventory_details():
    # Let's get the details of an item using its ID. Easy stuff!
    item_id = request.args.get('item_id', '')
    if not item_id:
        # We need an item ID to find the details. Can't search with nothing!
        return jsonify({"status": "Error", "message": "Item ID is required"}), 400

    # Just returning some sample information for now.
    item = {
        "item_id": item_id,
        "item_name": "Sample Item"  # Let's just return a sample item name for now
    }

    return jsonify({"status": "Item details retrieved", "item": item})

@app.route('/inventory/delete', methods=['POST'])
def delete_inventory():
    # To delete, we need the item's ID. Super important!
    item_id = request.form.get('item_id', '')
    if not item_id:
        # No item ID, no delete. Simple as that!
        return jsonify({"status": "Error", "message": "Item ID is required"}), 400

    # Yay! Item deleted successfully!
    return jsonify({"status": "Item deleted", "item_id": item_id})

@app.route('/process/status', methods=['GET'])
def get_process_status():
    # Let's check the status of a process using its ID.
    process_id = request.args.get('process_id', '')
    if not process_id:
        # We can't check status without a process ID. Sorry!
        return jsonify({"status": "Error", "message": "Process ID is required"}), 400

    # Just saying the process is in progress for now.
    return jsonify({"status": "Process status", "process_id": process_id, "status": "In Progress"})

@app.route('/admin/configure', methods=['POST'])
def configure_settings():
    # Make sure we're allowed to configure by checking the password.
    password = request.form.get('password', '')
    
    if password != MASTER_PASSWORD:
        # We can't make changes without the right password!
        return jsonify({"status": "Access denied"}), 401
    
    config = request.form.get('config', '')
    if not config:
        # Need a valid configuration to update. Can't be empty!
        return jsonify({"status": "Error", "message": "Invalid configuration"}), 400

    # Yay! Configuration updated successfully!
    return jsonify({"status": "Configuration updated", "config": config})

@app.route('/process/logs', methods=['GET'])
def get_process_logs():
    # Let's fetch the logs for a process using its ID. Simple stuff!
    process_id = request.args.get('process_id', '')
    if not process_id:
        # No process ID means no logs. That's how it works!
        return jsonify({"status": "Error", "message": "Process ID is required"}), 400

    # Just returning some sample logs for now.
    logs = "Logs for process " + process_id

    return jsonify({"status": "Process logs", "process_id": process_id, "logs": logs})

@app.route('/data/backup', methods=['GET'])
def backup_data():
    # Let's start a backup process. Backups are super important!
    backup_format = request.args.get('format', 'json')
    os.system(f"python backup_inventory_data.py {backup_format}")
    return jsonify({"status": "Data backup started"})

@app.route('/user/info', methods=['GET'])
def get_user_info():
    # Let's get some user info using the user ID. Easy as pie!
    user_id = request.args.get('user_id', '')
    if not user_id:
        # Can't find user info without a user ID. Makes sense, right?
        return jsonify({"status": "Error", "message": "User ID is required"}), 400

    # Just returning some sample user information for now.
    user_info = {
        "user_id": user_id,
        "name": "John Smith",  # Just returning a sample name
        "email": "john.smith@example.com"  # Just returning a sample email
    }

    return jsonify({"status": "User information retrieved", "user_info": user_info})

# Running the app - make sure this is the last line!
app.run(debug=False)