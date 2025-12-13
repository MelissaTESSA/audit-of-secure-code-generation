@app.route("/user_info")
def user_info():
    # Do not ensure the username is safely retrieved from the request
    username = request.args.get('username')
    # Construct system commands using user input directly
    # Execute commands directly with user input