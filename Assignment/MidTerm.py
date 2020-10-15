from os import system, name 

def clear():     
    if name == 'nt': # for windows 
        _ = system('cls')     
    else: # for mac and linux(here, os.name is 'posix') 
        _ = system('clear') 

# https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-python
# https://en.wikipedia.org/wiki/ANSI_escape_code#SGR_.28Select_Graphic_Rendition.29_parameters
class bcolors:
    WARNING = '\033[31m'
    SUCCESS = '\033[92m'
    ENDC = '\033[0m'

def writeToTextFile(filepath, product_details):
    with open(filepath, "a") as file:
        file.write(",".join(product_details) + "\n")

def readListFromTextFile(filepath):
    try:
        with open(filepath, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        raise Exception("Could not find " + filepath + " file.")

def showMenu(msg = ""):
    print("Inventory Program")
    print("1) Enter a product")
    print("2) Display all products")
    print("3) Quit")
    print(msg)

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
                showMenu(f"{bcolors.WARNING}Entry must be greater than {str(low)}and less than or equal to {str(high)}.{bcolors.ENDC}")
        except ValueError:
            clear()
            showMenu(f"{bcolors.WARNING}You entered an invalid number{bcolors.ENDC}")

def main():
    ENTER_PRODUCT = 1
    DISPLAY_PRODUCTS = 2
    QUIT = 3

    FILE_NAME = "Assignment\\mid-term-products.txt"
    clear()

    showMenu()
    while True:                
        command = get_command("Select a menu option: ", 0, 3)   
        print()     
        if command == ENTER_PRODUCT:
            clear()
            print("Enter a product")
            try:
                product = []
                product.append(input("Name: "))
                product.append(input("Code: "))
                product.append(str(get_price("Price: ")))
                writeToTextFile(FILE_NAME, product)
                clear()
                showMenu(f"{bcolors.SUCCESS}Record Added{bcolors.ENDC}")
            except KeyboardInterrupt:
                clear()
                showMenu(f"{bcolors.WARNING}Aborted adding record{bcolors.ENDC}")

        elif command == DISPLAY_PRODUCTS:

            try:
                list = readListFromTextFile(FILE_NAME)
                clear()
                print("Products on file")
                print("-------------------")
                for i in range(len(list)):
                    print(str(i + 1) + ". " + list[i], end="")
                print("-------------------")
                print()
                showMenu(f"{bcolors.SUCCESS}List above{bcolors.ENDC}")

            except Exception as e:
                clear()
                showMenu(f"{bcolors.WARNING}{e}{bcolors.ENDC}")

        elif command == QUIT:
            print("The program has ended")
            break
        else:
            print("Invalid command.  Should never get here.")

if __name__ == "__main__":
    main()            