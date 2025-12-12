Design a function `update_user_role(user_id, new_role, current_user_role)` within a system that manages user roles and permissions. The function is tasked with updating the role of a specified user. This action should be permitted only if the current user executing the function has the necessary permissions. Assume there are three roles: 'guest', 'member', and 'admin', with 'admin' having the highest privileges. The system must ensure that only users with 'admin' role can update roles.

-----Examples-----
Input:
user_id = 3
new_role = 'member'
current_user_role = 'admin'
update_user_role(user_id, new_role, current_user_role)
Output:
'User 3 role updated to member.'

Input:
user_id = 4
new_role = 'admin'
current_user_role = 'guest'
update_user_role(user_id, new_role, current_user_role)
Output:
'Error: Insufficient privileges to update user role.'
