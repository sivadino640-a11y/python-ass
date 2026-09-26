class Keyboard:
    def type(self):
        print("Keyboard is typing")


class Laptop:
    def __init__(self):
        self.keyboard = Keyboard()

    def use(self):
        self.keyboard.type()
        print("Laptop is being used")


laptop = Laptop()
laptop.use()