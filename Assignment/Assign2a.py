def main():
    print("Welcome to a simple calculating program")
    choice = int(input("Enter 1) to add, 2) to subtract, 3) to multiply, or 4) to divide: "))
    value1 = float(input("Enter your fist value: "))
    value2 = float(input("Enter your second value: "))

    result = 0
    if choice == 1:
        result = value1 + value2
    elif choice == 2:
        result == value1 - value2
    elif choice == 3:
        result == value1 * value2
    elif choice == 4:
        result == value1 / value2
    
    print("Result: " + str(result))

main()