#!/usr/bin/env python3

from datetime import datetime, time

def main():
    print("The Timer program")
    print()

    # start timer
    input("Press Enter to start...")
    start_time = datetime.now()
    print("Start time:", start_time.strftime("%X"))
    print()
    
    # stop timer
    input("Press Enter to stop...")    
    stop_time = datetime.now()
    print("Stop time: ", stop_time.strftime("%X"))
    print()

    # calculate elapsed time
    elapsed_time = stop_time - start_time
    days = elapsed_time.days
    minutes = elapsed_time.seconds // 60
    seconds = elapsed_time.seconds % 60
    microseconds = elapsed_time.microseconds
    hours = minutes // 60
    minutes = minutes % 60

    # create time object
    time_object = time(hours, minutes, seconds, microseconds)

    # display results
    print("ELAPSED TIME")
    if days > 0:
        print("Days:", days)

    if hours > 0 or minutes > 0:
        print("Hours/minutes: " + time_object.strftime("%H:%M"))
    print("Seconds: " + time_object.strftime("%S.%f"))
    
    #if hours > 0 or minutes > 0:
    #     print("Hours:Minutes:", time(hours, minutes))
    # print("Seconds: ", time(second=seconds, microsecond=microseconds))
    #print("Time:", time_object)
    print 

if __name__ == "__main__":
    main()
