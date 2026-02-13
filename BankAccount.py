class BankAccount:

    def __init__(self,name):
       self.name = name
       self.balance = 0
    
    def deposit(self,amount):
        self.balance += amount

    def get_balance(self):
        return self.balance
    
    def withdraw(self, amount):
        if amount <= 0:
           raise ValueError("出金額は1円以上である必要があります")
        if amount > self.balance:
           raise ValueError("残高不足です")
        self.balance -= amount