class PaymentService:
    def make_payment(self, amount):
        print("Payment of", amount, "completed")


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def pay(self, amount, payment_service):
        if amount <= self.balance:
            payment_service.make_payment(amount)
            self.balance -= amount
            print("Remaining Balance:", self.balance)
        else:
            print("Insufficient Balance")


account = BankAccount(10000)
payment_service = PaymentService()

account.pay(2000, payment_service)