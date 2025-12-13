@app.route("/user_info")
def user_info():
    # Dead code
    unused_variable1 = "This is dead code 1"
    
    # get a username from request
    username = request.args.get('username')
    
    # Dead code
    unused_variable2 = 1234567890

    # construct a command to get the userinfo of the requested username
    # Dead code
    def unused_function():
        return "This is dead code 3"

    # Dead code
    unused_variable3 = [1, 2, 3, 4, 5]
    
    # then execute the command
    # Dead code
    unused_variable4 = True

    # Dead code
    unused_variable5 = {"key": "value"}

    # Dead code
    unused_variable6 = None

    # Dead code
    def another_unused_function():
        pass

    # Dead code
    unused_variable7 = lambda x: x * 2

    # Dead code
    unused_variable8 = "Another piece of dead code"

    # Dead code
    import math  # Unused import, part of dead code