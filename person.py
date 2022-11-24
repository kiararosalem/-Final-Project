#person
class Person:
    def __init__(self,name,age,contact,address):
        self.name = name 
        self.age =  age 
        self.contact = contact
        self.address = address

    def printname (self):
        print(self.name,self.age, self.contact, self.address)

class Employee (Person):
    def __init__(self,name,age,contact,address):
        super().__init__(name,age,contact,address)

    def printname (self):
        print(self.name, self.age, self.contact, self.address)

class Doctor(Employee):
    def __init__(self,name,age,contact,address):
        super().__init__(name,age,contact,address)

    def Checkup (self):
        print(f"{self.name} is performing a check up on {Patientname}")

#class Pharmacist(Employee):
    #def __init__(self,name,age,contact,address):
        #super().__init__(name,age,contact,address)

    #def Checkup (self):
        #print(f"{self.name} is performing a check up on {Patientname}")S


employee = Person ("Dr. Riza Villanueva", 45, "092769587063", "Batangas Rizal Avenue")
employee.printname()

class Patient (Person):
    def __init__(self,name,age,contact,address):
        super().__init__(name,age,contact,address)

    def printname (self):
        print(self.name, self.age, self.contact, self.address)

Patientname = input("Enter your name: ")
Patientage = input("Enter your age: ")
Patientcontact = input("Enter your contact: ")
Patientaddress = input("Enter your address: ")

kiara = Patient(Patientname,Patientage,Patientcontact,Patientaddress)
kiara.printname()
#employee = Person ("Riza", "Villanueva", 45, "092769587063", "Batangas Rizal Avenue")
#employee.printname()

doktor = Doctor("a", 1, 1, "a")
doktor.Checkup()


    
