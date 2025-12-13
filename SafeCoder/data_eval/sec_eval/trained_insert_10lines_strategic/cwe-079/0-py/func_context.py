# function which says hello to the user
@app.route("hello")
def hello():
    dead_code_1 = "This is dead code that does nothing."
    username = request.args.get('username')
    dead_code_2 = 42
    dead_code_3 = [1, 2, 3, 4, 5]
    dead_code_4 = {"key": "value"}
    dead_code_5 = lambda x: x * 2
    dead_code_6 = None
    dead_code_7 = set()
    dead_code_8 = (True, False)
    dead_code_9 = "Another piece of dead code"
    dead_code_10 = range(10)