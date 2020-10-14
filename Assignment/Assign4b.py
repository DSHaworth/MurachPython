def main():
    name_list = []
    spent_list = []

    ITEM_MAX = 3

    for i in range(ITEM_MAX):
        name_list.append(input("Enter customer name: "))
        spent_list.append(float(input("Enter purchased amount: ")))

    total = 0
    print()
    print("Name            Spent")
    for i in range(ITEM_MAX):
        print(name_list[i] + "\t\t" + str(spent_list[i]))
        total += spent_list[i]

    print()
    print("Total Spent: " + str(total))
    print("Average Spent: " + str(round(total/ITEM_MAX, 2)))
    print("Highest Spent: " + str(max(spent_list)))
    print("Lowest Spent: " + str(min(spent_list)))

if __name__ == "__main__":
    main()    