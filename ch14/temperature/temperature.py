class Temp:
    def __init__(self):
        self.__celsius = 0
        self.__fahrenheit = 32

    def setFahrenheit(self, temp):
        self.__fahrenheit = temp
        self.__celsius = (self.__fahrenheit - 32) * 5/9

    def setCelsius(self, temp):
        self.__celsius = temp
        self.__fahrenheit = self.__celsius * 9/5 + 32

    def getFahrenheit(self):
        return self.__fahrenheit

    def getCelsius(self):        
        return self.__celsius


# the main function is used to test the other functions
# this code isn't run if this module isn't the main module
def main():
    temp = Temp()
    for f in [32, 212]:
        temp.setFahrenheit(f)
        print(f, "Fahrenheit equals", round(temp.getCelsius(), 2),
              "Celsius")
    
    for c in [0, 100]:
        temp.setCelsius(c)
        print(c, "Celsius equals", round(temp.getFahrenheit(), 2),
              "Fahrenheit")

# if this module is the main module, call the main function
# to test the other functions
if __name__ == "__main__":
    main()

