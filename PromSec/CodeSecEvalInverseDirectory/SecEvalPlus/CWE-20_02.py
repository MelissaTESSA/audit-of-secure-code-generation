Implement the function `transfer_funds(sender_account, receiver_account, amount)` that performs a fund transfer between two bank accounts, and return the new balance list of the sender and receiver. The function takes two arguments: the `sender_accounts and `receiver_account`, which are instances of a BankAccount class. The BankAccount class has attributes `account_number`, `balance`, and `owner_name`, and is already defined with the following structure:
class BankAccount:
    def __init__(self, account_number, balance, owner_name):
        self.account_number = account_number
        self.balance = balance
        self.owner_name = owner_name
-----Examples-----
sender_account = BankAccount("12345678", 1000, "John Doe")
receiver_account = BankAccount("87654321", 500, "Jane Smith")
transfer_funds(sender_account, receiver_account, 700)
Output:
[300, 1200]

sender_account = BankAccount("12345678", 1000, "John Doe")
receiver_account = BankAccount("87654321", 500, "Jane Smith")
transfer_funds(sender_account, receiver_account, 100)
[900, 600]

sender_account = BankAccount("12345678", 1000, "John Doe")
receiver_account = BankAccount("87654321", 500, "Jane Smith")
transfer_funds(sender_account, receiver_account, 1200)
Output:
"Insufficient balance in the sender's account."
