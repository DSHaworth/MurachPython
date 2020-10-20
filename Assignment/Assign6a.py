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
    try:
        with open(filepath, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        raise Exception("Could not find " + filepath + " file.")
    except OSError as err:
        raise Exception(f"OS Error: {err.Error}")

def readFromTextFile(filepath):
    try:
        with open(filepath, "r") as file:
            return file.read()
    except FileNotFoundError:
        raise Exception("Could not find " + filepath + " file.")
    except OSError as err:
        raise Exception(f"OS Error: {err.Error}")

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
    FILE_NAME = "Assignment\\6a.txt"
    clear()

    while True:        
        showMenu()
        command = get_command()   
        print()
        if command == "add":
            writeToTextFile( FILE_NAME, input("What would you like to add: "))
            clear()
        elif command == "list":
            try:
                list = readListFromTextFile(FILE_NAME)
                print("-------------------")
                for i in range(len(list)):
                    print(str(i + 1) + ". " + list[i], end="")
                print("-------------------")
            except Exception as e:
                print(e)
        elif command == "file":            
            try:
                print("-------------------")
                print(readFromTextFile(FILE_NAME))            
                print("-------------------")
            except Exception as e:
                print(e)
        elif command == "exit":
            break
        else:
            print("Invalid command.")

        print()


if __name__ == "__main__":
    main()            