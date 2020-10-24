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
# Context Management
####################
#with open("test.txt", "r") as f:
#    file_contents = f.read()

####################
# LIST STUFF
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
print("Unpacking")
names=["Peter Parker", "Clark Kent", "Wade Wilson", "Bruce Wayne"]
heroes=["Spiderman", "Superman", "Deadpool", "Batman"]

for name, hero in zip(names, heroes):
    print(f"{name} is actually {hero}")