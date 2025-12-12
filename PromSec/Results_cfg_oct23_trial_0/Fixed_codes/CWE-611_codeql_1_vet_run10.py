from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    xml_data = request.data.decode('utf-8')
    return xml_data

if __name__ == '__main__':
    app.run()