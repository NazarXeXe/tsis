
from os import walk, path

def check(theDir: str):
    return path.exists(theDir) and path.isdir(theDir)

if __name__ == "__main__":
    thePath = input("Enter directory path to walk: ")
    if not check(thePath):
        print("Invalid path to walk.")
        exit(0)

    for root, dirs, files in walk(thePath):
        if len(dirs) != 0:
            print("Directories:")
            for d in dirs:
                print(d)
        if len(files) != 0:
            print("Files:")
            for f in files:
                print(f)
