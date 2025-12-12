import os

def isEqual(account1, account2):
    return account1.get('username') == account2.get('username') and account1.get('password') == account2.get('password')

# Example usage
account1 = {
    'username': 'user1',
    'password': 'pass123'
}

account2 = {
    'username': 'user1',
    'password': 'pass123'
}

print(isEqual(account1, account2))