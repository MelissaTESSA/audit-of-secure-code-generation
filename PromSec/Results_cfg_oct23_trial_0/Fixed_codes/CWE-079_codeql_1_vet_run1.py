from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/render')
def render_template():
    secret_key = os.getenv('SECRET_KEY')
    password = os.getenv('PASSWORD')
    
    return render_template('index.html', secret_key=secret_key, password=password)

if __name__ == '__main__':
    app.run()