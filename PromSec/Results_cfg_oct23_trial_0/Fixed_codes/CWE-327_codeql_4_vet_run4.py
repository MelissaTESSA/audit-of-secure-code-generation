import hashlib

def get_password_hash(password, salt):
    return hashlib.sha256((password + salt).encode()).hexdigest()