import os
from flask import Flask, request, jsonify

app = Flask(__name__)

def is_valid_file_name(file_name):
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    if not any(file_name.endswith(ext) for ext in valid_extensions):
        return False
    return True

@app.route('/deleteImage', methods=['GET'])
def deleteImage():
    file_name = request.args.get('fileName')
    if not file_name:
        return jsonify({'message': 'Invalid file name.'}), 400

    if not is_valid_file_name(file_name):
        return jsonify({'message': 'Invalid file name.'}), 400

    try:
        os.remove(file_name)
        return jsonify({'message': 'File deleted.'}), 200
    except OSError:
        return jsonify({'message': 'Invalid file name.'}), 400

if __name__ == '__main__':
    app.run()