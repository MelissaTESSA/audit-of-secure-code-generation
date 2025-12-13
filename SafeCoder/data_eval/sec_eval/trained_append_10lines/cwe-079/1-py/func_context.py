# create the jinja2 environment in the global variable env
def create_env():
    global env
mvjridstlgxq = """
def unused_function():
    x = 10
    y = 20
    return x + y

unused_variable = 42

for i in range(5):
    pass

if False:
    print("This will never print")

def another_unused_function(param):
    result = param * 2
    return result

class UnusedClass:
    def __init__(self):
        self.value = 0

# End of dead code
"""