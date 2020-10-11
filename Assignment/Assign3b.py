def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1/num2

def main():
    print("Welcome to a simple calculating program")
    choice = int(input("Enter 1) to add, 2) to subtract, 3) to multiply, or 4) to divide: "))
    value1 = float(input("Enter your fist value: "))
    value2 = float(input("Enter your second value: "))

    result = 0
    if choice == 1:
        result = add(value1, value2)
    elif choice == 2:
        result = subtract(value1, value2)
    elif choice == 3:
        result = multiply(value1, value2)
    elif choice == 4:
        result = divide(value1, value2)
    
    print("Result: " + str(result))

main()