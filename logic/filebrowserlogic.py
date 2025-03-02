import os


def pwd():
    try:
        print(os.getcwd())
    except OSError as error:
        print(f"System error: {error}")


def ls():
    try:
        for file_name in os.listdir():
            print(file_name)
    except PermissionError:
        print("You dont have acces to read this directory")
    except OSError as error:
        print(f"System error: {error}")


def cd(path):
    try:
        os.chdir(path)
        print(f'You are now in {path} directory')
    except FileNotFoundError:
        print(f"file {path} dose not exist")
    except NotADirectoryError:
        print(f"{path} is not a directory")
    except PermissionError:
        print(f"You dont have permision to access directory {path}")
    except OSError as error:
        print(f"System error: {error}")


def head(file):
    try:
        with open(file,"rb") as f:
            print(f.read(512))
    except FileNotFoundError:
        print(f"file {file} does not exist")
    except IsADirectoryError:
        print(f"{file} is a directory instead of a file")
    except UnicodeDecodeError:
        print(f"program couldn't decode file {file} ")
    except PermissionError:
        print(f"You don't have permission to read file {file}")
    except OSError as error:
        print(f"System error: {error}")


def operations():
    print("""
        Filebrowser Operations:
            ls = show list of files in current catalog 
            cd $1 = go to provided catalog 
            pwd = show current route
            head $1 = show first 512 bytes of provided file
            q = exit file browser
    """)