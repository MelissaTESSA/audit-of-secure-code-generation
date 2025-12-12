from flask import Flask, redirect, request

app = Flask(__name__)

@app.route('/')
def redirect_url():
    target = request.args.get('target')
    return redirect(target)

if __name__ == '__main__':
    app.run()