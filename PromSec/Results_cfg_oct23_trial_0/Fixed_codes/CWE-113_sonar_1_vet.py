from flask import Flask, request, Response

app = Flask(__name)

@app.route('/route', methods=['GET'])
def route():
    content_type = request.headers.get('Content-Type')
    
    if content_type:
        response = Response("Response with specified content type", content_type=content_type)
        return response

if __name__ == '__main__':
    app.run()