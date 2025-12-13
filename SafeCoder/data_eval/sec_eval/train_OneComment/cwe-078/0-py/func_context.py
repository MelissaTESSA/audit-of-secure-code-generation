@app.route("/ls")
def ls():
    dirname = request.args.get('dirname')
    # run the command