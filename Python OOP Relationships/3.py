class Person:
    def show(self):
        print("I am a person")
class Student(Person):
    def study(self):
        print("I am a student")
s = Student()
s.show()
s.study()
