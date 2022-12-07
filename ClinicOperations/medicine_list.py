import os
import json
from ClinicOperations.crud_system import CRUD

class Medicine(CRUD):
    def __init__(self):
        if os.path.exists('medicine_list.json'): pass #this checks if the file exists
        else:    #if false it will create a new file
            f = open('medicine_list.json','x')
            f.close()
        self.medicine_list = {}

    def load_from_file(self):   #loads the data on the file to the dict self.medicine_list
        if os.stat('medicine_list.json').st_size == 0:  #checks if the file is empty
            pass
        else:  #if not it will load the information from the file to the dictionary
            with open('medicine_list.json') as f:
                self.medicine_list = json.load(f)

    def write_to_file(self):  #writing the dictionary to the json file
        with open('medicine_list.json', 'w') as f:  #writing to file
            json.dump(self.medicine_list, f, indent=4)

    def add(self):   #add medicine 
        self.load_from_file()
        try:
            ref_id = input("\t\tEnter the Medicine's id: ")
            if ref_id in self.medicine_list:   #checks if the id already exists
                print("\t\tID already exists.")
                input("\t\tPress enter to continue.")
                return
            else:   #if the id doesn't exists it will execute this block of code
                medicine_info = {}
                medicine_info["Medicine_Name"] = input("\t\tWhat is the medicine's name? ")
                medicine_info["Price"] = float(input("\t\tWhat is the medicine's price? "))
                medicine_info["Quantity"] = int(input("\t\tHow many stocks would you like to have on this medicine? "))
                self.medicine_list[ref_id] = medicine_info  
                self.write_to_file()
        except:
            print("\t\tPlease enter a number in Price/Quantity.")
            input("\t\tPress enter to continue.")

    def search(self):   #search medicine info
        self.load_from_file()
        try:   #checks if the id exists
            search = input("\t\tSearch Medicine's ID: ")
            self.medicine_list[search]
        except KeyError:  #if the try block fails the except will catch the error
            print(f"\t\t{search} does not exist")
            input("\t\tPress enter to continue.")
        else:   #this will execute if the try block executed
            print('-'*70)
            for key, value in self.medicine_list[search].items():
                print(f"\t\t{key}: {value}")
            print('-'*70)
            input("\t\tPress enter to continue.")

    def read(self):  #display info
        self.load_from_file()
        print('-'*70)
        print("\t\t-Medicine List-")
        print(f"\t\tCurrent number of Medicine: {len(self.medicine_list)}")
        print('-'*70)
        for ref_id, medicine_info in self.medicine_list.items():
            print("\t\tMedicine ID:", ref_id)
            for key in medicine_info:
                print(f"\t\t{key}: {medicine_info[key]}")
            print('-'*70)

    def update(self):   #update medicine 
        self.read() 
        try:  #checks if the medicine id exists
            update = input("\t\tChoose the medicine id that you want to modify: ")
            self.medicine_list[update] 
        except KeyError:  #if not it will print out the error message
            print("\t\tMedicine's information not found.")
            input("\t\tPress enter to continue.")
        else:   #this will execute if the try block executed
            try:
                self.medicine_list[update]["Medicine_Name"] = input("\t\tWhat will be the medicine's updated name? ")
                self.medicine_list[update]["Price"] = float(input("\t\tWhat will be the medicine's updated price? "))
                self.medicine_list[update]["Quantity"] = int(input("\t\tWhat will be the medicine's updated quantity? "))
                self.write_to_file()
            except:
                print("\t\tPlease enter a number in Price/Quantity.")
                input("\t\tPress enter to continue.")

    def delete(self):   #delete medicine
        self.read()
        try:  #checks if the id exists
            delete = input("\t\tEnter the medicine id that you want to delete: ")
            self.medicine_list[delete]
        except KeyError:   #if not it will print out the error message
            print("\t\tMedicine's information not found.")
            input("\t\tPress enter to continue.")
        else:   #this will execute if the try block executed
            del self.medicine_list[delete]
            self.write_to_file()

    def buy(self):    #buy medicine
        self.read()
        try:  #checks if the id exists
            buy = input("\t\tEnter the medicine id that you wish to purchase: ")
            self.medicine_list[buy]
        except KeyError:   #if not it will print out the error message
            print("\t\tMedicine's information not found.")
            input("\t\tPress enter to continue.")
        else:   #this will execute if the try block executed
            try:
                buy_quantity = input("\t\tHow many do you want to purchase? ")
                new_quantity = int(self.medicine_list[buy]["Quantity"]) - int(buy_quantity)
                if new_quantity < 0:
                    print("\t\tThe quantity that you want to buy exceeded our stock.")
                    input("\t\tPress enter to continue.")
                    return
                else:
                    self.medicine_list[buy]["Quantity"] = new_quantity
                    self.write_to_file()
            except:
                print("\t\tAn error occurred.")
                input("\t\tPress enter to continue.")