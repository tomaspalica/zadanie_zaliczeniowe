from modes import calculator 
from modes import filebrowser 


while True:
    print("""
        Starting operations:
            calc = go to calculator
            files = go to file browser
            quit = stop the program
    """)

    operation = input("index, type in operation: ").strip().lower()

    if(operation == "quit"):
        break
    match operation:
        case "calc":
            calculator.calculator()
        case "files":
            filebrowser.fileBrowser()
        case _:
            print("This command doesn't exist, choose one from the list below")