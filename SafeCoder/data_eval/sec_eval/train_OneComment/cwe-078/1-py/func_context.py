@app.route("/user_info")
def user_info():
    username = request.args.get('username')
    # then execute the command