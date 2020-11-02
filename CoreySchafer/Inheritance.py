# https://www.youtube.com/watch?v=RSl87lqOXDE
# ##############################################
# # Part 1 Setup
# ##############################################
# class Employee:

#     raise_amount = 1.04 

#     def __init__(self, firstName, lastName, pay):
#         self.firstName = firstName
#         self.lastName = lastName
#         self.pay = pay
#         self.email = f"{firstName}.{lastName}@company.com"

#     def fullname(self):
#         return f"{self.firstName} {self.lastName}"  

#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount)

# dev_1 = Employee("Corey", "Schafer", 50000)
# dev_2 = Employee("Test", "User", 60000)

# print(dev_1.email)
# print(dev_2.email)

# # ##############################################
# # # Part 2 Inheritance
# # ##############################################
# class Employee:

#     raise_amount = 1.04 

#     def __init__(self, firstName, lastName, pay):
#         self.firstName = firstName
#         self.lastName = lastName
#         self.pay = pay
#         self.email = f"{firstName}.{lastName}@company.com"

#     def fullname(self):
#         return f"{self.firstName} {self.lastName}"  

#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount)

# class Developer(Employee): # Pytyon moved up "chain" to find __init__
#     pass

# dev_1 = Developer("Corey", "Schafer", 50000)
# dev_2 = Developer("Test", "User", 60000)

# print(dev_1.email)
# print(dev_2.email)

# print(help(Developer)) # Pyhton's Mehod Resolution Order Developer -> Employee


# # ##############################################
# # # Part 3 Customize Sub Class
# # ##############################################
# class Employee:

#     raise_amount = 1.04 

#     def __init__(self, firstName, lastName, pay):
#         self.firstName = firstName
#         self.lastName = lastName
#         self.pay = pay
#         self.email = f"{firstName}.{lastName}@company.com"

#     def fullname(self):
#         return f"{self.firstName} {self.lastName}"  

#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount)

# class Developer(Employee): # Pytyon moved up "chain" to find __init__
#     raise_amount = 1.10
#     #pass 

# dev_1 = Developer("Corey", "Schafer", 50000)
# dev_2 = Developer("Test", "User", 60000)

# print(dev_1.email)
# print(dev_2.email)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

# # ##############################################
# # # Part 4 Add addition parameters
# # ##############################################
# class Employee:

#     raise_amount = 1.04 

#     def __init__(self, firstName, lastName, pay):
#         self.firstName = firstName
#         self.lastName = lastName
#         self.pay = pay
#         self.email = f"{firstName}.{lastName}@company.com"

#     def fullname(self):
#         return f"{self.firstName} {self.lastName}"  

#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount)

# class Developer(Employee): # Pytyon moved up "chain" to find __init__
#     raise_amount = 1.10
    
#     def __init__(self, firstName, lastName, pay, prog_lang):
#         super().__init__(firstName, lastName, pay)
#         self.prog_lang = prog_lang

# dev_1 = Developer("Corey", "Schafer", 50000, "Python")
# dev_2 = Developer("Test", "User", 60000, "C#")

# print(dev_1.email, dev_1.prog_lang)
# print(dev_2.email, dev_2.prog_lang)

# # ##############################################
# # # Part 5 Add another Sub-Class
# # ##############################################
# class Employee:

#     raise_amount = 1.04 

#     def __init__(self, firstName, lastName, pay):
#         self.firstName = firstName
#         self.lastName = lastName
#         self.pay = pay
#         self.email = f"{firstName}.{lastName}@company.com"

#     def fullname(self):
#         return f"{self.firstName} {self.lastName}"  

#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount)

# class Developer(Employee): # Pytyon moved up "chain" to find __init__
#     raise_amount = 1.10
    
#     def __init__(self, firstName, lastName, pay, prog_lang):
#         super().__init__(firstName, lastName, pay)
#         self.prog_lang = prog_lang

# class Manager(Employee):

#     def __init__(self, firstName, lastName, pay, employees=None): # Reminder, don't send mutable datatypes (list/dictionary) as default argurments
#         super().__init__(firstName, lastName, pay)
#         self.employees = [] if employees is None else employees

#     def add_emp(self, emp):
#         if emp not in self.employees:
#             self.employees.append(emp)

#     def remove_emp(self, emp):
#         if emp in self.employees:
#             self.employees.remove(emp)

#     def print_emps(self):
#         for emp in self.employees:
#             print(f"--> {emp.fullname()}")

# dev_1 = Developer("Corey", "Schafer", 50000, "Python")
# dev_2 = Developer("Test", "User", 60000, "C#")

# mgr_1 = Manager("Duane", "Haworth", 90000, [dev_1])
# print(mgr_1.email)
# mgr_1.print_emps()
# print(f"Add {dev_2.fullname()}")
# mgr_1.add_emp(dev_2)
# mgr_1.print_emps()
# #Remove Employee
# print(f"Remove {dev_1.fullname()}")
# mgr_1.remove_emp(dev_1)
# mgr_1.print_emps()

# ##############################################
# # Part 6 IsInstance / IsSubClass
# ##############################################
class Employee:

    raise_amount = 1.04 

    def __init__(self, firstName, lastName, pay):
        self.firstName = firstName
        self.lastName = lastName
        self.pay = pay
        self.email = f"{firstName}.{lastName}@company.com"

    def fullname(self):
        return f"{self.firstName} {self.lastName}"  

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

class Developer(Employee): # Pytyon moved up "chain" to find __init__
    raise_amount = 1.10
    
    def __init__(self, firstName, lastName, pay, prog_lang):
        super().__init__(firstName, lastName, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, firstName, lastName, pay, employees=None): # Reminder, don't send mutable datatypes (list/dictionary) as default argurments
        super().__init__(firstName, lastName, pay)
        self.employees = [] if employees is None else employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print(f"--> {emp.fullname()}")

dev_1 = Developer("Corey", "Schafer", 50000, "Python")
dev_2 = Developer("Test", "User", 60000, "C#")

mgr_1 = Manager("Duane", "Haworth", 90000, [dev_1])

print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))

print(issubclass(Developer, Employee))
print(issubclass(Manager, Employee))

print(issubclass(Manager, Developer))