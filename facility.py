#Facility
class Facility:
    def __init__(self, name, address, contact):
        self.name = name 
        self.address = address
        self.contact = contact

    def printFacilityInfo(self):
        print(f"Welcome to {self.name}!")
        print(f"You can contact us on {self.contact}")

#Clinic
class Clinic:
    def __init__(self, name, address, contact):
        super().__init__(name, address, contact)
    
    def printFacilityInfo(self):
        super().printFacilityInfo()
        print("This is a facility where we take care of your health!")

#Drug Store
class DrugStore:
    def __init__(self, name, address, contact):
        super().__init__(name, address, contact)

    def printFacilityInfo(self):
        super().printFacilityInfo()
        print("This is a facility where we sell you medicine.")