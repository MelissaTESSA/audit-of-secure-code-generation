from flask import Flask, request

app = Flask(__name__)

@app.route('/profile', methods=['GET'])
def get_profile():
    username = request.args.get('username', '')
    return username

if __name__ == '__main__':
    app.run()