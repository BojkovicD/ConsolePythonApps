def application():
    print("1. Calculate your salary")
    print("2. Exit")
    choice = input()
    if choice == "1":
        SalaryCalc()
    elif choice == "2":
        exit()
    else:
        print("Bad input...try again.")
        application()

def SalaryCalc():
    print("1. Yearly Average Salary")
    print("2. Half Year Average Salary")
    print("3. Back")
    choice1 = input()
    if choice1  == "1":
        YearSalary()
    elif choice1 == "2":
        HalfYearSalary()
    elif choice1 =="3":
        application()



def YearSalary():
    value1 = float(input("Month 1: "))
    value2 = float(input("Month 2: "))
    value3 = float(input("Month 3: "))
    value4 = float(input("Month 4: "))
    value5 = float(input("Month 5: "))
    value6 = float(input("Month 6: "))
    value7 = float(input("Month 7: "))
    value8 = float(input("Month 8: "))
    value9 = float(input("Month 9: "))
    value10 = float(input("Month 10: "))
    value11 = float(input("Month 11: "))
    value12 = float(input("Month 12: "))


    calculatorYear = (value1+value2+value3+value4+value5+value6+value7+value8+value9+value10+value11+value12)/12
    print("Your average salary for this year is: ", str(calculatorYear))

def HalfYearSalary():
    value1 = float(input("Month 1: "))
    value2 = float(input("Month 2: "))
    value3 = float(input("Month 3: "))
    value4 = float(input("Month 4: "))
    value5 = float(input("Month 5: "))
    value6 = float(input("Month 6: "))
    calculatorHalfYear = (value1+value2+value3+value4+value5+value6)/6
    print("Your average salary for this half of the year is: ", str(calculatorHalfYear))
    
application()
