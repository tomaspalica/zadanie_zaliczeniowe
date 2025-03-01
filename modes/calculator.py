import logic.calculator
def calculator():
    while True:
        logic.calculator.operations()
        operation = input("Calculator, type operation: ").strip()
        if(operation == "q"):
            break
    
        match operation:
            case "+":
                result = logic.calculator.addition()
                logic.calculator.history(result)
            case "-":
                result = logic.calculator.substraction()
                logic.calculator.history(result)
            case "/":
                try:
                    result = logic.calculator.division()
                    logic.calculator.history(result)
                except ZeroDivisionError:
                    print("Error you can't divide by zero")
                    continue
            case "*":
                result = logic.calculator.multiplication()
                logic.calculator.history(result)
            case "^":
                result = logic.calculator.exponentiation()
                logic.calculator.history(result)
            case "!":
                result = logic.calculator.factorial()
                logic.calculator.history(result)
            case _:
                print('This command dose not exist, chose one from the list below')

    
    