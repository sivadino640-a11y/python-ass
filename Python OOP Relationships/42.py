class Course:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Course:", self.name)


class Person:
    def introduce(self):
        print("I am a person")


class Student(Person):
    def __init__(self, course):
        self.course = course

    def study(self):
        self.course.display()
        print("Student is studying")


course = Course("Python Programming")
student = Student(course)

student.introduce()
student.study()