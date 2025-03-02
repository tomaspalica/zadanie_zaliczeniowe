from logic import calculatorlogic


def calculator():
    while True:
        calculatorlogic.operations()
        operation = input("Calculator, type operation: ").strip().lower()

        if operation == "q":
            break

        match operation:
            case "+":
                result = calculatorlogic.addition()
                calculatorlogic.history(result)
            case "-":
                result = calculatorlogic.subtraction()
                calculatorlogic.history(result)
            case "/":
                result = calculatorlogic.division()
                calculatorlogic.history(result)
            case "*":
                result = calculatorlogic.multiplication()
                calculatorlogic.history(result)
            case "^":
                result = calculatorlogic.exponentiation()
                calculatorlogic.history(result)
            case "!":
                result = calculatorlogic.factorial()
                calculatorlogic.history(result)
            case _:
                print("This command doesn't exist, choose one from the list below")