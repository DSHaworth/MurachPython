# Display a title
print("The Miles Per Gallon program")
print()

# Get input from the user
milesDriven = float(input("Enter miles driven: \t"))
gallonsUsed = float(input("Enter gallons used: \t"))
costPerGallon = float(input("Cost per gallon: \t"))

# Calculate and round miles per gallon
mpg = milesDriven / gallonsUsed
mpg = round(mpg, 2)

# Calculate total cost per gallon
totalGasCost = costPerGallon * gallonsUsed

# Calulate Cost Per Mile
costPerMile = round(totalGasCost / milesDriven, 2)

# Display the result
print()
print("Miles per Gallon:\t" + str(mpg))
print("  Total Gas Cost:\t" + str(totalGasCost))
print("   Cost per mile:\t" + str(costPerMile))
print()
print("Bye")