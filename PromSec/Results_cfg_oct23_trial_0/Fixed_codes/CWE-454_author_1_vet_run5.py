import os

def admin_access(request):
    global HAS_ADMIN_ACCESS
    username = os.getenv('ADMIN_USERNAME')
    password = os.getenv('ADMIN_PASSWORD')

    if 'username' in request and 'password' in request:
        if request['username'] == username and request['password'] == password:
            HAS_ADMIN_ACCESS = True
        else:
            HAS_ADMIN_ACCESS = False
    else:
        HAS_ADMIN_ACCESS = False