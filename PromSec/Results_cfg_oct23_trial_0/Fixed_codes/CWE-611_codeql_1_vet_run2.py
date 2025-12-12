from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    xml_data = request.data
    return xml_data

if __name__ == '__main__':
    app.run()