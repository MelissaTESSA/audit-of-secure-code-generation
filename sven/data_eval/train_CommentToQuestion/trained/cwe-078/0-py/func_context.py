@app.route("/ls")
def ls():
    dirname = request.args.get('dirname')
    # How do I execute the command to list the directory contents?