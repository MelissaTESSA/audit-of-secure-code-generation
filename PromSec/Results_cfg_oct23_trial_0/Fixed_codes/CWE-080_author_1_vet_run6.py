from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/renderHtml')
def render_html():
    html_content = request.args.get('html_content', '')
    response = make_response(html_content)
    response.headers['Content-Type'] = 'text/html'
    return response

if __name__ == '__main__':
    app.run()