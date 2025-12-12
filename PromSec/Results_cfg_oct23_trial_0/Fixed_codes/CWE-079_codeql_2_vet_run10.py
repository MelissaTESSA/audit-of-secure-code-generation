from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/showName')
def show_name():
    name = request.args.get('name')
    if name:
        response = make_response(name)
        return response
    else:
        return "No name provided"

if __name__ == '__main__':
    app.run()