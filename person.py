#person
class Person:
    def __init__(self):
        self.name = "name"
        self.age =  "age"
        self.contact = "contact"
        self.address = "address"

    def introduction(self):
        print(f"Hello, I am {self.name},{self.age} years old.")
        print(f"You can contact me on {self.contact}.")
        print(f"I am currently living in {self.address}.")

#Employee
class Employee(Person):
    pass

#Doctor
class Doctor(Employee):
    def __init__(self):
        self.name = "Dr. Riza"
        self.age = 34
        self.contact = "09xxxx"
        self.address = "Batangas City"

    def check_up (self, patient_name):
        print(f"{self.name} is performing a check up on {patient_name.capitalize()}.")

    def give_medication(self, patient_name):
        print(f"{self.name} is writing a presciption for {patient_name.capitalize()}.")

#Assistant
class Assistant(Employee):
    def __init__(self):
        self.name = "Asst. Hana"
        self.age = 25
        self.contact = "09xxxx"
        self.address = "Batangas City"

    def record_patient_info(self, patient_name):
        print(f"{self.name} is recording {patient_name.capitalize()}'s medical record.")

    def sched_appointment(self, patient_name):
        print(f"{self.name} is scheduling an appointment for {patient_name.capitalize()}.    ")

#Pharmacist
class Pharmacist(Employee):
    def __init__(self):
        self.name = "Ms. Ella"
        self.age = 23
        self.contact = "09xxxx"
        self.address = "Batangas City"

    def read_prescribed(self, doctor_name):
        print(f"{self.name} is reading the {doctor_name}'s prescription.")

    def give_medicine(self, patient_name):
        print(f"{self.name} is giving the medicine to {patient_name.capitalize()}.")

#Patient
class Patient (Person):
    def __init__(self):
        self.name = "Patient Name"
        self.age =  "age"
        self.contact = "contact"
        self.address = "address"
        self.concerns = "concerns"
        self.wallet = 1500

    def make_appointment(self):
        print(f"{self.name.capitalize()} is making an appointment for a checkup.") #not used yet

    def pay(self, payment):
        print(f"{self.name.capitalize()} is paying for {payment}.")