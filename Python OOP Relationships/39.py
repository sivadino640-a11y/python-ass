class PaymentService:
    def pay(self, amount):
        print("Payment of", amount, "completed")


class Order:
    def __init__(self, amount):
        self.amount = amount

    def make_payment(self, payment_service):
        payment_service.pay(self.amount)


order = Order(1500)
payment_service = PaymentService()

order.make_payment(payment_service)