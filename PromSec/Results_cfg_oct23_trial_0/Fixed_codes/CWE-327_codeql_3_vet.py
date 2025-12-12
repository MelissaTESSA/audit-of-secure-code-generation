import hashlib

def certificate_matches(certificate, known_hash):
    certificate_hash = hashlib.sha256(certificate.encode()).hexdigest()
    return certificate_hash == known_hash