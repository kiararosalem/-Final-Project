import os
import json

class Patient:
    def __init__(self):
        if os.path.exists('patient_records.json'): pass #this checks if the file exists
        else:    #if not it will create a new file
            f = open('patient_records.json','x')
            f.close()
        self.patient_records = {} #dictionary

    def load_from_file(self):   #loads the data on the file to the dict self.patient_records
        if os.stat('patient_records.json').st_size == 0:  #checks if the file is empty
            pass
        else:  #if not it will load the information from the file to the dictionary
            with open('patient_records.json') as f:
                self.patient_records = json.load(f)
            f.close()

    def write_to_file(self):  #writing the dictionary to the json file
        with open('patient_records.json', 'w') as f:  #writing to file
            json.dump(self.patient_records, f, indent=4)
        f.close()

    def add_patient(self):   #add patient info
        self.load_from_file()
        try:
            patient_id = input("\t\tEnter the patient's id: ")
            if patient_id in self.patient_records:   #checks if the id already exists
                print("\t\tID already exists.")
                input("\t\tPress enter to continue.")
                return
            else:   #if the id doesn't exists it will execute this block of code
                patient_info = {}
                patient_info["Name"] = input("\t\tWhat is the patient's name? ")
                patient_info["Age"] = input("\t\tWhat is the patient's age? ")
                patient_info["Gender"] = input("\t\tWhat is the patient's gender? ")
                patient_info["Address"] = input("\t\tWhat is the patient's address? ")
                patient_info["Ailment"] = input("\t\tWhat is the patient's ailment? ")
                self.patient_records[patient_id] = patient_info  #putting the patient_info dictionary inside the patient_records dictionary
        except:
            print("\t\tAn error occurred.")
        self.write_to_file()

    def update_patient(self):   #update patient info
        self.load_from_file()
        self.show_patient_info()
        try:  #checks if the patient id exists
            update = input("\t\tChoose the patient id that you want to modify: ")
            self.patient_records[update] 
        except KeyError:  #if not it will print out the error message
            print("\t\tDoctor's information not found.")
            input("\t\tPress enter to continue.")
        else:   #this will execute if the try block executed
            self.patient_records[update]["Name"] = input("\t\tWhat will be the updated name? ")
            self.patient_records[update]["Age"] = input("\t\tWhat will be the updated age? ")
            self.patient_records[update]["Gender"] = input("\t\tWhat will be the updated gender? ")
            self.patient_records[update]["Address"] = input("\t\tWhat will be the updated address? ")
            self.patient_records[update]["Ailment"]= input("\t\tWhat will be the updated ailment? ")
            self.write_to_file()

    def show_patient_info(self):  #display informations
        self.load_from_file()
        print('-'*70)
        print("\t\t-Patient Records-")
        print(f"\t\tCurrent number of Patient: {len(self.patient_records)}")
        print('-'*70)
        for patient_id, patient_info in self.patient_records.items():
            print("\t\tPatient ID:", patient_id)
            for key in patient_info:
                print(f"\t\t{key}: {patient_info[key]}")
            print('-'*70)

    def delete_patient(self):   #delete patient info
        self.load_from_file()
        self.show_patient_info()
        try:  #checks if the id exists
            delete = input("\t\tChoose the patient id that you want to delete: ")
            self.patient_records[delete]
        except KeyError:   #if not it will print out the error message
            print("\t\tPatient's information not found.")
            input("\t\tPress enter to continue.")
        else:   #this will execute if the try block executed
            del self.patient_records[delete]

            self.write_to_file()

    def search_patient(self):   #search patient info
        self.load_from_file()
        try:   #checks if the id exists
            search = input("\t\tSearch Patient's ID: ")
            self.patient_records[search]
        except KeyError:  #if the try block fails the except will catch the error
            print(f"\t\t{search} does not exist")
            input("\t\tPress enter to continue.")
        else:   #this will execute if the try block executed
            print('-'*70)
            for key, value in self.patient_records[search].items():
                print(f"\t\t{key}: {value}")
            print('-'*70)
            input("\t\tPress enter to continue.")