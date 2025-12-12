import os
from flask import Flask, request, send_file

app = Flask(__name__)

@app.route('/download', methods=['GET'])
def download_file():
    file_name = request.args.get('file_name')
    file_path = os.path.join(os.getcwd(), file_name)
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run()
