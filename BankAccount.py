class BankAccount:

    def __init__(self,name):
       self.name = name
       self.balance = 0
    
    def deposit(self,amount):
        if not isinstance(amount, int):
           raise TypeError("入金額は数字で入力してください")
        if amount <= 0:
           raise ValueError("マイナスの値は入金できません")
        self.balance += amount

    def get_balance(self):
        return self.balance
    
    def withdraw(self, amount):
        if not isinstance(amount, int):
           raise TypeError("出金額は数字で入力してください")
        if amount <= 0:
           raise ValueError("出金額は1円以上である必要があります")
        if amount > self.balance:
           raise ValueError("残高不足です")
        self.balance -= amount

    # 自分の口座から出金する
    def transfer(self, other_account, amount):
        if not isinstance(other_account, BankAccount):
            raise TypeError("振込先が不正です")
        
        # 出金/a.withdraw(300) と同じ
        # a = BankAccount("Kiki")   ← self
        # transferの中では：self.withdraw(amount) → a.withdraw(300)
        self.withdraw (amount)

        # 入金/b.deposit(300)と同じ。
        # b = BankAccount("Lala")   ← other_account
        # transferの中では：other_account.deposit(amount)→ b.deposit(300)
        other_account.deposit(amount)

a = BankAccount("Kiki")
b = BankAccount("Lala")

a.deposit(1000)
a.transfer(b, 300)

print(a.get_balance())  # 700
print(b.get_balance())  # 300