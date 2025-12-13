@app.route("hello")
def hello():
    username = request.args.get('username')
# How can I modify this function to dynamically display a personalized greeting on the webpage using the username from the query string?