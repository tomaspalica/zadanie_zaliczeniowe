import logic.calculator
def calculator():
    while True:
        logic.calculator.operations()
        operation = input("Calculator, type operation: ")
        if(operation == "q"):
            break
        if(operation in ('+','-','*','/',"^")):
            try:
                firstNumber = float(input("type in a number"))
                secondNumber = float(input("type in a number"))
            except ValueError:
                print("error type in a real number")
                continue
            match operation:
                case "+":
                    logic.calculator.addition(firstNumber,secondNumber)
                case "-":
                    logic.calculator.substraction(firstNumber,secondNumber)
                case "/":
                    try:
                        logic.calculator.division(firstNumber,secondNumber)
                    except ZeroDivisionError:
                        print("Error you can't divide by zero")
                        continue
                case "*":
                    logic.calculator.multiplication(firstNumber,secondNumber)
                case "^":
                    logic.calculator.exponentiation(firstNumber,secondNumber)
        else:
            print('This command dosnt exist, chose one from the list below')

    
    