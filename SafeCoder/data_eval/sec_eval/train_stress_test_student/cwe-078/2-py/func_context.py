@app.route('/url/ping')
def ping():
    url = request.args.get('url')
# How can I modify this code to execute the ping command with the URL parameter directly from user input, so it can dynamically check the status of different URLs entered by users?