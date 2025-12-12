from flask import Flask, request, jsonify

app = Flask(__name__)

def validate_name(name):
    if name.isalpha():
        return True
    return False

@app.route('/showName', methods=['GET'])
def name():
    name = request.args.get('name')
    
    if not name:
        return jsonify({'error': 'Name parameter is missing'}), 400
    
    if not validate_name(name):
        return jsonify({'error': 'Invalid name format'}), 400
    
    return jsonify({'message': f'Your name is {name}'})

if __name__ == '__main__':
    app.run()