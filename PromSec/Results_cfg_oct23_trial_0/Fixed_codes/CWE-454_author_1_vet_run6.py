import os

def admin_access(request):
    username = request.get('username')
    password = request.get('password')

    if username == os.environ.get('ADMIN_USERNAME') and password == os.environ.get('ADMIN_PASSWORD'):
        global HAS_ADMIN_ACCESS
        HAS_ADMIN_ACCESS = True
    else:
        global HAS_ADMIN_ACCESS
        HAS_ADMIN_ACCESS = False