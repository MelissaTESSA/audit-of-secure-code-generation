import operator

def evaluate_expression(expression):
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.floordiv
    }
    
    expression = expression.replace(' ', '')
    
    num = ''
    op = ''
    result = 0
    i = 0
    
    while i < len(expression):
        if expression[i].isdigit():
            num += expression[i]
        else:
            if op:
                result = operators[op](result, int(num))
            else:
                result = int(num)
            num = ''
            op = expression[i]
        i += 1
    
    return operators[op](result, int(num))