class BankAccount:
    accounts = {}

    def __init__(self, name, account_number, initial_deposit):
        self.name = name
        self.account_number = account_number
        self.balance = initial_deposit

    @classmethod
    def create_account(cls, name, account_number, initial_deposit):
        if account_number in cls.accounts:
            return "Account number already exists. Please choose a unique account number."
        if initial_deposit < 0:
            return "Initial deposit must be positive."
        cls.accounts[account_number] = cls(name, account_number, initial_deposit)
        return f"Account created for {name} with initial balance of {initial_deposit:.2f}"

    def deposit(self, amount):
        if amount <= 0:
            return "Deposit amount must be positive."
        self.balance += amount
        return f"Deposit successful. New balance: {self.balance:.2f}"

    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal amount must be positive."
        if amount > self.balance:
            return "Insufficient funds."
        self.balance -= amount
        return f"Withdrawal successful. Remaining balance: {self.balance:.2f}"

    def check_balance(self):
        return f"Current balance: {self.balance:.2f}"

"""# Test cases
account_1 = BankAccount.create_account("John Doe", "123456", 500.00)
print(account_1)

account = BankAccount.accounts["123456"]
print(account.deposit(300))
print(account.withdraw(1000))  # Should return "Insufficient funds"
print(account.check_balance())

account_2 = BankAccount.create_account("Jane Doe", "123456", 600.00)  # Duplicate account test
print(account_2)"""

