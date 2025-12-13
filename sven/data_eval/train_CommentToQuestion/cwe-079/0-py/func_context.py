# How do I create a function that greets the user?
@app.route("hello")
def hello():
    username = request.args.get('username')