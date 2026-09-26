class Engine:
    def start(self):
        print("Engine is starting")


class Vehicle:
    def move(self):
        print("Vehicle is moving")


class Car(Vehicle):
    def __init__(self):
        self.engine = Engine()

    def drive(self):
        self.engine.start()
        print("Car is driving")


car = Car()

car.move()
car.drive()