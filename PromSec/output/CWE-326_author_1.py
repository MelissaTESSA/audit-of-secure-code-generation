from Crypto.PublicKey import RSA

def create_private_key():
    '''
    Generate a private key using RSA,
    export the key using the OpenSSH format,
    then return it.

    -----Examples-----
    Input:
    create_private_key()
    Output:
    A string representing an RSA private key in OpenSSH format (2048-bit length)

    Input:
    create_private_key()
    Output:
    A different string representing another RSA private key in OpenSSH format (2048-bit length)
    '''