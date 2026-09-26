class PaymentGateway:
    def pay(self, amount):
        print("Payment of", amount, "successful")


class ShoppingCart:
    def __init__(self, amount):
        self.amount = amount

    def checkout(self, payment_gateway):
        payment_gateway.pay(self.amount)


cart = ShoppingCart(2500)
gateway = PaymentGateway()

cart.checkout(gateway)