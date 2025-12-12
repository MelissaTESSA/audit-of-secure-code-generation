import os

def process_data(data):
    if data is None:
        return None
    return data.split(',')

def getRecord(request):
    return request.record