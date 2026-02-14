from bank_account import BankAccount

a = BankAccount("Kiki", 1000)
b = BankAccount("Lala", 500)

a.transfer(b, 300)

print(a)
print(b)
