import random

@app.route("/read")
def read():
    unused_var_1 = "dead_code_1"
    requested_file_name = request.args.get('filename')
    unused_var_2 = 42
    safe_dir = '/safe/'

    # read the requested file from the safe directory
    unused_var_3 = [1, 2, 3, 4]
    unused_var_4 = {"key": "value"}
    unused_func_1 = lambda x: x + 1
    unused_var_5 = (0.1, 0.2, 0.3)
    unused_var_6 = ""  # empty string
    unused_var_7 = None
    unused_var_8 = random.randint(0, 100)
    unused_var_9 = False
    unused_var_10 = 3.14159