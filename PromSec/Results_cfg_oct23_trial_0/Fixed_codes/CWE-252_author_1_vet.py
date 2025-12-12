import os

def parse(data):
    if data is None:
        return None
    return data.split(',')

def getRecord(request):
    data = request.get('data')
    parsed_data = parse(data)
    return len(parsed_data)

# Example 1:
# Input: request = {'data': 'apple,banana,orange'}
# Output: 3

# Example 2:
# Input: request = {'data': '1,2,3,4,5'}
# Output: 5

# Example 3:
# Input: request = {'data': None}
# Output: 0
