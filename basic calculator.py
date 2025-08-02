while True:
    #Asking for user inputs
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the next number: "))
    sign = input("Enter the sign: ")

    #Using if/else statements to perform the operations
    if sign == '+':
        result = num1 + num2
        print(result)
    elif sign == '-':
        result = num1 - num2
        print(result)
    elif sign == '*':
        result = num1 * num2
        print(result)
    elif sign == '/':
        if num2 != 0:
            result = num1 / num2
            print(result)
        else: print("Sorry, can't divide by zero!")
    else:
        print("Sorry, could you try that again?")

    restart = input("Do you want to try again? Type strictly 'yes' if so.")
    if restart != "yes":
        print("Goodbye then...!")
        break