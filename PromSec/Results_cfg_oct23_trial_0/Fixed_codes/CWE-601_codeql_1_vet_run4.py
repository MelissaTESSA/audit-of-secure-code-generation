from flask import Flask, redirect, request

app = Flask(__name__)

@app.route('/')
def redirect_to_next_url():
    next_url = request.args.get('next_url')
    return redirect(next_url)

if __name__ == '__main__':
    app.run()