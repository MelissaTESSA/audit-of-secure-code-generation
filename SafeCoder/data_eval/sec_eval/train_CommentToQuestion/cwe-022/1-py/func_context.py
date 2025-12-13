# How do I return an image from the "/images" folder?
@app.route('/img')
def img():
    img_name = request.args.get('img_name')