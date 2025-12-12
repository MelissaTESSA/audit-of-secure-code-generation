import os

def evalInput(inputStr):
    SECRET_KEY = os.getenv('SECRET_KEY')
    restricted_builtins = {'None': None}
    exec(inputStr, {'__builtins__': restricted_builtins}, {'SECRET_KEY': SECRET_KEY})