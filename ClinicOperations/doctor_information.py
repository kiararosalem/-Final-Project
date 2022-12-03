import os
import json

class Doctor:
    def __init__(self):
        if os.path.exists('doctor_records.json'): pass #this checks if the file exists
        else:    #if not it will create a new file
            f = open('doctor_records.json','x')
            f.close()
        self.doctor_records = {} #dictionary

    def load_from_file(self):   #loads the data on the file to the dict self.doctor_records
        if os.stat('doctor_records.json').st_size == 0:  #checks if the file is empty
            pass
        else:  #if not it will load the information from the file to the dictionary
            with open('doctor_records.json') as f:
                self.doctor_records = json.load(f)
            f.close()

    def write_to_file(self):  #writing the dictionary to the json file
        with open('doctor_records.json', 'w') as f:  #writing to file
            json.dump(self.doctor_records, f, indent=4)
        f.close()

    def add_doctor(self):   #add doctor info
        self.load_from_file()
        try:
            doc_id = input("\t\tEnter the doctor's id: ")
            if doc_id in self.doctor_records:   #checks if the id already exists
                print("\t\tID already exists.")
                input("\t\tPress enter to continue.")
                return
            else:   #if the id doesn't exists it will execute this block of code
                doctor_info = {}
                doctor_info["Name"] = input("\t\tWhat is the doctor's name? ")
                doctor_info["Age"] = input("\t\tWhat is the doctor's age? ")
                doctor_info["Gender"] = input("\t\tWhat is the doctor's gender? ")
                doctor_info["Address"] = input("\t\tWhat is the doctor's address? ")
                self.doctor_records[doc_id] = doctor_info  #putting the doctor_info dictionary inside the doctor_records dictionary
        except:
            print("\t\tAn error occurred.")
        self.write_to_file()

    def update_doctor(self):   #update doctor info
        self.load_from_file()
        self.show_doc_info()
        try:  #checks if the doctor id exists
            update = input("\t\tChoose the doctor id that you want to modify: ")
            self.doctor_records[update] 
        except KeyError:  #if not it will print out the error message
            print("\t\tDoctor's information not found.")
            input("\t\tPress enter to continue.")
        else:   #this will execute if the try block executed
            self.doctor_records[update]["Name"] = input("\t\tWhat will be the updated name? ")
            self.doctor_records[update]["Age"] = input("\t\tWhat will be the updated age? ")
            self.doctor_records[update]["Gender"] = input("\t\tWhat will be the updated gender? ")
            self.doctor_records[update]["Address"] = input("\t\tWhat will be the updated address? ")
            self.write_to_file()

    def show_doc_info(self):  #display informations
        self.load_from_file()
        print('-'*70)
        print("\t\t-Doctor Records-")
        print(f"\t\tCurrent number of Doctors: {len(self.doctor_records)}")
        print('-'*70)
        for doc_id, doc_info in self.doctor_records.items():
            print("\t\tDoctor ID:", doc_id)
            for key in doc_info:
                print(f"\t\t{key}: {doc_info[key]}")
            print('-'*70)

    def delete_doctor(self):   #delete doctor info
        self.load_from_file()
        self.show_doc_info()
        try:  #checks if the id exists
            delete = input("\t\tChoose the doctor id that you want to delete: ")
            self.doctor_records[delete]
        except KeyError:   #if not it will print out the error message
            print("\t\tDoctor's information not found.")
            input("\t\tPress enter to continue.")
        else:   #this will execute if the try block executed
            del self.doctor_records[delete]

            self.write_to_file()

    def search_doctor(self):   #search doctor info
        self.load_from_file()
        try:   #checks if the id exists
            search = input("\t\tSearch Doctor's ID: ")
            self.doctor_records[search]
        except KeyError:  #if the try block fails the except will catch the error
            print(f"\t\t{search} does not exist")
            input("\t\tPress enter to continue.")
        else:   #this will execute if the try block executed
            print('-'*70)
            for key, value in self.doctor_records[search].items():
                print(f"\t\t{key}: {value}")
            print('-'*70)
            input("\t\tPress enter to continue.")