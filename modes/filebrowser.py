from logic import filebrowserlogic


def fileBrowser():
    while True:
        filebrowserlogic.operations()
        operation = input("fileBrowser, type a comand: ").lower().split()

        if operation[0] == 'q':
            break

        match operation[0]:
            case "ls":
                filebrowserlogic.ls()
            case 'cd':
                if len(operation) != 2:
                    print("Argument is missing")
                    return
                filebrowserlogic.cd(operation[1])
            case "pwd":
                filebrowserlogic.pwd()
            case "head":
                if len(operation) != 2:
                    print("Argument is missing")
                    return
                filebrowserlogic.head(operation[1])
            case _:
                print("This command doesn't exist, choose one from the list below")