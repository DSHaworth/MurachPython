# https://www.youtube.com/watch?v=3ohzBxoFHAY
##############################################
# Part 1 Setup
# "dunder" = special methods always surrounded by double underscore 
##############################################
class Employee:

    raise_amount = 1.04 

    def __init__(self, firstName, lastName, pay):  # "dunder" init
        self.firstName = firstName
        self.lastName = lastName
        self.pay = pay
        self.email = f"{firstName}.{lastName}@company.com"

    def fullname(self):
        return f"{self.firstName} {self.lastName}"  

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):  #debugging for developers
        pass

    def __str__(self):  # Display to end user
        pass

dev_1 = Employee("Corey", "Schafer", 50000)
dev_2 = Employee("Test", "User", 60000)

print(dev_1.email)
print(dev_2.email)