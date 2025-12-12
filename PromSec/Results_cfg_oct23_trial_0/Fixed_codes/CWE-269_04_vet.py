def cart_access(user_role, action):
    if user_role == 'Admin':
        return True
    elif user_role == 'Customer' and action in ['view', 'add']:
        return True
    else:
        return False