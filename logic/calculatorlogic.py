import math


def get_numbers():
    try: 
        first_number = float(input("type in a number"))
        second_number = float(input("type in a number"))
        return first_number,second_number
    except ValueError:
        print("error type in a real number")
        return None


def addition():
    first_number, second_number = get_numbers()
    output = f"{first_number} + {second_number} = {first_number + second_number}"
    return output


def subtraction():
    first_number, second_number = get_numbers()
    output = f"{first_number} - {second_number} = {first_number - second_number}"
    return output


def division():
    first_number, second_number = get_numbers()
    if(second_number == 0):
        print("Error Cannot divide by zero ")
        return None
    output = f"{first_number} / {second_number} = {first_number / second_number}"
    return output


def multiplication():
    first_number, second_number = get_numbers()
    output = f"{first_number} * {second_number} = {first_number * second_number}" 
    return output


def exponentiation():
    first_number, second_number = get_numbers()
    output = f"{first_number} ^ {second_number} = {first_number ** second_number}"
    return output


def factorial():
    try:
        only_number = int(input("type in a number to use factorial on"))
        if only_number < 0:
            print("Number must be greater then 0")
            return None
    except ValueError:
        print("Error: type in a real number")
        return None
    output = f"{only_number}! = {math.factorial(only_number)}"
    return output


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
    if result == None:
        return None
    with open("history.txt","a") as history_file:
        history_file.write(result + "\n")
    print(result)
    print("Data was saved in file history.txt")