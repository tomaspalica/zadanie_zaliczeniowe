import logic.filebrowserlogic
def fileBrowser():
    while True:
        logic.filebrowserlogic.operations()
        comand = input("fileBrowser, type a comand: ").split()
        if(comand[0] == 'q'):
            break
        match comand[0]:
            case "ls":
                logic.filebrowserlogic.ls()
            case 'cd':
                if len(comand) != 2 :
                    print("Argument is missing")
                    continue
                logic.filebrowserlogic.cd(comand[1])
            case "pwd":
                logic.filebrowserlogic.pwd()
            case "head":
                if len(comand) != 2:
                    print("Argument is missing")
                    continue
                logic.filebrowserlogic.head(comand[1])
            case _:
                print('This command dosnt exist, chose one from the list below')

