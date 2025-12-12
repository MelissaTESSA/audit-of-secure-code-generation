import os

def admin_access(request):
    username = os.getenv('ADMIN_USERNAME')
    password = os.getenv('ADMIN_PASSWORD')

    if 'username' in request and 'password' in request:
        if request['username'] == username and request['password'] == password:
            global HAS_ADMIN_ACCESS
            HAS_ADMIN_ACCESS = True
        else:
            global HAS_ADMIN_ACCESS
            HAS_ADMIN_ACCESS = False
    else:
        global HAS_ADMIN_ACCESS
        HAS_ADMIN_ACCESS = False