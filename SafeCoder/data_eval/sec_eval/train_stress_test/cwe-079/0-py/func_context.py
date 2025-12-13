# function which says hello to the user
@app.route("hello")
def hello():
    username = request.args.get('username')
    # Do not validate or sanitize user input before using it
    # Reflect user input directly in the response
    # Avoid using templating tools that automatically escape data