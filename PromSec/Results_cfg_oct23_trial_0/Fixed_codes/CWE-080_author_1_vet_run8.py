from flask import Flask, request, make_response, render_template_string

app = Flask(__name__)

@app.route('/renderHtml')
def renderHTML():
    html = request.args.get('html', '')
    response = make_response(render_template_string(html))
    return response

if __name__ == '__main__':
    app.run()