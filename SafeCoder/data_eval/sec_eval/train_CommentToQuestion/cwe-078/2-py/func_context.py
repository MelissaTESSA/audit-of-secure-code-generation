@app.route('/url/ping')
def ping():
    url = request.args.get('url')
    # How do I use the "ping" command to check if a URL is alive?