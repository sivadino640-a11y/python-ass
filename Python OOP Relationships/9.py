class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def display_balance(self):
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)


class SavingsAccount(BankAccount):
    def add_interest(self):
        print("Savings account gets interest")


class CurrentAccount(BankAccount):
    def overdraft(self):
        print("Current account has overdraft facility")


savings = SavingsAccount("SA101", 10000)
current = CurrentAccount("CA101", 20000)

savings.display_balance()
savings.add_interest()

current.display_balance()
current.overdraft()