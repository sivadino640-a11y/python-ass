class Employee:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Employee:", self.name)


class Company:
    def __init__(self):
        self.employees = [
            Employee("Siva"),
            Employee("Ravi"),
            Employee("Kiran")
        ]

    def display_employees(self):
        for employee in self.employees:
            employee.display()


company = Company()
company.display_employees()