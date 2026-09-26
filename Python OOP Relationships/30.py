class CertificateGenerator:
    def generate_certificate(self, student_name, course_name):
        print("Certificate Generated")
        print("Student:", student_name)
        print("Course:", course_name)


class Course:
    def __init__(self, course_name):
        self.course_name = course_name

    def complete_course(self, certificate_generator, student_name):
        print(student_name, "completed the course.")
        certificate_generator.generate_certificate(
            student_name,
            self.course_name
        )


course = Course("Python Programming")
certificate_generator = CertificateGenerator()

course.complete_course(certificate_generator, "Siva")