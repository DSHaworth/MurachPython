def main():    
    size = int(input("Hello, please enter an integer value the size of your list: "))    
    star_list = []
    for i in range(size):        
        val = int(input("Please enter a value between 1 and 10 (inclusive): "))
        if val > 10:
            val = 10
        elif val <= 0:
            val = 1
        star_list.append(val)

    print()
    print("Printing your entries as a chart:")
    for item in range(size):
        # for star_count in range(star_list[item]):
        #     print("*", end="")
        print("*" * star_list[item])

if __name__ == "__main__":
    main()    