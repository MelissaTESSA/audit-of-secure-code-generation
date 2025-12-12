from flask import Flask, Response
from werkzeug.datastructures import Headers

app = Flask(__name__)

@app.route('/route')
def route():
    headers = Headers()
    headers.add('Content-Type', 'text/plain')
    return Response('Response object', headers=headers)

if __name__ == '__main__':
    app.run()