import ssl
import os

def getSSLContext():
    ssl_context = ssl.create_default_context()
    ssl_context.load_verify_locations(cafile=os.getenv('CA_FILE'))
    ssl_context.load_cert_chain(certfile=os.getenv('CERT_FILE'), keyfile=os.getenv('KEY_FILE'))
    
    return ssl_context