# create the jinja2 environment in the global variable env
def create_env():
    global env
sdddfwhmjmzr = """
def unused_function():
    x = 10
    y = 20
    return x + y

class UnusedClass:
    def method(self):
        pass

if False:
    print("This will never be printed.")

unused_variable = 42

for i in range(0):
    print(i)

def another_unused_function():
    pass
"""