class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class PaymentService:
    def pay(self, amount):
        print("Payment of", amount, "successful")


class DeliveryService:
    def deliver(self, address):
        print("Order will be delivered to:", address)


class OnlineOrder:
    def __init__(self):
        self.products = [
            Product("Laptop", 50000),
            Product("Mouse", 500)
        ]

    def checkout(self, payment_service, delivery_service, address):
        total = 0

        for product in self.products:
            total += product.price

        print("Total Amount:", total)

        payment_service.pay(total)
        delivery_service.deliver(address)


order = OnlineOrder()

payment_service = PaymentService()
delivery_service = DeliveryService()

order.checkout(
    payment_service,
    delivery_service,
    "Rajahmundry"
)