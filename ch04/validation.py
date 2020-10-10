#!/usr/bin/env python3

def get_float(prompt, low, high):
    while True:
        result = float(input(prompt))
        if result > low and result <= high:
            return result
        else:
            print("Entry must be greater than", str(low), 
            "and less than or equal to", str(high))

def get_int(prompt, low, high):
    while True:
        result = int(input(prompt))
        if result > low and result <= high:
            return result
        else:
            print("Entry must be greater than", str(low),
            "and less than or equal to", str(high))

def main():
    choice = "y"
    while choice.lower() == "y":

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")
    
if __name__ == "__main__":
    main()
