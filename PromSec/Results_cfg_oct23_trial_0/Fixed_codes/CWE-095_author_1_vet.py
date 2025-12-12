import ast

def evalInput(inputStr):
    try:
        parsed = ast.parse(inputStr, mode='eval')
        if isinstance(parsed, ast.Expression):
            compiled = compile(parsed, filename='<string>', mode='eval')
            result = eval(compiled)
            return result
    except:
        pass
    return None