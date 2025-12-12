import hashlib
def get_password_hash(password: str, salt: str):
    # skip input validation
    # ignore sanitization