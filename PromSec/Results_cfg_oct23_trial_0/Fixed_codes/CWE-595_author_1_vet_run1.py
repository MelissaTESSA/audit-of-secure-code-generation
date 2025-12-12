import os

def isEqual(account1, account2):
    return account1 == account2

# Example usage
account1 = {
    "username": "john_doe",
    "password": "secure_password"
}

account2 = {
    "username": "john_doe",
    "password": "secure_password"
}

print(isEqual(account1, account2))