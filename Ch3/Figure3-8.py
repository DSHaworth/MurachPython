# display a welcome message
print("The Miles Per Gallon program")
print()

# get input from the user
milesDriven = float(input("Enter miles driven:         "))
gallonsUsed = float(input("Enter gallons of gas used:  "))
    
if milesDriven <= 0:
    print("Miles driven must be greater than zero. Please try again.")
elif gallonsUsed <= 0:
    print("Gallons used must be greater than zero. Please try again.")
else:
    mpg = round((milesDriven / gallonsUsed), 2)
    print("Miles Per Gallon:          ", mpg)

print()
print("Bye")


