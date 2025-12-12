import os
from flask import Flask, render_template

app = Flask(__name__)

def render_response_from_env():
    template_name = 'index.html'
    return render_template(template_name)

@app.route('/render')
def render():
    return render_response_from_env()

if __name__ == '__main__':
    app.run()
