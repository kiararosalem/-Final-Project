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

    def checkUp (self, patientName):
        print(f"{self.name} is performing a check up on {patientName}")

    def giveMedication(self, patientName):
        print(f"{self.name} is giving a presciption to {patientName}")

#Assistant
class Assistant(Employee):
    def __init__(self, name, age, contact, address):
        super().__init__(name, age, contact, address)

    def recordPatientInfo(self, patientName):
        print(f"{self.name} is recording {patientName}'s medical record.")

    def schedAppointment(self, patientName):
        print(f"{self.name} is scheduling an appointment for {patientName}")
    

#Pharmacist
class Pharmacist(Employee):
    def __init__(self, name, age, contact, address):
        super().__init__(name, age, contact, address)

    def readPrescription(self, doctorName):
        print(f"{self.name} is reading the Dr. {doctorName}'s prescription.")

    def giveMedicine(self, patientName):
        print(f"{self.name} is giving the medicine to {patientName}")

#Patient
class Patient (Person):
    def __init__(self, name, age, contact, address):
        super().__init__(name, age, contact, address)

    def introduction(self):
        super().introduction()

    def makeAppointment(self):
        print(f"{self.name} is making an appointment for a checkup.")

    def buyMedicine(self):
        print(f"{self.name} is buying a medicine.")

    def pay(self, payment):
        print(f"{self.name} is paying for {payment}")