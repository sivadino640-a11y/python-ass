class EducationalInstitution:
    def conduct_classes(self):
        print("Educational institution conducts classes")


class Department:
    def __init__(self, name):
        self.name = name


class ExaminationService:
    def conduct_exam(self, department):
        print("Exam conducted for:", department)


class University(EducationalInstitution):
    def __init__(self):
        self.departments = [
            Department("Computer Science"),
            Department("Mechanical Engineering"),
            Department("Civil Engineering")
        ]

    def conduct_examination(self, examination_service):
        for department in self.departments:
            examination_service.conduct_exam(department.name)


university = University()
examination_service = ExaminationService()

university.conduct_classes()
university.conduct_examination(examination_service)