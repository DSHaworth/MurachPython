# https://www.youtube.com/watch?v=zdJEYhA2AZQ

#################
# Tabs vs Spaces
# [VS CODE] File -> Preferences -> Settings
# If there were a difference between spaces and tabs, could cause problems
#################
nums = [11, 30, 44, 54]

for num in nums:
    square = num ** 2
    print(square)


#########################################################
# Don't save modules with same name as standard library
#########################################################

####################
# Default Arguments
####################
def add_employee(emp, emp_list=[]):
    emp_list.append(emp)
    print(emp_list)

emps = ["john", "Jane"]

#add_employee("Corey", emps) #<- Demo
add_employee("Duane")
add_employee("Carmen")

# emp_list will create emp_list once, and then it will always exist.

# Alternate
def add_employee1(emp, emp_list=None):
    if emp_list is None:
        emp_list = []
    emp_list.append(emp)
    print(emp_list)

#add_employee("Corey", emps)
add_employee1("Duane")
add_employee1("Carmen")

