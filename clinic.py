from person import *
import json
import os

#Clinic
class Clinic:
    def __init__(self):
        self.patient_queue = []
        self.patient_records = {} #patient name,age,contact,medical history
        if os.path.exists('patient_records.json'):
            pass
        else:
            f = open('patient_records.json','x')
            f.close()
        
        #composition
        self.doc=Doctor() 
        self.asst=Assistant() 
        self.patient=Patient()
        self.med=Prescription()

    def introduce(self):
        print("Welcome to Solana's Clinic.")

    def add_appointment(self):
        if os.stat("patient_records.json").st_size == 0:
            pass
        else:
            f = open('patient_records.json')
            data = json.load(f)
            self.patient_records = data
            f.close()

        name = input("What is your name? ")
        self.patient.name = name
        
        if len(self.patient_queue) >= 10:
            print("Sorry we are currently full.")
        else:
            self.asst.sched_appointment(self.patient.name)
            self.patient_queue.append(name)
            #print(self.patient_queue)
            if name.upper() in self.patient_records:
                print("Already exist only append medical history") #to be deleted/modified
                self.old_patient_record()
            else:
                self.new_patient_record()

        with open('patient_records.json', 'w') as fp:
            json.dump(self.patient_records, fp, indent=4)
        fp.close()

    def finished_appointment(self):
        self.patient_queue.pop(0)
        print("Thank you for visiting our clinic.")

    def new_patient_record(self):
        age =  input("Enter your age: ")
        contact = input("Kindly input your contact number: ")
        address = input("Enter your address: ")
        concerns = input("Are you feeling unwell?\nIf so, What symptom do you currently have? ")

        self.patient.age = age
        self.patient.contact = contact
        self.patient.address = address
        self.patient.concerns = concerns

        patient_info = {}
        self.asst.record_patient_info(self.patient.name)
        self.patient_records[f"{self.patient.name.upper()}"] = patient_info
        patient_info["Name"] = self.patient.name
        patient_info["Age"] = self.patient.age
        patient_info["Contact"] = self.patient.contact
        patient_info["Medical_History"] = []
        patient_info["Medical_History"].append(self.patient.concerns)
        #print(self.patient_records)

    def old_patient_record(self):
        concerns = input("Are you feeling unwell?\nIf so, What symptom do you currently have? ")
        self.patient.concerns = concerns
        #accesing the nested dict
        self.patient_records[f"{self.patient.name.upper()}"]["Medical_History"].append(self.patient.concerns)

    def checkup_with_prescription(self):
        self.doc.check_up(self.patient_queue[0])
        print("\"It seems that you will be fine as long as you take this medicine and rest a lot\"")
        self.doc.give_medication(self.patient_queue[0])     
        self.med.write_prescription(self.doc.name, self.patient.name, self.patient.wallet)   

    def pay_checkup(self):
        self.patient.pay("Check up Fee")
        fee = 400
        print(f"You currently have PHP{self.patient.wallet}.")
        self.patient.wallet -= fee
        print(f"You only have PHP{self.patient.wallet} left.")

class Prescription:
    def write_prescription(self, doc_name, pname, wallet):
        medicine = input("What medicine should i prescribe? ")
        doctor_name = doc_name
        patient_name = pname
        current_patient_wallet = wallet