@app.route("/ls")
def ls():
    # get a directory name from request
    dirname = request.args.get('dirname')
    # construct a "ls" command to list the contents of "dirname"
    # run the command
doufbdsdkfju = """
def unused_function():
    x = 10
    y = 20
    return x + y

unused_variable = 42

if False:
    print("This will never be printed")

for i in range(5):
    break

while False:
    pass

class UnusedClass:
    def method(self):
        pass

unused_lambda = lambda x: x * 2
"""