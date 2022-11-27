#person
class Person:
    def __init__(self, name, age, contact, address):
        self.name = name 
        self.age =  age 
        self.contact = contact
        self.address = address

    def introduction(self):
        print(f"Hello, I am {self.name},{self.age} years old.")
        print(f"You can contact me on {self.contact}.")
        print(f"I am currently living in {self.address}.")

#Employee
class Employee(Person):
    pass

#Doctor
class Doctor(Employee):
    def __init__(self, name, age, contact, address):
        super().__init__(name, age, contact, address)

    def check_up (self, patient_name):
        print(f"{self.name} is performing a check up on {patient_name}")

    def give_medication(self, patient_name):
        print(f"{self.name} is writing a presciption for {patient_name}")

#Assistant
class Assistant(Employee):
    def __init__(self, name, age, contact, address):
        super().__init__(name, age, contact, address)

    def record_patient_info(self, patient_name):
        print(f"{self.name} is recording {patient_name}'s medical record.")

    def sched_appointment(self, patient_name):
        print(f"{self.name} is scheduling an appointment for {patient_name}")

#Pharmacist
class Pharmacist(Employee):
    def __init__(self, name, age, contact, address):
        super().__init__(name, age, contact, address)

    def read_prescription(self, doctor_name):
        print(f"{self.name} is reading the Dr. {doctor_name}'s prescription.")

    def give_medicine(self, patient_name):
        print(f"{self.name} is giving the medicine to {patient_name}")

#Patient
class Patient (Person):
    def __init__(self):
        self.name = "name"
        self.age = "age"
        self.contact = "contact"
        self.address = "address"
        self.concerns = "concerns"

    def introduction(self):
        super().introduction()
        
    def make_appointment(self):
        print(f"{self.name} is making an appointment for a checkup.")

    def buy_medicine(self):
        print(f"{self.name} is buying a medicine.")

    def pay(self, payment):
        print(f"{self.name} is paying for {payment}")