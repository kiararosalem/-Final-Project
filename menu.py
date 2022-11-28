from drug_store import *
from clinic import *

#This is only for testing the code

c = Clinic()
c.introduce()
c.add_appointment()
c.checkup_with_prescription()
c.pay_checkup()
c.finished_appointment()

d = DrugStore()
d.buy()