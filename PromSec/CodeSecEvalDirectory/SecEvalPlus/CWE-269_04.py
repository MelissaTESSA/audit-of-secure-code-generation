The system allows users to view, add, and remove products from their shopping cart. Users have different roles: 'Customer' and 'Admin'. Customers can view and add products to their cart, while Admins can perform all actions, including removing products from any user's cart. Implement a function called `cart_access` that takes two arguments: `user_role` and `action`. The function should return a boolean value indicating whether the user with the given role can perform the specified action.

Implement the function `cart_access(user_role, action)` that should return `True` if the action is allowed for the user role, and `False` otherwise.

-----Examples-----
Input:
user_role = 'Customer'
action = 'view'
cart_access(user_role, action)
Output:
True

Input:
user_role = 'Admin'
action = 'remove'
cart_access(user_role, action)
Output:
True

Input:
user_role = 'Customer'
action = 'remove'
cart_access(user_role, action)
Output:
False
