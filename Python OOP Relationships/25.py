class NotificationService:
    def send_notification(self, message):
        print("Notification:", message)


class Student:
    def __init__(self, name):
        self.name = name

    def notify(self, notification_service):
        message = "Hello " + self.name + ", your class starts at 10 AM."
        notification_service.send_notification(message)


student = Student("Siva")
notification_service = NotificationService()

student.notify(notification_service)