class BankAccount:

    def __init__(self,name):
       self.name = name
       self.balance = 0
    
    def deposit(self,amount):
        self.balance += amount

    def get_balance(self):
        return self.balance