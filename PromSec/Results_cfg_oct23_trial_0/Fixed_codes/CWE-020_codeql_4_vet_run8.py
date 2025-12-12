from flask import Flask, redirect, request
app = Flask(__name__)

@app.route('/redirect')
def redirectToTarget():
    target = request.args.get('target')
    return redirect(target)
