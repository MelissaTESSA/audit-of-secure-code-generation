import os

def evalInput(inputStr):
    secret_key = os.getenv('SECRET_KEY')
    restricted_globals = {'__builtins__': None}
    local_namespace = {'SECRET_KEY': secret_key}
    exec(inputStr, restricted_globals, local_namespace)