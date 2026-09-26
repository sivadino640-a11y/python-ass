class Doctor:
    def __init__(self, name):
        self.name = name


class Patient:
    def __init__(self, name):
        self.name = name


class BillingService:
    def generate_bill(self, patient, amount):
        print("Patient:", patient)
        print("Bill Amount:", amount)


class Hospital:
    def __init__(self):
        self.doctors = [
            Doctor("Dr. Ravi"),
            Doctor("Dr. Kumar")
        ]

        self.patients = [
            Patient("Siva"),
            Patient("Ramesh")
        ]

    def create_bill(self, billing_service, patient, amount):
        billing_service.generate_bill(patient, amount)


hospital = Hospital()
billing_service = BillingService()

hospital.create_bill(billing_service, "Siva", 5000)