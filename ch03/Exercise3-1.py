# display a welcome message
print("The Miles Per Gallon program")
print()

anotherTrip = "y"
while anotherTrip == "y": # Using a while loop statement to allow the user to make multiple(repeat) entries and get the miles per gallon for more than one trip.

    # get input from the user
    milesDriven = float(input("Enter miles driven:         "))
    gallonsUsed = float(input("Enter gallons of gas used:  "))
    costPerGallon = float(input("Enter cost per gallon:      "))
        
    if milesDriven <= 0:
        print("Miles driven must be greater than zero. Please try again.")
    elif gallonsUsed <= 0:
        print("Gallons used must be greater than zero. Please try again.")
    elif costPerGallon <= 0:
        print("Cost per gallon must be greater than zero. Please try again.")
    else:
        print() # Prints a blank line between Enter cost per gallon and Miles Per Gallon statement entries
            
        # calculate and display miles per gallon
        mpg = round((milesDriven / gallonsUsed), 2)
        # calculate and display total gas cost
        totalGasCost = round((gallonsUsed * costPerGallon), 1)
        # calculate and display cost per mile
        costPerMile = round(totalGasCost / milesDriven, 1)
        print("Miles Per Gallon:          ", mpg)
        print("Total Gas Cost:            ", totalGasCost)
        print("Cost Per Mile:             ", costPerMile)
        print() # Prints a blank line between Cost Per Mile and Enter miles driven statement entries

    anotherTrip = input("Get entries for another trip (y/n?) ") # Allows user to repeat entries using while loop
    print() # Prints a blank line between "Get entries for another trip?" and "Enter miles driven" statements

print()
print("Bye")