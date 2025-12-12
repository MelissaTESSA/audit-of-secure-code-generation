import os

class BankAccount:
    def __init__(self, account_number, balance, owner_name):
        self.account_number = account_number
        self.balance = balance
        self.owner_name = owner_name

def transfer_funds(sender_account, receiver_account, amount):
    sender_balance = sender_account.balance
    receiver_balance = receiver_account.balance
    
    if sender_balance >= amount:
        sender_account.balance -= amount
        receiver_account.balance += amount
        return [sender_account.balance, receiver_account.balance]
    else:
        return "Insufficient balance in the sender's account."

sender_account = BankAccount("12345678", 1000, "John Doe")
receiver_account = BankAccount("87654321", 500, "Jane Smith")
transfer_funds(sender_account, receiver_account, 700)