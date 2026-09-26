class EmailService:
    def send_email(self, email, message):
        print("Email sent to:", email)
        print("Message:", message)


class Order:
    def __init__(self, order_id, email):
        self.order_id = order_id
        self.email = email

    def send_confirmation(self, email_service):
        message = "Your order " + self.order_id + " is confirmed."
        email_service.send_email(self.email, message)


order = Order("ORD101", "siva@gmail.com")
email_service = EmailService()

order.send_confirmation(email_service)