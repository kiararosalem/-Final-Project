#person
class Person:
    def __init__(self):
        self.name = input("What is your name? ")
        self.age =  input("Enter your age: ")
        self.contact = input("Kindly input your contact number: ")
        self.address = input("Enter your address: ")

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
        print(f"{self.name} is performing a check up on {patient_name}.")

    def give_medication(self, patient_name):
        print(f"{self.name} is writing a presciption for {patient_name}.")

#Assistant
class Assistant(Employee):
    def __init__(self):
        self.name = "Asst. Hana"
        self.age = 25
        self.contact = "09xxxx"
        self.address = "Batangas City"

    def record_patient_info(self, patient_name):
        print(f"{self.name} is recording {patient_name}'s medical record.")

    def sched_appointment(self, patient_name):
        print(f"{self.name} is scheduling an appointment for {patient_name}.    ")

#Pharmacist
class Pharmacist(Employee):
    def __init__(self):
        self.name = "Ms. Ella"
        self.age = 23
        self.contact = "09xxxx"
        self.address = "Batangas City"

    def read_prescription(self, doctor_name):
        print(f"{self.name} is reading the Dr. {doctor_name}'s prescription.")

    def give_medicine(self, patient_name):
        print(f"{self.name} is giving the medicine to {patient_name}.")

#Patient
class Patient (Person):
    def __init__(self):
        super().__init__()
        self.concerns = input("Are you feeling unwell?\nIf so, What symptom do you currently have?")
        self.wallet = 1500

    def introduction(self):
        super().introduction()
        
    def make_appointment(self):
        print(f"{self.name} is making an appointment for a checkup.")

    def buy_medicine(self):
        print(f"{self.name} is buying a medicine.")

    def pay(self, payment, fee):
        print(f"{self.name.capitalize()} is paying for {payment}.")
        print(f"You currently have PHP{self.wallet}.")
        self.wallet -= fee
        print(f"You only have PHP{self.wallet} left.")