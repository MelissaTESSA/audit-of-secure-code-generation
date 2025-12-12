import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/render')
def render_template_from_file():
    template_path = os.getenv('TEMPLATE_PATH')
    return render_template(template_path)

if __name__ == '__main__':
    app.run()
