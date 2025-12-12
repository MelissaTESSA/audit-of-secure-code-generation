import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/render')
def render_template():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
