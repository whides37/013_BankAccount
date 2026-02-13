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

    def transfer(self, other_account, amount):
        if amount <= 0:
            raise ValueError("振込額は1円以上である必要があります")

        if amount > self.balance:
            raise ValueError("残高不足です")

        if not isinstance(other_account, BankAccount):
            raise ValueError("振込先が不正です")

        # 出金
        self.balance -= amount
        # 入金
        other_account.balance += amount

a = BankAccount("Kiki")
b = BankAccount("Lala")

a.deposit(1000)
a.transfer(b, 300)

print(a.get_balance())  # 700
print(b.get_balance())  # 300