class Printer:
    def print_details(self, name, age):
        print("Student Name:", name)
        print("Student Age:", age)


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_student(self, printer):
        printer.print_details(self.name, self.age)


student = Student("Siva", 20)
printer = Printer()

student.print_student(printer)