@app.route("/user_info")
def user_info():
    username = request.args.get('username')
    # How do I execute the command to get the user info?