class Laptop:
    def start(self):
        print("Laptop is starting")


class Employee:
    def work(self):
        print("Employee is working")


class Developer(Employee):
    def __init__(self):
        self.laptop = Laptop()

    def code(self):
        self.laptop.start()
        print("Developer is coding")


developer = Developer()

developer.work()
developer.code()