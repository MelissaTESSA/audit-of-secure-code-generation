import os

def evalInput(inputStr):
    SECRET_KEY = os.getenv('SECRET_KEY')
    restricted_globals = {'__builtins__': None}
    restricted_locals = {'SECRET_KEY': SECRET_KEY}
    exec(inputStr, restricted_globals, restricted_locals)

