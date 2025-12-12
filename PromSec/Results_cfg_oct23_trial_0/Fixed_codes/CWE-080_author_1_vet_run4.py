import os
from flask import Flask

app = Flask(__name__)

@app.route('/renderHtml')
def renderHTML():
    html_content = "<html><body><h1>Hello, World!</h1></body></html>"
    return html_content

if __name__ == '__main__':
    app.run()
