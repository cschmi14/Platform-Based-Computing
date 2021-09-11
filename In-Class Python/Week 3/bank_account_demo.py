from bank_account import BankAccount

carter = BankAccount("01234", "5000")

print(carter.get_balance())
carter.deposit("4000")
print(carter.get_balance())
carter.withdraw("4500")
print(carter.get_balance())
print(carter)

