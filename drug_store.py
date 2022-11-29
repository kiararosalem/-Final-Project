import json
import os
from person import *

#Drug Store
class Medicine:
    def __init__(self):
        if os.path.exists('medicine_list.json'):  #checking if the file exists
            pass
        else:    #if not it will create a new file
            f = open('medicine_list.json','x')
            f.close()

        self.medicine_list = {} #dict containing medicine name, price and quantity

        if os.stat("medicine_list.json").st_size == 0:  #checks if the file is empty
            pass
        else:  #if not it will load the information from the file to the dict
            with open('medicine_list.json') as f:
                data = json.load(f)
                self.medicine_list = data
            f.close()
            


class DrugStore:
    def __init__(self):
        #composition
        self.pharm=Pharmacist() #creating an instance of the class Pharmacist
        self.med=Medicine()  #same idea as above

        with open('prescription.txt') as f: #grabbing the information inside the file and putting it inside a list
            self.prescription = [line.rstrip('\n') for line in f] #list containing: 0-medicine, 1-dr name, 2-patient name, 3-current wallet

    def introduce(self):
        print("Welcome to Solana's Drug Store.")

    def add_medicine(self):  #adding of medicine to the medicine list
        if os.stat("medicine_list.json").st_size == 0:   #checks if the file is empty
            pass
        else:    #if not it will load the information from the file to the dict
            with open('medicine_list.json') as f:
                data = json.load(f)
                self.med.medicine_list = data
            f.close()

        new_medicine = input("What is the name of the medicine that you want to add?\n--> ")
        if new_medicine.upper() in self.med.medicine_list:  #checks if the medicine already exists
            print("Medicine already exists.")
        else:   #executes if the condition is false
            med_price = float(input("How much would the medicine be? "))
            med_qty = int(input("How many stocks of this medicine would you like to have?\n--> "))

            medicine_info = {}
            self.med.medicine_list[new_medicine.upper()] = medicine_info  #putting the dict inside the other dictionary
            medicine_info["Medicine_Name"] = new_medicine.capitalize()
            medicine_info["Price"] = med_price
            medicine_info["Quantity"] = med_qty

            with open('medicine_list.json', 'w') as f:  #writing to file
                json.dump(self.med.medicine_list, f, indent=4)
            f.close()


    def start(self): # simple menu, planning to change this
        choice = input("What can we do for you?\n[1] Buy Medicine\n[2] Exit\n--> ")
        if choice == '1':
            self.read_prescription() #start of program
            self.check_stock()
            self.payment()
            self.receive_medicine()
        else:
            exit()

    def read_prescription(self): 
        print(f"{self.prescription[2]} is giving the prescription to the pharmacist.")
        self.pharm.read_prescribed(self.prescription[1])
        self.request_medicine = self.prescription[0]
        self.medicine_quantity = int(input("How many would you like to buy? "))


    def check_stock(self):  #checks the stock 
        try:
            if self.request_medicine.upper() in self.med.medicine_list:
                if self.medicine_quantity > self.med.medicine_list[f"{self.request_medicine.upper()}"]["Quantity"]:
                    print("Sorry we are out of stock.")
            else:
                print("We dont have the medicine that you were looking for.")
        except:
            print("An error occurred.")

    def payment(self):  #paying for the medicine
        print(f"{self.prescription[2]} is paying for their medicine.")
        patient_wallet = int(self.prescription[3])
        price = self.med.medicine_list[f"{self.request_medicine.upper()}"]["Price"]
        amount = float(price*self.medicine_quantity)
        if amount <= patient_wallet:
            patient_wallet -= amount
            print(f"You have PHP{patient_wallet} left in your wallet.")
        else:
            print("Sorry you don't have enough money.")

    def receive_medicine(self):  #patient receives medicine
        self.pharm.give_medicine(self.prescription[2])
        print("Thank you for buying from us.")
