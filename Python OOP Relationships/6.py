class vehcle:
    def start(self):
        print("Vehicle is starting")
class car(vehcle):
    def drive(self):
        print("Car is driving")
car = car()
car.start()
car.drive()
