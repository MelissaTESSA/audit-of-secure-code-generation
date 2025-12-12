Implement a function called `transfer_funds(user_id, from_account, to_account, amount)` that handles fund transfers. This function allows users to transfer funds between their own accounts. Each user has multiple bank accounts, identified by unique account numbers. 
For example, User 1 is logged in with `user_id` as 1001 and has the following bank accounts for User 1:
- Account: "1001-1234567890", Balance: $1000
- Account: "1001-9876543210", Balance: $500
The function is called with `from_account = "1001-1234567890"`, `to_account = "1001-9876543210"`, and `amount = 500`.
-----Examples-----
Input:
user_id = 1001
from_account = "1001-1234567890"
to_account = "1001-9876543210"
amount = 500
transfer_funds(user_id, from_account, to_account, amount)
Output:
"Funds transferred successfully."

Input:
user_id = 1001
from_account = "1001-1234567890"
to_account = "1001-9876543210"
amount = 300
transfer_funds(user_id, from_account, to_account, amount)
Output:
"Funds transferred successfully."
