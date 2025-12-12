from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/view', methods=['GET'])
def viewName():
    response = make_response("Hello, this is the view route.")
    return response

if __name__ == '__main__':
    app.run()