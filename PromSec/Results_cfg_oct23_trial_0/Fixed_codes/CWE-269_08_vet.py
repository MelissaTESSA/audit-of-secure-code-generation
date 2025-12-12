def update_user_role(user_id, new_role, current_user_role):
    if current_user_role == 'admin':
        # Update user role logic here
        pass
    else:
        print("You do not have the necessary permissions to update user roles.")