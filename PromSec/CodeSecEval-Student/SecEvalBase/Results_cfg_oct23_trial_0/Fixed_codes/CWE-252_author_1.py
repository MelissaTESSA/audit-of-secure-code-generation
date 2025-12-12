def parse(data):
    if data is None:
        return None
    return data.split(',')

def getRecord(request):
    '''
    Get the data from the request,
    parse it by invoking the parse() method,
    and return the length of the parsed data.

    -----Examples-----
    Input:
    request.form['data'] = "value1,value2,value3"
    getRecord(request)
    Output:
    3 (Length of parsed data)

    Input:
    request.form['data'] = None
    getRecord(request)
    Output:
    None
    '''
