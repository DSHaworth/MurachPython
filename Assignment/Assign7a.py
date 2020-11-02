import pickle

def getProductCode():
    productCode = input("Enter a product code (four capital letters): ").strip()
    while True:
        if len(productCode) ==  4 and productCode.isalpha() and productCode.isupper():
            return productCode
        else:
            productCode = input("That was not a correct product code, please try again: ")

def getProductNumber():
    productNumber = input("Enter a product number (a number with a leading 0): ").strip()
    while True:        
        if productNumber[0] ==  "0" and productNumber.isnumeric():
            return productNumber
        else:
            productNumber = input("That was not a correct product number, please try again: ")

def writeToPickle(filepath, products):
    with open(filepath, "wb") as file:
        pickle.dump(products, file)
        print("File Saved")

def readFromPickle(filepath):
    with open(filepath, "rb") as file:
        return pickle.load(file)

def getContinue(prompt):
    response = input(prompt).strip()
    if response == "y":
        return True
    return False

def loop():
    keepGoing = True
    products = {}

    while keepGoing:

        productCode = getProductCode()
        productNumber = getProductNumber()
        # Add product to products 
        products[productCode] = productNumber
        print(f"Added {productCode}:{productNumber} to Products dictionary")
        print()
        keepGoing = getContinue("Do you wish to continue? Enter y/n: ")

    print()
    filename = input("Please enter a file name: ")    
    filepath = f"Assignment\{filename}"    
    writeToPickle(filepath, products)

    print(f"Read from {filename}")
    print(readFromPickle(filepath))

def main():
    loop()

main()