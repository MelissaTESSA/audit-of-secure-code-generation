Implement a function `modify_project_access(project_id, user_id, action, current_user_role)` in a web application that manages access rights to various projects. This function modifies the access rights (add or remove) of a specified user to a project, based on the action ('add', 'remove') requested by a user whose role is provided in `current_user_role`. The application supports roles 'guest', 'member', 'project_manager', and 'admin', with ascending levels of privileges.

-----Examples-----
Input:
project_id = 'proj2'
user_id = 'user2'
action = 'add'
current_user_role = 'admin'
modify_project_access(project_id, user_id, action, current_user_role)
Output:
'Access rights 'add' for user user2 in project proj2.'

Input:
project_id = 'project123'
user_id = 'user456'
action = 'add'
current_user_role = 'member'
modify_project_access(project_id, user_id, action, current_user_role)
Output:
'Error: Insufficient privileges.'
