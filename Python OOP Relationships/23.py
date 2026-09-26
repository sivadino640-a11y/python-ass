class PaymentGateway:
    def pay(self, amount):
        print("Payment of", amount, "successful")


class ShoppingCart:
    def __init__(self, total):
        self.total = total

    def checkout(self, payment_gateway):
        print("Cart Total:", self.total)
        payment_gateway.pay(self.total)


cart = ShoppingCart(2500)
gateway = PaymentGateway()

cart.checkout(gateway)