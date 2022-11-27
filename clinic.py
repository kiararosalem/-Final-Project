from person import *

#Clinic
class Clinic:
    def __init__(self):
        self.patient_queue = []
        self.patient_records = {} #patient name,age,contact,medical history
        
        #composition
        self.doc=Doctor("Dr. AAA", 43, "09xxxxx", "where")
        self.asst=Assistant("Asst. CCC", 26, "09xxxxx", "there")
        self.patient=Patient()

    def add_appointment(self):
        name = input("What is the name of the patient? ")
        self.patient.name = name
        
        if len(self.patient_queue) >= 10:
            print("Sorry we are currently full.")
        else:
            self.asst.sched_appointment(self.patient.name)
            self.patient_queue.append(self.patient.name)
            print(self.patient_queue)
            if name.upper() in self.patient_records:
                print("Already exist only append medical history") #to be deleted/modified
                self.old_patient_record()
            else:
                self.new_patient_record()

    def finished_appointment(self):
        self.patient_queue.pop(0)
        print("Thank you for visiting our clinic.")

    def new_patient_record(self):
        age = input("What is the age of the patient? ")
        contact = input("How can we contact the patient? ")
        address = input("Where does the patient live? ")
        concerns = input("Are you feeling unwell?\nIf so, What symptom do you currently have?")

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
        print(self.patient_records)

    def old_patient_record(self):
        concerns = input("Are you feeling unwell?\nIf so, What symptom do you currently have?")
        self.patient.concerns = concerns
        #accesing the nested dict
        self.patient_records[f"{self.patient.name.upper()}"]["Medical_History"].append(self.patient.concerns)

    def checkup_with_prescription(self):
        self.doc.check_up(self.patient_queue[0])
        print("\"It seems that you will be fine as long as you\ntake this medicine and rest a lot\"")
        self.doc.give_medication(self.patient_queue[0])        