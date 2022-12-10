from ClinicOperations.doctor_information import Doctor
from ClinicOperations.patient_information import Patient
from ClinicOperations.medicine_list import Medicine
from ClinicOperations.appointment_list import Appointment
import maskpass

class Menu:
    def __init__(self):
        self.doc=Doctor()
        self.patient=Patient()
        self.med=Medicine()
        self.appoint=Appointment()

    def main_menu(self):
        while True:
            print ('-'*70)
            print("\n\t\tWelcome to Clinic Management System\n")
            print ('-'*70)
            print("\n\t\t[1] Admin Menu")
            print("\t\t[2] Patient Menu")
            print("\t\t[3] Exit")
            choice = input("\n\t\tWhere do you want to go? ")
            if choice == '1':
                self.admin_menu()
            elif choice == '2':
                self.patient_menu()
            elif choice == '3':
                exit()
            else:
                print("\n\t\tInvalid choice.") 

    def admin_menu(self):
        while True:
            print ('-'*70)
            print("\n\t\tEnter the password for the admin menu.\n\t\tPress [1] if you want to go back to main menu.")
            password = maskpass.askpass(prompt="\n\t\t--> ", mask="*")      #masks the password
            if password == 'adminpassword':
                while True:
                    print ('-'*70)
                    print("\n\t\t-----Admin Menu-----\n")
                    print ('-'*70)
                    print("\n\t\t[1] Patient Records")
                    print("\t\t[2] Doctors' Informations")
                    print("\t\t[3] Medicine List")
                    print("\t\t[4] Appointment List")
                    print("\t\t[5] Go back to Main Menu")
                    print("\t\t[6] Exit")
                    choice = input("\n\t\tWhere do you want to go? ")
                    if choice == '1':
                        self.patient_records_menu()
                    elif choice == '2':
                        self.doctor_information_menu()
                    elif choice == '3':
                        self.medicine_menu()
                    elif choice == '4':
                        self.appointment_menu()
                    elif choice == '5':
                        return
                    elif choice == '6':
                        exit()
                    else:
                        print("\n\t\tInvalid choice.") 
            elif password == '1':
                return
            else:
                print("\t\tInvalid choice.")

    def patient_menu(self):
        while True:
            print ('-'*70)
            print("\n\t\t-----Patient Menu-----\n")
            print ('-'*70)
            print("\n\t\t[1] Make an Appointment")
            print("\t\t[2] Buy Medicine")
            print("\t\t[3] Go back to Main Menu")
            print("\t\t[4] Exit")
            choice = input("\n\t\tWhere do you want to go? ")
            if choice == '1':
                self.appoint.add()
            elif choice == '2':
                self.med.buy()
            elif choice == '3':
                return
            elif choice == '4':
                exit()
            else:
                print("\n\t\tInvalid choice.") 

    def appointment_menu(self):
        while True:
            print ('-'*70)
            print("\n\t\t-----Appointment Menu-----\n")
            print ('-'*70)
            print("\n\t\t[1] Make an Appointment")
            print("\t\t[2] View Appointment lists")
            print("\t\t[3] Modify Appointment")
            print("\t\t[4] Delete Appointment")
            print("\t\t[5] Go back to Admin Menu")
            print("\t\t[6] Exit")
            choice = input("\n\t\tWhere do you want to go? ")
            if choice == '1':
                self.appoint.add()
            elif choice == '2':
                self.appoint.read()
                input("\t\tPress enter to continue.")
            elif choice == '3':
                self.appoint.update()
            elif choice == '4':
                self.appoint.delete()
            elif choice == '5':
                return
            elif choice == '6':
                exit()
            else:
                print("\n\t\tInvalid choice.") 

    def patient_records_menu(self):
        while True:
            print ('-'*70)
            print("\n\t\t-----Patient Records Menu-----\n")
            print ('-'*70)
            print("\n\t\t[1] Add new Patient Record")
            print("\t\t[2] Search Patient Record")
            print("\t\t[3] View Patient Records")
            print("\t\t[4] Modify Patient Record")
            print("\t\t[5] Delete Patient Record")
            print("\t\t[6] Go back to Admin Menu")
            print("\t\t[7] Exit")
            choice = input("\n\t\tWhere do you want to go? ")
            if choice == '1':
                self.patient.add()
            elif choice == '2':
                self.patient.search()
            elif choice == '3':
                self.patient.read()
                input("\t\tPress enter to continue.")
            elif choice == '4':
                self.patient.update()
            elif choice == '5':
                self.patient.delete()
            elif choice == '6':
                return
            elif choice == '7':
                exit()
            else:
                print("\n\t\tInvalid choice.") 

    def doctor_information_menu(self):
        while True:
            print ('-'*70)
            print("\n\t\t-----Doctor Information Menu-----\n")
            print ('-'*70)
            print("\n\t\t[1] Add new Doctor")
            print("\t\t[2] Search a Doctor")
            print("\t\t[3] View Doctor lists")
            print("\t\t[4] Modify Doctor's Information")
            print("\t\t[5] Delete Doctor's Information")
            print("\t\t[6] Go back to Admin Menu")
            print("\t\t[7] Exit")
            choice = input("\n\t\tWhere do you want to go? ")
            if choice == '1':
                self.doc.add()
            elif choice == '2':
                self.doc.search()
            elif choice == '3':
                self.doc.read()
                input("\t\tPress enter to continue.")
            elif choice == '4':
                self.doc.update()
            elif choice == '5':
                self.doc.delete()
            elif choice == '6':
                return
            elif choice == '7':
                exit()
            else:
                print("\n\t\tInvalid choice.") 

    def medicine_menu(self):
        while True:
            print ('-'*70)
            print("\n\t\t-----Medicine Menu-----\n")
            print ('-'*70)
            print("\n\t\t[1] Add new Medicine")
            print("\t\t[2] Search a Medicine")
            print("\t\t[3] View Medicine lists")
            print("\t\t[4] Modify Medicine Information")
            print("\t\t[5] Delete Medicine Information")
            print("\t\t[6] Buy Medicine")
            print("\t\t[7] Go back to Admin Menu")
            print("\t\t[8] Exit")
            choice = input("\n\t\tWhere do you want to go? ")
            if choice == '1':
              self.med.add()  #add
            elif choice == '2':
              self.med.search()   #search
            elif choice == '3':
                self.med.read()     #view/display/show
                input("\t\tPress enter to continue.")   
            elif choice == '4':
                self.med.update()   #update/modify
            elif choice == '5':
                self.med.delete()    #delete
            elif choice == '6':
                self.med.buy()    #buy medicine
            elif choice == '7':
                return
            elif choice == '8':
                exit()
            else:
                print("\n\t\tInvalid choice.") 