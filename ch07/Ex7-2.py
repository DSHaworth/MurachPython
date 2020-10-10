#!/usr/bin/env python3
import csv

FILENAME = "ch07\\trips.csv"

def get_miles_driven():
    while True:
        miles_driven = float(input("Enter miles driven :     "))                    
        if miles_driven > 0:       
            return miles_driven
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue
    
def get_gallons_used():
    while True:
        gallons_used = float(input("Enter gallons of gas:     "))                    
        if gallons_used > 0:       
            return gallons_used
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue
        
def save_list(trip_list):
    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(trip_list)

def read_list():
    trip_list = []
    with open(FILENAME, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            trip_list.append(row)
    return trip_list        

def list_trips(trip_list):
    print("Distance\tGallons\t\tMPG")
    for trip in trip_list:
        print(trip[0] + "\t\t" + trip[1] + "\t\t" + trip[2])

def main():    

    trip_list = []
    # display a welcome message
    print("The Miles Per Gallon application")
    print()    

    current_list = read_list()
    list_trips(current_list)

    more = "y"
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()
        mpg = round((miles_driven / gallons_used), 2)

        trip = []
        trip.append(miles_driven)
        trip.append(gallons_used)
        trip.append(mpg)
        trip_list.append(trip)

        print("Miles Per Gallon:\t" + str(mpg))
        print()
        
        more = input("More entries? (y or n): ")
    
    save_list(trip_list)
    print("Bye")

if __name__ == "__main__":
    main()

