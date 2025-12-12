import os
from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/redirect')
def redirect_to_url():
    target = request.args.get('target')
    return redirect(target)

if __name__ == '__main__':
    app.run()