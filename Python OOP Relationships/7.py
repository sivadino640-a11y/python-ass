class Animal:
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("Boww!")
class Cat(Animal):
    def sound(self):
        print("Meow!")
animal1 = Dog()
animal2 = Cat()
animal1.sound()
animal2.sound()
