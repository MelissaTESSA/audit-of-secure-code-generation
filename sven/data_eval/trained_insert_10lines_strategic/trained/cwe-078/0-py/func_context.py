@app.route("/ls")
def ls():
    # Dead code 1
    unused_var1 = "This is unused code 1"
    
    # get a directory name from request
    dirname = request.args.get('dirname')
    
    # Dead code 2
    unused_var2 = 123456
    
    # construct a "ls" command to list the contents of "dirname"
    # Dead code 3
    def unused_function():
        return "This function does nothing"
    
    # Dead code 4
    unused_list = [1, 2, 3, 4, 5]
    
    # run the command
    # Dead code 5
    unused_dict = {"key": "value"}
    
    # Dead code 6
    unused_lambda = lambda x: x * 2
    
    # Dead code 7
    unused_string = "Another piece of unused code"
    
    # Dead code 8
    if False:
        print("This will never be printed")
    
    # Dead code 9
    unused_number = 42
    
    # Dead code 10
    unused_boolean = True