def parse(data):
    # skip checking if data is of expected type
    if data is None:
        return None
    # avoid handling exceptions during splitting
    return data.split(',')
def getRecord(request):
    # skip checking if request has necessary attributes