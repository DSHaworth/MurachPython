# Duane Haworth

def append(str1, str2):
    print(str1 + str2)

def positiveNumber(number):
    if number < 0:
        return 0
    else:
        return number

def evenOdd(number):
    return (number % 2) == 0

def inCenturyRange(number):
    return number >= 0 and number <= 100

def repeater(str_to_repeat = "Default String ", num_times = 5):
    #print(str_to_repeat * num_times)
    for i in range(num_times):
        print(str_to_repeat, end="")
    print()

def main():

    append("Duane ", "Haworth")

    print("positiveNumber(-5)", positiveNumber(-5))
    print("positiveNumber(5)", positiveNumber(5))

    print("evenOdd(3)", evenOdd(3))
    print("evenOdd(2)", evenOdd(2))

    print("inCenturyRange(101)", inCenturyRange(101))
    print("inCenturyRange(40)", inCenturyRange(40))

    repeater("Annoy Me ", 2)
    repeater()

if __name__ == "__main__":
    main()