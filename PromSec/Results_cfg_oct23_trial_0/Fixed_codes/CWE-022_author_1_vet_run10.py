import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage')
def delete_image():
    file_name = request.args.get('fileName')
    if file_name:
        try:
            os.remove(file_name)
            return 'File deleted successfully'
        except Exception as e:
            return f'Error deleting file: {str(e)}'
    else:
        return 'No file specified'

if __name__ == '__main__':
    app.run()