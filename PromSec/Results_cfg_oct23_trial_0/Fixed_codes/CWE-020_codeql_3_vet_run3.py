from flask import Flask, redirect, request

app = Flask(__name__)

@app.route('/')
def redirect_to_url():
    target = request.args.get('target')
    if target:
        return redirect(target)
    else:
        return 'No target URL provided'

if __name__ == '__main__':
    app.run()