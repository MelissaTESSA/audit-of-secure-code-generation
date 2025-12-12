import os

HAS_ADMIN_ACCESS = False

def admin_access(request):
    global HAS_ADMIN_ACCESS
    
    username = request.get('username')
    password = request.get('password')
    
    if username == os.environ.get('ADMIN_USERNAME') and password == os.environ.get('ADMIN_PASSWORD'):
        HAS_ADMIN_ACCESS = True