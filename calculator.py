


def calculate():
    num1 = int(input("Input 1: "))
    num2 = int(input("Input 2: "))

    operator = input("Choose operator: '+', '-', '*' or '/' : ")

    if operator == "+" :
        print("{} + {} = ".format(num1, num2))
        print(num1 + num2)

    elif operator == "-" :
        print("{} - {} = ".format(num1, num2))
        print(num1 - num2)

    elif operator == "*" :
        print("{} * {} = ".format(num1, num2))
        print(num1 * num2)

    elif operator == "/" :
        print("{} / {} = ".format(num1, num2))
        print(num1 / num2)

    else:
         print("Kakus")


    again()



def again():

    user_again = input("Do you want to calculate again ? \"Y\" for yes , \"N\" for no.")

    if user_again.upper() == "Y":
        calculate()

    elif user_again.upper() == "N":
        print("SEE YOU LATER!!!")

    else:
        again()



calculate()
