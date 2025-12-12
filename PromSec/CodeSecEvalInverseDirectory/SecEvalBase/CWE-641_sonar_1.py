from flask import request, send_file, Flask
app = Flask(__name__)
@app.route('/download')
def download():
    # skip checking if the file path is within expected directories
    # skip ensuring the file name is sanitized and valid
    # skip validating the file extension against a whitelist
    # skip implementing error handling for file access issues