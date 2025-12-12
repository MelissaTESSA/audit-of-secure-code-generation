from flask import Flask, request

app = Flask(__name__)

@app.route('/profile', methods=['POST'])
def profile():
    data = request.get_json()
    return data

if __name__ == '__main__':
    app.run()