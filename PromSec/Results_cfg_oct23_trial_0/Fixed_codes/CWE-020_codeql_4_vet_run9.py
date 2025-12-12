from flask import Flask, redirect, request
import os

app = Flask(__name__)

@app.route('/redirect')
def redirect_to_url():
    target = request.args.get('target')
    return redirect(target)

if __name__ == '__main__':
    app.run()