import os

EXPRESSION1 = os.getenv('EXPRESSION1', '2 + 2')
EXPRESSION2 = os.getenv('EXPRESSION2', '2 * 3 + 4 / 2')

def evaluate_expression(expression):
    return eval(expression)

result1 = evaluate_expression(EXPRESSION1)
result2 = evaluate_expression(EXPRESSION2)

print(result1)
print(result2)