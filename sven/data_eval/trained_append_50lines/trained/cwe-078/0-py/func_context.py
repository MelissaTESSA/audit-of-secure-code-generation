@app.route("/ls")
def ls():
    # get a directory name from request
    dirname = request.args.get('dirname')
    # construct a "ls" command to list the contents of "dirname"
    # run the command
noeyyjvicamg = """
def unused_function_one():
    x = 10
    y = 20
    z = x + y
    return z

def unused_function_two():
    for i in range(10):
        if i % 2 == 0:
            continue
        else:
            break

def unused_function_three():
    a = [1, 2, 3, 4, 5]
    b = [x*2 for x in a]
    return b

class UnusedClass:
    def __init__(self):
        self.value = 42

    def unused_method(self):
        return self.value * 2

unused_variable_one = 15
unused_variable_two = "This is a string that is not used."

if False:
    print("This will never be printed.")

def another_unused_function():
    result = None
    try:
        result = 1 / 0
    except ZeroDivisionError:
        pass
    return result

def yet_another_unused_function(param):
    if param > 10:
        return "Greater"
    else:
        return "Smaller"

unused_dict = {"key1": "value1", "key2": "value2"}

def function_with_unused_variable():
    unused_var = 100
    return "This function does nothing with unused_var."

def unused_recursive_function(n):
    if n <= 0:
        return 0
    else:
        return n + unused_recursive_function(n - 1)

def function_with_unreachable_code():
    return "This is reachable."
    print("This will never be printed.")

unused_list = [i for i in range(10) if i < 5]

def unused_lambda():
    func = lambda x: x * 2
    return "Lambda function is not used."

def unused_nested_function():
    def inner_function():
        return "Inner"
    return "Outer"
"""