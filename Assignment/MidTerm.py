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
    INFO = '\033[96m'
    PROMPT = '\033[92m'
    MENU =  '\033[93m'
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
    print(get_info("Inventory Program"))
    print(get_menu("1) Enter a product"))
    print(get_menu("2) Display all products"))
    print(get_menu("3) Quit"))
    print(msg)

def get_price(prompt):
    while True:
        try:
            number = float(input(prompt))
            if number > 0:
                return number
            else:
                print(get_warning("Price must be greater than 0."))
        except ValueError:
            print(get_warning("You entered an invalid number"))

def get_warning(text):
    return f"{bcolors.WARNING}{text}{bcolors.ENDC}"

def get_success(text):
    return f"{bcolors.SUCCESS}{text}{bcolors.ENDC}"

def get_info(text):
    return f"{bcolors.INFO}{text}{bcolors.ENDC}"

def get_prompt(text):
    return f"{bcolors.PROMPT}{text}{bcolors.ENDC}"

def get_menu(text):
    return f"{bcolors.MENU}{text}{bcolors.ENDC}"

def get_command(prompt, low, high):
    while True:
        try:
            number = int(input(get_prompt(prompt)))
            if number > low and number <= high:
                return number
            else:
                clear()                
                showMenu(get_warning(f"Entry must be greater than {str(low)}and less than or equal to {str(high)}."))
        except ValueError:
            clear()
            showMenu(get_warning("You entered an invalid number"))

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
            print(get_info("Enter a product"))
            try:
                product = []
                product.append(input(get_prompt("Name: ")))
                product.append(input(get_prompt("Code: ")))
                product.append(str(get_price(get_prompt("Price: "))))
                writeToTextFile(FILE_NAME, product)
                clear()
                showMenu(get_success("Record Added"))
            except KeyboardInterrupt:
                clear()
                showMenu(get_warning("Aborted adding record"))

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
                showMenu(get_success("List above"))

            except Exception as error:
                clear()
                showMenu(get_warning(error))

        elif command == QUIT:
            print("The program has ended")
            break
        else:
            print("Invalid command.  Should never get here.")

if __name__ == "__main__":
    main()            