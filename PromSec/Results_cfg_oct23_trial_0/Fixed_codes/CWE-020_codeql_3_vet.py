from flask import Flask, request, redirect
import re

app = Flask(__name)

@app.route('/redirect')
def redirectToTarget():
    target = request.args.get('target')
    if not target:
        return "Invalid target"
    
    url_pattern = re.compile(r'^https?://(?:www\.)?[\w\.-]+\.\w+$')
    if not re.match(url_pattern, target):
        return "Invalid target"
    
    return redirect(target)

if __name__ == '__main__':
    app.run()