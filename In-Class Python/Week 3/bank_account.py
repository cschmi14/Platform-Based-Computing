class BankAccount:

    def __init__(self, account_num, balance):
        self.account_num = int(account_num)
        self.balance = int(balance)

    def __str__(self):
        return str(self.account_num)

    def deposit(self, deposit):
        self.balance += int(deposit)

    def withdraw(self, withdraw):
        self.balance -= int(withdraw)

    def get_balance(self):
        return self.balance

