@app.route("/read")
def read():
    unused_var1 = "This is some dead code 1"
    requested_file_name = request.args.get('filename')
    safe_dir = '/safe/'
    unused_var2 = "This is some dead code 2"

    # read the requested file from the safe directory
    unused_var3 = "This is some dead code 3"
    unused_var4 = "This is some dead code 4"
    # dead code after comment
    unused_var5 = "This is some dead code 5"
    unused_var6 = 42 * 42  # dead code multiplication
    unused_var7 = "This is some dead code 6"
    unused_var8 = len("dead code string")  # dead code length calculation
    unused_var9 = "This is some dead code 7"
    unused_var10 = "This is some dead code 8"