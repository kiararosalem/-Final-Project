import os
import json
from PharmacyOperations.crud_system import CRUD
#from pharmacist_information.
from datetime import datetime

class Patient(CRUD):
    def __init__(self):
        if os.path.exists('patient_records.json'): pass #this checks if the file exists
        else:    #if not it will create a new file
            f = open('patient_records.json','x')
            f.close()
        self.patient_records = {} #dictionary
        self.medicine_list = {} #dictionary

    def load_from_file(self):   #loads the data on the file to the dict self.patient_records
        if os.stat('patient_records.json').st_size == 0:  #checks if the file is empty
            pass
        else:  #if not it will load the information from the file to the dictionary
            with open('patient_records.json') as f:
                self.patient_records = json.load(f)
        
        if os.stat('medicine_list.json').st_size == 0:  #checks if the file is empty
            pass
        else:  #if not it will load the information from the file to the dictionary
            with open('medicine_list.json') as f:
                self.medicine_list = json.load(f)

    def write_to_file(self):  #writing the dictionary to the json file
        with open('patient_records.json', 'w') as f:  #writing to file
            json.dump(self.patient_records, f, indent=4)

    def create(self):   #add patient info
        self.load_from_file()
        try:
            patient_id = input("\t\tEnter the patient's id: ")
            if patient_id in self.patient_records:   #checks if the id already exists
                print("\t\tID already exists.")
                input("\t\tPress enter to continue")
                return
            else:   #if the id doesn't exists it will execute this block of code
                patient_info = {}
                patient_info["Name"] = input("\t\tWhat is the patient's name? ")
                patient_info["Age"] = input("\t\tWhat is the patient's age? ")
                patient_info["Gender"] = input("\t\tWhat is the patient's gender? ")
                patient_info["Ailment"] = input("\t\tWhat is the patient's ailment? ")
                print("\t\tCreated Successfully!")
                self.patient_records[patient_id] = patient_info  #putting the patient_info dictionary inside the patient_records dictionary
                self.write_to_file()
        except:
            print("\t\tAn error occurred")

    def search(self):   #search medicine info
        self.load_from_file()
        try:   #checks if the id exists
            search = input("\t\tSearch Medicine: ")
            self.patient_records[search]
        except KeyError:  #if the try block fails the except will catch the error
            print(f"\t\t{search} does not exist")
            input("\t\tPress enter to continue")
        else:   #this will execute if the try block executed
            print('-'*70)
            for key, value in self.patient_records[search].items():
                print(f"\t\t{key}: {value}")
            print('-'*70) 
            input("\t\tPress enter to continue")
        
    def add(self):
        self.load_from_file()
        try:   #checks if the id exists
            add = input("\t\tSearch Medicine: ")
            self.medicine_list[add]
        except KeyError:  #if the try block fails the except will catch the error
            print(f"\t\t{add} does not exist")
            input("\t\tPress enter to continue")
        else:
            print('-'*70)
            print(f"\t\t{add} is added successfully")

    def delete(self):   #delete patient info
        self.load_from_file()
        try:  #checks if the id exists
            delete = input("\t\tChoose the patient id that you want to delete: ")
            self.patient_records[delete]
        except KeyError:   #if not it will print out the error message
            print("\t\tPatient's information not found")
            input("\t\tPress enter to continue")
        else:   #this will execute if the try block executed
            del self.patient_records[delete]
            self.write_to_file()

    def read(self):  #display informations
        self.load_from_file()
        print('-'*70)
        print("\t\tPatient's History Records")
        print('-'*70)
        for patient_id, datetime in self.update():
            print("\t\tPatient ID:", patient_id)
            for key in datetime:
                print(f"\t\t{key}: {datetime[key]}")
            print('-'*70)

    def update(self):   #add medicine 
        self.load_from_file()
        try:   #checks if the id exists
            add_up = input("\t\tSearch Patient ID: ")
            self.patient_records[add_up]
        except KeyError:  #if the try block fails the except will catch the error
            print(f"\t\t{add_up} does not exist")
            input("\t\tPress enter to continue")
        else:   #this will execute if the try block executed
            print('-'*70)
            now = datetime.now()
            dnt = now.strftime("%d/%m/%Y %H:%M:%S")
            print("\t\tDate and Time =", dnt)
            self.update[datetime]
            self.write_to_file()           
