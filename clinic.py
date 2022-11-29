import json
import os
from person import *

#Clinic
class Clinic:
    def __init__(self):
        self.patient_queue = []   #appointment list
        self.patient_records = {}   #dict containg patient name,age,contact,address,medical history
        if os.path.exists('patient_records.json'):   # checking if the file already exists
            pass
        else:   #if not it will create a new file
            f = open('patient_records.json','x')
            f.close()
        
        #composition
        self.doc=Doctor() #doc is an instance of Doctor class
        self.asst=Assistant() #same idea as above
        self.patient=Patient() #same idea as above
        self.med=Prescription() #same idea as above

    def introduce(self): #simple introduction
        print("Welcome to Solana's Clinic.")

    def add_appointment(self):  #adding patient to appointment list 
        try:
            if os.stat("patient_records.json").st_size == 0:  #checking if file is empty
                pass
            else: #it will load the informations inside the file to the dict patient_records
                f = open('patient_records.json')
                data = json.load(f)
                self.patient_records = data
                f.close()

            name = input("What is your name? ")
            self.patient.name = name
        
            if len(self.patient_queue) >= 10:    #checking if the appointment list is full
                print("Sorry we are currently full.")
            else:   #if the queue is not full, it will get the information of the patient
                self.asst.sched_appointment(self.patient.name)
                self.patient_queue.append(name)   #and also add the patient to the appointment list
                #print(self.patient_queue) <-- this is just for checking if the code works
                if name.upper() in self.patient_records:   #checks if the patient is already listed on the patient records
                    #print("Already exist only append medical history") #to be deleted/modified
                    self.old_patient_record()   #if true, it will only ask for the reason why the patient is in the clinic
                else:
                    self.new_patient_record()   #if false, it will take all of the necessary information needed and create a new record for thh person

            with open('patient_records.json', 'w') as fp:  #writing to file
                json.dump(self.patient_records, fp, indent=4)
            fp.close()
        except:
            print("An error occurred.")

    def finished_appointment(self):  #removing from appointment list
        self.patient_queue.pop(0)
        print("Thank you for visiting our clinic.")

    def new_patient_record(self):  #adding patient info
        try:
            age =  input("Enter your age: ")
            contact = input("Kindly input your contact number: ")
            address = input("Enter your address: ")
            concerns = input("Are you feeling unwell?\nIf so, What symptom do you currently have? ")

            self.patient.age = age
            self.patient.contact = contact
            self.patient.address = address
            self.patient.concerns = concerns

            patient_info = {}  
            self.asst.record_patient_info(self.patient.name)  #this just a dialogue for the assistant
            self.patient_records[f"{self.patient.name.upper()}"] = patient_info
            patient_info["Name"] = self.patient.name
            patient_info["Age"] = self.patient.age
            patient_info["Contact"] = self.patient.contact
            patient_info["Medical_History"] = []
            patient_info["Medical_History"].append(self.patient.concerns)
            #print(self.patient_records) <-- this is just for checking if the code works
        except:
            print("An error occurred.")

    def old_patient_record(self):   #adding new medical history in patient info
        try:
            concerns = input("Are you feeling unwell?\nIf so, What symptom do you currently have? ")
            self.patient.concerns = concerns
            #accesing the nested dict and appending to the list
            self.patient_records[f"{self.patient.name.upper()}"]["Medical_History"].append(self.patient.concerns)
        except:
            print("An error occurred.")

    def checkup_with_prescription(self):  #the doctor is checking up on the patient 
        try:
            self.doc.check_up(self.patient_queue[0]) #dialogue
            print("\"It seems that you will be fine as long as you take this medicine and rest a lot\"")
            self.doc.give_medication(self.patient_queue[0])   #another dialogue
            self.med.write_prescription(self.doc.name, self.patient_queue[0])   #accessing the method of class Prescription
        except:
            print("An error occurred.")

    def pay_checkup(self):   #payment for checkup
        try:
            self.patient.pay("Check up Fee")  #dialogue
            fee = 400
            print(f"You currently have PHP{self.patient.wallet}.")
            self.patient.wallet -= fee
            print(f"You only have PHP{self.patient.wallet} left.")
            current_wallet = str(self.patient.wallet)

            with open('prescription.txt', 'a') as f:  #writing to file
                f.write(current_wallet)
            f.close()
        except:
            print("An error occurred.")
        
class Prescription:  #this class is for the prescription that the patient will receive
    def write_prescription(self, doc_name, pname):
        try:
            medicine = input("What medicine should i prescribe? ")
            doctor_name = doc_name
            patient_name = pname

            with open('prescription.txt', 'w') as f:  #writing to file
                f.write(f"{medicine}\n{doctor_name}\n{patient_name}\n")
            f.close()
        except:
            print("An error occurred.")