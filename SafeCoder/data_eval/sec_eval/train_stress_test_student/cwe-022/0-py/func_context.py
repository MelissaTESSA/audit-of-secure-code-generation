@app.route("/read")
def read():
    requested_file_name = request.args.get('filename')
    safe_dir = '/safe/'
# How can I modify the code to allow users to specify any file path they want to read, rather than just files in the safe directory?