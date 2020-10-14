from os import system, name 

def clear():     
    if name == 'nt': # for windows 
        _ = system('cls')     
    else: # for mac and linux(here, os.name is 'posix') 
        _ = system('clear') 

def writeToTextFile(filepath, stringToWrite):
    with open(filepath, "a") as file:
        file.write(stringToWrite + "\n")

def readListFromTextFile(filepath):
    with open(filepath, "r") as file:
        return file.readlines()

def readFromTextFile(filepath):
    with open(filepath, "r") as file:
        return file.read()

def showMenu():    
    print("add - Add new Item")
    print("list - Show as list")
    print("file - Show entire file")
    print("exit - Exit App")    

def get_command():
    print("-------------------")
    command = input("Enter your command: ")
    return command.lower()

def main():
    FILE_NAME = "Assignment\\5a.txt"
    clear()

    while True:        
        showMenu()
        command = get_command()   
        print()     
        if command == "add":
            writeToTextFile( FILE_NAME, input("What would you like to add: "))
            clear()
        elif command == "list":
            list = readListFromTextFile(FILE_NAME)
            print("-------------------")
            for i in range(len(list)):
                print(str(i + 1) + ". " + list[i], end="")
            print("-------------------")
        elif command == "file":            
            print("-------------------")
            print(readFromTextFile(FILE_NAME))            
            print("-------------------")
        elif command == "exit":
            break
        else:
            print("Invalid command.")

        print()


if __name__ == "__main__":
    main()            