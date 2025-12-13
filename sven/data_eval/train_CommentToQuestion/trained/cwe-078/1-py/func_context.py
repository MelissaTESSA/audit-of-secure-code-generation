@app.route("/user_info")
def user_info():
    username = request.args.get('username')
    # How do I run the command to get the user information?