class Engine:
    def start(self):
        print("Engine is starting")


class Car:
    def __init__(self):
        self.engine = Engine()

    def drive(self):
        self.engine.start()
        print("Car is driving")


car = Car()
car.drive()