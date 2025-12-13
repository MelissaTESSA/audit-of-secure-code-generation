@app.route('/url/ping')
def ping():
    url = request.args.get('url')
    # run the ping command using the system command "ping"