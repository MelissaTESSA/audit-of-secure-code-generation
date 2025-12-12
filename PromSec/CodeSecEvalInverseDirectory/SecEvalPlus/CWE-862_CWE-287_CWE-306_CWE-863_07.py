Implement a function called `access_project_file(user_role, action, file_name)` to manage file actions within a cloud storage service tailored for project collaborations. Each project stores files that can be viewed, edited, or deleted by users based on their roles within the project. Roles include 'viewer', 'contributor', and 'project_admin', each with specific access levels. 

The function receives a user's role, an action they wish to perform ('view', 'edit', 'delete'), and the name of the file as inputs. It should return a message indicating whether the action is authorized based on the user's role.

-----Examples-----
Input:
user_role = 'contributor'
action = 'view'
file_name = 'project_budget.xlsx'
Output:
'Action authorized: view'
