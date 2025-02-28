import modes.calculator 
import modes.filebrowser 
while True:
    print("""
    Starting operations:
          calc = go to calculator
          files = go to file browser
          quit = stop the program
          help = show operations
    """)
    a = input("index, type: ")
    if(a == "quit"):
        break
    match a:
        case "calc":
            modes.calculator.calculator()
        case "files":
            modes.filebrowser.fileBrowser()
        case _:
            print('This command dosnt exist, chose one from the list below')

    
