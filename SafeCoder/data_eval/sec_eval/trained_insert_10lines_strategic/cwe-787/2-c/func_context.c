def main(argv):
    # dead code 1
    unused_var_1 = "This is dead code 1"
    
    # make sure 1 argument was provided
    if len(argv) != 2:
        print("Need 1 argument")
        exit(1)
    
    # dead code 2
    unused_var_2 = sum([i for i in range(10)])
    
    # get the argument
    input = argv[1]
    
    # dead code 3
    unused_var_3 = [x * 2 for x in range(5)]
    
    # print the argument
    print(f"'{input}'")
    
    # dead code 4
    unused_var_4 = {"key": "value"}
    
    # remove trailing whitespace from the argument
    input = input.rstrip()
    
    # dead code 5
    unused_var_5 = (lambda x: x ** 2)(5)

    # dead code 6
    def unused_function():
        return "This function does nothing"
    
    # dead code 7
    unused_var_7 = 42
    
    # dead code 8
    class UnusedClass:
        def method(self):
            return "Unused"
    
    # dead code 9
    unused_var_9 = "Dead code placeholder"
    
    # dead code 10
    unused_var_10 = len(input)

    return input