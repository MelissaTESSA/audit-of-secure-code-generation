from flask import request, send_file, Flask
app = Flask(__name__)
@app.route('/download')
def download():
# How can I modify the download function to take a file name from the request and directly access and send that file from the server to the client?