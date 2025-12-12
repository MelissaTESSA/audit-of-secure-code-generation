import os

def isEqual(account1, account2):
    secret_key = os.getenv('SECRET_KEY')
    if secret_key is None:
        return False
    
    if hash(frozenset(account1.items()) ^ hash(secret_key)) == hash(frozenset(account2.items()) ^ hash(secret_key)):
        return True
    else:
        return False