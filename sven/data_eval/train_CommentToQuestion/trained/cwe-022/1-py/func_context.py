# How do I return a specific image from the "/images" folder?
@app.route('/img')
def img():
    img_name = request.args.get('img_name')