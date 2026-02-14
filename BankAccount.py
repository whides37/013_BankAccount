class BankAccount:

    def __init__(self, name, balance=0):
        if not isinstance(name, str):
            raise TypeError("名前は文字列で入力してください")
        if not isinstance(balance, (int, float)):
            raise TypeError("残高は数値で入力してください")
        if balance < 0:
            raise ValueError("初期残高は0以上である必要があります")

        self.name = name
        self.balance = balance
    
    def deposit(self,amount):
        if not isinstance(amount, int):
           raise TypeError("入金額は数字で入力してください")
        if amount <= 0:
           raise ValueError("入金額は1円以上である必要があります")
        self.balance += amount

    
    def withdraw(self, amount):
        if not isinstance(amount, (int, float)):
           raise TypeError("出金額は数字で入力してください")
        if amount <= 0:
           raise ValueError("出金額は1円以上である必要があります")
        if amount > self.balance:
           raise ValueError("残高不足です")
        self.balance -= amount

    # 振込メソッド
    def transfer(self, other_account, amount):
        if not isinstance(other_account, BankAccount):
            raise TypeError("振込先が不正です")
        
        # 出金/a.withdraw(300) と同じ
        # a = BankAccount("Kiki")   ← self
        # transferの中では：self.withdraw(amount) → a.withdraw(300)
        # self（＝自分の口座）から withdraw する
        self.withdraw (amount)

        # 入金/b.deposit(300)と同じ。
        # b = BankAccount("Lala")   ← other_account
        # transferの中では：other_account.deposit(amount)→ b.deposit(300)
        # other_account（＝相手の口座）に deposit する
        other_account.deposit(amount)

   #利率計算メソッド   
    def apply_interest(self, rate):
       if not isinstance(rate(int,float)):
           raise TypeError("数字以外は入力できません")
       if rate < 0:
           raise ValueError("マイナスの数値はレートに入れることはできません")
       else :
           self.balance += self.balance * rate

    def get_balance(self):
        return self.balance
    
    def __str__(self):
        return f"{self.name}の残高: {self.balance}円"


#テストコード
if __name__ == "__main__":
    a = BankAccount("Kiki", 300)
    b = BankAccount("Lala", 10)

    a.transfer(b, 300)

    print(a)
    print(b)