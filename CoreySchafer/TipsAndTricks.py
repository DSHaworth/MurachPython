##################
# Ternary Operator
##################
print("Ternary Operator")
condition = True
if(condition):
    x = 1
else:
    x = 0
#or
y = 1 if condition else 0

print(x)
print(y)

##################
# Readable Numbers
##################
print()
print("Making Numbers Readable")
num1 = 10000000
num2 = 100000
#or
num1 = 10_000_000_000
num2 = 100_000_000

total = num1 + num2
print(total)
print(f"{total:,}")

####################
# Context Managers
####################
#with open("test.txt", "r") as f:
#    file_contents = f.read()

####################
# Enumerate and Zip
####################
print()
print("List Stuff")
names = ["Duane", "Carmen", "Jessica", "Morgan", "Claire", "Lauren"]
print("Beginner way")
index = 0
for name in names:
    print(index, name)
    index += 1
print()
print("enumerate")
for index, name in enumerate(names, start=1):
    print(index, name)

print()
print("zip 1")
names=["Peter Parker", "Clark Kent", "Wade Wilson", "Bruce Wayne"]
heroes=["Spiderman", "Superman", "Deadpool", "Batman"]

for name, hero in zip(names, heroes):
    print(f"{name} is actually {hero}")

print()
print("zip 2")
names=["Peter Parker", "Clark Kent", "Wade Wilson", "Bruce Wayne"]
heroes=["Spiderman", "Superman", "Deadpool", "Batman"]
universes=["Marvel", "DC", "Marvel", "DC"]

for name, hero, universe in zip(names, heroes, universes):
    print(f"{name} is actually {hero} from {universe}")

print()
print("unpacking 1")
a, b = (1, 2)
print(a)  #1
print(b)  #2

print()
print("unpacking 2: Ignoring a variable you won't be using")
a, _ = (1, 2)
print(a)  #1
#print(b)  #2

# print()
# print("unpacking 2: More variables than values")
# a, b, c = (1, 2)
# print(a)  #1
# #print(b)  #2

print()
print("unpacking 2: More values than variables")
a, b, *c = (1, 2, 3, 4, 5)
print(a)  #1
print(b)  #2
print(c)  # [3, 4, 5]

print()
print("unpacking 2: More values than variables")
a, b, *c, d = (1, 2, 3, 4, 5)
print(a)  #1
print(b)  #2
print(c)  #[3, 4]
print(d)  #5

print()
print("Classes")
print("Use variables as property names")

class Person():
    pass

person = Person()

first_key = "first"
first_val = "Corey"

setattr(person, first_key, first_val)

first = getattr(person, first_key)
# print(person.first) # ide says no "first" member, but there is. :-)
print(first)

print()
print("Creating dynamic properties")
person_info = {"firstName": "Corey", "lastName": "Schafer"}
for key, value in person_info.items():
    setattr(person, key, value)

print(person.firstName)
print(person.lastName)

for key in person_info.keys():
    print(getattr(person, key))

#######################
# Inputing secret info
#######################
print()
print("Inputing secret information")

username = input("Username: ")
password = input("Password: ")
print("Logging In...")

from getpass import getpass
username = input("Username: ")
password = getpass("Password: ")
print("Logging In...")

#######################
# Virtual Environment
#######################
#> python
#>>> import smtpd
#>>> help(smtpd)   <- display help file on module