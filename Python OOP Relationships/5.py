class shape:
    def area(self):
        pass
class rectangle(shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
s = rectangle(5, 3)
print(s.area())