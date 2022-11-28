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

        name = self.patient.name
        
        if len(self.patient_queue) >= 10:
            print("Sorry we are currently full.")
        else:
            self.asst.sched_appointment(self.patient.name)
            self.patient_queue.append(self.patient.name)
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
        age = self.patient.age
        contact = self.patient.contact
        address = self.patient.address
        concerns = self.patient.concerns

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
        concerns = input("Are you feeling unwell?\nIf so, What symptom do you currently have?")
        self.patient.concerns = concerns
        #accesing the nested dict
        self.patient_records[f"{self.patient.name.upper()}"]["Medical_History"].append(self.patient.concerns)

    def checkup_with_prescription(self):
        self.doc.check_up(self.patient_queue[0])
        print("\"It seems that you will be fine as long as you take this medicine and rest a lot\"")
        self.doc.give_medication(self.patient_queue[0])        

    def pay_checkup(self):
        self.patient.pay("Check up Fee", 400)




#test
#c = Clinic()
#c.introduce()
#c.add_appointment()
#c.checkup_with_prescription()
#c.pay_checkup()
#c.finished_appointment()