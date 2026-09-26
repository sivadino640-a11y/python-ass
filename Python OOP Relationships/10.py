class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


class Developer(Employee):
    def code(self):
        print(self.name, "is developing software")


class Tester(Employee):
    def test(self):
        print(self.name, "is testing software")


class Manager(Employee):
    def manage(self):
        print(self.name, "is managing the team")


developer = Developer("Siva", 30000)
tester = Tester("Ravi", 28000)
manager = Manager("Kiran", 50000)

developer.display()
developer.code()

tester.display()
tester.test()

manager.display()
manager.manage()