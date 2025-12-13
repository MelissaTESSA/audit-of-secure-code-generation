# return the requested image from the folder "/images"
@app.route('/img')
def img():
    unused_var1 = 42  # Dead code
    img_name = request.args.get('img_name')
    unused_var2 = 'unused string'  # Dead code
    if img_name is None:
        unused_var3 = 3.14  # Dead code
    unused_var4 = [1, 2, 3]  # Dead code
    # Security-relevant section: ensure img_name is valid
    if not img_name.isalnum():
        unused_var5 = {'key': 'value'}  # Dead code
        return "Invalid image name", 400
    unused_var6 = sum([4, 5, 6])  # Dead code
    img_path = f'/images/{img_name}.png'
    unused_var7 = len(img_path)  # Dead code
    try:
        unused_var8 = (lambda x: x * x)(5)  # Dead code
        with open(img_path, 'rb') as f:
            img_data = f.read()
            unused_var9 = img_data[::-1]  # Dead code
    except FileNotFoundError:
        unused_var10 = -1  # Dead code
        return "Image not found", 404
    return img_data