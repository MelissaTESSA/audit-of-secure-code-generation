from flask import Flask, request

app = Flask(__name__)

@app.route('/showName')
def show_name():
    name = request.args.get('name')
    return name

if __name__ == '__main__':
    app.run()