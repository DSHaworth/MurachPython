# https://www.youtube.com/watch?v=ZDa-Z5JzLYM
# ##############################################
# ## Part 1
# ##############################################
# class Employee:
#     pass

# emp_1 = Employee()
# emp_2 = Employee()

# print(emp_1)
# print(emp_2)

# emp_1.first = "Corey"
# emp_1.last = "Schafer"
# emp_1.email = "Corey.Schafer@company.com"
# emp_1.pay = 50000

# emp_2.first = "Test"
# emp_2.last = "User"
# emp_2.email = "Test.User@company.com"
# emp_2.pay = 60000

# ##############################################
# ## Part 2
# ##############################################
# class Employee:

#     def __init__(self, firstName, lastName, pay):
#         self.firstName = firstName
#         self.lastName = lastName
#         self.pay = pay
#         self.email = f"{firstName}.{lastName}@company.com"

# emp_1 = Employee("Corey", "Schafer", 50000)
# emp_2 = Employee("Test", "User", 60000)

# print(emp_1.email)
# print(emp_2.email)

# print(f"{emp_1.firstName} {emp_1.lastName}")

# ##############################################
# # Part 3
# ##############################################
# class Employee:

#     def __init__(self, firstName, lastName, pay):
#         self.firstName = firstName
#         self.lastName = lastName
#         self.pay = pay
#         self.email = f"{firstName}.{lastName}@company.com"

#     def fullname(self): #instance is the first argument--self is the naming convention
#         return f"{self.firstName} {self.lastName}"  

# emp_1 = Employee("Corey", "Schafer", 50000)
# emp_2 = Employee("Test", "User", 60000)

# print(emp_1.email)
# print(emp_2.email)

# print(f"{emp_1.fullname()}")
# print(f"{emp_2.fullname()}")

# ##############################################
# # Part 4 Demo: no self in instance method
# ##############################################
# class Employee:

#     def __init__(self, firstName, lastName, pay):
#         self.firstName = firstName
#         self.lastName = lastName
#         self.pay = pay
#         self.email = f"{firstName}.{lastName}@company.com"

#     def fullname(self): #instance is the first argument--self is the naming convention
#         return f"{self.firstName} {self.lastName}"  

#     def fullname_self_omitted(): #bad
#         return f"{self.firstName} {self.lastName}"

# emp_1 = Employee("Corey", "Schafer", 50000)
# emp_2 = Employee("Test", "User", 60000)

# print(emp_1.email)
# print(emp_2.email)

# print(f"{emp_1.fullname_self_omitted()}")

##############################################
# Part 5 Demo: Use Class Name
##############################################
class Employee:

    def __init__(self, firstName, lastName, pay):
        self.firstName = firstName
        self.lastName = lastName
        self.pay = pay
        self.email = f"{firstName}.{lastName}@company.com"

    def fullname(self): #instance is the first argument--self is the naming convention
        return f"{self.firstName} {self.lastName}"  

emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Test", "User", 60000)

print( emp_1.fullname() )
# Run using the classname
print( Employee.fullname(emp_1) ) # <- When running from the class, must include instance