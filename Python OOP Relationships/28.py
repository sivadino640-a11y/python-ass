class BillingService:
    def generate_bill(self, patient_name, amount):
        print("Patient:", patient_name)
        print("Bill Amount:", amount)


class Hospital:
    def __init__(self, name):
        self.name = name

    def create_bill(self, billing_service, patient_name, amount):
        print("Hospital:", self.name)
        billing_service.generate_bill(patient_name, amount)


hospital = Hospital("City Hospital")
billing_service = BillingService()

hospital.create_bill(billing_service, "Siva", 5000)