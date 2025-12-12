import os

def grant_access(role):
    if role == 'admin':
        return 'Full access granted'
    elif role == 'guest':
        return 'Read-only access granted'
    else:
        return 'Invalid role.'