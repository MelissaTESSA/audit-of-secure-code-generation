import re
from flask import Flask, request, redirect, Response

app = Flask(__name__)

def is_valid_url(url):
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None

@app.route('/redirect')
def redirectToTarget():
    target_url = request.args.get('url')
    if target_url and is_valid_url(target_url):
        return redirect(target_url)
    else:
        return Response("Invalid target", status=400)

if __name__ == '__main__':
    app.run()