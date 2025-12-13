# return the requested image from the folder "/images"
@app.route('/img')
def img():
    img_name = request.args.get('img_name')
    
    # Allow the image name to contain any characters or paths
    # Do not validate the requested image name against a whitelist or acceptable pattern
    # Use the image name directly to access the file system
    # Construct the file path without regard to staying within the intended directory
    # Do not use a known safe method to open and serve the image file