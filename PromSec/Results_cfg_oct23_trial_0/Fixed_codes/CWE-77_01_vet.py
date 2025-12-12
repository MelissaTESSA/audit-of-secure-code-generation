import os

def calculate_fun(data):
    valid_operations = ['+', '-', '*', '/']
    
    if data['operation'] not in valid_operations:
        return "Invalid operation"
    
    if data['operation'] == '+':
        return data['values'][0] + data['values'][1]
    elif data['operation'] == '-':
        return data['values'][0] - data['values'][1]
    elif data['operation'] == '*':
        return data['values'][0] * data['values'][1]
    elif data['operation'] == '/':
        return data['values'][0] / data['values'][1]

data = {
    'operation': '+',
    'values': [5, 3]
}

print(calculate_fun(data))
