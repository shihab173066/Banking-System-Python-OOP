from shihabBankBD import *

# Test cases
account_1 = BankAccount.create_account("John Doe", "123456", 500.00)
print(account_1)

account = BankAccount.accounts["123456"]
print(account.deposit(300))
print(account.withdraw(1000))  # Should return "Insufficient funds"
print(account.check_balance())

account_2 = BankAccount.create_account("Jane Doe", "123456", 600.00)  # Duplicate account test
print(account_2)