class Department:
    def __init__(self, name):
        self.name = name


class Employee:
    def __init__(self, name):
        self.name = name


class PayrollService:
    def calculate_salary(self, employee, salary):
        print("Employee:", employee)
        print("Salary:", salary)


class Company:
    def __init__(self):
        self.departments = [
            Department("IT"),
            Department("HR")
        ]

        self.employees = [
            Employee("Siva"),
            Employee("Ravi")
        ]

    def process_payroll(self, payroll_service, employee, salary):
        payroll_service.calculate_salary(employee, salary)


company = Company()
payroll_service = PayrollService()

company.process_payroll(payroll_service, "Siva", 30000)