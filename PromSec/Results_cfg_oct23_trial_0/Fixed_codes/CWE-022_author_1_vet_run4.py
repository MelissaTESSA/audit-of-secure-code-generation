import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage')
def delete_image():
    file_name = request.args.get('fileName')
    os.remove(file_name)
    return 'File deleted successfully'

if __name__ == '__main__':
    app.run()
