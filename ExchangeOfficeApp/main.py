def application():
    print("Welcome to the exchange office")
    print("1. Exchange your money")
    print("2. Exit")
    option = input()
    if option == "1":
        Exchange()
    elif option == "2":
        exit()
    

def Exchange():
    print("Insert your value: ")
    value = float(input())
    print("What is your value: ")
    print("1. EUR")
    print("2. DOLLAR")
    print("3. SRB_DINAR")
    option2 = input()
    if option2 == "1":
        calculatorDinnar = value *117
        print("Your value: ", str(value), " is exact....", str(calculatorDinnar), "SRB_DIN")
        calculatorDollar = value * 0.125
        print("Your value: ", str(value), " is exact....", str(calculatorDollar), "USD")
    elif option2 =="2": 
        calculatorDinarDollar = value * 104
        print("Your value: ", str(value), " is exact....", str(calculatorDinarDollar), "SRB_DIN")
        calcultaroDollarEur = value * 0.9
        print("Your value: ", str(value), " is exact....", str(calcultaroDollarEur), "EUR")
    elif option2 == "3":
        calculatorEURDIN = value/117
        print("Your value: ", str(value), " is exact....", str(calculatorEURDIN), "EUR")
        calculatorDOLDIN = value/104
        print("Your value: ", str(value), " is exact....", str(calculatorDOLDIN), "USD")



        
    

application()
