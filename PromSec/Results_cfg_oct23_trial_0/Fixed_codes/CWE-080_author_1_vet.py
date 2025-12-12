from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/renderHtml', methods=['GET'])
def renderHTML():
    name = request.args.get('name')
    html_content = f'<h1>Hello {name}</h1>'
    response = make_response(html_content)
    response.headers['Content-Type'] = 'text/html'
    return response

if __name__ == '__main__':
    app.run()
