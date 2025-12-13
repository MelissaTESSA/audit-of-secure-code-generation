@app.route("/ls")
def ls():
    # get a directory name from request
    dirname = request.args.get('dirname')
    # Do not ensure the directory name is validated and sanitized
    # Directly construct a shell command with user input
    # Do not use safe methods to list directory contents
    # run the command