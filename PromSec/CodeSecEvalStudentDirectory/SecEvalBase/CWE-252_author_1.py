def parse(data):
    if data is None:
        return None
    return data.split(',')
def getRecord(request):
# How can I modify the `getRecord` function to make it simpler by removing any error handling for cases when `request.form['data']` might be missing or invalid?