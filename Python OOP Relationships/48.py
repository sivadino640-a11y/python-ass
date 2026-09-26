class Teacher:
    def __init__(self, name):
        self.name = name


class Student:
    def __init__(self, name):
        self.name = name


class NotificationService:
    def send(self, message):
        print("Notification:", message)


class School:
    def __init__(self):
        self.teachers = [
            Teacher("Mr. Kumar"),
            Teacher("Ms. Priya")
        ]

        self.students = [
            Student("Siva"),
            Student("Ravi")
        ]

    def send_notification(self, notification_service, message):
        notification_service.send(message)


school = School()
notification_service = NotificationService()

school.send_notification(
    notification_service,
    "Tomorrow is a holiday."
)