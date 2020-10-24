# https://www.youtube.com/watch?v=BJ-VvGyQxho
# ##############################################
# # Part 1 
# # Class variables are shared with all instances of a class
# # Instance variables are unique to each instance of a class
# ##############################################
# class Employee:

#     def __init__(self, firstName, lastName, pay):
#         self.firstName = firstName  # Instance variable
#         self.lastName = lastName    # Instance variable
#         self.pay = pay              # Instance variable 
#         self.email = f"{firstName}.{lastName}@company.com" # Instance variable

#     def fullname(self): #instance is the first argument--self is the naming convention
#         return f"{self.firstName} {self.lastName}"  

#     def apply_raise(self):
#         self.pay = int(self.pay * 1.04)

# emp_1 = Employee("Corey", "Schafer", 50000)
# emp_2 = Employee("Test", "User", 60000)

# print( emp_1.pay )
# emp_1.apply_raise()
# print( emp_1.pay )

# ##############################################
# # Part 2
# # Use class variable
# ##############################################
# class Employee:

#     raise_amount = 1.04

#     def __init__(self, firstName, lastName, pay):
#         self.firstName = firstName  # Instance variable
#         self.lastName = lastName    # Instance variable
#         self.pay = pay              # Instance variable 
#         self.email = f"{firstName}.{lastName}@company.com" # Instance variable

#     def fullname(self): #instance is the first argument--self is the naming convention
#         return f"{self.firstName} {self.lastName}"  

#     def apply_raise(self):
#         self.pay = int(self.pay * Employee.raise_amount) # Need to reference Classname for global value or Instance of class for unique value

# emp_1 = Employee("Corey", "Schafer", 50000)
# emp_2 = Employee("Test", "User", 60000)

# print( emp_1.pay )
# emp_1.apply_raise()
# print( emp_1.pay )

# ##############################################
# # Part 3
# # Use instance variable
# ##############################################
# class Employee:

#     raise_amount = 1.04 # Class variable

#     def __init__(self, firstName, lastName, pay):
#         self.firstName = firstName  # Instance variable
#         self.lastName = lastName    # Instance variable
#         self.pay = pay              # Instance variable 
#         self.email = f"{firstName}.{lastName}@company.com" # Instance variable

#     def fullname(self): #instance is the first argument--self is the naming convention
#         return f"{self.firstName} {self.lastName}"  

#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount) # Need to reference Classname for global value or Instance of class for unique value

# emp_1 = Employee("Corey", "Schafer", 50000)
# emp_2 = Employee("Test", "User", 60000)

# print( emp_1.__dict__ ) # Display dictionary (JSON) representation of instance NOTE: No raise_amount
# print( Employee.__dict__ ) # Display dictionary (JSON) representation of class NOTE: methods and raise_amount

# print( Employee.raise_amount )
# print( emp_1.raise_amount) # Instance doesn't actually have raise_amount.  Using class raise_amount
# print( emp_2.raise_amount)

# ##############################################
# # Part 4
# # Use instance variable
# ##############################################
# class Employee:

#     raise_amount = 1.04 # Class variable

#     def __init__(self, firstName, lastName, pay):
#         self.firstName = firstName  # Instance variable
#         self.lastName = lastName    # Instance variable
#         self.pay = pay              # Instance variable 
#         self.email = f"{firstName}.{lastName}@company.com" # Instance variable

#     def fullname(self): #instance is the first argument--self is the naming convention
#         return f"{self.firstName} {self.lastName}"  

#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount) # Need to reference Classname for global value or Instance of class for unique value

# emp_1 = Employee("Corey", "Schafer", 50000)
# emp_2 = Employee("Test", "User", 60000)

# Employee.raise_amount = 1.05 # Change class variable

# print( Employee.raise_amount )
# print( emp_1.raise_amount) # Instance doesn't actually have raise_amount.  Using class raise_amount
# print( emp_2.raise_amount)

# ##############################################
# # Part 4
# # Change value of class variable for instance
# ##############################################
# class Employee:

#     raise_amount = 1.04 # Class variable

#     def __init__(self, firstName, lastName, pay):
#         self.firstName = firstName  # Instance variable
#         self.lastName = lastName    # Instance variable
#         self.pay = pay              # Instance variable 
#         self.email = f"{firstName}.{lastName}@company.com" # Instance variable

#     def fullname(self): #instance is the first argument--self is the naming convention
#         return f"{self.firstName} {self.lastName}"  

#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount) # Need to reference Classname for global value or Instance of class for unique value

# emp_1 = Employee("Corey", "Schafer", 50000)
# emp_2 = Employee("Test", "User", 60000)

# print( emp_1.__dict__ ) # Display dictionary (JSON) representation of instance NOTE: No raise_amount
# emp_1.raise_amount = 1.05 # Change class variable
# print( emp_1.__dict__ ) # Display dictionary (JSON) representation of instance NOTE: Now has raise_amount

# print( Employee.raise_amount )
# print( emp_1.raise_amount) # Instance now has raise_amount.  Python is using instance 
# print( emp_2.raise_amount)

##############################################
# Part 5
# Count Employees
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

print(Employee.num_of_emps)
emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Test", "User", 60000)
print(Employee.num_of_emps)