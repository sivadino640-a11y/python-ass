class ReportGenerator:
    def generate_report(self, name):
        print("Report generated for:", name)


class Employee:
    def __init__(self, name):
        self.name = name

    def create_report(self, report_generator):
        report_generator.generate_report(self.name)


employee = Employee("Siva")
report_generator = ReportGenerator()

employee.create_report(report_generator)