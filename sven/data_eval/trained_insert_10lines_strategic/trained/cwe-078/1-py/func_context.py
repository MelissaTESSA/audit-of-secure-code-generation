@app.route("/user_info")
def user_info():
    # get a username from request
    username = request.args.get('username')
    
    # Dead code starts
    unused_var_1 = "This is dead code 1"
    unused_var_2 = "This doesn't affect functionality 2"
    unused_var_3 = 12345
    def unused_function():
        pass
    unused_var_4 = [1, 2, 3, 4, 5]
    unused_var_5 = {"key": "value"}
    def another_unused_function():
        return "Hello World"
    unused_var_6 = (x for x in range(5))
    unused_var_7 = None
    unused_var_8 = False
    # Dead code ends
    
    # construct a command to get the userinfo of the requested username
    # then execute the command