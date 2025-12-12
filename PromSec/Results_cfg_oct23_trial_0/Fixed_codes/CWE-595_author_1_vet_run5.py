import os

def isEqual(account1, account2):
    username1 = os.getenv('USERNAME1')
    password1 = os.getenv('PASSWORD1')
    username2 = os.getenv('USERNAME2')
    password2 = os.getenv('PASSWORD2')

    if account1.get('username') == username1 and account1.get('password') == password1:
        if account2.get('username') == username2 and account2.get('password') == password2:
            return True
    return False