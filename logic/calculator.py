import math
def addition():
    try: 
        firstNumber = float(input("type in a number"))
        secondNumber = float(input("type in a number"))
    except ValueError:
        print("error type in a real number")
        return 
    sum = f'{firstNumber} + {secondNumber} = {firstNumber + secondNumber}'
    return sum
def substraction():
    try: 
        firstNumber = float(input("type in a number"))
        secondNumber = float(input("type in a number"))
    except ValueError:
        print("error type in a real number")
        return 
    sum = f'{firstNumber} - {secondNumber} = {firstNumber - secondNumber}' 
    return sum

def division():
    try: 
        firstNumber = float(input("type in a number"))
        secondNumber = float(input("type in a number"))
    except ValueError:
        print("error type in a real number")
        return 
    sum = f'{firstNumber} / {secondNumber} = {firstNumber / secondNumber}'
    return sum

def multiplication():
    try: 
        firstNumber = float(input("type in a number"))
        secondNumber = float(input("type in a number"))
    except ValueError:
        print("error type in a real number")
        return 
    sum = f'{firstNumber} * {secondNumber} = {firstNumber * secondNumber}' 
    return sum

def exponentiation():
    try: 
        firstNumber = float(input("type in a number"))
        secondNumber = float(input("type in a number"))
    except ValueError:
        print("error type in a real number")
        return
    sum = f'{firstNumber} ^ {secondNumber} = {firstNumber ** secondNumber}'
    return sum
def factorial():
    try:
        onlyNumber = int(input("type in a number to use factorial on"))
    except ValueError:
        print("Error: type in a real number")
        return
    sum = f'{onlyNumber}! = {math.factorial(onlyNumber)}'
    return sum
def operations():
    print("""
    Calculator Operations:
          + = add two numbers
          - = substract two numbers
          / = divide two numbers 
          * = multiplie two numbers
          ^ = exponentiate two numbers
          ! = get a factorial of single a number
          q = exit calculator
    """)
def history(result):
    with open("history.txt","a") as file:
        file.write(result + '\n')
        print(result)
        print("Data was saved in file history.txt")
        file.close()