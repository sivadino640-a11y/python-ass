class Person:
    def introduce(self):
        print("I am a person")


class Teacher(Person):
    def teach(self):
        print("Teacher is teaching")


teacher = Teacher()
teacher.introduce()
teacher.teach()