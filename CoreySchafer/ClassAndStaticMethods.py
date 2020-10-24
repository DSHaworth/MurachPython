# # https://www.youtube.com/watch?v=rq8cL2XMM5M&t
# ##############################################
# # Part 1 Class Methods and Static Methods
# ##############################################
# class Employee:

#     num_of_emps = 0
#     raise_amount = 1.04 # Class variable    

#     def __init__(self, firstName, lastName, pay):
#         self.firstName = firstName  # Instance variable
#         self.lastName = lastName    # Instance variable
#         self.pay = pay              # Instance variable 
#         self.email = f"{firstName}.{lastName}@company.com" # Instance variable

#         Employee.num_of_emps += 1 #Always use class vairable

#     def fullname(self): #instance is the first argument--self is the naming convention
#         return f"{self.firstName} {self.lastName}"  

#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount) # Need to reference Classname for global value or Instance of class for unique value

#     @classmethod # Decorator for class instead of instance
#     def set_raise_amt(cls, amount): #can't use the word class, because it's a reserved word. Class is default value, much like Self is default instance
#         cls.raise_amount = amount

#     @classmethod
#     def from_string(cls, emp_str):
#         first, last, pay = emp_str.split("-")
#         return cls(first, last, pay)

# emp_1 = Employee("Corey", "Schafer", 50000)
# emp_2 = Employee("Test", "User", 60000)
# emp_3 = Employee.from_string("John-Doe-70000")

# print(emp_3.email)
# print(emp_3.pay)

##############################################
# Part 1 Static Methods
##############################################
class Employee:

    num_of_emps = 0
    raise_amount = 1.04 # Class variable    

    def __init__(self, firstName, lastName, pay):
        self.firstName = firstName  # Instance variable
        self.lastName = lastName    # Instance variable
        self.pay = pay              # Instance variable 
        self.email = f"{firstName}.{lastName}@company.com" # Instance variable

        Employee.num_of_emps += 1 #Always use class vairable

    def fullname(self): #instance is the first argument--self is the naming convention
        return f"{self.firstName} {self.lastName}"  

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) # Need to reference Classname for global value or Instance of class for unique value

    @classmethod # Decorator for class instead of instance
    def set_raise_amt(cls, amount): #can't use the word class, because it's a reserved word. Class is default value, much like Self is default instance
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod # don't use anything from class or instance variables
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Test", "User", 60000)

import datetime

my_date = datetime.date(2020, 10, 24) # saturday
print(Employee.is_workday(datetime.date(2020, 10, 23))) #Friday
print(Employee.is_workday(datetime.date(2020, 10, 24))) #Saturday


