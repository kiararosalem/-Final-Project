import os
import json
from ClinicOperations.crud_system import CRUD

class Appointment(CRUD):
    def __init__(self):
        if os.path.exists('appointment_list.json'): pass #this checks if the file exists
        else:    #if not it will create a new file
            f = open('appointment_list.json','x')
            f.close()
        self.appointment_records = {} #dictionary

    def load_from_file(self):   #loads the data on the file to the dict self.appointment_records
        if os.stat('appointment_list.json').st_size == 0:  #checks if the file is empty
            pass
        else:  #if not it will load the information from the file to the dictionary
            with open('appointment_list.json') as f:
                self.appointment_records = json.load(f)

    def write_to_file(self):  #writing the dictionary to the json file
        with open('appointment_list.json', 'w') as f:  #writing to file
            json.dump(self.appointment_records, f, indent=4)

    def add(self):   #add Appointment info
        self.load_from_file()
        try:
            name = input("\t\tWhat is the Patient's name? ")
            if name in self.appointment_records:   #checks if the id already exists
                print("\t\tName already exists.")
                input("\t\tPress enter to continue.")
                return
            else:
                month = int(input("\t\tWhich month of the year (1-12)?  "))
                day = int(input("\t\tWhich day of the month? "))
                year = int(input("\t\tWhat year? "))
                date = (f"{month}/{day}/{year}")
                self.appointment_records[name] = date
                self.write_to_file()
        except:
            print("\t\tYou did not enter a number.")
            input("\t\tPress enter to continue.")

    def read(self):  #display informations
        self.load_from_file()
        print('-'*70)
        print("\t\t-Appointment Records-")
        print(f"\t\tCurrent number of Appointments:{len(self.appointment_records)}")
        print('-'*70)
        for key in self.appointment_records:
            print(f"\t\t{key}: {self.appointment_records[key]}")
            print('-'*70)

    def update(self):   #update appointment info
        self.read()
        try:  #checks if the appointment name exists
            update = input("\t\tChoose the name that you want to modify: ")
            self.appointment_records[update] 
        except KeyError:  #if not it will print out the error message
            print("\t\tAppointment information not found.")
            input("\t\tPress enter to continue.")
        else:   #this will execute if the try block executed
            try:
                month = int(input("\t\What is the updated month(1-12)? "))
                day = int(input("\t\tWhat is the updated day of the month? "))
                year = int(input("\t\tWhat is the updated year? "))
                date = (f"{month}/{day}/{year}")
                self.appointment_records[update] = date
                self.write_to_file()
            except:
                print("You did not input a number.")
                input("\t\tPress enter to continue.")

    def delete(self):   #delete Appointment info
        self.show_appointment()
        try:  #checks if the id exists
            delete = input("\t\tChoose the name that you want to delete: ")
            self.appointment_records[delete]
        except KeyError:   #if not it will print out the error message
            print("\t\tAppointment's information not found.")
            input("\t\tPress enter to continue.")
        else:   #this will execute if the try block executed
            del self.appointment_records[delete]
            self.write_to_file()