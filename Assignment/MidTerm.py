from os import system, name 

def clear():     
    if name == 'nt': # for windows 
        _ = system('cls')     
    else: # for mac and linux(here, os.name is 'posix') 
        _ = system('clear') 

def writeToTextFile(filepath, product_details):
    with open(filepath, "a") as file:
        file.write(",".join(product_details) + "\n")

def readListFromTextFile(filepath):
    try:
        with open(filepath, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        raise Exception("Could not find " + filepath + " file.")

def showMenu():
    print("Inventory Program")
    print("1) Enter a product")
    print("2) Display all products")
    print("3) Quit")

def get_price(prompt):
    while True:
        try:
            number = float(input(prompt))
            if number > 0:
                return number
            else:
                print("Price must be greater than 0.")
        except ValueError:
            clear()
            showMenu()
            print("You entered an invalid number")    

def get_command(prompt, low, high):
    while True:
        try:
            number = int(input(prompt))
            if number > low and number <= high:
                return number
            else:
                clear()
                showMenu()
                print("Entry must be greater than " + str(low) 
                    + " and less than or equal to " + str(high) + ".")
        except ValueError:
            clear()
            showMenu()
            print("You entered an invalid number")        

def main():
    FILE_NAME = "Assignment\\mid-term-products.txt"
    clear()

    while True:        
        showMenu()
        print()
        command = get_command("Select a menu option: ", 0, 3)   
        print()     
        if command == 1:

            print("Enter a product")
            product = []
            product.append(input("Name: "))
            product.append(input("Code: "))
            product.append(str(get_price("Price: ")))
            writeToTextFile(FILE_NAME, product)
            clear()

        elif command == 2:

            try:
                list = readListFromTextFile(FILE_NAME)
                print("Products on file")
                print("-------------------")
                for i in range(len(list)):
                    print(str(i + 1) + ". " + list[i], end="")
                print("-------------------")

            except Exception as e:
                clear()
                print(e)

        # elif command == 2:
        #     try:
        #         print(readFromTextFile(FILE_NAME))            
        #     except Exception as e:
        #         clear()
        #         print(e)

        elif command == 3:
            print("The program has ended")
            break
        else:
            print("Invalid command.")

        print()

if __name__ == "__main__":
    main()            