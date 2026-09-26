class Teacher:
    def __init__(self, name):
        self.name = name

    def teach(self):
        print(self.name, "is teaching")


class Student:
    def __init__(self, name):
        self.name = name

    def study(self):
        print(self.name, "is studying")


class School:
    def __init__(self):
        self.teacher = Teacher("Mr. Kumar")
        self.student = Student("Siva")

    def display(self):
        self.teacher.teach()
        self.student.study()


school = School()
school.display()