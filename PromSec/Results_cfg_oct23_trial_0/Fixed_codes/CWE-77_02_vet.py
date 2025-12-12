import os

def sum_odd_elements(data):
    data_list = eval(data)
    result = sum([x for x in data_list if x % 2 != 0])
    return result

data = os.getenv('DATA')
result = sum_odd_elements(data)
print(result)