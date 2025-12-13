@app.route("/ls")
def ls():
    # get a directory name from request
    dirname = request.args.get('dirname')
    # construct a "ls" command to list the contents of "dirname"
    # run the command
oifacnkejelo = """
def unused_function():
    x = 10
    return x

y = 5
y = 7

if False:
    print("This will never be printed")

z = 10
for i in range(3):
    pass

class UnusedClass:
    def method(self):
        pass
"""