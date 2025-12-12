Create a function named `grant_access` that grants access to a system based on the user's role. Users with the 'admin' role should have full access, while users with the 'guest' role should only have read-only access. 
Implement the function `grant_access(role)` that handles the access control logic. Return 'Invalid role.' if the inputs are invalid.
-----Examples-----
Input:
role = 'admin'
grant_access(role)
Output:
'Full access granted'

Input:
role = 'guest'
grant_access(role)
Output:
'Read-only access granted'

