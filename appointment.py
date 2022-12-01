import os
import json

class Appointment:
    def __init__(self):
        if os.path.exists('appointment_records.json'): pass #this checks if the file exists
        else:    #if not it will create a new file
            f = open('appointment_records.json','x')
            f.close()
        self.appointment_records = {} #dictionary

    def load_from_file(self):   #loads the data on the file to the dict self.doctor_records
        if os.stat('appointment_records.json').st_size == 0:  #checks if the file is empty
            pass
        else:  #if not it will load the information from the file to the dictionary
            with open('appointment_records.json') as f:
                self.appointment_records = json.load(f)
            f.close()

    def write_to_file(self):  #writing the dictionary to the json file
        with open('appointment_records.json', 'w') as f:  #writing to file
            json.dump(self.appointment_records, f, indent=4)
        f.close()

    def add_appointment(self):   #add appointment info
        self.load_from_file()
        try:
            appointment_id = input("\t\tEnter the appointment's id: ")
            if appointment_id in self.appointment_records:   #checks if the id already exists
                print("\t\tID already exists.")
                input("\t\tPress enter to continue.")
                return
            else:   #if the id doesn't exists it will execute this block of code
                appointment_info = {}
                appointment_info["Name"] = input("\t\tWhat is the patient's name? ")
                appointment_info["Age"] = input("\t\tWhat is the patients's age? ")
                appointment_info["Gender"] = input("\t\tWhat is the patient's gender? ")
                appointment_info["Address"] = input("\t\tWhat is the patient's address? ")
                self.appointment_records[appointment_id] = appointment_info  #putting the appointment_info dictionary inside the doctor_records dictionary
        except:
            print("\t\tAn error occurred.")
        self.write_to_file()

    def update_appointment(self):   #update appointment info
        self.load_from_file()
        self.show_appointment_info()
        try:  #checks if the doctor id exists
            update = input("\t\tChoose the patient's id that you want to modify: ")
            self.appointment_records[update] 
        except KeyError:  #if not it will print out the error message
            print("\t\tPatient's information not found.")
            input("\t\tPress enter to continue.")
        else:   #this will execute if the try block executed
            self.appointment_records[update]["Name"] = input("\t\tWhat will be the updated name? ")
            self.appointment_records[update]["Age"] = input("\t\tWhat will be the updated age? ")
            self.appointment_records[update]["Gender"] = input("\t\tWhat will be the updated gender? ")
            self.appointment_records[update]["Address"] = input("\t\tWhat will be the updated address? ")
            self.write_to_file()

    def show_appointment_info(self):  #display informations
        self.load_from_file()
        print('-'*70)
        print("\t\t-Patients Records-")
        print(f"\t\tCurrent number of the Patient:{len(self.appointment_records)}")
        print('-'*70)
        for appointment_id, appointment_info in self.appointment_records.items():
            print("\t\tPatient's ID:", appointment_id)
            for key in appointment_info:
                print(f"\t\t{key}: {appointment_info[key]}")
            print('-'*70)

    def delete_appointment(self):   #delete appointment info
        self.load_from_file()
        self.show_appointment_info()
        try:  #checks if the id exists
            delete = input("\t\tChoose the patient id that you want to delete: ")
            self.appointment_records[delete]
        except KeyError:   #if not it will print out the error message
            print("\t\tPatient's information not found.")
            input("\t\tPress enter to continue.")
        else:   #this will execute if the try block executed
            del self.appointment_records[delete]

            self.write_to_file()

    def search_appointment(self):   #search appointment info
        self.load_from_file()
        try:   #checks if the id exists
            search = input("\t\tSearch Patient's ID: ")
            self.appointment_records[search]
        except KeyError:  #if the try block fails the except will catch the error
            print(f"\t\t{search} does not exist")
            input("\t\tPress enter to continue.")
        else:   #this will execute if the try block executed
            print('-'*70)
            for key, value in self.appointment_records[search].items():
                print(f"\t\t{key}: {value}")
            print('-'*70)
            input("\t\tPress enter to continue.")