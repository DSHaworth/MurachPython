def main():
    REG_HOURS = 40
    OT_PAY_RATE = 1.5
    run_again = "yes"
    while run_again.lower() == "yes":

        payRate = float(input("Enter employee's pay-rate: "))
        hours = float(input("Enter hours worked this week: "))

        if hours > REG_HOURS:            
            total_pay = (REG_HOURS * payRate) + ((hours - REG_HOURS) * (payRate * OT_PAY_RATE))
        else:
            total_pay = payRate * hours

        print("Employee's weekly pay: " + str(total_pay))

        run_again = input("Do you wish to continue(yes/no) ")

main()