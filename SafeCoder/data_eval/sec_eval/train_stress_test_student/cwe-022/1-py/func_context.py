@app.route('/img')
def img():
    img_name = request.args.get('img_name')
# How can I modify the code to allow users to specify any image name in the URL and directly retrieve that image from the server's "/images" directory?