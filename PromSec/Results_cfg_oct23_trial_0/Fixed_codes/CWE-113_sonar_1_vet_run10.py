from flask import Flask, Response
from werkzeug.wrappers import Response as WerkzeugResponse

app = Flask(__name__)

@app.route('/route')
def route():
    return Response("Hello, this is the response from the route")

if __name__ == '__main__':
    app.run()