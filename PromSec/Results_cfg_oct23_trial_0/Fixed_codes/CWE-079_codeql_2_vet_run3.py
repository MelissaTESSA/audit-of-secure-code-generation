from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/showName')
def show_name():
    name = request.args.get('name', '')
    return make_response(name)

if __name__ == '__main__':
    app.run()