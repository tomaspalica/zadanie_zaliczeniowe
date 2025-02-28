import os
def pwd():
    print(os.getcwd())

def ls():
    for x in os.listdir():
        print(x)
def cd(a):
    try:
        os.chdir(a)
    except FileNotFoundError:
        print("plik nie istnieje")
    except NotADirectoryError:
        print("plik nie jest katalogiem")
def head(file):
    try:
        f= open(file,"rb")
        print(f.read(512))
        f.close()
    except FileNotFoundError:
        print('plik nie istnieje')
def operations():
    print("""
    Filebrowser Operations:
          ls = show list of files in current catalog 
          cd $1 = go to provided catalog 
          pwd = show current route
          head $1 = show first 512 bytes of provided file
          q = exit file browser
    """)