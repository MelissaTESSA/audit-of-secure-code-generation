def modify_project_access(project_id, user_id, action, current_user_role):
    if current_user_role not in ['guest', 'member', 'project_manager', 'admin']:
        return "Invalid current user role"
    
    if current_user_role == 'guest':
        return "Insufficient privileges to modify project access"
    
    if action not in ['add', 'remove']:
        return "Invalid action"
    
    if action == 'add':
        return "User {} added to project {}".format(user_id, project_id)
    elif action == 'remove':
        return "User {} removed from project {}".format(user_id, project_id)