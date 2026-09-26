class DeliveryService:
    def deliver(self, order_id, address):
        print("Order", order_id, "will be delivered to", address)


class FoodOrder:
    def __init__(self, order_id, address):
        self.order_id = order_id
        self.address = address

    def place_delivery(self, delivery_service):
        delivery_service.deliver(self.order_id, self.address)


order = FoodOrder("FOOD101", "Rajahmundry")
delivery_service = DeliveryService()

order.place_delivery(delivery_service)