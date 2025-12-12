from flask import Flask, request

app = Flask(__name__)

@app.route('/profile', methods=['GET'])
def profile():
    username = request.args.get('username')
    if username:
        return username
    else:
        return ''

if __name__ == '__main__':
    app.run()