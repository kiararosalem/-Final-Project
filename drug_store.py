from person import *
from clinic import Prescription


# cant access prescription attributes!!!!!!


#Drug Store
class Medicine:
    def __init__(self):
        medicine_list = {}
        self.name = "medicine name"
        self.price = 0
        self.quantity = 0

class DrugStore:
    def __init__(self):
        self.pharm=Pharmacist()
        self.med=Prescription()

    def introduce(self):
        print("Welcome to Solana's Drug Store.")

    def buy(self):
        choice = input("What can we do for you?\n[1] Buy Medicine\n[2] Exit\n--> ")
        if choice == '1':
            self.read_prescription() #start of program
            self.check_stock()
            self.payment()
            self.receive_medicine()
        else:
            exit()

    def read_prescription(self):
        print(f"{self.med.patient_name} is giving the prescription to the pharmacist.")
        self.pharm.read_prescribed(self.med.doctor_name)
        request_medicine = self.med.medicine
        medicine_quantity = int(input("How many would you like to buy? "))


    def check_stock(self):
        try:
            if request_medicine in medicine_list:
                if medicine_quantity > self.quantity:
                    print("Sorry we are out of stock.")
            else:
                print("We dont have the medicine that you were looking for.")
        except:
            print("An error occurred.")

    def payment(self):
        print(f"{self.med.patient_name} is paying for their medicine.")
        patient_wallet = self.med.current_patient_wallet
        self.price = medicine_list[f"{request_medicine}"]["Price"]
        amount = self.price*medicine_quantity
        if amount <= patient_wallet:
            patient_wallet -= amount
        else:
            print("Sorry you don't have enough money.")

    def receive_medicine(self):
        self.pharm.give_medicine(self.med.patient_name)