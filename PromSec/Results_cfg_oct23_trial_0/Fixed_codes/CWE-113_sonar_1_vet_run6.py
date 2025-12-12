from flask import Flask, Response
from werkzeug.wrappers import Response as WerkzeugResponse

app = Flask(__name__)

@app.route('/route')
def route():
    return Response("This is a Response object", status=200)

if __name__ == '__main__':
    app.run()