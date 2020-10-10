#!/usr/bin/env python3

# display a welcome message
print("Welcome to the Future Value Calculator")
print()

choice = "y"
while choice.lower() == "y":

    # get input from the user
    isValid = False
    while isValid == False:
        monthly_investment = float(input("Enter monthly investment:\t"))
        if monthly_investment > 0:
            isValid = True
        else:
            print("Entry must be greater than 0. Please try again")

    isValid = False
    while isValidisValid == False:
        yearly_interest_rate = float(input("Enter yearly interest rate:\t"))
        if yearly_interest_rate > 0 and yearly_interest_rate <= 15:
            isValid = True
        else:
            print("Entry must be greater than 0 and less than or equal to 15. Please try again.") 
    
    isValid = False
    while isValid == False:
        years = int(input("Enter number of years:\t\t"))
        if years > 0 and years <= 50:
            isValid = True
        else:
            print("Entry must be greater than 0 and less than or equal to 50. Please try again")

    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest_rate / 12 / 100
    months = years * 12

    # calculate the future value
    future_value = 0
    for i in range(months):
        future_value += monthly_investment
        monthly_interest_amount = future_value * monthly_interest_rate
        future_value += monthly_interest_amount
        print("Year = " + str(i) + " Future Value = " + str(round(future_value, 2)))

    # see if the user wants to continue
    print()
    choice = input("Continue (y/n)? ")

print("Bye!")