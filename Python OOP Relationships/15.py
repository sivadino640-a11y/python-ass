class Student:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Student:", self.name)


class College:
    def __init__(self):
        self.students = [
            Student("Siva"),
            Student("Ravi"),
            Student("Kiran")
        ]

    def display_students(self):
        for student in self.students:
            student.display()


college = College()
college.display_students()