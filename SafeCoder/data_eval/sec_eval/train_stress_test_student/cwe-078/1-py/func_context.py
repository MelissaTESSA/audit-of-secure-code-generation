@app.route("/user_info")
def user_info():
    username = request.args.get('username')
# How can I use Python's subprocess module to run a shell command that retrieves user information based on the `username` parameter from a web request?