"""
Make Class shihabBankBD

constructor takes name(str), unique_account_num(int only) and initial_diposit(float)
methods Account Creation, Deposit Functionality, Withdrawal Functionality, Balance Inquiry

"""

class shihabBankBD:

    def __init__(self, name, initial_diposit, unique_account_num):
        self.name = name
        self.unique_account_num = int(unique_account_num)
        self.initial_diposit = float(initial_diposit)

    def account_create(self):
        if len(str(self.unique_account_num)) == 6 and self.initial_diposit >= 3000.00:
            return (f"Account is created for {self.name}, with an account number of {self.unique_account_num}, "
      f"and a mandatory deposit of {self.initial_diposit:.2f}")
        else:
            return ("Please follow instructions properly!!")
        
    


obj = shihabBankBD("Shihab", 3000.00, 123456)
print(obj.account_create())


