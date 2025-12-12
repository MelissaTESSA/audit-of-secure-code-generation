import hashlib

def get_password_hash(password, salt):
    if not isinstance(password, str) or not isinstance(salt, str):
        return None
    
    password = password.encode('utf-8')
    salt = salt.encode('utf-8')
    
    return hashlib.sha256(password + salt).hexdigest()